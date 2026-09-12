---
title: "A hive and a cortex, described the same way"
description: >-
  Two systems — a honeybee colony choosing a nest and a cortical population
  choosing between two motions — have been given the same formal description
  since at least 2009. What that description covers, and where it stops.
date: 2026-09-12 07:00:00 -0600
project: biosignal-translation
status: published
tier: C
claims:
citations:
  - marshall2009b
  - marshall2009
  - seeley2012
  - reina2017
  - lin2026
  - dong2023b
  - barron2007
  - dong2023
  - linn2020
  - cardosojunior2020
  - myersjoseph2024
image: /assets/posts/waggle-dance.jpg
image_alt: >-
  A dense crowd of European honeybee workers covering comb, bodies overlapping
  in every orientation, with open cells visible at the lower edge.
image_credit: Nick Pitsas, CSIRO
image_license: CC BY 3.0
image_license_url: https://creativecommons.org/licenses/by/3.0/
image_source_url: https://commons.wikimedia.org/wiki/File:CSIRO_ScienceImage_7077_European_honeybees_Apis_mellifera_in_a_hive.jpg
summary: >-
  A swarm deciding where to nest and a cortical population deciding which way
  dots are moving have been modelled with the same equations for over fifteen
  years, and the idea is older than that. This is an inventory of what the
  correspondence actually covers, which parts of it are the authors' own claim
  rather than an inference, and the two places the papers themselves say it
  stops.
---

This is an inventory, not an argument. The parallel described below is not mine and is
not new; the point of writing it down is to be precise about how much of it is
established, and where the edges are.

## The observation, and whose it is

A honeybee swarm choosing between two candidate nest sites and a cortical population
choosing which way a field of dots is moving have been given the same formal description.
The clearest statement of it is a 2009 paper in *Journal of the Royal Society Interface*
{% include cite.html key="marshall2009b" %}, which sets a model of primate cortical
decision-making beside three models of house-hunting in ants and honeybees and works
through what they share.

Its own opening is careful to say the idea was already old: speculation about whether
decision-making in brains and in insect colonies is related, in the authors' words,
begins "at least with Hofstadter (1979)" and had been taken up repeatedly before they
wrote. They describe their contribution as a first step toward a common theoretical
framework — one based on the interactions between a system's components rather than on
what the components are. A companion piece the same year discusses the same territory
under the heading of colony-level cognition {% include cite.html key="marshall2009" %}.

So the lineage runs roughly: an analogy in the 1970s, recurring discussion, a formal
treatment in 2009, and then the experimental
work most often cited alongside it, on inhibitory signalling between scouts
{% include cite.html key="seeley2012" %} — a paper whose own title and framing put the
comparison to brains front and centre rather than leaving it to a reader.

## What the correspondence actually covers

Three things, as set out in the 2009 treatment:

- **Populations, not individuals.** Both systems are modelled as mutually interacting
  populations that accumulate noisy evidence for competing alternatives.
- **A threshold on one population.** A choice is made when one population's activity
  crosses a threshold, and the alternative that population represents is the one taken.
- **A threshold that can be moved.** The same threshold trades speed against accuracy.
  Raise it and decisions get slower and more reliable; lower it and the reverse. In the
  cortical model this is a parameter; in the ants it is the number of individuals that
  must accumulate at a site.

The formal claim attached to this is stronger than a resemblance. Under particular
settings, the cortical model reduces to a diffusion process that implements the
sequential probability ratio test — the procedure that, for a two-way choice, minimises
decision time for any given error rate. The 2009 analysis asks which of the colony
models can do the same thing, and treats the answer as a source of testable predictions
about how colonies ought to behave if they are deciding optimally. That is the substance
of the parallel: not that a hive resembles a brain, but that both can be written as the
same statistical procedure.

Extending the same analysis past two options changes it. The best-of-N case — more than two
options — has been analysed separately for whether the controlling parameter stays the
same {% include cite.html key="reina2017" %}
— which is also the point where this literature meets the best-of-N problem in
distributed and robotic systems, since that is the same problem stated without the bees.

## Where the papers say it stops

Two limits come from the 2009 treatment itself, not from a critic.

