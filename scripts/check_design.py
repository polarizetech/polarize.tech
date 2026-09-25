#!/usr/bin/env python3
"""DESIGN GATE — does this site still obey the monorepo's design system?

The look is defined in polarizetech/polarize-ui, mounted here as the design/
submodule (the monorepo mounts the same repo at tools/design). That folder has its own dev_check.py; this one checks the
part it cannot see: the SITE's own styles.css and markup.

It enforces the rules that were set on the shared system and are easy to break
by hand (design/CLAUDE.md, operator 2026-08-19/20):

  RULE 1  No network font, no CDN. Every asset is local, or the offline rule
          and the "no live network dependency" convention are both broken.

  RULE 2  The sans is NEVER BOLD. Weight >= 600 appears only inside @font-face.
          Hierarchy comes from size, face, colour and case — never weight.

  RULE 3  UPPERCASE IS ALWAYS MONO. Every rule that sets
          `text-transform: uppercase` sets var(--font-mono) in the same block.

  RULE 4  The sans is NEVER TRACKED. Every letter-spacing belongs to a mono
          block, an uppercase block, the display serif's optical correction,
          or an explicit reset.

  RULE 5  No raw colour. styles.css is a project layer over the tokens; a hex
          literal here is a value that escaped design/tokens.json.

  RULE 6  design/ is the polarize-ui submodule, pinned to a release tag, with no
          local edits. A patched copy is a fork nobody is maintaining; changes go
          upstream to github.com/polarizetech/polarize-ui and come back as a new tag.

  RULE 8  Stylesheets are cache-busted. GitHub Pages caches on the URL, so a
          deploy that keeps /styles.css unchanged serves a returning visitor the
          PREVIOUS stylesheet against the current HTML. That happened on
          2026-08-31 and presented as a broken layout, not as a cache problem.

  RULE 7  A tier badge carries a word AND a glyph, never colour alone — the
          five epistemic families fail an all-pairs colour-blindness check.

Usage:  python3 scripts/check_design.py
"""
import argparse
import subprocess
import re
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
FAILS = []


def fail(rule, msg):
    FAILS.append(f'[RULE {rule}]  {msg}')


def strip_at_font_face(css):
    return re.sub(r'@font-face\s*\{[^}]*\}', '', css)


def main():
    ap = argparse.ArgumentParser()
    args = ap.parse_args()

    css = (SITE / 'styles.css').read_text()
    body = strip_at_font_face(css)
    html = '\n'.join(p.read_text() for p in
                     list(SITE.glob('*.html')) + list(SITE.glob('_layouts/*.html'))
                     + list(SITE.glob('_includes/*.html')) + list(SITE.glob('blog/*.html'))
                     + list(SITE.glob('rants/*.html')) + list(SITE.glob('changelog/**/*.html')))

    # ---- RULE 1 — no network font / CDN ------------------------------------
    for m in re.finditer(r'https?://[^\s"\')]+', html + css):
        url = m.group(0)
        if any(h in url for h in ('fonts.googleapis', 'fontshare', 'cdn.', 'unpkg', 'jsdelivr')):
            fail(1, f'network asset: {url}')
    if 'design/design.css' not in html:
        fail(1, 'design/design.css is never linked — the site is not on the system')

    # ---- RULE 2 — never bold ----------------------------------------------
    for m in re.finditer(r'font-weight:\s*(600|700|800|900|bold)', body):
        fail(2, f'font-weight {m.group(1)} in styles.css — the sans is never bold')

    # ---- RULE 3 — uppercase is always mono --------------------------------
    upper = re.findall(r'([^{}]+)\{([^{}]*text-transform:\s*uppercase[^{}]*)\}', body)
    for sel, blk in upper:
        if 'var(--font-mono)' not in blk:
            fail(3, f'uppercase without the mono face: {sel.strip().splitlines()[-1].strip()[:60]}')

    # ---- RULE 4 — the sans is never tracked -------------------------------
    for m in re.finditer(r'([^{}]+)\{([^{}]*letter-spacing[^{}]*)\}', body):
        sel = m.group(1).strip().splitlines()[-1].strip()
        blk = m.group(2)
        ok = ('var(--font-mono)' in blk or 'uppercase' in blk
              or 'letter-spacing: 0' in blk or 'var(--font-display)' in blk
              or 'ui-display' in sel)
        if not ok:
            fail(4, f'tracked sans: {sel[:60]}')

    # ---- RULE 5 — no raw colour -------------------------------------------
    for m in re.finditer(r'#[0-9a-fA-F]{3,8}\b', css):
        fail(5, f'hex literal {m.group(0)} in styles.css — use a token from design/tokens.json')

    # ---- RULE 6 — design/ is the polarize-ui submodule, untouched -------
    def git(*a):
        r = subprocess.run(['git', *a], cwd=SITE, capture_output=True, text=True)
        return r.returncode, r.stdout.strip()
    code, mode = git('ls-files', '-s', 'design')
    if code or not mode.startswith('160000'):
        fail(6, 'design/ is not a git submodule — it must be github.com/polarizetech/polarize-ui')
    code, url = git('config', '-f', '.gitmodules', 'submodule.design.url')
    if 'polarizetech/polarize-ui' not in url:
        fail(6, f'design/ points at {url or "nothing"}, not polarizetech/polarize-ui')
    for rel in ('design.css', 'publication.css', 'design.js', 'tokens.json'):
        if not (SITE / 'design' / rel).exists():
            fail(6, f'design/{rel} is missing — run `git submodule update --init design`')
    code, dirty = git('-C', 'design', 'status', '--porcelain', '--untracked-files=no')
    if dirty:
        fail(6, 'design/ has local edits — change polarize-ui upstream, never patch it here')
    code, tag = git('-C', 'design', 'describe', '--tags', '--exact-match')
    if code:
        fail(6, 'design/ is not pinned to a polarize-ui release tag')

    # ---- RULE 7 — a badge is never colour alone ---------------------------
    tier = SITE / '_includes' / 'tier.html'
    if not tier.exists():
        fail(7, '_includes/tier.html is missing — tier badges have no shared renderer')
    else:
        t = tier.read_text()
        if 'ui-tier__glyph' not in t:
            fail(7, 'tier.html renders no glyph — hue would carry the meaning alone')
        for fam in ('measured', 'predicted', 'exploring', 'spec'):
            if fam not in t:
                fail(7, f'tier.html never maps to the "{fam}" family')

    # ---- RULE 8 — the stylesheet URL changes when the deploy does ---------
    layout = (SITE / '_layouts' / 'default.html').read_text()
    for asset in ('design.css', 'publication.css', 'styles.css'):
        line = next((l for l in layout.splitlines() if asset in l and 'rel="stylesheet"' in l), None)
        if line is None:
            fail(8, f'{asset} is not linked from _layouts/default.html')
        elif '?v=' not in line:
            fail(8, f'{asset} is linked without ?v= — a returning visitor will get '
                    f'the previous deploy\'s stylesheet against this HTML')

    for f in FAILS:
        print(f'FAIL  {f}', file=sys.stderr)
    if FAILS:
        print(f'\n{len(FAILS)} design violation(s).', file=sys.stderr)
        return 1
    print('OK    site matches the polarize-ui design system.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
