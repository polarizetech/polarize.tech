---
title: "Can a $70 board tell me I'm wrong?"
description: >-
  An n-of-1 EEG rig, an analog ceiling that removes the signal I was designing
  for, and a question I can't answer alone.
date: 2026-08-25 09:00:00 -0600
project: audio-evoked-potentials
status: draft
tier: C
claims:
  - AEP-0005
citations:
  - iaccarino2016
  - martorell2019
  - goldwyn2014
---

I've been running a solo research program for about two months. The honest next step
is to have someone tell me my instrument is inadequate.

This is the rig, what it has shown, and the gap. It's written for people who validate
portable EEG hardware for a living. The ask is at the bottom and it's small.

## The rig

A single-channel Olimex SHIELD-EKG/EMG on an Arduino. **Active Oz, reference Cz, ground
mastoid** — a posterior montage chosen for alpha. 250 Hz sampling, 10-bit ADC at roughly
7.9 µV per count, and a **~40 Hz analog low-pass**. Closed-back headphones. Python doing
Welch PSD with FOOOF for aperiodic separation, and Web Audio generating the stimulus, so
the delivered envelope is measured rather than assumed.

Microvolt EEG on a 10-bit converter is only a few counts. It's quantisation-limited and
low-SNR by construction, and I want to be precise about what it has and hasn't shown.

## Why this board, and what the alternatives cost

I bought the cheap board on hearsay — forum consensus that the expensive one buys a
quieter front end and convenience, not a capability you can't otherwise reach. **That's
not a measurement.** I've never seen a matched-conditions noise-floor comparison of the
two, and I didn't run one, because running one means owning both.

Here's the actual landscape, checked 2026-08-25:

| | channels | price |
|---|---|---|
| Olimex SHIELD-EKG/EMG *(what I have)* | 1 | **€19.95** |
| Olimex EEG-SMT | 2 | €99.00 |
| OpenBCI Cyton | 8 | $1,759 |
| OpenBCI Cyton + Daisy | 16 | $3,518 |
| OpenBCI Complete Ultracortex | 16 | $4,222 |
| OpenBCI Galea | — | $60,504 |

The gap between rows one and three is the whole question. Two failure modes I can't rule
out from here: the noise-floor claim may hold for alpha and fail for anything smaller;
or I optimised the wrong axis entirely, in which case **neither** Olimex board solves my
problem and cheap-versus-expensive was never the interesting comparison.

## What the noise floor actually is

Median in-band noise at 40 Hz over 60 s: **238 nV**, ranging 65 to 750 nV across eight
sessions. An **11× spread on the same hardware in the same room** — electrode prep
dominates everything the software does.

One correction worth passing on, because it pointed the dangerous way. I'd been carrying
a broadband RMS figure as if it were the noise floor at the frequency of interest. Real
EEG is drift-dominated, so broadband RMS **overstated 40 Hz noise by 20–90× in
amplitude**. That error declares a runnable measurement unrunnable, which quietly kills
experiments you should have attempted.

## What I've actually run

Isochronic tones at the alpha resonant frequency, looking for a measurable aftereffect.

I want to report this the way the data reads rather than the way I remember it. **Of six
resonance profiles on file, five are `inconclusive`** — flagged by the app itself as
drift-dominated, or with no alpha peak above the 1/f floor, or with a peak below the
alpha band entirely. The one session marked `strong` sits at 10 Hz with 2.8 dB SNR. My
best recorded run gives a resonant frequency of 11 Hz against a peak of 9.77, a
divergence of 1.23 Hz, and its own verdict is **`LOW QUALITY / no valid comparison`**.

So: the chain demonstrably recovers alpha, and I treat that as **rig validation and
nothing else** — evidence that board, electrode, amplifier and analysis code together
find a real, expected signal. It is a calibration, not a finding. n = 1, unblinded, no
sham for arousal or attention, effect measured *during* drive rather than after, and
acute entrainment of an ongoing oscillation is among the least surprising results in the
auditory literature.

I also ran a beta-band version of this and experimented with dichotic drive — a
different tone in each ear, 10 Hz apart, with an isochronic envelope on top. **I'm not
reporting numbers for either, because I can't currently produce the records.** The beta
app was retired and its results aren't where I expected them. Until I can put the data
in front of you, those are anecdotes and I'd rather say so.

## The published precedent

