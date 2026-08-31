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
summary: >-
  Every reference on this site is machine-resolved against Crossref or PubMed
  and copied in by a script — none is typed by hand, so none can be invented,
  by a person or by a model. Every post carries a tier it inherits rather than
  asserts. This post documents that machinery, the tools it is built from, and
  the division of labour between the author and the assistant.
---

This site is the public face of a private research corpus. The corpus already refuses
to let bad citations in. This post is about the second gate — the one that makes sure
nothing gets *weaker* on the way out the door.

The rule that generates all the others: **a reader must be able to check everything
here, and an error must not be able to survive a commit.**

## How this is written

**The questions, the claims, and every verdict are the author's.** What gets built,
what would count as killing a claim, and what rung a claim sits on are human decisions.
The protocol governing this work forbids an AI from promoting a claim or calling one
falsified — that requires a measurement and a person.

**Drafting and analysis are AI-assisted.** Prose, analysis code and measurement
pipelines are produced with an AI assistant working inside those protocols, then read
and edited by the author. Research assistance runs on a local, zero-retention model on
hardware the author controls.

**Citations are neither hand-written nor model-generated.** Every reference is resolved
against Crossref or PubMed by a separate tool and copied in mechanically. A validator
rejects any citation typed by hand, any bare DOI, and any key not already in the
ledger — so a reference here cannot be invented, by a person or by a model. Where a
source is cited without its full text having been read, the article says so rather than
describing what it found.

**Confidence tiers are copied, not argued.** An article may not claim more confidence
than the weakest claim it rests on, and that is checked before it can publish.

That disclosure used to live in a collapsed drawer in the footer of every page. It
belongs in an article instead, where it can be read rather than dismissed.

## The gate

Publishing is blocked by a script rather than by good intentions. It enforces, among
other things:

- **Cite by key only.** A citation in the body is `key="levin2018"` and nothing else.
  A bare DOI in prose fails the build. So does an inline `Author et al. 2021` — because
  if a name cannot be typed by hand, it cannot be invented. That rule exists because an
  audit once found a paper cited for months under an author who does not exist.
- **Both directions must agree.** Every key declared in a post's front matter is cited
  in the body, and every key cited in the body is declared. A source that is listed but
  never used is dead weight; one used but not listed has no verified provenance.
- **Every key resolves in the ledger**, which is machine-copied from the research repo.
  If a key is not there, it does not exist for publication purposes.
- **No tier laundering.** A post may not assert a confidence tier stronger than the
  weakest claim it rests on.
- **Nothing from a retracted or archived directory**, and no self-asserted `[VERIFIED]`
  badges — that is a check that passes upstream, not a label anyone applies.

The gate runs again in CI against the *committed* data, without access to the private
research repo. That is deliberate: what this site claims must be checkable from the
public repository alone.

## What the gate cannot do

It proves the citation plumbing is sound. It cannot prove the prose is honest. A
correctly-cited paper can still be misrepresented, and only reading catches that.

So there is a manual pass every time, looking for the specific ways a claim outruns its
source: correlation written as causation, animal results written as human results,
in-vitro written as in-vivo, a single study written as consensus, an effect reported
without an effect size. And the standing rule that an abstract is not a paper — if the
full text has not been read, the post may say the work exists but not what it found.

## The tools

Everything here is built from open, inspectable pieces, which is the point:

| | |
|---|---|
| **Site** | Jekyll on GitHub Pages, no custom plugins — so the build is reproducible by anyone with the repository |
| **Gates** | Python, standard library only. No dependencies to install means no excuse not to run them |
| **Registries** | Crossref and PubMed, queried directly. Every author, year, title, journal and identifier on this site came out of one of those responses |
| **Signal analysis** | Welch's method for spectral estimation, FOOOF for separating periodic from aperiodic components, MNE for reference implementations to check against |
| **Public data** | OpenNeuro and PhysioNet, for validating apparatus against recordings made by people with better instruments |
| **Design** | A shared design system with self-hosted OFL typefaces and MIT-licensed icons. Nothing on this site is fetched from a CDN |

The confidence badges are worth one note. The five tiers are distinguishable by colour,
but colour never carries the meaning alone — each badge also ships a glyph and a word,
because the palette fails a colour-blindness check past three categories and a reader
who cannot see the difference should not be the one who loses information.

## How posts stay in sync with the research

A post is not a snapshot that drifts. The chain runs one way:

1. A claim lives in the research repo with its sources, its computed tier, and the
   conditions that would prove it false.
2. A sync script copies **only** what published posts actually reference into this
   repository — the bibliography and the claim tiers, nothing else. It refuses to copy a
   key that never resolved against a registry, or a claim with no tier, or anything from
   a retracted directory.
3. The gate then validates the posts against that copied data, and a separate check
   fails if the copy is stale relative to the research repo.

So a tier displayed on this site is the tier the corpus computed, at the commit the data
was copied. If a claim weakens upstream, the post cannot keep the stronger badge past
the next sync.

**Corrections are amended, never erased.** A factual error gets a dated correction
appended to the post that made it, and if a claim is retracted upstream it is retracted
here in the same change that updates the data. Nothing is quietly edited away.

## What this site is not

It is not a results feed. Most of what gets established here is a fact about an
instrument — that a given piece of hardware cannot reach a given question — and that is
a different statement from the question being answered. The distinction is load-bearing
and it gets its own post.

If something here overreaches its source, that is a defect. The whole point of citing by
key is that you can go and check.

## Note — 2026-08-31

This post replaced a placeholder of the same date that existed to give the publishing
machinery something to validate. The original made no claims and cited two sources
purely to exercise the citation renderer; both have been removed along with it, and the
post is now tiered `A` as a description of settled process rather than `C`. It is filed
under **method** rather than audio-evoked potentials, which is what it was always about.
