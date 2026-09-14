---
title: "Can a $70 board tell me I'm wrong?"
description: >-
  A single-channel EEG rig characterised in numbers: in-band 40 Hz power across
  six captures, why broadband RMS is the wrong figure to specify a rig by, and a
  proposed test of analog bandwidth as a validation axis.
date: 2026-08-25 09:00:00 -0600
project: audio-evoked-potentials
status: published
inline_sources: true
tier: C
claims:
  - AEP-0005
citations:
  - krigolson2017
  - boere2023
  - goldwyn2014
  - iaccarino2016
  - martorell2019
image: /assets/posts/eeg-recording-cap.jpg
image_alt: >-
  A person wearing a multi-electrode EEG recording cap in profile, ringed
  electrodes and their lead wires covering the scalp.
image_credit: Chris Hope
image_license: CC BY 2.0
image_license_url: https://creativecommons.org/licenses/by/2.0/
image_source_url: https://commons.wikimedia.org/wiki/File:EEG_Recording_Cap.jpg
---

n-of-1 instrument characterisation. Written for people who validate low-cost EEG. One ask,
after the rig sections. The auditory question that prompted the work is last.

## In-band power at 40 Hz: median 157 nV, 11.7× spread

Six captures. One rig, one montage, one person. Amplitude at 40 Hz over 60 s of
pre-stimulus baseline, estimated from neighbouring frequency bins.

| | |
|---|---|
| median | **157 nV** |
| range | **64–750 nV** (11.7×) |
| captures with ≥20 s usable baseline | 6 of 12 |
| baseline segments whose noise integrates with dwell | 5 of 9; the other 4 are drift-limited |

What this figure is not:

- **Not instrument noise.** No shorted-input capture exists. This is in-band power of a scalp
  recording, EEG and scalp EMG included.
- **Not explained by electrode prep.** The one capture the app scored good-contact (alpha SNR
  36) has the highest value, 750 nV. The one it flagged no-scalp-contact gives 238 nV. The
  spread is unexplained.
- **Not absolutely calibrated.** Counts convert at 7.9 µV/count, measured from the shield's
  calibration signal. The datasheet implies 1.72. That 4.6× disagreement is unresolved, and every
  nV figure here inherits it.

## Broadband RMS overstates in-band noise 3.5–24×

Specifying a rig by broadband RMS assumes white noise. EEG is drift-dominated. On the same six
captures, a white-noise estimate built from broadband RMS put the 40 Hz noise **3.5–24× too high
in amplitude** (median 15×), which is **12–594× too long in required dwell**.

The error runs one direction: it declares runnable measurements unrunnable. A low-cost rig
costed from a broadband figure gets ruled out of experiments it could run. Measure noise at the
frequency of interest.

Scope: six captures, one person, one rig. The direction transfers. The ratio may not.

## The rig

<div class="parts">
{% include part.html name="Olimex SHIELD-EKG-EMG" role="Analog front end. 0.16–40 Hz, ahead of the converter." price="C$34.02" href="https://www.digikey.ca/en/products/detail/olimex-ltd/SHIELD-EKG-EMG/3471383" img="/assets/posts/rig/olimex-shield-ekg-emg.jpg" credit="DigiKey" %}
{% include part.html name="Olimex SHIELD-EKG-EMG-PRO" role="Passive electrode cable for the shield: 3.5 mm jack to three snap leads." price="C$16.91" href="https://www.digikey.ca/en/products/detail/olimex-ltd/SHIELD-EKG-EMG-PRO/5247133" img="/assets/posts/rig/olimex-shield-ekg-emg-pro-cable.jpg" credit="DigiKey" %}
{% include part.html name="Arduino Uno R3" role="10-bit converter and USB serial." price="C$40.99" href="https://www.amazon.ca/dp/B008GRTSV6" img="/assets/posts/rig/arduino-uno-r3.jpg" credit="Amazon.ca" %}
{% include part.html name="AVCOO snap TENS pads, 20" role="The electrodes. Self-adhesive, reusable gel." price="C$13.99" href="https://www.amazon.ca/dp/B09R1WSVJS" img="/assets/posts/rig/avcoo-snap-tens-pads.jpg" credit="Amazon.ca" %}
</div>

Board and microcontroller about C$75; the whole rig about C$106, at listing prices on
2026-09-13.

| parameter | value |
|---|---|
| channels | 1 differential |
| montage | active Oz, reference Cz, ground mastoid; chosen for posterior alpha |
| electrodes | self-adhesive snap **TENS pads** — made for stimulation on skin, not recording through hair |
| impedance | **not measured** |
| analog band | 0.16–40 Hz, in the shield, ahead of the converter |
| converter | 10-bit |
| sample rate | 250 Hz in three captures, 256 Hz in three |
| gain | ≈2848, set by a hardware trimmer |
| scale | 7.9 µV/count measured; datasheet implies 1.72 |
| input-referred noise | **not measured** |
| stimulus timing | **not measured** (below) |
| analysis | Python; Welch PSD; FOOOF for aperiodic separation |

Chosen on forum consensus that a costlier board buys a quieter front end, not a capability. No
matched comparison was run. Landscape, checked 2026-08-25:

| | channels | price |
|---|---|---|
| Olimex SHIELD-EKG/EMG *(this rig)* | 1 | **€19.95** |
| Olimex EEG-SMT | 2 | €99.00 |
| OpenBCI Cyton | 8 | $1,759 |
| OpenBCI Cyton + Daisy | 16 | $3,518 |
| OpenBCI Complete Ultracortex | 16 | $4,222 |
| OpenBCI Galea | — | $60,504 |

## Timing: no number exists

Stimulus from Web Audio in a browser. EEG over USB serial. No loopback channel, no shared clock.
**No latency or jitter figure exists for this rig.**

