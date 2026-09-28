---
title: "One question per study: laying out research across repositories"
description: >-
  Why the work here is split into studies, simulators and one shared research corpus,
  and scientific-research-scaffold, the small CLI that sets new repositories up in that
  shape and checks existing ones against it.
date: 2026-09-28 09:00:00 -0600
project: method
status: published
tier: A
claims:
citations:
summary: >-
  A study is one question and everything used to pursue it. Its findings live in one shared
  corpus, its predictions are tagged before anything runs, and nothing in it resolves a path on
  one person's machine. The scaffold writes that down as a protocol and checks it in CI.
---

Preregistration decides the order things happen in inside one experiment. It says nothing about
where the experiment lives. The work here is spread across repositories: a bench in one, a
simulator in another, shared tools in a monorepo, and findings in a separate research corpus.
The layout was being decided one repository at a time, and a decision made that way is a
decision nobody checks.

[scientific-research-scaffold](https://github.com/polarizetech/scientific-research-scaffold)
is the result of writing those decisions down once. It is a protocol for how a piece of research
is laid out across repositories, and `scaffold`, a small command-line tool that sets new
repositories up in that shape and checks existing ones against it.

## What the layout has to protect

Every rule in the protocol exists to keep a result checkable by someone who is not the author,
on a machine that is not the author's. Four things break that quietly:

- **A classification baked into a name.** A simulator here started life as `sim-neural-memory`
  and was later renamed to `neural-memory`. A prefix fixes a category into a name that outlives
  it, and renaming breaks every link and path that pointed at the old one.
- **Two copies of one thing.** A simulator imported as a folder by two studies is two copies
  waiting to diverge.
- **A path on one person's machine.** A result produced through an absolute home-directory path
  is a result nobody else can regenerate.
- **Findings in more than one place.** A research corpus mounted inside each study is several
  working copies of one record, and they drift.

## Two kinds of repository

The protocol has two kinds of repository, declared in a manifest rather than in the name:

- A **study** is one research question and everything used to pursue it: small versioned apps
  for exploring it by hand, simulators for modelling it, preregistered experiments for testing
  it, and pinned datasets to test it against.
- A **sim** is one simulator under adaptive preregistration. Its versions are tags inside one
  repository, never new repositories.

Neither holds findings. A study's findings go to the shared corpus, and the study refers to them
by claim ID. Everything specific to one organisation (which repository is the corpus, which design
system the apps use, where shared tools live) sits in a profile, so the protocol itself stays
generic and can be forked.

An app is for exploring and an experiment is for testing. An app answers "is this worth testing?"
A number from an app is never a finding; a finding comes from a preregistered experiment.

## When a simulator moves out

A simulator starts as a folder inside the study that needs it. It moves to its own repository when
one of three things becomes true: a second study uses it, it needs releases on its own schedule,
or it is shared outside on its own. Tidiness, size and "it might be reused someday" are not
reasons.

`scaffold promote-sim` does the mechanical part. It splits the folder's history into its own
branch, so the new repository keeps every commit, and the study then pins the new repository by
tag like any other dependency.

## Strictness that scales, and rules that don't

How strict a repository has to be depends on what a mistake would cost, and the protocol names
four stages. A sketch owes honest labels and a note of what was not done. Once a number is being
produced, it owes a preregistration before any run that could be quoted. Once another repository
depends on it, or a number from it is quoted, it owes CI, a lockfile and tagged releases. Once
someone outside relies on it, it owes a frozen release, a DOI and an external preregistration.

Some things never relax at any stage: the safety of anyone taking part, honest labels, other
people's data licences, and saying plainly what was not done.

## What the tool does

`scaffold new study` renders a template, makes the first commit, installs the
[preregistration kit](https://github.com/polarizetech/adaptive-preregistration), and prints the
command that would create the repository on GitHub. It leaves the visibility decision to the
person, and it never publishes anything. `scaffold new app` adds the next versioned app, and
`scaffold new sim` adds a simulator, inside a study or as its own repository.

`scaffold check` is the part that matters day to day. It confirms that the manifest is valid,
that the name carries no prefix, and that the kind in the README matches the manifest. It checks
that visibility was decided and dated, that the preregistration kit is installed, and that every
external simulator is pinned to a tag rather than a branch. It checks that the corpus is not a
submodule, and it warns about absolute home-directory paths. It exits nonzero on any failure, so
it can gate CI.

## Adopting it without breaking anything

An existing repository already has working code, frozen results and gates that pass, and adopting
the protocol must not break any of them. Adoption is additive first: add the manifest and point
its entries at wherever things already live, add the kind line and the research register, install
the kit, and run the repository's own gate. It must pass exactly as it did before. Moving folders
into their default places is optional and comes later, one commit per move.

Analyses frozen under an earlier preregistration system stay exactly as they were frozen. They are
listed in the experiment register with a note saying which system froze them, and the kit is used
for new experiments only. Converting a frozen record would change the very thing the freeze exists
to protect.

## Where it comes from, and what it is not

The rules draw on published practice on organising computational projects, scientific computing,
reproducible research, preregistration, adaptive preregistration for model-based research, and
research software as a citable output. The protocol lists those sources in its
[closing section](https://github.com/polarizetech/scientific-research-scaffold/blob/main/PROTOCOL.md#where-this-comes-from).
No published protocol was found for laying out a whole research programme across repositories. The
split into studies, simulators and one shared corpus is an extrapolation from that practice, and it
should be read as one.

## Using it

The protocol is licensed CC BY 4.0 and the code MIT. It needs Python 3.9 or later and git, and
nothing else. To use it for your own work, fork it and write a profile naming your own corpus,
preregistration kit, design system and workbench; any of them can be left empty. The first release,
v0.1.0, is on GitHub at
[polarizetech/scientific-research-scaffold](https://github.com/polarizetech/scientific-research-scaffold).
