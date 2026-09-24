---
title: "Adaptive preregistration when an agent runs the model"
description: >-
  A protocol for simulations and research software in which the predictions, the pass
  criteria and the environment are fixed in git before a language-model agent is allowed to
  run anything a report will cite.
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

A coding agent makes this faster. It can try twenty variants in the time it takes to read one,
and it has no stake in which one gets reported. The fix is the same one experimental science
uses: write down what would count as success before looking, and keep a record that shows the
order things happened in.

This is the protocol used for model experiments here. It adapts published work on adaptive
preregistration for model-based research and on reporting deviations from a preregistered
plan. It is written for simulations and research software, and for the agents that now do much
of the running.

## The five rules

- **No run before the preregistration.** A run whose result a report will cite may not
  execute until `PREREG.md` is complete and tagged.
- **The environment is part of the plan.** The preregistration names the model version it runs
  against, and a lockfile pins every dependency. Adding a dependency afterwards is a deviation.
- **Failure closes the version; it does not edit it.** A failed experiment is closed with its
  failure written up, and the next attempt gets a new experiment ID.
- **Every departure from the plan is logged,** dated, with whether the outcome was known at
  the time.
- **Exploratory work is quarantined.** Anything not in the plan lives in `exploratory/` and is
  labelled exploratory everywhere it is mentioned.

## What makes it adaptive

Modelling is iterative, and a protocol that forbids iteration gets ignored. The rule is about
order, not rigidity.

- A plan may change between stages. The change is committed and tagged *before* the run it
  governs, and logged with the outcome marked as not yet known.
- A plan may also change after a result is seen. It is still logged, with the outcome marked as
  known, and it can never be used to convert a fail into a pass.
- An experiment that fails stays in the record. Nothing is deleted or cleaned up.

## What the preregistration contains

Ten sections, all written before any scoring run:

- the question, as one mechanistic sentence;
- risky, numeric, directional predictions, each with the result that would count against it;
- pass and fail thresholds, with any analytic expectation derived here rather than afterwards;
- the outcomes that would close the line of work;
- the model specification, with every parameter tagged as taken from literature, derived, or
  arbitrary. A pass that depends on an arbitrary parameter does not count;
- the design: conditions, a fixed list of seeds, controls and exclusion rules;
- the environment, down to the execution backend and thread count, because the same seed does
  not give the same result everywhere;
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
timestamp comes from the hosting service, not from the machine that made the commit.

The conversation that produced the work is recorded too. Each turn, the prompt and the agent's
final reply are posted to the same pull request and committed as a log beside the experiment,
with secrets redacted. The diffs are already in the commits.

## Rules for the agent

- Before running anything citable, confirm the plan is complete and tagged. If it is not,
  write it and stop for a human to review.
- Never edit the plan after it is tagged. Changes go in the deviations table.
- Asked to "make it pass" or "try a few values and keep the best", do the runs under
  `exploratory/` and say plainly that they are not preregistered evidence.
- State every open decision before the run that depends on it.
- In every report, state how deeply each source was read: full text, abstract, background
  knowledge, or supplied by the user.
- If a human asks to skip a step, write the skip into the deviations table first, with the
  outcome-known field filled in honestly.

## How it reaches every project

The protocol is maintained in one repository and installed into each project with a small
command-line tool, `kit_ap`. It copies the protocol documents and tools into the project's
`.agents/` folder and records the exact version in a lockfile. It also adds a short managed
block of rules to `AGENTS.md`.

`AGENTS.md` is the file Codex, Copilot and Cursor read, and Claude Code reads it through an
import in `CLAUDE.md`. Every agent sees the same rules whatever tool is open, including in
cloud sandboxes that only have the repository.

Where a tool supports hooks, the rules are backed by code rather than left to the agent:

- conversations are logged automatically;
- Claude Code is told on every prompt whether the current experiment's plan is frozen;
- an optional commit guard refuses outputs for an experiment that has no preregistration tag,
  and refuses any change to a plan after it is tagged;
- at the start of a session, the project checks whether the protocol has changed upstream. The
  agent reports it but does not update without permission.

## Limits

This protects the record, not the idea. A well-preregistered experiment on a wrong model is
still wrong.

A local git date is not tamper-evident. The pull-request receipt is a third-party clock but not
an archive. For outside credibility, the preregistration tag should also be deposited with an
archive, and the plan should say which.

Most of the protocol is instructions an agent is asked to follow. Only the commit guard and the
hooks enforce anything, and only in tools that run hooks. The rest relies on the record making
a violation visible afterwards.
