---
title: "How research gets published here"
description: >-
  The publishing protocol behind this site: a citation gate that makes an
  invented reference impossible, a confidence tier that is computed rather than
  claimed, and an honest account of what is written by a human and what is not.
date: 2026-07-24 09:00:00 -0600
project: method
status: published
tier: A
claims:
citations:
image: /assets/posts/card-catalog.jpg
image_alt: >-
  An open library card catalog drawer, index cards standing upright in a long wooden tray.
image_credit: Michael Holley
image_license: Public domain
image_license_url: https://en.wikipedia.org/wiki/Public_domain
image_source_url: https://commons.wikimedia.org/wiki/File:Copyright_Card_Catalog_Drawer.jpg
summary: >-
  Every reference on this site is machine-resolved against Crossref or PubMed
  and copied in by a script — none is typed by hand, so none can be invented,
  by a person or by a model. Every post carries a tier it inherits rather than
  asserts. This post documents that machinery, the tools it is built from, and
  the division of labour between the author and the assistant.
---

How this site publishes. The rule that generates the others: a reader must be able to check
everything here, and an error must not survive a commit.

## How this is written

**Questions, claims and verdicts are the author's.** What gets built, what would count as
killing a claim, and what rung a claim sits on are human decisions. The protocol forbids an
AI from promoting a claim or calling one falsified — that needs a measurement and a person.

**Drafting and analysis are AI-assisted.** Prose, analysis code and measurement pipelines
are produced with an AI assistant working inside those protocols, then read and edited.
Research assistance runs on a local, zero-retention model on hardware the author controls.

**Citations are neither hand-written nor model-generated.** Every reference is resolved
against Crossref or PubMed by a separate tool and copied in mechanically. A validator
rejects any citation typed by hand, any bare DOI, and any key not already in the ledger. A
reference here cannot be invented, by a person or a model.

**Tiers are copied, not argued.** A post may not claim more confidence than the weakest
claim it rests on, and that is checked before it publishes.

## The gate

Publishing is blocked by a script, not by intentions.

- **Cite by key only.** A citation is a key and nothing else. A bare DOI fails the build; so
  does an inline `Author et al. 2021`. If a name cannot be typed by hand it cannot be
  invented. That rule exists because an audit once found a paper cited for months under an
  author who does not exist.
- **Both directions must agree.** Every declared key is cited in the body; every cited key
  is declared. A listed-but-unused source is dead weight; a used-but-unlisted one has no
  verified provenance.
- **Every key resolves in the ledger**, machine-copied from the research repo. Not there
  means it does not exist for publication.
- **No tier laundering.** A post may not assert a tier stronger than its weakest claim.
- **Nothing from retracted or archived directories**, and no self-asserted `[VERIFIED]` —
  that is a check that passes upstream, not a label anyone applies.

CI re-runs the gate against the *committed* data, without access to the private research
repo. What this site claims must be checkable from the public repository alone.

## What the gate cannot do

It proves the citation plumbing is sound. It cannot prove the prose is honest. A correctly
cited paper can still be misrepresented, and only reading catches that.

So there is a manual pass every time, looking for the specific ways a claim outruns its
source: correlation written as causation, animal results as human results, in-vitro as
in-vivo, a single study as consensus, an effect without an effect size.

And the standing rule: **an abstract is not a paper.** If the full text has not been read,
the post may say the work exists but not what it found. Whether a paper has been read is an
assertion by a person, so no script writes that field.

## The tools

| | |
|---|---|
| **Site** | Jekyll on GitHub Pages, no custom plugins — the build is reproducible by anyone with the repository |
| **Gates** | Python, standard library only. No dependencies to install means no excuse not to run them |
| **Registries** | Crossref and PubMed, queried directly. Every author, year, title and identifier here came out of one of those responses |
| **Signal analysis** | Welch's method for spectral estimation, FOOOF for separating periodic from aperiodic, MNE for reference implementations to check against |
| **Public data** | OpenNeuro and PhysioNet, for validating apparatus against recordings made on better instruments |
| **Design** | A shared design system, self-hosted OFL typefaces, MIT-licensed icons. Nothing is fetched from a CDN |

The confidence badges carry a glyph and a word, not only a colour: the palette fails a
colour-blindness check past three categories, and a reader who cannot see the difference
should not lose information.

## How posts stay in sync with the research

One direction only.

1. A claim lives in the research repo with its sources, its computed tier, and the
   conditions that would prove it false.
2. A sync script copies **only** what published posts reference — bibliography and claim
   tiers, nothing else. It refuses a key that never resolved against a registry, a claim
   with no tier, or anything from a retracted directory.
3. The gate validates posts against that copy, and a separate check fails if the copy is
   stale.

A tier shown here is the tier the corpus computed at the commit the data was copied. If a
claim weakens upstream, the post cannot keep the stronger badge past the next sync.

**Corrections are amended, never erased.** A factual error gets a dated correction appended
to the post that made it. A claim retracted upstream is retracted here in the same change
that updates the data.

## What this site is not

Not a results feed. Most of what gets established here is a fact about an instrument — that
a given piece of hardware cannot reach a given question — which is a different statement
from the question being answered.

If something here overreaches its source, that is a defect. The point of citing by key is
that you can go and check.

## Note — 2026-08-31

This replaced a placeholder of the same date that existed to give the machinery something to
validate. The original made no claims and cited two sources only to exercise the citation
renderer; both were removed with it. Retiered `C` to `A`, and refiled under **method**.
