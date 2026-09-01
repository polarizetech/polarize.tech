---
title: "What software can and cannot buy you"
description: >-
  Two months of trying to push a phone magnetometer past what its hardware
  should allow — what the discipline actually bought, how it compares to the
  other implementations, and the wall that no amount of code moves.
date: 2026-09-01 09:00:00 -0600
project: bioem-propagation
status: published
tier: C
claims:
citations:
  - roth2024
  - odenwald2022
summary: >-
  Every phone has a magnetometer in it. The interesting question is not whether
  you can read a body with one — you cannot — but how far careful software
  gets you before the hardware stops you, and how you would know which of the
  two you were up against. This is what was tried, what the other
  implementations do, and where the line turned out to be.
---

There is a magnetometer in every phone, sitting there being a compass. The question
that got me started was whether disciplined software could push it somewhere it was
never meant to go.

The short version: **software buys you enormously more than I expected, and none of it
is sensitivity.** This is a walk through what was actually tried, what the other
implementations in this space do, and where the line sits.

## The mentality

The instinct when you have inadequate hardware is to look for the clever trick — the
processing step that recovers what the sensor missed. That instinct is mostly wrong, and
it took a while to internalise why.

What software can do, it turns out, is a long list:

- **Verify rather than assume.** Every parameter you did not measure is a parameter you
  are guessing at.
- **Know its own noise**, in the band that matters rather than across the whole
  spectrum.
- **Refuse to believe itself** — surrogate nulls, held-out thresholds, injection tests
  that establish what the pipeline would have detected.
- **Keep everything on one clock**, so that motion can be separated from field.
- **Report its own gaps** instead of quietly interpolating them.

What software cannot do is manufacture information that never entered the converter. If
the quantisation step is larger than the thing you want to see, no amount of averaging,
whitening or filtering invents it. That is the whole lesson and it took building the
thing to learn it properly.

## The other implementations, and what each one is for

I did not build this in a vacuum, and the most useful hours were spent reading what
other people had already done. Four are worth documenting, because each is built for a
different purpose and each is better than mine at its own job.

**NOAA's CrowdMag** collects smartphone magnetometer readings as a distributed
geomagnetic survey. Its defining property is that **it validates every contribution
against a field model** — it knows whether a reading is *correct*, in absolute terms.
Mine does not, and has never checked.

**phyphox and Physics Toolbox** are physics-education tools. Their defining property is
that they **expose the raw and the calibrated channel side by side**, switchable in two
taps. That distinction matters more than it sounds and I will come back to it.

**The NASA/Odenwald citizen-science work** characterises what a phone magnetometer can
do for space-weather monitoring {% include cite.html key="odenwald2022" %}, and is the
closest published reference point for the noise performance of this class of sensor.

**ADVIO** is a visual-inertial odometry research dataset — not a magnetometry project at
all, but it ships real multi-sensor phone recordings under an open licence, which makes
it a cross-device control for anyone testing whether an effect is a property of one
handset or of the platform.

**How I use them.** CrowdMag is the model for an absolute-accuracy check I have not yet
built. phyphox is the reason I know the dual-channel decision is a defect and not a
preference. ADVIO is the corpus that lets a finding be checked on hardware I do not own.
None of that required permission; all of it required reading.

## What was actually tried

**Measure the delivered sample rate, per recording.** Not the requested rate — the
delivered one. It is not the same number, the difference is systematic, and every
frequency-domain result is wrong by that factor if you assume instead of check. None of
the implementations above verifies this per record.

**Measure the noise floor in-band, not broadband.** This one produced the most useful
correction of the whole project, in the opposite direction from the one you would fear:
a broadband figure **overstated** the noise at the frequency of interest by a large
factor, because real recordings are drift-dominated. Carrying the wrong number around
declares runnable experiments unrunnable. An instrument that makes you *too* pessimistic
kills experiments silently, and nothing in the output tells you it happened.

**Build the nulls before the result.** Four families of surrogate, thresholds taken as a
maximum statistic over the entire search rather than per-cell, and a refusal to quote a
false-alarm bound above a stated ceiling. The comparators run quality control against a
model; none of them runs a null. This is the single biggest difference and it is
entirely software.

**Validate by injection.** Put a known signal into the real path and measure what
fraction the pipeline recovers. Without this you have no idea whether a null result
means absence or means your analysis would have missed it anyway.

**One monotonic timebase across every sensor stream.** Magnetometer, accelerometer,
gyroscope, attitude — all on one clock. Almost every useful discriminator for
separating "the phone moved" from "the field changed" depends on this, and it is
impossible to retrofit.

## Where it is worse, including one real defect

Being honest about this is most of the value of having done the comparison.

**The calibrated channel is not logged, and that is a genuine defect.** Recording the raw
channel as primary is right — calibration is a filter with unpublished behaviour, and you
cannot undo it. But the calibrated channel alongside it is a *free diagnostic*, phyphox
does it, and its absence directly caused a multi-day misattribution: a large static field
offset was read as an external accessory when it was internal to the device. A diagnostic
channel I chose not to record would have shown that immediately. It is the cheapest fix
on my list and it needs an app build.

**No absolute accuracy validation.** CrowdMag would have caught the same thing a
different way.

**One operating system, and a private archive.** The cross-device control leans on other
people's corpora because mine is not shareable.

**Dropped samples across long recordings**, reported rather than hidden — and the
"zero dropped gaps" figure that circulated in my own notes came from a single short run
and does not survive contact with hours of recording.

## The wall

The target for reading cardiac activity magnetically is described in the review
literature {% include cite.html key="roth2024" %}, and the gap between it and a phone is
not a factor of a few. It is orders of magnitude, and it is a property of the sensor.

That is the part worth stating plainly, because it is where the mentality I started with
runs out. Every item in the "what software can do" list above is real, and I would defend
all of it as worth building. Not one of those things moves the floor. They tell you
where the floor *is*, they stop you fooling yourself about what is above it, and they
make a null result mean something — which is a great deal, and is not the same as
sensitivity.

**The honest summary:** for what it is actually for — searching for weak periodic
structure with real nulls — this is a more careful instrument than the comparators, and
the gap is not close. For what the comparators are built for, it is worse, and one of
those gaps is a defect rather than a trade-off.

## What would change my mind

If someone demonstrates that a stock phone magnetometer resolves a signal at the
amplitude the cardiac literature describes, under a protocol with real nulls and an
injection test, then the sensitivity wall I am describing is not where I think it is and
this post is wrong. I would want to see the null machinery before the result, which is
the same standard I am holding myself to.