**The colony has to go and get its information.** In the cortical task, evidence for both
alternatives arrives at a fixed, equal rate. A colony's scouts discover sites
stochastically, which leaves the colony holding an explore-or-exploit problem the
cortical version does not have: assess the sites already known, or look for better ones.
The authors describe this as a hybrid of a bandit problem and a minimum-decision-time
problem, and say no one had formalised it.

**Consensus and foraging are different problems.** This one is easy to lose. The paper
states plainly that the decision a colony solves while emigrating is *optimal consensus*
decision-making, and that this "differs from the problem of distributed resource intake
maximization that colonies tackle during foraging." The quorum figures, and the
cross-inhibition result, come from nest-site selection during swarming. Foraging
recruitment is governed by different machinery. A description that moves freely between
the two is describing two systems, not one.

## Two directions the mapping is being pushed, neither established

The following are working framings, recorded here as untested rather than as findings.

**A modulatory layer.** The decision models above have recruitment and inhibition in
them, and nothing that sets the regime those operate in. Bees have candidates for such a
layer: octopamine dosing has been examined for its effect on how strongly value is
reported in dances {% include cite.html key="barron2007" %}, octopamine and dopamine have
been examined in dance following and information use
{% include cite.html key="linn2020" %}, and an inhibitory signal associated with danger
has been examined against dopamine levels {% include cite.html key="dong2023" %}. Whether
these belong in the decision architecture as a separate axis — gain rather than content —
is a framing, not a result. Note also that the last of those cuts across the tidy version
of it: if a targeted inhibitory signal moves a diffuse modulator, then "selecting among
candidates" and "setting the regime" are not cleanly separable.

**A write step.** Queen mandibular pheromone has been examined against the expression of
genes responsible for epigenetic modifications in worker brains
{% include cite.html key="cardosojunior2020" %}. Placing that as the durable-change step
of a decision architecture is an analogy across levels, and the level mismatch is real:
the bee side of most of these mappings is role-level — dancer, follower, scout — while
the neural side is cell-type-level.

## Two observations that cut the other way

**The signal is shaped by its audience.** Recent work tested whether the information
content of the dance depends on who is watching, by removing bees from the dance floor and
separately by replacing adults with bees too young to follow
{% include cite.html key="lin2026" %}. Directional and distance precision tracked the
number of followers; the precision measures moved, and the paper reports the mean waggle
run duration and distance per run as unchanged. Anything built on
this should preserve that shape: it is a variance effect, not a bias effect. A population
whose output precision depends on the size of its readership is not a one-way sender.

**There is no offline replay on the bee side.** The dance has a fixed structure — a waggle
run, then a return loop that alternates left and right. The return loop repositions the
dancer; no reversed waggle run is reported. On the neural side, compressed reactivation of
place-cell sequences in both directions is a large literature. The absence of a bee
counterpart is an absence of reported evidence rather than a study that looked and found
none, and it is the clearest gap in the correspondence as it currently stands.

## What would make this description wrong

The parallel is about dynamics, so the things that would break it are dynamical:

- Follower recruitment turning out to be determined almost entirely by the instantaneous
  properties of a dance, with no contribution from the prior state of the dance floor.
- Simultaneous dances that do not measurably interact through competition for a finite
  pool.
- Cross-inhibition in swarms and in cortex producing qualitatively different dynamics
  under matched conditions.
- The thresholds turning out to be observer cutoffs rather than nonlinear transitions in
  a population variable.

One more caution belongs here, because it is about the neural side rather than the bee
side. It is tempting to reach for cortical disinhibition as the mechanism of attention and
then borrow it. Whether that link holds is an
open question in its own literature, and has been tested directly for one interneuron
class in primary visual cortex {% include cite.html key="myersjoseph2024" %}. Importing
"disinhibition is attention" would import an unsettled claim, whichever way it settles.

## On sources

Two of the papers cited here have been read beyond their abstracts: the 2009 framework
paper, in the sections carrying its conclusions rather than its derivations, and the
audience study, whose results section was read in full. The rest are cited as entry points
to their topics. Where this post describes what a study examined, that
wording is deliberate — it marks the difference between pointing at a result and having
checked it. Social learning of the dance itself {% include cite.html key="dong2023b" %}
is cited on the same footing.
