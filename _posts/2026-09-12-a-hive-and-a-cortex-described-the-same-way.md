---
title: "A hive and a cortex, described the same way"
description: >-
  A honeybee colony choosing a nest and a cortical population choosing between
  two motions have carried the same formal description since 2009. What it
  covers, and where its own authors say it stops.
date: 2026-09-12 07:00:00 -0600
project: biosignal-translation
status: published
tier: C
inline_sources: true
claims:
citations:
  - marshall2009b
  - marshall2009
  - seeley2012
  - reina2017
  - lin2026
  - dong2023b
  - barron2007
  - linn2020
  - dong2023
  - cardosojunior2020
  - myersjoseph2024
citation_notes:
  - marshall2009b >> The formal treatment. Read at full text for the sections carrying its conclusions; the model derivations were not read.
  - marshall2009 >> Same authors, same year, the idea under a different heading.
  - seeley2012 >> The experimental result usually paired with the framework above.
  - reina2017 >> Extends the analysis past two options.
  - lin2026 >> Results section read in full. The statistics quoted here come from it; no interpretation is attributed to it.
  - myersjoseph2024 >> Published version of a preprint; the published title narrows the claim to cross-modal attention.
image: /assets/posts/waggle-dance.jpg
image_alt: >-
  A dense crowd of European honeybee workers covering comb, bodies overlapping
  in every orientation, with open cells visible at the lower edge.
image_credit: Nick Pitsas, CSIRO
image_license: CC BY 3.0
image_license_url: https://creativecommons.org/licenses/by/3.0/
image_source_url: https://commons.wikimedia.org/wiki/File:CSIRO_ScienceImage_7077_European_honeybees_Apis_mellifera_in_a_hive.jpg
summary: >-
  Inventory of an existing parallel, not a proposal. A swarm choosing a nest and
  a cortical population choosing a direction are modelled as the same
  statistical procedure. The parallel is not mine; it dates to at least 1979 and
  was formalised in 2009.
---

An inventory. The parallel below is not mine and is not new.

## The parallel, and whose it is

A swarm choosing between two nest sites and a cortical population choosing which way dots
move have been given one formal description.

{% include source.html key="marshall2009b" %}

That paper dates the idea to "at least Hofstadter (1979)" in its own introduction, and
describes itself as a first step toward a common framework — one built on how a system's
components interact rather than on what they are.

{% include source.html key="marshall2009" %}

The experimental work usually paired with it concerns inhibitory signalling between scouts.
Its title and framing put the comparison to brains in front, rather than leaving it to a
reader.

{% include source.html key="seeley2012" %}

## What the description covers

Three properties, per the 2009 treatment:

- **Populations, not individuals.** Interacting populations accumulate noisy evidence for
  competing alternatives.
- **A threshold on one population.** The alternative whose population crosses first is the
  one taken.
- **A threshold that moves.** Raising it buys accuracy and costs speed. A parameter in the
  cortical model; a headcount at a site in the ants.

The claim is stronger than resemblance. Under particular settings the cortical model
reduces to a diffusion process implementing the sequential probability ratio test — for a
two-way choice, the procedure minimising decision time at any given error rate. The
analysis asks which colony models do the same, and treats the answer as a prediction about
how colonies should behave if deciding optimally.

Past two options the analysis changes.

{% include source.html key="reina2017" %}

This is also where the literature meets the best-of-N problem in distributed and robotic
systems — the same problem stated without the bees.

## Where its own authors say it stops

**The colony must go and get its evidence.** In the cortical task, evidence for both
alternatives arrives at a fixed equal rate. Scouts discover sites stochastically, leaving
an explore-or-exploit problem the cortical version does not have: assess what is known, or
look for better. The authors call it a hybrid of a bandit problem and a
minimum-decision-time problem, and say nobody had formalised it.

**Consensus is not foraging.** The paper states that colony emigration is *optimal
consensus* decision-making and "differs from the problem of distributed resource intake
maximization that colonies tackle during foraging." Quorum figures and the cross-inhibition
result come from nest-site selection during swarming. Foraging recruitment runs on
different machinery. A description that moves between the two is describing two systems.

## Two extensions, neither established

Recorded as framings, not findings.

**A modulatory layer.** The models have recruitment and inhibition, and nothing setting the
regime those run in. Bees have candidates.

{% include source.html key="barron2007" %}
{% include source.html key="linn2020" %}
{% include source.html key="dong2023" %}

Whether these belong in the architecture as a separate axis — gain rather than content — is
untested. The third cuts across the tidy version: if a targeted inhibitory signal moves a
diffuse modulator, then selecting among candidates and setting the regime are not cleanly
separable.

**A write step.** Queen pheromone has been examined against expression of genes responsible
for epigenetic modifications in worker brains.

{% include source.html key="cardosojunior2020" %}

Placing that as the durable-change step is an analogy across levels. The level mismatch is
real: the bee side is role-level — dancer, follower, scout — and the neural side is
cell-type-level.

## Two observations that cut the other way

**The signal is shaped by its audience.** Removing bees from the dance floor, and separately
replacing adults with bees too young to follow, was used to test whether dance information
content depends on who is watching. Directional and distance precision tracked follower
numbers; mean waggle-run duration and distance per run are reported unchanged.

{% include source.html key="lin2026" %}

A variance effect, not a bias effect. A population whose output precision depends on its
readership is not a one-way sender.

**No offline replay on the bee side.** The dance is a waggle run, then a return loop
alternating left and right. The loop repositions; no reversed waggle run is reported.
Compressed reactivation of place-cell sequences in both directions is a large neural
literature. The bee-side absence is absence of reported evidence, not a study that looked.

{% include source.html key="dong2023b" %}

## What would make this wrong

- Follower recruitment determined almost entirely by instantaneous dance properties, with
  no contribution from prior dance-floor state.
- Simultaneous dances that do not measurably interact through competition for a finite pool.
- Cross-inhibition in swarms and cortex producing qualitatively different dynamics under
  matched conditions.
- Thresholds turning out to be observer cutoffs rather than nonlinear population
  transitions.

One caution on the neural side. Reaching for cortical disinhibition as the mechanism of
attention and then borrowing it imports an unsettled claim.

{% include source.html key="myersjoseph2024" %}

## On sources

Two of the papers above were read beyond their abstracts: the 2009 framework, in the
sections carrying its conclusions, and the audience study, its results section. The rest are
entry points. Where this post says a study *examined* or *tested* something, that wording is
load-bearing — it marks pointing at a result rather than having checked it.
