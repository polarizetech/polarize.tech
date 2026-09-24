---
title: "Adaptive preregistration: predict first, then run the code"
description: >-
  A protocol for simulations and research software in which the predictions, the pass
  criteria and the environment are fixed in git before anything a report will cite is
  allowed to run.
date: 2026-09-24 12:00:00 -0600
project: method
status: published
tier: A
claims:
citations:
summary: >-
  Write the prediction and the pass criteria first, tag them, then run. Plans may change, but
  every change is dated, says whether the result was already known, and cannot turn a fail
  into a pass.
---

A simulation can be tuned until it agrees with you. Each choice is small: a seed, a threshold,
an analysis window, a parameter nobody measured. None of them looks like cheating, and
together they can manufacture any result.

Software makes this cheap. A new variant costs seconds, and the run that finally agrees looks
exactly like one that was planned. The fix is the same one experimental science uses: write
down what would count as success before looking, and keep a record that shows the order things
happened in.

This is the protocol used for model experiments here. It adapts published work on adaptive
preregistration for model-based research and on reporting deviations from a preregistered
plan. It is written for simulations, analysis pipelines and research software, whoever or
whatever is doing the running. The full protocol, with its sources and how deeply each was read,
is in the [protocol document](https://github.com/polarizetech/kit-adaptive-preregistration/blob/main/modules/prereg/protocols/PREREG_PROTOCOL.md).

## The five rules

- **No run before the preregistration.** A run whose result a report will cite may not
  execute until `PREREG.md` is complete and tagged.
- **The environment is part of the plan.** The preregistration names the model version it runs
  against, and a lockfile pins every dependency. Adding a dependency afterwards is a deviation.
- **Failure closes the version; it does not edit it.** A failed experiment is closed with its
  failure written up, and the next attempt gets a new experiment ID. Every ID stays in a
  registry, so a pass after earlier failures is reported as one attempt among several.
- **Every departure from the plan is logged,** dated, with whether the outcome was known at
  the time.
- **Exploratory work is quarantined.** Anything not in the plan lives in `exploratory/` and is
  labelled exploratory everywhere it is mentioned.

## What makes it adaptive

Modelling is iterative, and a protocol that forbids iteration gets ignored. The rule is about
order, not rigidity.

- A plan may change between stages. Each stage says in advance which result leads to which
  change. The change is committed and tagged *before* the run it governs, and logged with the
  outcome marked as not yet known.
- A plan may also change after a result is seen. It is still logged, with the outcome marked as
  known, and it can never be used to convert a fail into a pass.
- An experiment that fails stays in the record. Nothing is deleted or cleaned up.

## What the preregistration contains

Eleven sections, all written before any scoring run:

- the question, as one mechanistic sentence;
- risky, numeric, directional predictions, each with the result that would count against it;
- pass and fail thresholds for each estimated quantity, with its uncertainty: a pass means the
  interval clears the threshold, not just the point estimate;
- the outcomes that would close the line of work;
- the model specification, with every parameter tagged as taken from literature, derived, or
  arbitrary;
- the design: conditions, a fixed list of seeds, controls, exclusion rules, a justified number of
  runs with a stopping rule, and a sensitivity analysis for every arbitrary parameter. A pass that
  flips to a fail anywhere in a preregistered range is reported as not robust;
- the environment, down to the execution backend and thread count, because the same seed does
  not give the same result everywhere;
- what the authors already knew: which target data they had seen, and which targets the model
  was calibrated to rather than tested against;
- any adaptive stages, every decision the specification left open, and how the plan was
  timestamped.

The results file answers the plan line by line. It also has to list the patterns the model
failed to reproduce, what only worked because it was tuned, and the result of every control.

## The record

Git holds the ordering. Each milestone is an annotated tag:

| Tag | Marks |
|---|---|
| `model-vX.Y.Z` | a change to the model that alters its output |
| `<EID>-prereg` | the complete plan, lockfile and configuration |
| `<EID>-interim-N` | a plan revision, before the run it governs |
| `<EID>-run` | the outputs and the results file |
| `<EID>-closed` | the end of the experiment, pass or fail |

Each experiment gets its own branch and draft pull request. Tagging a milestone posts a receipt
to the pull request with the commit and a checksum of the plan and the lockfile. The comment's
timestamp comes from the hosting service, not from the machine that made the commit, so it shows
the plan existed by then.

When the work is done with a coding assistant, the conversation is recorded too: each prompt
and reply is posted to the same pull request and committed beside the experiment, with secrets
redacted.

## Rules for whoever runs it

The same rules apply to a person at the keyboard, a script, or a coding assistant.

- Before running anything citable, confirm the plan is complete and tagged. If it is not,
  write it and stop for someone else to review.
- Never edit the plan after it is tagged. Changes go in the deviations table.
- Asked to "make it pass" or "try a few values and keep the best", do the runs under
  `exploratory/` and say plainly that they are not preregistered evidence.
- State every open decision before the run that depends on it.
- In every report, state how deeply each source was read: full text, abstract, background
  knowledge, or supplied by the user.
- If anyone asks to skip a step, write the skip into the deviations table first, with the
  outcome-known field filled in honestly.

## How it reaches every project

The protocol is maintained in one public repository,
[KIT Adaptive Preregistration](https://github.com/polarizetech/kit-adaptive-preregistration), and
installed into each project with a small command-line tool, `kit_ap`. It copies the protocol documents and tools into the project's
`.agents/` folder and records the exact version in a lockfile. It also writes the rules into
`AGENTS.md`, so coding assistants working in the repository read the same rules a person
would.

Some of the rules are backed by code rather than left to good intentions:

- an optional commit guard refuses outputs for an experiment that has no preregistration tag,
  and refuses any change to a plan after it is tagged (like any git hook, it can be bypassed);
- where the tools support hooks, the current experiment's plan status is surfaced on every
  session, and assistant conversations are logged automatically;
- at the start of a session, the project checks whether the protocol has changed upstream, and
  reports it without updating on its own.

## Limits

This protects the record, not the idea. A well-preregistered experiment on a wrong model is
still wrong.

A local git history is not tamper-evident: tags can be moved unless they are signed and
protected on the host. The pull-request receipt is a third-party clock but not an archive, since
comments can be edited, and it can't show that nothing ran before the plan. For outside
credibility, the preregistration tag should also be deposited with an archive, and the plan should
say which.

Nothing stops a new attempt after a failure. The registry only makes the attempts visible, so a
reader can weigh a pass against them.

Most of the protocol is rules that people and tools are asked to follow. Only the commit guard
and the hooks enforce anything, and the hooks only in tools that run them. The rest relies on the
record making a violation visible afterwards.

## Update — 2026-09-24

The kit's repository is now public and linked from the section on how the protocol reaches
each project.

After a methods review, the protocol was tightened, and this post was revised to match. It now
describes: the registry of attempts, uncertainty in the pass criteria, a justified run count, a
sensitivity rule fixed in advance, a section on prior knowledge and calibration (eleven sections,
previously ten), and decision rules for adaptive stages. The limits section now says more about
what the record can and can't prove. Previously the post said a pass that depends on an arbitrary
parameter does not count; the rule is now that a pass which flips within a preregistered range is
reported as not robust.
