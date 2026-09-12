---
title: "What software can and cannot buy you"
description: >-
  Two months of trying to push a phone magnetometer past what its hardware
  should allow — what the discipline actually bought, how it compares to the
  other implementations, and the wall that no amount of code moves.
date: 2026-09-01 09:00:00 -0600
project: bioem-propagation
status: published
inline_sources: true
tier: C
claims:
citations:
  - roth2024
  - odenwald2022
image: /assets/posts/fluxgate-magnetometer.jpg
image_alt: >-
  A fluxgate magnetometer under a glass dome in a museum case, its permalloy cores and mounting plates visible.
image_credit: Daderot
image_license: CC0
image_license_url: https://creativecommons.org/publicdomain/zero/1.0/
image_source_url: https://commons.wikimedia.org/wiki/File:Fluxgate_magnetometer,_of_the_type_installed_in_a_lunar_surface_probe_for_the_Apollo_Project_-_National_Museum_of_Nature_and_Science,_Tokyo_-_DSC07833.JPG
summary: >-
  Every phone has a magnetometer in it. The interesting question is not whether
  you can read a body with one — you cannot — but how far careful software
  gets you before the hardware stops you, and how you would know which of the
  two you were up against. This is what was tried, what the other
  implementations do, and where the line turned out to be.
---

Two months pushing a phone magnetometer past what its hardware should allow. What the
discipline bought, and the wall it does not move.

**Short version: software buys a great deal, and none of it is sensitivity.**

## What software can do

- **Verify rather than assume.** Every parameter not measured is a parameter being guessed.
- **Know its own noise**, in the band that matters rather than across the spectrum.
- **Refuse to believe itself** — surrogate nulls, held-out thresholds, injection tests
  establishing what the pipeline would have detected.
- **Keep everything on one clock**, so motion separates from field.
- **Report its own gaps** instead of interpolating them.

## What software cannot do

Manufacture information that never entered the converter. If the quantisation step is larger
than the thing you want to see, no averaging, whitening or filtering invents it.

## The other implementations

Four, each better than this rig at its own job.

**NOAA CrowdMag** — smartphone magnetometer readings as a distributed geomagnetic survey.
Validates every contribution against a field model, so it knows whether a reading is
*correct* in absolute terms. This rig does not, and has never checked.

**phyphox / Physics Toolbox** — physics-education tools. Expose raw and calibrated channels
side by side, switchable in two taps.

**NASA / citizen-science smartphone magnetometry** — characterises what a phone magnetometer
can do for space-weather monitoring, and is the closest published reference point for this
sensor class.

{% include source.html key="odenwald2022" %}

**ADVIO** — a visual-inertial odometry dataset, not a magnetometry project, but it ships
real multi-sensor phone recordings under an open licence. That makes it a cross-device
control for testing whether an effect belongs to one handset or to the platform.

**How they are used here.** CrowdMag is the model for an absolute-accuracy check not yet
built. phyphox is why the single-channel decision is a defect rather than a preference.
ADVIO is the corpus that lets a finding be checked on hardware not owned.

## What was tried

**Measure the delivered sample rate, per recording.** Not the requested rate. The difference
is systematic, and every frequency-domain result is wrong by that factor if assumed. None of
the comparators verifies this per record.

**Measure the noise floor in-band, not broadband.** This produced the most useful correction
of the project, in the opposite direction from the one you would fear: a broadband figure
**overstated** noise at the frequency of interest, because real recordings are
drift-dominated. Carrying the wrong number declares runnable experiments unrunnable. An
instrument that makes you too pessimistic kills experiments silently.

**Build the nulls before the result.** Four surrogate families, thresholds as a maximum
statistic over the whole search rather than per-cell, and a refusal to quote a false-alarm
bound above a stated ceiling. The comparators run quality control against a model; none runs
a null. Biggest single difference, and entirely software.

**Validate by injection.** Put a known signal into the real path and measure what fraction
the pipeline recovers. Without it, a null result cannot be distinguished from an analysis
that would have missed it anyway.

**One monotonic timebase across every sensor stream.** Magnetometer, accelerometer,
gyroscope, attitude. Almost every discriminator separating "the phone moved" from "the field
changed" depends on it, and it cannot be retrofitted.

## Where it is worse, including one defect

**The calibrated channel is not logged.** Recording raw as primary is right — calibration is
a filter with unpublished behaviour and cannot be undone. But the calibrated channel
alongside it is a free diagnostic, phyphox does it, and its absence caused a multi-day
misattribution: a large static field offset read as an external accessory when it was
internal to the device. Cheapest fix on the list; needs an app build.

**No absolute accuracy validation.** CrowdMag would have caught the same thing differently.

**One operating system, and a private archive.** The cross-device control leans on other
people's corpora.

**Dropped samples across long recordings**, reported rather than hidden — and the "zero
dropped gaps" figure in early notes came from a single short run.

## The wall

The target for reading cardiac activity magnetically is described in the review literature.

{% include source.html key="roth2024" %}

The gap between it and a phone is not a factor of a few. It is orders of magnitude, and it
is a property of the sensor.

Every item in "what software can do" is real and worth building. Not one moves the floor.
They tell you where the floor is, stop you fooling yourself about what is above it, and make
a null result mean something — which is a great deal, and is not sensitivity.

**Honest summary.** For searching weak periodic structure with real nulls, this is a more
careful instrument than the comparators, and the gap is not close. For what the comparators
are built for, it is worse, and one of those gaps is a defect rather than a trade-off.

## What would change my mind

A demonstration that a stock phone magnetometer resolves a signal at the amplitude the
cardiac literature describes, under a protocol with real nulls and an injection test. The
null machinery would need to come before the result — the same standard applied here.
