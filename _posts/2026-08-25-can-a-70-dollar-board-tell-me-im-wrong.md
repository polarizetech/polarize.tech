---
title: "Can a $70 board tell me I'm wrong?"
description: >-
  An n-of-1 EEG rig, an analog ceiling that removes the signal I was designing
  for, and a question I can't answer alone.
date: 2026-08-25 09:00:00 -0600
project: audio-evoked-potentials
status: published
inline_sources: true
tier: C
claims:
  - AEP-0005
citations:
  - iaccarino2016
  - martorell2019
  - goldwyn2014
image: /assets/posts/eeg-recording-cap.jpg
image_alt: >-
  A person wearing a multi-electrode EEG recording cap in profile, ringed
  electrodes and their lead wires covering the scalp.
image_credit: Chris Hope
image_license: CC BY 2.0
image_license_url: https://creativecommons.org/licenses/by/2.0/
image_source_url: https://commons.wikimedia.org/wiki/File:EEG_Recording_Cap.jpg
---

Solo research programme, about two months old. The honest next step is to have someone tell
me the instrument is inadequate.

Written for people who validate portable EEG hardware. The ask is at the bottom and it is
small.

## The rig

Single-channel Olimex SHIELD-EKG/EMG on an Arduino. **Active Oz, reference Cz, ground
mastoid** — a posterior montage chosen for alpha. 250 Hz sampling, 10-bit ADC at roughly
7.9 µV per count, **~40 Hz analog low-pass**. Closed-back headphones. Python doing Welch PSD
with FOOOF for aperiodic separation; Web Audio generating the stimulus, so the delivered
envelope is measured rather than assumed.

Microvolt EEG on a 10-bit converter is a few counts. Quantisation-limited and low-SNR by
construction.

## The alternatives, and why this board

Bought on hearsay — forum consensus that the expensive board buys a quieter front end and
convenience, not a capability you cannot otherwise reach. **That is not a measurement.** No
matched-conditions noise-floor comparison of the two has been seen here, and none was run,
because running one means owning both.

Landscape, checked 2026-08-25:

| | channels | price |
|---|---|---|
| Olimex SHIELD-EKG/EMG *(what I have)* | 1 | **€19.95** |
| Olimex EEG-SMT | 2 | €99.00 |
| OpenBCI Cyton | 8 | $1,759 |
| OpenBCI Cyton + Daisy | 16 | $3,518 |
| OpenBCI Complete Ultracortex | 16 | $4,222 |
| OpenBCI Galea | — | $60,504 |

The gap between rows one and three is the question. Two failure modes that cannot be ruled
out from here: the noise-floor claim may hold for alpha and fail for anything smaller; or
the wrong axis was optimised entirely, in which case **neither** Olimex board solves the
problem and cheap-versus-expensive was never the interesting comparison.

## The noise floor

Median in-band noise at 40 Hz over 60 s: **238 nV**, ranging 65 to 750 nV across eight
sessions. An **11× spread on the same hardware in the same room** — electrode prep dominates
everything the software does.

One correction worth passing on. A broadband RMS figure had been carried as if it were the
noise floor at the frequency of interest. Real EEG is drift-dominated, so broadband RMS
**overstated 40 Hz noise by 20–90× in amplitude.** That error declares a runnable
measurement unrunnable, which quietly kills experiments that should have been attempted.

## What has been run

Isochronic tones at the alpha resonant frequency, looking for a measurable aftereffect.

Reported as the data reads, not as remembered. **Of six resonance profiles on file, five are
`inconclusive`** — flagged by the app as drift-dominated, or with no alpha peak above the
1/f floor, or with a peak below the alpha band entirely. The one marked `strong` sits at
10 Hz with 2.8 dB SNR. The best recorded run gives a resonant frequency of 11 Hz against a
peak of 9.77, a divergence of 1.23 Hz, and its own verdict is **`LOW QUALITY / no valid
comparison`**.

So: the chain demonstrably recovers alpha, and that counts as **rig validation and nothing
else** — evidence that board, electrode, amplifier and analysis code together find a real,
expected signal. A calibration, not a finding. n = 1, unblinded, no sham for arousal or
attention, effect measured *during* drive rather than after, and acute entrainment of an
ongoing oscillation is among the least surprising results in the auditory literature.

