---
title: "What a wave can tell you about the thing that made it"
description: >-
  Building a list of every kind of information a biological signal is known to
  carry, and which structural feature of the wave carries it — then asking the
  same question of tides, seismic noise and the solar cycle.
date: 2026-09-01 11:00:00 -0600
project: audio-evoked-potentials
status: published
tier: C
claims:
citations:
  - fratini2015
  - chan2018
  - attia2019
  - lima2021
summary: >-
  A heartbeat is usually treated as a trace of a heart working. The published
  literature says it is considerably more than that — identity, sex, age and
  health have all been read out of one. This is the survey of what a biological
  wave is known to carry, which signals have been catalogued so far, and what
  happened when the same reader was pointed at waves with no organism in them.
---

This is a process post. It is about building a list, why the list turned out to be the
useful artefact, and what checking it against non-living waves did to it.

The starting observation is unremarkable once stated: **an ECG is not only a record of a
heart contracting.** The published literature has read identity, sex, age and health out
of the same trace. If that is true of one signal, the obvious question is what *every*
biological signal carries, and whether the same structural features carry it each time.

Answering that properly starts with a boring inventory.

## The signals catalogued so far

Six, named by the tissue they come from rather than the application they serve. These are
representative textbook ranges, not hard bounds.

| signal | source | band | amplitude | what its shape is like |
|---|---|---|---|---|
| **ECG** | myocardium | ~0.05–100 Hz | 1–10 mV | strongly periodic, one sharp recurring event, very consistent beat shape |
| **EEG** | cortex | ~0.5–100 Hz | 2 µV – 0.1 mV | broadband, oscillatory, band-structured, weakly event-locked |
| **EMG** | skeletal muscle | ~2–500 Hz | 50 µV – 5 mV | burst-structured, high-frequency, amplitude tracks effort |
| **EOG** | corneo-retinal dipole | ~DC–10 Hz | 10 µV – 5 mV | slow steps and ramps — saccades, blinks — essentially DC |
| **EDA** | sweat glands | ~DC–2 Hz | µS-scale | a slow level with responses on top; not oscillatory at all |
| **EGG** | stomach smooth muscle | ~0.03–0.15 Hz | 10–500 µV | a very-low-frequency near-sinusoidal pacemaker rhythm |

Writing that table was the first useful thing, and not for the reason I expected. Laid
out together, the six are separated by properties that have nothing to do with
physiology: how periodic they are, how sharp their events are, where their spectral
weight sits, how much DC they carry. **You can tell them apart without knowing what
tissue you are looking at.** That is either an interesting fact about biological signals
or an artefact of how they are all recorded, and I genuinely do not know which yet.

## The axes, and where each one comes from

The second list is the map: what kind of information is a biological wave known to carry?
Each row below is an entry point to a literature, not a claim of mine.

**Identity.** Attributing a trace to a specific person is a mature field for
ECG {% include cite.html key="fratini2015" %}, and there is a parallel line of work on
individuating signatures in EEG {% include cite.html key="chan2018" %}.

**Sex and age.** Both have been read from short clinical
recordings {% include cite.html key="attia2019" %}, and the *discrepancy* between an
age estimated from the signal and the person's actual age has itself been studied as a
marker {% include cite.html key="lima2021" %}.

**Autonomic and affective state.** Heart-rate variability is the standard non-invasive
window onto autonomic balance, and electrodermal activity indexes a sympathetic pathway
directly.

**Intention.** Muscle activity decodes motor intent; cortical activity carries potentials
that precede movement rather than follow it.

**Health.** The axis with the most literature behind it, and the only one this bench has
measured anything on directly.

I want to be careful here, because this is exactly the point where a survey turns into an
overclaim: **I have not read any of those papers at full text.** They are cited as the
entry point to their topic. What I can say is that these axes exist and are established;
what I cannot say from this page is what any individual study found.

## The part I did not expect

Building the list changed what I thought the project was.

I had been treating this as *signal processing* — a question about extracting a feature
from a trace. Laying the axes out next to each other makes it look like a **taxonomy
problem** instead. Identity, sex and age are properties that barely change. State and
intention change minute to minute. Health drifts. Those are not the same kind of quantity,
and lumping them together as "information in the signal" hides the most important
distinction between them.

That reframing is the actual output of the exercise, and it came from making a table, not
from running anything.

## Pointing it at waves with nothing alive in them

Here is the part that keeps the whole thing honest, and it is the reason I would defend
this method to anyone building something similar.

If you build a reader that finds rich structure in biological signals, you have to ask
whether it finds rich structure in *everything*. So the same reader gets pointed at waves
with no organism anywhere in them:

- **Tide gauges** — two stations, 61 days. A blind read recovered the principal lunar
  semidiurnal period and correctly separated the moon's contribution from the weather's.
- **Solar flux against cosmic-ray flux** — 14.6 years. It recovered the known
  anticorrelation, but only when given the full cycle. That makes it a result about
  *how much data you need*, not about the sun.
- **Seismic, infrasound, ocean sound and the geomagnetic field** — it recovered the
  secondary microseism and the daily solar-quiet variation, blind.

The standing rule on that log is the sentence I would put on the wall:

> A high structure score on a signal with no organism in it is a caution about the
> instrument, not a finding about nature.

**Reading tides well is partly bad news.** It means the structure the reader is finding
might be a property of the reader rather than of life. Every one of those runs was a test
of the instrument that could have embarrassed it, and two of them did — one exposed
silent bugs at low sample rates, another showed a standard statistical null to be invalid
on deterministic signals.

## Sound, light, and water

The obvious next question is whether the same characteristics carry information in
non-biological waves, and here I want to be honest about the state of it: **this is
mapped, not tested.**

The structural properties in question — how loud, how bright, how periodic, how
consistent the repeating unit is, whether a slow rhythm modulates a fast one — all have
natural readings in sound and in light. Loudness and timbre in acoustics; brightness and
colour in optics; amplitude and morphology in a bioelectric trace. Water gave the
cleanest test so far precisely because a tide is so well characterised that the reader
had nowhere to hide.

But a correspondence you can *write down* is not a correspondence you have *shown*.
Applying these characteristics across modalities is, until it is tested the same way the
cardiac work was, **a hypothesis carried by analogy.** I would rather say that plainly
than let a tidy table imply otherwise.

## What would make this wrong

If the structural characteristics that separate biological signals turn out to separate
*any* filtered time series equally well, then the shared-grammar idea is an artefact of
everyone using similar analysis pipelines, and this survey is describing the pipeline
rather than describing life. That is a real possibility, it is the reason the
non-biological waves get read at all, and nothing on this page rules it out.
