#!/usr/bin/env python3
"""Pull citation + claim metadata from polarizetech/research into _data/.

This is the ONLY way bibliographic data enters this repo. It copies, it never
composes: every author, year, title, journal and DOI written to
_data/citations.yml came out of a Crossref or PubMed response recorded in the
research repo's machine-generated ledger.

It syncs only what published posts actually reference, so the site never ships a
3,000-entry ledger, and so an unused key can't rot here unnoticed.

Usage:
    python3 scripts/sync_research.py                 # ../research
    python3 scripts/sync_research.py --research PATH
    python3 scripts/sync_research.py --drafts        # include _drafts/
    python3 scripts/sync_research.py --check         # fail if _data/ is stale

Refuses to sync:
  * a citation key absent from the ledger
  * a citation key whose identifier never resolved against a registry
  * a claim whose file lives under RETRACTED/ or archive/
  * a claim with no tier computed
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (SITE, FORBIDDEN_SOURCE_DIRS, load_ledger, parse_claim,
                     split_post, cite_keys_in, posts, y)

LEDGER_FIELDS = ('doi', 'pmid', 'first_author', 'year', 'title', 'journal',
                 'volume', 'pages', 'registry', 'verified_on')


def collect_wanted(include_drafts):
    """Return (citation_keys, claim_ids) referenced by every post."""
    cites, claims, errors = set(), set(), []
    for p in posts(include_drafts):
        try:
            fm, body = split_post(p)
        except Exception as e:                       # noqa: BLE001 — reported, not raised
            errors.append(str(e))
            continue
        cites.update(fm.get('citations') or [])
        cites.update(cite_keys_in(body))
        claims.update(fm.get('claims') or [])
    return cites, claims, errors


def find_claim_file(research, claim_id):
    hits = [p for p in research.glob(f'projects/*/claims/{claim_id}-*.md')]
    hits += [p for p in research.glob(f'projects/*/claims/{claim_id}.md')]
    return hits[0] if hits else None


def build_citations(ledger, keys):
    out, errors = {}, []
    for k in sorted(keys):
        rec = ledger.get(k)
        if rec is None:
            errors.append(f'citation key "{k}" is not in the research ledger — '
                          f'run build_ledger.py in polarizetech/research first')
            continue
        if str(rec.get('resolved', '')).lower() != 'true':
            errors.append(f'citation key "{k}" never resolved against a registry — '
                          f'it does not exist for publication purposes')
            continue
        out[k] = rec
    return out, errors


def build_claims(research, ids):
    out, errors = {}, []
    for cid in sorted(ids):
        path = find_claim_file(research, cid)
        if path is None:
            errors.append(f'claim "{cid}" has no file in {research}/projects/*/claims/')
            continue
        rel = str(path.relative_to(research))
        if any(bad in rel for bad in FORBIDDEN_SOURCE_DIRS):
            errors.append(f'claim "{cid}" lives under {rel} — retracted/archived '
                          f'material is never published')
            continue
        c = parse_claim(path)
        if not c.get('tier'):
            errors.append(f'claim "{cid}" has no computed tier — run tier.py in the '
                          f'research repo before citing it publicly')
            continue
        if not c['has_disproof']:
            errors.append(f'claim "{cid}" records no disproof conditions — '
                          f'"a claim with no recorded attempt to disconfirm it is not a claim"')
            continue
        c['path'] = rel
        out[cid] = c
    return out, errors


HEADER = ('# GENERATED — DO NOT HAND-EDIT.\n'
          '# Source: polarizetech/research (machine-verified against Crossref/PubMed).\n'
          '# Regenerate: python3 scripts/sync_research.py\n')


def render_citations(cites):
    lines = [HEADER]
    for k, r in cites.items():
        lines.append(f'{k}:')
        for f in LEDGER_FIELDS:
            if r.get(f):
                lines.append(f'  {f}: {y(r[f])}')
        lines.append(f'  full_text_read: {y(str(r.get("full_text_read", "false")).lower() == "true")}')
        if r.get('authors'):
            lines.append('  authors:')
            lines.extend(f'    - {y(a)}' for a in r['authors'])
        lines.append('')
    return '\n'.join(lines)


def render_claims(claims):
    lines = [HEADER]
    for cid, c in claims.items():
        lines.append(f'{cid}:')
        lines.append(f'  tier: {y(c["tier"])}')
        lines.append(f'  statement: {y(c["statement"])}')
        lines.append(f'  path: {y(c["path"])}')
        lines.append(f'  has_disconfirming: {y(c["has_disconfirming"])}')
        if c['sources']:
            lines.append('  sources:')
            lines.extend(f'    - {y(s)}' for s in c['sources'])
        lines.append('')
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--research', default=str(Path.home() / 'Sites' / 'research'),
                    help='path to a polarizetech/research checkout')
    ap.add_argument('--drafts', action='store_true', help='include _drafts/')
    ap.add_argument('--check', action='store_true',
                    help='do not write; exit non-zero if _data/ is out of date')
    args = ap.parse_args()

    research = Path(args.research).expanduser().resolve()
    if not (research / 'CITATIONS.yaml').exists():
        print(f'FAIL  no CITATIONS.yaml under {research}\n'
              f'      clone polarizetech/research or pass --research PATH', file=sys.stderr)
        return 2

    keys, claim_ids, errors = collect_wanted(args.drafts)
    ledger = load_ledger(research / 'CITATIONS.yaml')

    cites, e1 = build_citations(ledger, keys)
    claims, e2 = build_claims(research, claim_ids)
    errors += e1 + e2

    if errors:
        for e in errors:
            print(f'FAIL  {e}', file=sys.stderr)
        return 1

    data = SITE / '_data'
    data.mkdir(exist_ok=True)
    targets = {data / 'citations.yml': render_citations(cites),
               data / 'claims.yml': render_claims(claims)}

    if args.check:
        stale = [p.name for p, body in targets.items()
                 if not p.exists() or p.read_text() != body]
        if stale:
            print(f'FAIL  _data/ is stale: {", ".join(stale)}\n'
                  f'      run: python3 scripts/sync_research.py', file=sys.stderr)
            return 1
        print(f'OK    _data/ current — {len(cites)} citations, {len(claims)} claims')
        return 0

    for p, body in targets.items():
        p.write_text(body)
    print(f'OK    synced {len(cites)} citations, {len(claims)} claims from {research}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