A beta-band version and dichotic drive experiments were also run. **No numbers are reported
for either, because the records cannot currently be produced.** The beta app was retired and
its results are not where expected. Until the data can be put in front of you, those are
anecdotes.

## The published precedent

The nearest thing in the literature to the shape being chased is the 40 Hz sensory drive
work in mouse models, later extended to combined auditory and visual stimulation.

{% include source.html key="iaccarino2016" %}
{% include source.html key="martorell2019" %}

Cited as **precedent that the shape exists**, not as support. Neither was read at full text.
Four differences bound how far they travel: mouse versus human, invasive tissue readout
versus scalp EEG, 40 Hz gamma versus alpha, cortex and hippocampus versus a brainstem
nucleus. **The readout difference is binding.** Those studies read the consequence in
tissue. Nothing available here reads anything but a far-field.

## The gap

The interesting version of the question lives in the medial superior olive — the first place
in the ascending pathway where the two ears are compared. There is a far-field potential
from phase-locked activity there, the neurophonic.

The constraint comes from modelling work on that signal.

{% include source.html key="goldwyn2014" %}

Engagement here was with the released model rather than the paper's full text, so only what
is checkable is stated: the published code contains **no sodium conductance and no axon** —
only an h-current and a low-threshold potassium current — and it reproduces the far-field
with no spike-generating machinery in it.

Taken seriously rather than routed around. A matched far-field licenses *drive arrived at
the nucleus*. It does not license *cells crossed threshold*. Those are different statements
and a postsynaptic far-field cannot separate them. Most of the downstream biology of
interest depends on the second.

So the defensible claim is smaller: **can a designed acoustic protocol put a specified
structure into a recorded evoked response, such that it tracks a parameter sweep and is
distinguishable from a matched-energy plain tone?** A delivery-verification question. A
methods result. Runnable.

Except for one thing.

## The analog ceiling

The board passes roughly 0.16 to 40 Hz. The signal needed sits at carrier rates in the
hundreds of hertz.

Not a limitation to work around. Reviewing the logs, **three consecutive workstreams were
designed against an instrument whose bandwidth removes the target signal.** The question was
fitted to the rig rather than the rig chosen for the question. A reasoning failure, not a
hardware problem.

Fatal rather than inconvenient because the filter is in silicon *ahead of the converter*. A
100 Hz fundamental has **zero harmonics inside the passband.** No dwell, no averaging, no
clever choice of stimulus frequency recovers what was removed before digitisation. Hence the
viability gate — *is the readout in the analog band at all* — before building anything.

A partial escape: under dichotic drive the response envelope can modulate at the difference
frequency even though no envelope exists acoustically at either ear. That appears spectrally
as **sidebands around the carrier**, not as energy at the difference frequency — searching
at the difference frequency is a null about a frequency the physics never predicted. Whether
a single-channel Oz–Cz montage can recover sideband structure at all is open, and it is a
hardware question.

## What I'd like

Not a collaborator, co-author or funding. A competence I do not have.

1. **A bandwidth reality check.** Is a sub-$100 board recoverable into a usable range with
   better front-end filtering and averaging, or is the ceiling the ceiling?
2. **A montage correction.** Oz–Cz was chosen for alpha, then inherited by a question it
   does not suit. What would you use?
3. **A benchmark, if there is appetite.** How far does consumer-grade EEG extend before it
   stops recovering what lab-grade systems get, and where is the boundary? Publishable with
   or without this programme attached, and I would run the tedious conditions.

A bench test is queued that will probably close a large part of this programme — a
sustained-response decay measurement. If it fails, most of what was built downstream was
wasted effort. **A null is a result and it will be published.**

## Devil's advocate

**A distraction from the bench.** The sustained-response test needs a headphone, an
electrode and an afternoon. It has been the named next step for weeks. Writing an outreach
post is a legible way to not run it, and that risk is live.

**The interesting claim and the defensible claim have come apart.** What is defensible is a
delivery-verification methods result. What prompted the work was more ambitious. A hostile
reader can grant the first and deny it bears on the second, and nothing here answers them.

**A warm response does not solve the actual problem.** Better instrument, corrected montage
— neither gets tissue access and pharmacological control. That is a different building,
probably a different institution, possibly a different species.