For scale: a consumer Bluetooth headband, tested with 5,000 pulses looped through its auxiliary
input, measured a mean lag of 40 ms (±20 ms), with fewer than ten extreme latencies inflating the
spread.

{% include source.html key="krigolson2017" %}

The serial stream carries a second column. It has not been confirmed as an independent input and
may be a floating pin. Until it is, there is no known-good channel to loop the audio into.

## Retention

| stage | kept |
|---|---|
| captures with ≥20 s usable pre-stimulus baseline | 6 of 12 |
| of those, protocol run to completion | 3 of 6 — two stopped in baseline, one in drive |
| resting-alpha resonance profiles scored usable by the app | 1 of 6 |

The five unusable profiles: drift-dominated baseline (1), no alpha peak above the 1/f floor (3),
inconclusive at 12 Hz (1). The usable one peaks at 10 Hz with 2.8 dB SNR.

The headband validation above reports loss the same way: participants lost fell to one in twenty
once its assistants had experience fitting the headband.

## Alpha was the wrong calibration

The chain recovers resting alpha: SNR 36 in the good-contact capture, and one usable resonance
profile of six. Alpha is the weakest available check:
present at rest, needs no stimulus timing, exercises nothing between stimulus and record.

The planned replacement is a visual oddball. The headband validation used one — 25% oddballs,
three blocks of 40 trials, filtered 0.1–15 Hz — and recovered the N200 and P300 on consumer
hardware. Its task code and a data converter are published. A two-channel forehead-mounted system
has been examined on the same two components.

{% include source.html key="boere2023" %}

An oddball tests stimulus, timing and record together, against a published yardstick. It needs a
montage change first: the lab-grade arm of that validation measured the P300 at Pz. Oz–Cz is not
a P300 montage.

## The ask: analog bandwidth as a validation axis

Low-cost EEG validation has a channel axis: how few electrodes still recover ERPs. The two-channel
work above sits on it. The validation read for this post targets the N200, P300 and reward
positivity, and filtered its consumer arm at 0.1–15 Hz. For those components a 40 Hz analog
ceiling costs nothing.

The other axis is analog bandwidth: how narrow the front end can be before a given evoked
response is lost. None of the sources read for this post examine it. No systematic search was
done, so it is not claimed to be untested. This rig sits on its edge: 40 Hz is the filter corner,
and anything faster is gone before digitisation.

**The proposal.** A bandwidth sweep on existing lab-grade recordings. An oddball and a 40 Hz
auditory steady-state response, each re-filtered with a causal low-pass at a series of cutoffs —
for example 15, 30, 40, 60 and 100 Hz — reporting at each cutoff: component amplitude and
latency, detection rate, and participants retained. A causal filter approximates an analog front
end's phase lag; a zero-phase filter would not. No new participants. The analysis would be done
here, on the lab's data, under the lab's protocol.

**Deliverable:** a cutoff-versus-recovery table for components spanning the band.

## The auditory question this started from

The alpha runs were isochronic tones at the alpha resonant frequency, looking for an aftereffect.
The question underneath is auditory.

The medial superior olive is the first place in the ascending pathway where the two ears are
compared. Phase-locked activity there produces a far-field potential, the neurophonic.

{% include source.html key="goldwyn2014" %}

Engagement was with the released model, not the paper's full text. The published code has **no
sodium conductance and no axon** — an h-current and a low-threshold potassium current only — and
reproduces the far-field without spike-generating machinery. A matched far-field licenses *drive
arrived at the nucleus*. It does not license *cells crossed threshold*.

The defensible question: can a designed acoustic protocol put a specified structure into a
recorded evoked response that tracks a parameter sweep and is distinguishable from a
matched-energy tone? A delivery-verification methods result.

This rig cannot run it. The target sits at carrier rates in the hundreds of hertz; the analog
filter removes it before the converter. A 100 Hz fundamental has **zero harmonics in the
passband**, and no averaging recovers what was never digitised. Three consecutive workstreams were
designed against that ceiling before it was checked.

Under dichotic drive the response envelope can modulate at the difference frequency with no
acoustic envelope at either ear. That appears as **sidebands around the carrier**, not energy at
the difference frequency. Whether a single channel can recover that structure is a hardware
question.

The nearest published shape is 40 Hz sensory drive in mice, later combined auditory and visual.

{% include source.html key="iaccarino2016" %}
{% include source.html key="martorell2019" %}

Neither read at full text. Mouse tissue readout, not scalp EEG. Precedent that the shape exists,
nothing more.

A sustained-response decay test is queued. If it fails, most of what was built on top of it was
wasted. **A null will be published.**

## Devil's advocate

**A distraction from the bench.** The decay test needs a headphone, an electrode and an afternoon.
Writing this is a legible way not to run it.

**The instrument figures above are weaker than their first version.** The median, the ratio and
the attribution all changed on inspection. Anything else from this rig deserves the same
recomputation before it is trusted.

**A warm response does not solve the actual problem.** A better instrument or montage does not
give tissue access or pharmacological control.

## Correction — 2026-09-13

This post originally stated a median in-band noise at 40 Hz of **238 nV across eight sessions**, a
broadband overstatement of **20–90×**, that the spread showed **electrode preparation dominates**,
and that the delivered stimulus envelope was **measured rather than assumed**. None held.

The 238 nV came from an analysis script that took the upper-middle of six values; the median is
157 nV, over six captures. "20–90×" was a hard-coded literal in the same script's output; computed
per capture it is 3.5–24×. The session records contradict the electrode-prep attribution. No
stimulus-timing measurement exists. All four are corrected at source in the research records.

A paragraph noting that beta-band and dichotic runs had no producible records was removed rather
than kept as anecdote. The post was restructured to lead with the instrument characterisation.
