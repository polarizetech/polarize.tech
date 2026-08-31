# CLAUDE.md — polarize.tech publishing protocol

Read this before touching `_posts/`, `_drafts/`, or `_data/`.

This site is the **public face** of a private, falsification-first research corpus
(`polarizetech/research`, checked out at `~/Sites/audio-projects/research`, where it is a
submodule of the `audio-projects` monorepo). That repo already
enforces a citation gate. This repo's job is to make sure nothing gets weaker on
the way out the door.

**The rule that generates all the others:** a reader must be able to check
everything on this site, and an error must not be able to survive a commit.

---

## Architecture

| Path | What it is |
|---|---|
| `index.html`, `app.js` | The homepage. Keeps its own `<head>` and hand-built markup — **no layout, and the design is never templated away.** It carries `layout: null` front matter for one reason only: so Liquid runs and the page can list *real* posts instead of hand-maintained links. Adding Liquid beyond the post list and shared includes is out of scope. |
| `design/` | **Vendored, never edited.** A verbatim copy of the monorepo's shared design system (`polarizetech/audio-projects` → `tools/design`, theme INSTRUMENT): `design.css` generated from `tokens.json`, the self-hosted Instrument Serif / Inter / IBM Plex Mono faces, and the icon sprite. Update by re-copying; `scripts/check_design.py` fails if this copy has drifted. |
| `styles.css` | The **project layer only** — what a research blog needs and `design/` does not already provide. No hex literals, no font stacks, no palette: everything is a token. |
| `blog/index.html` | Post index — flat and chronological. |
| `_posts/` | Published posts. `YYYY-MM-DD-slug.md`. |
| `_drafts/` | Work in progress. Never deployed. |
| `_layouts/`, `_includes/` | Shell, post layout, `cite.html`, `references.html`, `ai-disclosure.html`, `postitem.html`. |
| `_config.yml` → `projects:` | Hand-written display labels for the `project:` front-matter key, shown as a badge on each post row. **Not a citation surface** — nothing in it is machine-resolved, and nothing in it may assert a finding. A post whose `project:` has no entry here still lists normally, just without the badge. |
| `_data/citations.yml` | **Generated.** Bibliography, machine-copied from the research ledger. |
| `_data/claims.yml` | **Generated.** Claim tiers + statements from the research repo. |
| `scripts/sync_research.py` | The only path by which research data enters this repo. |
| `scripts/validate_posts.py` | The publication gate. |
| `scripts/check_design.py` | The design gate — no CDN, never-bold, uppercase-is-mono, never-tracked-sans, no raw colour, vendored copy untouched, and a tier badge that carries a glyph as well as a hue. |

GitHub Pages builds this repo with its own Jekyll. **No custom plugins are
possible** — that is why citations are a Liquid include and not a `{% cite %}` tag.

---

## Hard rules

- **Never hand-write a citation.** Not the author, not the year, not the DOI, not
  the journal. Every one of those fields is machine-fetched from Crossref/PubMed
  by `polarizetech/research` and copied here by `sync_research.py`.
- **Cite by key only** — `{% include cite.html key="levin2018" %}`. No inline
  author names, no bare DOIs, no `doi.org` links in prose. The gate rejects all of them.
- **Never edit `_data/*.yml` by hand.** Regenerate it. If a key is missing, the fix
  is in the research repo, not here.
- **Never publish from `RETRACTED/` or `archive/`.** They exist for the git record.
- **Never write `[VERIFIED]`.** It is not a badge anyone asserts; it is a check that
  passes in the research repo.
- **A tier is copied, never argued.** A post cannot claim a stronger tier than the
  weakest claim it rests on.
- **Abstract ≠ paper.** If `full_text_read` is false for a source, you may cite it
  as existing, but you may **not** state what it found, measured, or concluded.
- **Nothing is deleted.** Corrections are amended in place with a dated note.

---

## Design — the rules that come with the system

The look is **not decided here.** It comes from the monorepo's shared design
system, vendored under `design/`. Its own `CLAUDE.md` is the authority; these are
the rules easiest to break from this repo, and `scripts/check_design.py` enforces
each one:

- **Three type roles, no others.** Instrument Serif for headings (`.ui-display`,
  **never uppercased**), Inter for running text, uppercase IBM Plex Mono for
  labels (`.ui-label`). **Uppercase is always the mono face.**
- **The sans is never bold and never tracked.** Hierarchy comes from size, face,
  colour and case. `font-weight: 600` and above exists only inside `@font-face`.
- **No hex in `styles.css`.** Every colour is a token; light and dark both come
  from `design.css`'s three-state root for free.
- **No CDN, ever.** All three faces are self-hosted under `design/fonts/` with
  their OFL texts. A network font also breaks the monorepo's offline rule.
- **A tier badge carries a word and a glyph, never a hue alone** — the five
  epistemic families fail an all-pairs colour-blindness check past three slots.
  Render tiers with `{% include tier.html tier=... %}`, never by hand.
