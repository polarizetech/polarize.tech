# POLARIZE — The Hidden Electricity of Life

Two things live here:

1. **The landing page** (`/`) — a single-page, dark-themed introduction to
   **bioelectricity** and **cellular polarization**, with four hand-built
   `<canvas>` animations and zero dependencies.
2. **Research notes** (`/blog/`) — published excerpts from an ongoing
   falsification-first research program on audio-evoked potentials,
   bioelectricity, neuroscience and neuromedicine.

Built by GitHub Pages' own Jekyll. Custom domain: `polarize.tech`.

## The landing page

Four canvas animations, no libraries:

1. **Hero ion field** — drifting positive/negative ions connected by a faint bioelectric field.
2. **Polarization, Live** *(the centerpiece)* — an interactive slice of cell membrane. Press **Stimulate** to fire a wave of **depolarization**: voltage-gated channels open, Na⁺ floods inward, and the membrane potential flips from the resting −70 mV toward +40 mV before repolarizing.
3. **Action-potential trace** — a live voltage-over-time graph synced to the membrane.
4. **Signal propagation** — a self-renewing depolarization wave racing down a nerve fibre.

Respects `prefers-reduced-motion` and scales to mobile.

## Research notes

Posts are markdown in `_posts/`. They are **not** free-form: every source is cited
by a key that resolves to a machine-verified entry in the citation ledger of
[`polarizetech/research`](https://github.com/polarizetech/research), and every post
carries a confidence tier copied from the claims it rests on.

Two scripts enforce that, both stdlib-only Python:

```bash
# Pull citation + claim metadata from the research repo into _data/
python3 scripts/sync_research.py --research ~/Sites/research

# The publication gate — run before every commit
python3 scripts/validate_posts.py --strict
```

The gate rejects hand-typed DOIs, inline author-year citations, undeclared or
unused citation keys, unresolved sources, missing claims, and any post asserting a
confidence tier stronger than the claims beneath it. CI re-runs it on every push
against the committed `_data/`, without access to the private research repo.

**Read [CLAUDE.md](CLAUDE.md) before adding or editing a post.** It is the
authoring protocol, including the manual fact-validation pass the gate cannot do.

## Run locally

```bash
bundle install
bundle exec jekyll serve --drafts
# then open http://localhost:4321
```

## Files

| Path | |
|---|---|
| `index.html`, `app.js` | Landing page. Plain HTML, no front matter — Jekyll copies it verbatim. |
| `styles.css` | One stylesheet. Document/blog styles are appended at the bottom. |
| `blog/index.html` | Post index. |
| `_posts/`, `_drafts/` | Research notes. |
| `_layouts/`, `_includes/` | Page shell, post layout, citation includes. |
| `_data/` | **Generated** — never hand-edited. |
| `scripts/` | Sync + publication gate. |
| `CLAUDE.md` | Authoring protocol. |

## Brand

| | |
|---|---|
| Background | near-black `#06080c` |
| Accent | white `#ffffff` |
| Polarized / resting | cyan `#3fe0ff` |
| Depolarized | warm `#ff7a3c` |
| Type | Familjen Grotesk |

Tier badges reuse those tokens: `A` cyan, `B` white, `C` warm, `SPEC` magenta.

*An educational exploration. Figures are illustrative, not to scale.*
