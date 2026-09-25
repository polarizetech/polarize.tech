---
title: "A spiking network built to lose: what it would and would not remember"
description: >-
  A small, biologically grounded network was asked to store sounds and play them back. It could
  not. Along the way it showed which habituation mechanisms keep a stimulus-specific memory, and
  where a published single-cell model parts ways with the cell it describes.
date: 2026-09-25 09:00:00 -0600
project: audio-evoked-potentials
status: published
tier: SPEC
claims:
citations:
  - rajan2025
  - rajan2026
  - beck1997
  - vogels2011
summary: >-
  In simulation, synaptic depletion never kept a sound-specific memory, and only plasticity gated
  by the receiving cell did. A published receptor model drained untrained responses under a
  protein-synthesis block, where the real cell does not.
---

Everything below is a result about a computer model with chosen parameters. None of it is a
measurement of a brain, an animal or a cell, and the tier says so. The code, every preregistered
plan and every raw output are in a public repository:
[polarizetech/sim-neural-memory](https://github.com/polarizetech/sim-neural-memory).

## The question

Could a network of spiking neurons, with synapses that tag and consolidate the way published
models describe, store several sounds at once and play them back later from its own activity?

The project was set up to fail visibly. Every mechanism has an off switch, every result sits
beside the same run with that mechanism removed, and a plain reservoir network is always run
alongside as a baseline.

## The tape did not work

Sound went in readably: a linear decoder recovered the input envelopes from the network's activity
while it listened. Nothing came back out. At every delay, and with every way of prompting recall
that was tried, the decoded output matched the stored sound no better than it matched sounds the
network had never heard. The plain reservoir encoded better.

An early result looked like a partial success: which stored sound was dominant at a given moment could
be read from the order in which cells fired, 77% of the time where shuffled labels reached 57%. A later
code review showed that ordering was measured while the sound was playing and was driven mostly by the
input itself. It says the cells followed the input, not that the network kept anything.

The weight changes explain the failure. What the network wrote into its synapses was set by which
cells happened to fire hardest, not by what they heard. A weight change predicted from any of
twenty sounds the network never heard matched the real one as well as the played sound's did.

## Habituation as memory

The project then asked a smaller question. Repeated sounds evoke smaller responses. Is that
fading a memory of the particular sound, or just fatigue?

Four mechanisms were compared in a small auditory network, each with its own switch:

- depletion of the input synapses;
- depression of a synapse only when the receiving cell also fires;
- inhibition that learns, using a rule of the form published in {% include cite.html key="vogels2011" %};
- receptor removal and replacement, as modelled for a single-celled organism {% include cite.html key="rajan2025" %}.

Two experiments were preregistered: predictions, pass criteria and code were fixed in git before
anything ran. Both closed as failures, because some predictions missed. What they showed:

**Depletion kept no sound-specific memory.** At no delay, from 2 seconds to 90 minutes, did it
suppress the trained sound more than a different one. The main reason is in the ear model. At a
normal listening level, the least-similar of twenty random test sounds still overlapped the
trained one by 0.59 in the simulated auditory nerve, on a scale where 1 is identical. Depleting
shared input fibres cannot tell the two apart.

**Only plasticity gated by the receiving cell was specific.** Depression that needed the
receiving cell to fire picked out the trained sound 30 minutes later. The learned inhibition
suppressed the trained sound too, and removing that inhibitory pathway undid all of it. Its
specificity was limited by the same 0.59 overlap.

## A model that drains where the cell does not

The fourth mechanism reproduces a published model of habituation in *Stentor*, a single-celled
organism. In that model, stimulated receptors are pulled inside the cell and then recycled or
destroyed, and new receptors are made continuously {% include cite.html key="rajan2025" %}. In
real cells, blocking protein synthesis made habituation faster and memory longer, while untrained
cells given the same drug kept responding normally {% include cite.html key="rajan2026" %}.

Run with the published model's own rates, and the paper's time step read as one minute (the paper
states no unit), the block did not do that here:

- untrained responses fell by 32% after 20 minutes and 79% after 90 minutes;
- the extra memory the block produced was at most 1.4 points of suppression.

The published model has basal loss of surface receptors, so a synthesis block drains untrained
cells in the model too. There the drain is hidden by a hard threshold: a cell far above its
contraction threshold keeps contracting while its receptors run down. A readout without that
threshold, like this network's, exposes it. **In this model, the cell's normal untrained response
depends on the threshold, not on the receptor pool.** Whether that holds in the organism is a
question for an experiment, not this simulation.

## Spacing did not help

In roundworms trained at 60-second intervals, long-term habituation followed training split into
blocks with hour-long rests.
Training all at once lowered next-day responses too, but only the spaced group responded
significantly less on the second day than on the first {% include cite.html key="beck1997" %}.

None of the mechanisms reproduced a spacing benefit. With the same number of presentations, spaced
training left less suppression than massed training in the receptor and learned-inhibition models,
and no difference for depletion. (The excitatory-depression model also favoured massed training, but
a later review found its untrained comparison network drifts during a long schedule, so that
comparison is confounded.) Each mechanism has a single decay rate, so earlier blocks simply fade. A spacing effect seems to need a
second, slower consolidation stage that none of these models has.

## What would change these conclusions

- A test pair with genuinely low overlap in the auditory nerve (below about 0.2), at which
  depletion does keep a specific trace. The overlap limit is a property of this ear model at this
  level, not a general law.
- Adding a hard response threshold to the receptor model's readout and finding the untrained
  response still drains.
- A single-timescale mechanism that nonetheless favours spaced training.

The project is paused here. Its findings, defects and the next experiments each would need are
listed in the repository.
