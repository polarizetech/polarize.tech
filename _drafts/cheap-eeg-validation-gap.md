---
title: "Can a $70 board tell me I'm wrong?"
description: >-
  Notes on an n-of-1 EEG rig, an analog ceiling that removes the signal I was
  designing for, and a question I can't answer alone.
date: 2026-08-25 09:00:00 -0600
project: audio-evoked-potentials
status: draft
tier: C
claims:
  - AEP-0005
citations:
  - goldwyn2014
---

I've been running a solo research program for about two months, and I've reached the
point where the honest next step is to have someone tell me my instrument is
inadequate.

This post is a description of the rig, one result, and one gap. It's written for
people who validate portable EEG hardware for a living — a category that includes at
least one lab a fifteen-minute drive from where I'm sitting. If that's you, the ask is
at the bottom and it's small.

## The setup

A single-channel Olimex SHIELD-EKG-EMG on an Arduino, Oz–Cz montage, closed-back
headphones, and a Python stack doing Welch PSD with FOOOF for aperiodic separation.
Stimulus generation is Web Audio in the browser, which means the delivered envelope is
measured rather than assumed — a distinction that turns out to matter, because hard
gating of an amplitude-modulated tone injects a second harmonic that a raised-cosine
ramp doesn't.

That's the whole apparatus. It's a hobbyist rig by any reasonable standard, and I want
to be precise about what it has and hasn't shown.

## Why the EKG/EMG shield and not the EEG-SMT

This is the first decision I'd like checked, because I made it on hearsay.

Olimex sells a purpose-built EEG board — the EEG-SMT — and I didn't buy it. It's
roughly five times the price, and the argument I found in hobbyist EEG communities was
that the SMT's advantage is essentially a quieter front end, which you can approach on
the cheaper shield with careful grounding, shielded leads, good electrode prep, and a
short cable run. The reasoning was that the expensive board buys convenience and a
better noise floor out of the box, not a capability you can't otherwise reach.

The epistemic status of that matters. **It's forum consensus, not a measurement.** I
haven't seen a side-by-side noise-floor comparison of the two boards under matched
conditions, and I didn't run one, because running one requires owning both — which
defeats the purpose of the decision. So I bought the cheap board on an unverified claim
and then built two months of work on top of it.

That may well have been fine. But there are two failure modes I can't rule out from
where I'm standing:

- **The noise-floor claim may hold for alpha and fail for anything smaller.** A board
  adequate for a 10 Hz cortical rhythm at microvolt scale says nothing about a far-field
  brainstem potential two or three orders of magnitude down.
- **I may have optimised the wrong axis entirely.** If analog bandwidth is the binding
  constraint — see below — then neither Olimex board solves my problem and the
  cheap-versus-expensive question was never the interesting one. Cheap and wrong is not
  better than expensive and wrong.

If someone with a calibrated signal generator has ever put these two boards on a bench
together, I'd like to see the numbers.

## What the rig's noise floor actually is

Since writing the above I've measured the part I can measure, across eight sessions on
this rig.

The headline is that **electrode prep dominates everything the software does.** Median
in-band noise at 40 Hz over a 60-second window is **238 nV**, with a session-to-session
range of 65 to 750 nV — an 11× spread on the same hardware in the same room. No
processing choice I have made moves the result as much as that spread does.

One correction is worth passing on because it pointed the dangerous way. I had been
carrying a broadband RMS figure as though it were the noise floor at the frequency of
interest. Real EEG is drift-dominated, so a broadband RMS **overstated the noise at
40 Hz by 20–90× in amplitude** — thousands of times over in required dwell. That error
declares a runnable measurement unrunnable, which is the direction that quietly kills
experiments you should have attempted.

## The one result

Isochronic auditory drive at individual alpha frequency (~9.7 Hz for me) produces
roughly a **22% rise in alpha-band power at IAF** during stimulation, reproducibly,
on-rig.

Every caveat you're already forming is correct. **n = 1.** No blinding. No sham designed
to control for arousal or attention. Single channel, non-standard montage, and Oz–Cz is
not what anyone would choose for this if they had a choice. The effect is acute —
measured *during* drive, not after — and acute entrainment of an ongoing oscillation is
one of the least surprising things in the auditory literature.

I treat this as **rig validation and nothing else**: evidence that the board, the
electrode, the amplifier chain and my analysis code together can recover a real,
expected signal. It's a calibration, not a finding, and it's filed at the lowest tier
this project has — a first-person unblinded observation, which no amount of repetition
can promote.

One further honesty note. When I went to record that result formally, I found it had
only ever existed as a number quoted inside a design document — the sessions were never
logged at the granularity that would let me recover exact dates or per-session figures.
So read the 22% as approximate, and read its registration as retroactive, which is
weaker than pre-registered.

