---
title: "A computer science approach to neuroscience"
description: >-
  How this work is done: build first and narrow later, write down what would kill
  a claim before measuring, and refuse to specialise. A method post — it makes no
  empirical claim and cites nothing, because there is nothing here to cite.
date: 2026-08-30 09:00:00 -0600
project: method
status: published
tier: A
claims:
citations:
image: /assets/posts/oscilloscope-waves.jpg
image_alt: >-
  An oscilloscope screen showing a triangular wave above a square wave against the instrument graticule.
image_credit: Xato
image_license: CC0
image_license_url: https://creativecommons.org/publicdomain/zero/1.0/
image_source_url: https://commons.wikimedia.org/wiki/File:Triangular_wave_and_square_wave_on_oscilloscope_screen.jpg
summary: >-
  The questions here are open — none of them has been settled on this bench, and
  most are not settled anywhere. What follows is the method: build first and
  narrow later, write down what would kill a claim before measuring it, and
  follow a question down through every layer rather than handing it off at each
  boundary. The distinction that took longest to get right is that a door closed
  for this bench is not a door closed in science.
---

Method. No empirical claim, no citations — there is nothing here to cite.

Almost everything on this site is an open question. None has been settled here, and most
are not settled anywhere.

## Build first, narrow later

**First, anything goes.** An idea need not be plausible, funded or peer-reviewed to be
built. Absence of evidence is a reason to construct something. Traditional practice, fringe
claims, "I want to hear what this sounds like" — all sufficient. A thing that turns out to
be nothing costs a weekend. Never building it costs the ability to tell a bad idea from an
untried one.

**Then, narrow.** Every built thing is aimed at a claim that could kill it, and the killing
conditions are written down *before* the measurement.

- **A viability gate** runs before anything is built. Four questions, asked of the
  instrument actually owned: is the target inside the band the hardware passes; is the
  effect above a *measured* noise floor in a session a human would sit through; can the
  stimulus be produced, at what cost; is there a control isolating the claim. Any "no" stops
  the build. Bought expensively — an entire apparatus was written, *then* the gate computed,
  and the arithmetic that killed it was four lines.
- **Kill conditions are pre-registered.** A claim arrives with the results that would end
  it, fixed before data exists. A hypothesis whose death you cannot describe is not being
  tested.
- **Blind reads are structural.** Where judgement could leak, the answer is not reachable
  from the analysis: the truth lives in a file the reading code does not name, and the
  reveal refuses while any case is uncalled. "We were careful" is not a control.
- **A negative is worth the test's power.** A non-detection from an instrument that could
  never have seen the effect is a gap in the instrument, not evidence of absence. Different
  words, never merged.
- **Refusals live in code.** A predicted value may not be styled as a measured one. A tier
  may not be argued upward.

## What "narrowed" means, and does not

**Nothing here has been falsified.** No claim under test has been shown false about the
world. What gets established is almost always about the *apparatus*.

| rung | meaning |
|---|---|
| **untested** | stated, with kill conditions. Nothing run. |
| **instrumented** | the rig exists and records; the decisive test has not run |
| **flagged** | forward arithmetic says this bench probably cannot reach it. **A caution, not a verdict** |
| **parked** | the bench provably cannot ask it with the hardware on the desk. **The claim is untouched** |
| **attempted** | a real measurement ran to completion. The claim survived, or the test was underpowered |
| **falsified** | shown false. Requires a measurement and a human decision. **Currently: none** |

**A door closed for this bench is not a door closed in science.** When a gate fails, the
honest sentence is that the amplifier in front of me filters away what I wanted to read, and
no processing downstream recovers it. That is a fact about a board. The question stays as
open as it was.

Getting this backwards is the most common way a research programme lies to itself. An agent
on this corpus once marked several claims *falsified* on forward arithmetic alone, with no
measurement. The protocol now forbids it: arithmetic flags, it does not close.

So the useful output is rarely "this is false." It is usually the number that says the
instrument cannot reach it, what would change that, and what it would cost. That saves the
next person the months, and nobody writes it down.

## Full-stack, on purpose

A refusal to specialise, taken from software. A full-stack developer is not the strongest at
any one layer; they can follow a problem *down* — interface, protocol, transport, hardware —
without handing it off, because most real bugs live at the hand-offs.

One question here routinely crosses: **neuroscience · cardiology and electrophysiology ·
audiology and psychoacoustics · molecular biology and gene regulation · developmental
bioelectricity · acoustics and archaeoacoustics · geophysics and space weather ·
electromagnetics and propagation · signal processing · information theory · statistics and
meta-research · materials science · and the history of the practices that got here first.**

Not a list of interests — the layers one question passes through. Ask whether a sound can
change what a cell transcribes and you are immediately in acoustics (what leaves the
speaker), psychoacoustics (what the ear encodes), systems neuroscience (where it lands),
electrophysiology (how it is measured), signal processing (whether the measurement is real),
molecular biology (what a durable change looks like) and statistics (whether you would
know). Hand it off at each boundary and the parts come back individually correct and jointly
meaningless.

The cost: nobody working this way is the strongest person in any of those rooms. The
compensation: the boundaries get looked at, and the boundaries are where the question lives.

## What that produces

Open questions, narrowed carefully, with the reasoning and the arithmetic in public — and a
clear line between what the world has not told us yet and what this bench cannot hear.
