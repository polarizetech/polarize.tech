#!/usr/bin/env python3
"""THE PUBLICATION GATE — run before every commit. Exit non-zero on any violation.

polarize.tech is a public face on a falsification-first research corpus. The
research repo's gate proves the corpus is sound; this one proves the *website*
did not weaken it on the way out. It enforces:

  RULE 1  Front matter is complete. No post publishes without title, description,
          date, project, status, tier, claims and citations declared.

  RULE 2  Cite by key, only by key. Every {% include cite.html key="x" %} in the
          body is declared in front matter, and every declared key is used.
          -> a key that exists but is never cited is dead weight; a key cited but
             never declared has no bibliography entry and no verified provenance.

  RULE 3  Every key resolves in _data/citations.yml, which is machine-copied from
          the research ledger. A citation that has not been resolved against a
          registry does not exist.

  RULE 4  No inline bibliographic data in prose — no bare DOI, no PMID, no
          doi.org / pubmed URL, no "Author et al. 2021". This is the structural
          defence: if a name or identifier cannot be typed by hand, it cannot be
          invented. (The 2026-07-11 audit found a paper cited for months under an
          author who does not exist.)

  RULE 5  Every claim ID resolves in _data/claims.yml, carries a computed tier,
          and records disconfirming evidence.

  RULE 6  No tier laundering. A post may not assert a confidence tier stronger
          than the weakest claim it rests on.

  RULE 0  _data/*.yml is parseable. A double-quoted scalar that never closes -- a
          Crossref title arriving with raw newlines produced exactly this -- makes
          the file unreadable to a stricter YAML parser. The local Jekyll build
          tolerated it and said nothing; GitHub Pages failed the deploy. Checked
          here so the failure is caught before the push, not after.

  RULE 7  No forbidden provenance — nothing sourced from RETRACTED/ or archive/,
          no [VERIFIED] self-assertions, no unresolved TODO tiers.

What it cannot catch: prose that misrepresents what a correctly-cited paper
actually says. That is what full-text reading and the research repo's challenge
records are for — RULE 8 surfaces the exposure rather than pretending it away.

Usage:  python3 scripts/validate_posts.py [--drafts] [--strict]
        --strict   treat warnings (unread full text, SPEC tier) as failures
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (SITE, TIERS, TIER_RANK, load_generated, split_post,
                     cite_keys_in, posts)

REQUIRED = ('title', 'description', 'date', 'project', 'status', 'tier',
            'claims', 'citations')

# RULE 4 — patterns that mean somebody typed bibliographic data by hand.
BARE_DOI = re.compile(r'\b10\.\d{4,9}/[^\s)>\]"\']+')
BARE_PMID = re.compile(r'\bPMID:?\s*\d{6,9}\b', re.I)
BIB_URL = re.compile(r'https?://(?:dx\.)?(?:doi\.org|pubmed\.ncbi\.nlm\.nih\.gov|'
                     r'www\.ncbi\.nlm\.nih\.gov/pmc)/\S+', re.I)
NAME_YEAR = re.compile(r'\b([A-Z][a-zà-ÿ]{2,})\s+(?:et al\.?|&\s+[A-Z][a-zà-ÿ]{2,})[,\s]*\(?((?:19|20)\d{2})\)?')
VERIFIED_TAG = re.compile(r'\[VERIFIED\]', re.I)

# Prose outside code fences only — a fenced example of a bad citation is fine.
FENCE = re.compile(r'```.*?```|`[^`\n]+`', re.DOTALL)


class Report:
    def __init__(self):
        self.fails, self.warns = [], []

    def fail(self, post, rule, msg):
        self.fails.append(f'{post}  [RULE {rule}]  {msg}')

    def warn(self, post, msg):
        self.warns.append(f'{post}  [warn]  {msg}')


def prose_only(body):
    """Body with code fences and inline code blanked out, length preserved."""
    return FENCE.sub(lambda m: ' ' * len(m.group(0)), body)


def check_post(path, cites, claims, rep):
    name = path.name
    try:
        fm, body = split_post(path)
    except Exception as e:                            # noqa: BLE001
        rep.fail(name, 1, str(e))
        return

    # ---- RULE 1 — front matter completeness -----------------------------
    for field in REQUIRED:
        if field not in fm:
            rep.fail(name, 1, f'missing front-matter field: {field}')
    if fm.get('status') not in ('published', 'draft'):
        rep.fail(name, 1, f'status must be published|draft, got {fm.get("status")!r}')
    if fm.get('status') == 'draft' and path.parent.name == '_posts':
        rep.fail(name, 1, 'status: draft but the file is in _posts/ — move it to _drafts/')
    tier = str(fm.get('tier', '')).upper()
    if tier not in TIERS:
        rep.fail(name, 1, f'tier must be one of {"/".join(TIERS)}, got {fm.get("tier")!r}')

    declared = list(fm.get('citations') or [])
    used = cite_keys_in(body)

    # ---- RULE 2 — cite by key, only by key ------------------------------
    for k in used:
        if k not in declared:
            rep.fail(name, 2, f'cited "{k}" but it is not in front-matter citations:')
    for k in declared:
        if k not in used:
            rep.fail(name, 2, f'declared "{k}" in citations: but never cited in the body')

    # ---- RULE 3 — every key is in the synced ledger ----------------------
    for k in declared:
        rec = cites.get(k)
        if rec is None:
            rep.fail(name, 3, f'"{k}" is not in _data/citations.yml — '
                              f'run scripts/sync_research.py')
            continue
        if not rec.get('verified_on'):
            rep.fail(name, 3, f'"{k}" has no verified_on date — it never resolved')
        # ---- RULE 8 — full-text exposure ---------------------------------
        if str(rec.get('full_text_read', 'false')).lower() != 'true':
            rep.warn(name, f'"{k}" cited without reading full text — abstract is not '
                           f'the paper; do not state what it "found"')

    # ---- RULE 4 — no hand-typed bibliographic data in prose --------------
    text = prose_only(body)
    for pat, what in ((BARE_DOI, 'a bare DOI'), (BARE_PMID, 'a bare PMID'),
                      (BIB_URL, 'a bibliographic URL')):
        for m in pat.finditer(text):
            rep.fail(name, 4, f'{what} in prose: {m.group(0)[:60]!r} — cite by ledger key')
    for m in NAME_YEAR.finditer(text):
        rep.fail(name, 4, f'inline author-year {m.group(0)!r} — cite by ledger key; '
                          f'names are machine-fetched, never typed')
    if VERIFIED_TAG.search(text):
        rep.fail(name, 7, '[VERIFIED] is not a tag anyone asserts here — it is a '
                          'check that passes in the research repo')

    # ---- RULE 5/6 — claims resolve, and no tier laundering ---------------
    weakest = None
    for cid in (fm.get('claims') or []):
        c = claims.get(cid)
        if c is None:
            rep.fail(name, 5, f'claim "{cid}" is not in _data/claims.yml — '
                              f'run scripts/sync_research.py')
            continue
        ctier = str(c.get('tier', '')).upper()
        if ctier not in TIERS:
            rep.fail(name, 5, f'claim "{cid}" has no computed tier (got {ctier!r})')
            continue
        if str(c.get('has_disconfirming', 'false')).lower() != 'true':
            rep.warn(name, f'claim "{cid}" records no disconfirming evidence yet — '
                           f'a null is a result; populate it before leaning on this')
        weakest = ctier if weakest is None else min(
            (weakest, ctier), key=lambda t: TIER_RANK[t])

    if weakest and tier in TIERS and TIER_RANK[tier] > TIER_RANK[weakest]:
        rep.fail(name, 6, f'post asserts tier {tier} but rests on a tier {weakest} '
                          f'claim — an upstream [A] never launders a downstream [C]')

    if tier == 'SPEC':
        rep.warn(name, 'tier SPEC — make sure the prose reads as speculation, not finding')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--drafts', action='store_true', help='also validate _drafts/')
    ap.add_argument('--strict', action='store_true', help='treat warnings as failures')
    args = ap.parse_args()

    cites = load_generated(SITE / '_data' / 'citations.yml')
    claims = load_generated(SITE / '_data' / 'claims.yml')
    rep = Report()

    # ---- RULE 0 — the generated data must actually parse ------------------
    for name in ('citations.yml', 'claims.yml'):
        path = SITE / '_data' / name
        if not path.exists():
            continue
        for n, line in enumerate(path.read_text().splitlines(), 1):
            stripped = line.strip()
            if re.match(r'^[\w-]+: ".*', stripped) and not stripped.endswith('"'):
                rep.fail(f'_data/{name}', 0,
                         f'line {n}: double-quoted value is never closed — '
                         f'{stripped[:60]!r}. Regenerate the ledger upstream; '
                         f'GitHub Pages will refuse to build this.')


    found = posts(args.drafts)
    if not found:
        print('FAIL  no posts found under _posts/', file=sys.stderr)
        return 1

    for p in found:
        check_post(p, cites, claims, rep)

    for w in rep.warns:
        print(f'WARN  {w}')
    for f in rep.fails:
        print(f'FAIL  {f}', file=sys.stderr)

    if rep.fails or (args.strict and rep.warns):
        print(f'\n{len(rep.fails)} failure(s), {len(rep.warns)} warning(s) '
              f'across {len(found)} post(s) — NOT publishable.', file=sys.stderr)
        return 1

    print(f'\nOK    {len(found)} post(s) pass the gate '
          f'({len(rep.warns)} warning(s), {len(cites)} citations in ledger).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
