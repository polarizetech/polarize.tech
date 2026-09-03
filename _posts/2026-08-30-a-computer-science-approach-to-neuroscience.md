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

Almost everything on this site is an open question. Not one of them has been settled
here, and most of them are not settled anywhere.

What this post describes is the method — how the questions get picked, built for, and
narrowed. It asserts nothing about biology, so it cites nothing. Everything else here
is held to a different standard, and the difference is the point.

## Build first, narrow later

The order matters, and it is the opposite of how caution usually works.

**First, anything goes.** An idea is not required to be plausible, funded,
peer-reviewed, or even likely in order to be built. Absence of evidence is a reason
to construct something, not a reason to decline. Traditional practice, fringe claims,
"I want to hear what this sounds like" — all sufficient. The cost of building a thing
that turns out to be nothing is a weekend. The cost of never building it is that you
cannot tell the difference between a bad idea and an untried one.

**Then, narrow.** Every constructed thing is aimed at a claim that could kill it, and
the conditions that would kill it are written down **before** the measurement, not
after. That machinery is unglamorous and it is most of the work:

- A **viability gate** runs before anything is built, and asks four questions of the
  instrument you actually own rather than the one you wish you had. Is the thing you
  want to read even inside the band the hardware passes? Is the effect above a
  *measured* noise floor, in a session a human would sit through? Can the stimulus be
  produced, and what does it cost? Is there a control that isolates the claim from
  everything else? Any "no" stops the build. This rule was bought expensively: an
  entire apparatus was once written, and *then* the gate was computed, and the
  arithmetic that killed the build was four lines long.
- **Kill conditions are pre-registered.** A claim arrives with the list of results
  that would end it, fixed before data exists. A hypothesis you cannot describe the
  death of is not being tested.
- **Blind reads are structural, not promised.** Where a judgement could leak, the
  analysis is built so the answer is not reachable from it — the truth lives in a
  file the reading code does not name, and the reveal refuses while any case is still
  uncalled. "We were careful" is not a control.
- **A negative is worth exactly what the test's power was.** A non-detection from an
  instrument that could never have seen the effect is not evidence of absence; it is
  a gap in the instrument. Those two get different words and are never merged.
- **Refusals live in code.** Where a mistake would be invisible in prose, the
  software raises instead. A predicted value may not be styled as a measured one. A
  confidence tier may not be argued upward.

## What "narrowed" actually means — and what it does not

This is worth being exact about, because the obvious reading is wrong.

**Nothing here has been falsified.** Not one claim under test has been shown false
about the world. What gets established is almost always something about the
*apparatus* — and those are completely different statements.

The ladder in use, roughly weakest to strongest:

| rung | what it means |
|---|---|
| **untested** | stated, with kill conditions. Nothing has been run. |
| **instrumented** | the rig exists and records; the decisive test has not been run |
| **flagged** | forward arithmetic says this bench probably cannot reach the question. **A flag is a caution, not a verdict** |
| **parked** | the bench provably cannot ask it with the hardware on the desk. **The claim itself is untouched** |
| **attempted** | a real measurement ran to completion. The claim survived, or the test turned out to be underpowered |
| **falsified** | shown false. Requires a measurement, and a human decision. **Currently: none** |

The distinction that took a while to get right: **a door closed for this bench is not
a door closed in science.** When a gate fails, the honest sentence is "the amplifier
in front of me filters away the thing I wanted to read, and no amount of processing
downstream recovers it" — a fact about a $70 board. The underlying question stays
exactly as open as it was, and someone with better hardware should go ask it.

Getting this backwards is easy and it is the most common way a research programme
lies to itself. An agent working on this corpus once marked several claims
*falsified* on forward arithmetic alone, with no measurement taken. The protocol now
forbids it: arithmetic flags, it does not close, and the promotion to *falsified*
needs a measurement and a person.

So the useful output is rarely "this is false." It is usually:

- here is the number that says this instrument cannot reach it,
- here is precisely what would change that,
- and here is what it would cost.

That is worth publishing. It saves the next person the months, and it is the part
nobody writes down.

## Full-stack, on purpose

The other half of the approach is a refusal to specialise, and it comes from
software. A full-stack developer is not the best in the world at any one layer. They
are someone who can follow a problem *down* — from the interface, through the
protocol, into the transport, to the hardware — without handing it off at every
boundary, because most real bugs live exactly where the hand-offs happen.

Applied here, one question routinely crosses:

**neuroscience** · **cardiology and electrophysiology** · **audiology and
psychoacoustics** · **molecular biology and gene regulation** · **developmental
bioelectricity** · **acoustics and archaeoacoustics** · **geophysics and space
weather** · **electromagnetics and propagation** · **signal processing** ·
**information theory** · **statistics and meta-research** · **materials science** ·
**and the history of the practices that got here first**

Those are not a list of interests. They are the layers one question passes through.
Ask whether a sound can change what a cell transcribes, and you are immediately in
acoustics (what leaves the speaker), psychoacoustics (what the ear encodes), systems
neuroscience (where it lands), electrophysiology (how it is measured), signal
processing (whether the measurement is real), molecular biology (what a durable
change would even look like), and statistics (whether you would know). Hand that
question off at each boundary and the parts come back individually correct and
jointly meaningless.

The cost is real and worth stating: nobody working this way is the strongest person
in any one of those rooms. The compensation is that the boundaries get looked at, and
the boundaries are where this particular question lives.

## What that produces

Open questions, narrowed carefully, with the reasoning and the arithmetic in public —
and a clear line between what the world has not told us yet and what this bench
cannot currently hear.

The posts that follow are those questions.
