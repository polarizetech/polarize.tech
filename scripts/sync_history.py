#!/usr/bin/env python3
"""Write _data/history.json — the version history of every post and rant, from git.

For each file in _posts/ and _essays/, every commit that touched it (following
renames), newest first, with:

  sha, date, subject     straight from git
  author                 the commit author
  llm                    true when the commit carries a Co-Authored-By trailer for
                         an Anthropic model (noreply@anthropic.com). This is the
                         ONLY LLM signal git holds: it says an LLM took part in
                         the commit, not which words it wrote, and an LLM edit
                         committed without the trailer is indistinguishable
                         from a hand edit.
  added, removed         word counts
  hunks                  the diff against the previous revision, pre-rendered:
                         changed paragraphs with one paragraph of context, and
                         inside a changed paragraph the words marked <ins>/<del>.
                         The first revision has no diff — it IS the original.

Keyed by the file's current path, which is what Jekyll exposes as page.path.
The page renders it with _includes/history.html. Never edit the output by hand.

Commits cannot contain their own hash, so this runs AFTER a post changes: the
history workflow (.github/workflows/history.yml) regenerates and commits it on
every push that touches _posts/ or _essays/.

Usage:  python3 scripts/sync_history.py [--check]
"""
import argparse
import difflib
import html
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import SITE

OUT = SITE / '_data' / 'history.json'
LLM_TRAILER = re.compile(r'^Co-Authored-By:\s*(.+?)\s*<[^>]*@anthropic\.com>\s*$', re.I | re.M)
TOKEN = re.compile(r'\s+|\w+|[^\w\s]')
CONTEXT = 1


def git(*args):
    return subprocess.run(('git', *args), cwd=SITE, check=True,
                           capture_output=True, text=True).stdout


def revisions(path):
    """Commits touching `path`, newest first, each with the file's path at that commit."""
    log = git('log', '--follow', '--name-status', '--format=%x1e%H%x1f%an%x1f%aI%x1f%s%x1f%b%x1f',
              '--', path)
    out = []
    for block in log.split('\x1e')[1:]:
        sha, author, date, subject, body, files = block.split('\x1f')
        status = files.strip().splitlines()[-1].split('\t')
        m = LLM_TRAILER.search(body)
        out.append({'sha': sha, 'author': author, 'date': date, 'subject': subject,
                    'llm': bool(m), 'llm_name': m.group(1) if m else None,
                    'path': status[-1]})
    return out


def words(s):
    return TOKEN.findall(s)


def inline(old, new):
    """One changed line, with the changed words themselves wrapped in <del>/<ins>."""
    a, b = words(old), words(new)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            out.append(html.escape(''.join(a[i1:i2])))
            continue
        if i2 > i1:
            out.append(f'<del>{html.escape("".join(a[i1:i2]))}</del>')
        if j2 > j1:
            out.append(f'<ins>{html.escape("".join(b[j1:j2]))}</ins>')
    return ''.join(out)


def count_words(parts):
    return sum(len(re.findall(r'\w+', x)) for x in parts)


def paragraphs(text):
    """The file as paragraphs, each unwrapped onto one line.

    Posts are hard-wrapped at ~95 columns, so a one-word edit can re-wrap every
    following line of its paragraph. Diffing by line would show all of them as
    changed; diffing by paragraph shows the edit. Front matter keeps one entry
    per line, since each line there is its own field.
    """
    out, buf = [], []
    lines = text.splitlines()
    i = 0
    if lines and lines[0].strip() == '---':
        out.append('---')
        i = 1
        while i < len(lines) and lines[i].strip() != '---':
            out.append(lines[i])
            i += 1
        if i < len(lines):
            out.append('---')
            i += 1
    for line in lines[i:]:
        if not line.strip():
            if buf:
                out.append(' '.join(buf))
                buf = []
        # a list item, heading, table row or fence starts its own unit
        elif re.match(r'\s*([-*+]|\d+\.|#|\||```)', line) and buf:
            out.append(' '.join(buf))
            buf = [line.strip()]
        else:
            buf.append(line.strip())
    if buf:
        out.append(' '.join(buf))
    return out


