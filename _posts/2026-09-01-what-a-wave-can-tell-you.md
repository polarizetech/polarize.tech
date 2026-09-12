---
title: '"Frequencies" are just one piece of the puzzle'
description: >-
  Building a list of every kind of information a biological signal is known to
  carry, and which structural feature of the wave carries it — then asking the
  same question of tides, seismic noise and the solar cycle.
date: 2026-09-01 11:00:00 -0600
project: audio-evoked-potentials
status: published
inline_sources: true
tier: C
claims:
citations:
  - fratini2015
  - chan2018
  - attia2019
  - lima2021
image: /assets/posts/sea-wave.jpg
image_alt: >-
  A breaking ocean wave photographed close to the water surface.
image_credit: Editor abcdef
image_license: CC0
image_license_url: https://creativecommons.org/publicdomain/zero/1.0/
image_source_url: https://commons.wikimedia.org/wiki/File:Sea_wave_saipan.JPG
summary: >-
  A heartbeat is usually treated as a trace of a heart working. The published
  literature says it is considerably more than that — identity, sex, age and
  health have all been read out of one. This is the survey of what a biological
  wave is known to carry, which signals have been catalogued so far, and what
  happened when the same reader was pointed at waves with no organism in them.
---

Process note. Building a list of what a biological signal is known to carry, then pointing
the same reader at waves with nothing alive in them.

Starting observation: an ECG is not only a record of a heart contracting. Identity, sex, age
and health have all been read out of one. If that holds for a single signal, the question is
what *every* biological signal carries, and whether the same structural features carry it
each time.

## The signals catalogued

Six, named by source tissue rather than application. Representative textbook ranges, not
hard bounds.

| signal | source | band | amplitude | shape |
|---|---|---|---|---|
| **ECG** | myocardium | ~0.05–100 Hz | 1–10 mV | strongly periodic, one sharp recurring event, consistent beat shape |
| **EEG** | cortex | ~0.5–100 Hz | 2 µV – 0.1 mV | broadband, oscillatory, band-structured, weakly event-locked |
| **EMG** | skeletal muscle | ~2–500 Hz | 50 µV – 5 mV | burst-structured, high-frequency, amplitude tracks effort |
| **EOG** | corneo-retinal dipole | ~DC–10 Hz | 10 µV – 5 mV | slow steps and ramps; essentially DC |
| **EDA** | sweat glands | ~DC–2 Hz | µS-scale | slow level with responses on top; not oscillatory |
| **EGG** | stomach smooth muscle | ~0.03–0.15 Hz | 10–500 µV | very-low-frequency near-sinusoidal pacemaker rhythm |

**The useful part was unexpected.** Laid out together, the six separate on properties that
have nothing to do with physiology: how periodic, how sharp the events, where the spectral
weight sits, how much DC. You can tell them apart without knowing the tissue.

That is either an interesting fact about biological signals or an artefact of how they are
all recorded. Which one is not known here.

## The information axes

What kind of information is a biological wave known to carry. Each row is an entry point to
a literature.

**Identity.** Attributing a trace to a specific person is a mature field for ECG, with a
parallel line on individuating signatures in EEG.

{% include source.html key="fratini2015" %}
{% include source.html key="chan2018" %}

**Sex and age.** Both have been read from short clinical recordings.

{% include source.html key="attia2019" %}

The *discrepancy* between an age estimated from the signal and a person's actual age has
itself been studied as a marker.

{% include source.html key="lima2021" %}

**Autonomic and affective state.** Heart-rate variability is the standard non-invasive
window onto autonomic balance; electrodermal activity indexes a sympathetic pathway
directly.

**Intention.** Muscle activity decodes motor intent; cortical activity carries potentials
preceding movement rather than following it.

**Health.** The axis with the most literature behind it, and the only one this bench has
measured anything on.

None of those papers was read at full text. They are cited as entry points; what they exist
to study is stated, not what any of them found.

## The reframing

Building the list changed what the project looked like.

It had been treated as signal processing — extracting a feature from a trace. Laid out
together the axes look like a **taxonomy** problem instead.

Identity, sex and age barely change. State and intention change minute to minute. Health
drifts. Those are not the same kind of quantity, and calling them all "information in the
signal" hides the most important distinction between them.

That came from making a table, not from running anything.

## Waves with nothing alive in them

A reader that finds rich structure in biological signals has to be asked whether it finds
rich structure in everything. So the same reader gets pointed at waves with no organism in
them:

- **Tide gauges** — two stations, 61 days. A blind read recovered the principal lunar
  semidiurnal period and separated the moon's contribution from the weather's.
- **Solar flux against cosmic-ray flux** — 14.6 years. Recovered the known anticorrelation,
  but only given the full cycle. That makes it a result about *how much data you need*.
- **Seismic, infrasound, ocean sound, geomagnetic field** — recovered the secondary
  microseism and the daily solar-quiet variation, blind.

The standing rule on that log:

> A high structure score on a signal with no organism in it is a caution about the
> instrument, not a finding about nature.

**Reading tides well is partly bad news.** The structure being found might be a property of
the reader rather than of life. Two of those runs did embarrass the instrument — one exposed
silent bugs at low sample rates, another showed a standard statistical null invalid on
deterministic signals.

## Sound, light, water

Mapped, not tested.

The structural properties in question — how loud, how bright, how periodic, how consistent
the repeating unit, whether a slow rhythm modulates a fast one — have natural readings in
sound and in light. Loudness and timbre in acoustics; brightness and colour in optics;
amplitude and morphology in a bioelectric trace. Water gave the cleanest test so far because
a tide is well enough characterised that the reader had nowhere to hide.

A correspondence you can write down is not one you have shown. Applying these
characteristics across modalities is, until tested the way the cardiac work was, **a
hypothesis carried by analogy.**

## What would make this wrong

If the structural characteristics separating biological signals turn out to separate *any*
filtered time series equally well, then the shared-grammar idea is an artefact of everyone
using similar pipelines, and this survey describes the pipeline rather than life. That is a
live possibility, it is why the non-biological waves get read at all, and nothing here rules
it out.