## The gap, stated plainly

The interesting version of my question lives in the auditory brainstem, in the medial
superior olive — the first place in the ascending pathway where signals from the two
ears are compared. There's a far-field potential associated with phase-locked activity
there, called the neurophonic.

The constraint I've had to absorb comes from the modelling work on that potential
{% include cite.html key="goldwyn2014" %}. I want to be careful about how I state this,
because I have engaged with the released model rather than with the paper's full text.
What I can verify directly is what's in the authors' own published code: **the model
contains no sodium conductance and no axon at all** — only a hyperpolarisation-activated
current and a low-threshold potassium current. It reproduces the far-field signal
without any spike-generating machinery in it.

I've taken the implication seriously rather than routing around it. A matched far-field
licenses the claim *phase-locked drive arrived at the nucleus*. It does not license
*cells crossed threshold*. Those are different statements, and a postsynaptic far-field
cannot distinguish them. Much of the interesting downstream biology depends on the
second one, and I can't get there with the instrument I have — or, as far as I can
determine, with any non-invasive instrument.

So the claim I'm left with is smaller and more defensible: **can a designed acoustic
protocol put a specified structure into a recorded evoked response, such that the
structure tracks a designed parameter sweep and is distinguishable from a matched-energy
plain tone?** That's a delivery-verification question. It's a methods result. It's also
runnable.

Except for one thing.

## The analog ceiling

The Olimex board passes roughly 0.16 to 40 Hz. The signal I need to characterise sits at
carrier rates in the hundreds of hertz.

I want to be blunt about what that means, because I've caught myself doing the softer
version. It is not "a limitation to work around." Reviewing my own logs, I found that
**three consecutive workstreams were designed against an instrument whose bandwidth
removes the target signal.** The question was being fitted to the rig rather than the rig
chosen for the question. That's not a hardware problem, it's a reasoning failure, and
I'd rather name it than have someone else find it.

The reason it's fatal rather than inconvenient is that the filter is in silicon *ahead of
the converter*. A 100 Hz response fundamental has **zero harmonics inside the passband**.
No amount of dwell, averaging, or clever choice of stimulus frequency recovers something
that was removed before the signal was digitised. I now run a viability gate — is the
readout in the analog band at all — before building anything, because I built an entire
apparatus first and computed that gate afterwards.

There's a partial escape. Under dichotic drive — a slightly different pure tone to each
ear — the envelope of the response can modulate at the difference frequency even though
no envelope exists acoustically at either ear. That structure appears spectrally as
**sidebands around the carrier**, not as energy at the difference frequency itself.
Searching at the difference frequency is a null about a frequency the physics never
predicted. Whether a single-channel Oz–Cz montage can recover sideband structure at all
is genuinely open, and it's a hardware question, not a theory question.

## What I'd like

I'm not looking for a collaborator, a co-author, or funding. I'm looking for a competence
I don't have.

1. **A bandwidth reality check.** Is a sub-$100 board recoverable into a usable range with
   better front-end filtering and averaging, or is the ceiling the ceiling? I suspect I
   know, but I've been wrong about hardware before and I'd rather be told than discover it
   after another month.
2. **A montage correction.** Oz–Cz was chosen for alpha, then inherited by a question it
   doesn't suit. What would you use?
3. **A benchmark, if there's appetite.** There's a real methodological question here: how
   far does consumer-grade EEG extend before it stops recovering signals lab-grade systems
   get, and where exactly is the boundary? That's publishable with or without my program
   attached, and I'd happily run the tedious comparison conditions.

I have a bench test queued that will probably close a large part of my program — a
sustained-response decay measurement, testing whether the candidate envelope holds above
50% of initial amplitude. If it fails, most of what I've built downstream was wasted
effort, and I'd rather find out this month than next year. **A null is a result and I
will publish it.**

If you have five minutes and an opinion about my montage, I'd like to hear it.

## Devil's advocate

Three objections I'd rather raise than have raised.

**It's a distraction from the bench.** The sustained-response test needs a headphone, an
electrode, and an afternoon. It has been the named next step for weeks. Writing an
outreach post is a legible, satisfying way to not run it, and that risk is live.

**The interesting claim and the defensible claim have come apart.** What I can defend is
a delivery-verification methods result. What made me start was considerably more
ambitious. A hostile reader can grant the first entirely and deny it bears on the second,
and nothing above answers them. I think that's the correct state to be in, and I'd rather
sit in it visibly.

**Even a warm response doesn't solve my actual problem.** EEG methodology expertise gets
me a better instrument and a corrected montage. It doesn't get me what the ambitious half
of the question requires, which is tissue access and pharmacological control — a
different building, probably a different institution, and possibly a different species.