def similar(x, y):
    sm = difflib.SequenceMatcher(None, words(x), words(y), autojunk=False)
    return sm.quick_ratio() >= 0.5 and sm.ratio() >= 0.5


def diff(old_text, new_text):
    a, b = paragraphs(old_text), paragraphs(new_text)
    rows, added, removed = [], 0, 0
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            rows += [('ctx', html.escape(x)) for x in a[i1:i2]]
        elif op == 'replace':
            # Pair each old paragraph with the next new one that is still
            # recognisably the same paragraph, and mark the words inside it.
            # Anything left unpaired was removed or added outright.
            olds, news, j = a[i1:i2], b[j1:j2], 0
            for o in olds:
                k = next((k for k in range(j, len(news)) if similar(o, news[k])), None)
                if k is None:
                    rows.append(('del', html.escape(o)))
                    removed += count_words([o])
                    continue
                rows += [('add', html.escape(x)) for x in news[j:k]]
                added += count_words(news[j:k])
                rows.append(('mod', inline(o, news[k])))
                wa, wb = re.findall(r'\w+', o), re.findall(r'\w+', news[k])
                sm = difflib.SequenceMatcher(None, wa, wb, autojunk=False)
                same = sum(bl.size for bl in sm.get_matching_blocks())
                added += len(wb) - same
                removed += len(wa) - same
                j = k + 1
            rows += [('add', html.escape(x)) for x in news[j:]]
            added += count_words(news[j:])
        elif op == 'delete':
            rows += [('del', html.escape(x)) for x in a[i1:i2]]
            removed += count_words(a[i1:i2])
        else:
            rows += [('add', html.escape(x)) for x in b[j1:j2]]
            added += count_words(b[j1:j2])

    # Keep changed paragraphs and CONTEXT paragraphs around them; split the rest
    # into hunks.
    keep = set()
    for i, (t, _) in enumerate(rows):
        if t != 'ctx':
            keep.update(range(max(0, i - CONTEXT), min(len(rows), i + CONTEXT + 1)))
    hunks, cur, last = [], [], None
    for i in sorted(keep):
        if last is not None and i != last + 1:
            hunks.append(cur)
            cur = []
        t, h = rows[i]
        cur.append({'t': t, 'h': h})
        last = i
    if cur:
        hunks.append(cur)
    return [h for h in hunks if any(r['t'] != 'ctx' for r in h)], added, removed


def build():
    files = sorted(SITE.glob('_posts/*.md')) + sorted(SITE.glob('_essays/*.md'))
    data = {}
    for f in files:
        rel = f.relative_to(SITE).as_posix()
        revs = revisions(rel)
        if not revs:
            continue                                  # not committed yet
        out = []
        for i, r in enumerate(revs):
            prev = revs[i + 1] if i + 1 < len(revs) else None
            entry = {k: r[k] for k in ('sha', 'author', 'date', 'subject', 'llm', 'llm_name')}
            entry['short'] = r['sha'][:7]
            if prev is None:
                entry.update(first=True, hunks=[], added=0, removed=0)
            else:
                new = git('show', f'{r["sha"]}:{r["path"]}')
                old = git('show', f'{prev["sha"]}:{prev["path"]}')
                hunks, added, removed = diff(old, new)
                entry.update(first=False, hunks=hunks, added=added, removed=removed)
            out.append(entry)
        data[rel] = out
    return json.dumps(data, indent=1, ensure_ascii=False) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    text = build()
    current = OUT.read_text() if OUT.exists() else ''
    if args.check:
        if text != current:
            print('STALE  _data/history.json — run scripts/sync_history.py', file=sys.stderr)
            return 1
        print('OK    _data/history.json is current')
        return 0
    if text != current:
        OUT.write_text(text)
        n = sum(len(v) for v in json.loads(text).values())
        print(f'WROTE _data/history.json ({n} revisions across {len(json.loads(text))} files)')
    else:
        print('OK    _data/history.json unchanged')
    return 0


if __name__ == '__main__':
    sys.exit(main())