The nearest thing in the literature to the shape I'm chasing is the MIT gamma work —
40 Hz sensory drive producing downstream cellular consequences in mouse models
{% include cite.html key="iaccarino2016" %}, later extended to combined auditory and
visual stimulation {% include cite.html key="martorell2019" %}.

I cite these as **precedent that the shape exists**, not as support. I haven't read
either at full text, and four differences bound how far they travel: mouse versus human,
invasive tissue readout versus scalp EEG, 40 Hz gamma versus alpha, cortex and
hippocampus versus a brainstem nucleus. **The readout difference is the binding one.**
Those studies read the consequence in tissue. Nothing I can do reads anything but a
far-field.

## The gap

The interesting version of my question lives in the medial superior olive — the first
place in the ascending pathway where the two ears are compared. There's a far-field
potential from phase-locked activity there, the neurophonic.

The constraint comes from the modelling work on that signal
{% include cite.html key="goldwyn2014" %}. I've engaged with the released model rather
than the paper's full text, so I'll state what's checkable: the authors' published code
contains **no sodium conductance and no axon** — only an h-current and a low-threshold
potassium current — and it reproduces the far-field with no spike-generating machinery in
it at all.

I've taken that seriously rather than routing around it. A matched far-field licenses
*drive arrived at the nucleus*. It does not license *cells crossed threshold*. Those are
different statements and a postsynaptic far-field can't separate them. Most of the
downstream biology I care about depends on the second, and I can't get there with this
instrument — or, as far as I can tell, with any non-invasive one.

So the defensible claim is smaller: **can a designed acoustic protocol put a specified
structure into a recorded evoked response, such that it tracks a parameter sweep and is
distinguishable from a matched-energy plain tone?** A delivery-verification question. A
methods result. Runnable.

Except for one thing.

## The analog ceiling

The board passes roughly 0.16 to 40 Hz. The signal I need sits at carrier rates in the
hundreds of hertz.

This is not "a limitation to work around." Reviewing my own logs I found that **three
consecutive workstreams were designed against an instrument whose bandwidth removes the
target signal.** The question was fitted to the rig rather than the rig chosen for the
question. That's a reasoning failure, not a hardware problem, and I'd rather name it than
have someone else find it.

It's fatal rather than inconvenient because the filter is in silicon *ahead of the
converter*. A 100 Hz fundamental has **zero harmonics inside the passband**. No dwell, no
averaging, no clever choice of stimulus frequency recovers what was removed before
digitisation. I now run a viability gate — *is the readout in the analog band at all* —
before building anything, because I built an entire apparatus first and computed that
gate afterwards.

There's a partial escape. Under dichotic drive the response envelope can modulate at the
difference frequency even though no envelope exists acoustically at either ear. That
appears spectrally as **sidebands around the carrier**, not as energy at the difference
frequency — searching at the difference frequency is a null about a frequency the physics
never predicted. Whether a single-channel Oz–Cz montage can recover sideband structure at
all is open, and it's a hardware question.

## What I'd like

Not a collaborator, co-author, or funding. A competence I don't have.

1. **A bandwidth reality check.** Is a sub-$100 board recoverable into a usable range with
   better front-end filtering and averaging, or is the ceiling the ceiling?
2. **A montage correction.** Oz–Cz was chosen for alpha, then inherited by a question it
   doesn't suit. What would you use?
3. **A benchmark, if there's appetite.** How far does consumer-grade EEG extend before it
   stops recovering what lab-grade systems get, and where exactly is the boundary? That's
   publishable with or without my program attached, and I'd run the tedious conditions.

I have a bench test queued that will probably close a large part of my program — a
sustained-response decay measurement. If it fails, most of what I've built downstream was
wasted effort. **A null is a result and I will publish it.**

If you have five minutes and an opinion about my montage, I'd like to hear it.

## Devil's advocate

**It's a distraction from the bench.** The sustained-response test needs a headphone, an
electrode, and an afternoon. It's been the named next step for weeks. Writing an outreach
post is a legible way to not run it, and that risk is live.

**The interesting claim and the defensible claim have come apart.** What I can defend is
a delivery-verification methods result. What made me start was more ambitious. A hostile
reader can grant the first and deny it bears on the second, and nothing here answers them.
That's the correct state to be in and I'd rather sit in it visibly.

**Even a warm response doesn't solve my actual problem.** Better instrument, corrected
montage — neither gets me tissue access and pharmacological control. That's a different
building, probably a different institution, and possibly a different species.
