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
| `index.html` | The home page — **now a normal Jekyll page** (`layout: home`), not a standalone file. Since 2026-09-25 it is a three-section summary: the latest posts (no topic badges), the latest rants as portrait cards, and the most recently active repos with their latest merged PR. It is **not** paginated; `/blog/` is. The hand-built one-pager, its hero canvas and `app.js` were removed on 2026-08-31 when the site became a blog; the earlier "don't Jekyll-ify it" rule died with the page it protected. |
| `_layouts/`, `_includes/` | `default.html` is the sidebar + main shell. `sidebar.html` (brand, author note, topics, RSS/GitHub), `postlist.html`, `postitem.html`, `tier.html`, `cite.html`, `references.html`. |
| `blog/topics/*.html` | One page per `project:` (the sidebar shows Topics only in the blog section). **Written by hand because GitHub Pages runs no plugin that can generate them** — `jekyll-paginate` v1 is the only paginator available and it paginates one index (`blog/index.html`) and nothing else. Add a page whenever you add a project. |
| `design/` | **A git submodule: [`polarizetech/polarize-ui`](https://github.com/polarizetech/polarize-ui), pinned to a release tag, never edited here.** The same repo the monorepo mounts at `tools/design`. The site serves `design.css` (tokens, type, base components, theme INSTRUMENT), `publication.css` (the blog components — `ui-shell`, `ui-sidebar`, `ui-postlist`, `ui-article`, `ui-prose`, `ui-source`, `ui-cite`, `ui-claims`, `ui-refs`, `ui-parts`, `ui-pager`, `ui-form`, `ui-footer`, extracted from this site on 2026-09-25), `design.js`, the self-hosted faces and the icon sprite; `_config.yml` excludes the rest (React source, Storybook). **Update** with `git -C design fetch --tags && git -C design checkout vX.Y.Z`, then commit the pointer. A fresh clone needs `git clone --recurse-submodules` (GitHub Pages fetches public submodules itself). `scripts/check_design.py` fails if `design/` is not the submodule, has local edits, or is not on a tag. |
| `styles.css` | The **site layer only** — the homepage sections, the contact page width, one post's figure, a category pill, and (for now) the rant cards, changelog entries, repo cards and the version-history diff. Every reusable component lives in `design/publication.css`; **a new component that another site could use goes to polarize-ui, not here.** No hex literals, no font stacks, no palette: everything is a token. |
| `blog/index.html` | The paginated post list (`paginate_path: /blog/page:num/` — jekyll-paginate v1 pages only the `index.html` in that directory). |
| `_essays/`, `rants/index.html` | **Rants** — short dictated pieces, served at `/rants/`. A separate collection (`essays`), not posts: no claims, no citations, always tier SPEC, never in `site.posts` or the topic pages. The gate's RULE E enforces all of it. |
| `changelog/`, `_layouts/changelog.html`, `_layouts/repo.html` | The paginated changelog (merged PRs in public polarizetech repos, each entry in full) and one feature page per public repo at `/changelog/<repo>/`. **Every `index.html` under `changelog/` is a generated stub** — never edit or add one by hand. |
| `_data/changelog.json`, `_data/repos.json` | **Generated** by `scripts/sync_changelog.py` from GitHub (public repos only), together with the stubs above. `.github/workflows/changelog.yml` re-runs it once a day (and on demand). |
| `_data/history.json`, `_includes/history.html` | **Generated** by `scripts/sync_history.py` from git: every revision of every post and rant, with word-level diffs and an LLM co-author flag (from `Co-Authored-By` trailers only). Rendered as the version drawer at the foot of each page and the `vN` in its meta line. `.github/workflows/history.yml` regenerates it after every push touching `_posts/` or `_essays/`. |
| `_posts/` | Published posts. `YYYY-MM-DD-slug.md`. |
| `_drafts/` | Work in progress. Never deployed. |
| `_config.yml` → `projects:` | Hand-written display labels for the `project:` front-matter key, shown as a badge on each post row. **Not a citation surface** — nothing in it is machine-resolved, and nothing in it may assert a finding. A post whose `project:` has no entry here still lists normally, just without the badge. |
| `_data/citations.yml` | **Generated.** Bibliography, machine-copied from the research ledger. |
| `_data/claims.yml` | **Generated.** Claim tiers + statements from the research repo. |
| `scripts/sync_research.py` | The only path by which research data enters this repo. |
| `scripts/sync_changelog.py`, `scripts/sync_history.py` | The only paths by which changelog/repo data and version history enter this repo. Stdlib only. |
| `scripts/validate_posts.py` | The publication gate. |
| `scripts/check_design.py` | The design gate — no CDN, never-bold, uppercase-is-mono, never-tracked-sans, no raw colour, `design/` is the pinned polarize-ui submodule with no local edits, every stylesheet cache-busted, and a tier badge that carries a glyph as well as a hue. |

GitHub Pages builds this repo with its own Jekyll. **No custom plugins are
possible** — that is why citations are a Liquid include and not a `{% cite %}` tag.


**Changing a component?** Do it upstream in polarize-ui. Every push to its `main` is a public release, and outside users are promised that a patch never breaks. **Read the first section of its `CLAUDE.md` (or `AGENTS.md`) before committing there:** mark breaking changes with `!:` or `BREAKING CHANGE:`, and prefer a deprecated alias to a removal. This repo picks up new releases by itself once a day (`.github/workflows/polarize-ui.yml`). If that run fails, a release broke something here and this repo needs a migration commit.

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

## Claude Code responses — two bullet lists, nothing else (operator, 2026-09-01)

Same rule as the monorepo's `CLAUDE.md`; repeated here because this repo is often
opened on its own.

1. **What was done** — one bullet per thing. Past tense, concrete.
2. **What I need from you** — questions, decisions, anything blocked on the operator.
   Say what changes depending on the answer. If nothing is needed, say so in one line.
3. *(only when it applies)* **Not done, and not blocked on you** — skipped, deferred or
   impossible, no operator input required. Omit the list when empty, which is most of
   the time.

**Usually only the first two lists appear.** No prose summaries, no narrative walkthroughs,
no headed essay-style status reports — they bury the two things actually being read.

A bullet may carry a short sub-bullet where a decision needs context; it may not carry a
paragraph. **Failures and corrections are bullets in list 1**, stated plainly.

**This is a response-format rule, not a work rule.** It does not shorten the work or
license skipping any gate.

---

## Design — the rules that come with the system

The look is **not decided here.** It comes from the monorepo's shared design
system, the polarize-ui submodule under `design/`. Its own `CLAUDE.md` is the authority; these are
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

**Drafting a post from sources:** use the monorepo's `tools/opendraft` with target `blog`
(`~/Sites/audio-projects/tools/opendraft/PIPELINE.md`). Its `render` writes the cite includes,
the front matter (citations in first-appearance order, `status: draft`) and an AI-use line, and
refuses any DOI not in the research ledger. Output goes to `_drafts/`; the tier it writes is a
placeholder to replace with the weakest claim's tier. Steps 1–3 above still apply.

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