- **A label may never be hidden; its explanation must be.** The tier badge, the
  numbers and the units stay inline. The prose explaining them goes in a
  `<details>` drawer — which is exactly what `ai-disclosure.html` is.

---

## Adding a post — the process

### 1. Establish what is actually being claimed
Before writing a word, work out which **claim IDs** in `~/Sites/audio-projects/research` the post
rests on (`AEP-`, `AUD-`, `BIO-`, `COS-`, `SCH-`).

```bash
ls ~/Sites/audio-projects/research/projects/*/claims/
```

- If the post rests on a formal claim → list its ID in front matter.
- If the post asserts something with **no** claim behind it → **stop.** Either drop
  the assertion, or add the claim to the research repo first (with disproof
  conditions and a computed tier). Do not invent a finding on the website.
- A post that is pure explanation of settled textbook material needs no claim, but
  must be tiered `A` and must contain nothing specific, empirical, or current.

### 2. Choose the tier honestly
Copied from the research repo's tiering, never invented here:

| Tier | Means | Prose must read as |
|---|---|---|
| `A` | Derivable or textbook | statement of fact |
| `B` | Empirical, grounded in resolved full-text sources | reporting a finding |
| `C` | Our own inference from cited work | explicit reasoning, "this suggests" |
| `SPEC` | Speculation | flagged as speculation in the body, not just the badge |

The gate enforces `post tier ≤ weakest claim tier`.

### 3. Confirm every source is in the ledger
Every source must already exist in `~/Sites/audio-projects/research/CITATIONS.yaml`.

```bash
grep -n '^somekey:' ~/Sites/audio-projects/research/CITATIONS.yaml
```

**If it isn't there, it does not exist yet.** Do not add it here. Go to the research
repo and add it properly:

```bash
cd ~/Sites/audio-projects/research
python3 scripts/build_ledger.py --corpus . --out CITATIONS.yaml
python3 scripts/verify_citations.py
```

A source that will not resolve against Crossref or PubMed **never goes on the site**.

### 4. Write the post

```markdown
---
title: "Sentence-case title"
description: >-
  One or two sentences. Shows on the index and in meta description.
date: 2026-07-24 09:00:00 -0600
project: audio-evoked-potentials
status: published          # published | draft
tier: C                    # A | B | C | SPEC
claims:
  - BIO-0001
citations:
  - levin2014
  - levin2018
---
```

Body rules:
- Cite inline with `{% include cite.html key="levin2018" %}` immediately after the
  clause it supports — before punctuation, no space.
- Every key in `citations:` must be cited in the body, and vice versa. Both
  directions are enforced.
- Order `citations:` in the order they first appear — that ordering is the
  superscript numbering.
- `## Heading` for sections. No `#` — the title is the `<h1>`.

### 5. Sync and gate

```bash
python3 scripts/sync_research.py --research ~/Sites/audio-projects/research
python3 scripts/validate_posts.py --strict
```

`--strict` promotes warnings to failures. **Use `--strict` for anything tier `A` or
`B`.** For `C`/`SPEC`, the full-text warnings are acceptable *only* if the prose is
correspondingly hedged.

Then confirm `_data/` is committed in the same change as the post:

```bash
python3 scripts/sync_research.py --research ~/Sites/audio-projects/research --check
```

CI re-runs the gate against the committed `_data/`, without access to the private
research repo. That's deliberate: what the site claims must be checkable from the
public repo alone.

### 6. Preview

```bash
bundle exec jekyll serve --drafts
```

---

## Fact validation — what to check before publishing

The gate is mechanical. It proves the citation *plumbing* is sound; it cannot
prove the prose is honest. Do this pass by hand, every time:

1. **Every sentence that states a fact has a citation or is textbook.** Read the
   post looking only for unsupported specifics — numbers, mechanisms, "studies show".
2. **Each citation supports the specific clause it sits on**, not the general topic.
   A paper about auditory cortex plasticity does not support a claim about gene
   expression timing.
3. **No claim exceeds its source.** Check for: correlation written as causation,
   animal results written as human results, in-vitro written as in-vivo, single
   study written as consensus, effect written without effect size.
4. **Full text read?** If `full_text_read: false`, the post may not characterize what
   the paper found. Read it, update the research repo, re-sync — or hedge the prose.
5. **Check retractions** before publishing anything that leans on a source:
   ```bash
   cd ~/Sites/audio-projects/research && python3 scripts/check_retractions.py
   ```
6. **Disproof condition stated.** For tier `B`/`C` posts, the body should say what
   would make it wrong. If you can't write that sentence, the claim isn't ready.
7. **Read it as an adversary.** What would the strongest good-faith critic say? If
   the answer is "that's overstated," it is.

---

## Correcting a published post

Never silently edit a factual error. In the post body, append:

```markdown
## Correction — 2026-08-02
The original text stated X. That was wrong: [what and why].
```

If a claim is retracted upstream, retract it here in the same commit that updates
`_data/`, and record it in `AMENDMENTS.md` in the research repo. Amend, timestamp,
quarantine — never delete.
