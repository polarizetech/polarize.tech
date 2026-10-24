---
title: "The signal in the mixing"
description: >-
  A speculation that the byproducts of competing neural activity may carry information about
  attention, memory and recall, rather than being merely noise to remove.
date: 2026-09-28 06:00:00 -0600
tier: SPEC
---

I keep coming back to a comparison between remembering a sound and listening to one. A memory
of a sound and a live sound could recruit overlapping parts of the brain, but they are different
signals, with potentially different timing and periodicities. If both are active at once, they
do not only coexist. They mix. That mixing is the part I want to understand.

I want a strong mathematical way to identify which frequencies in an EEG—or, with a different
physiological source model, an ECG—are likely to be source components, which are harmonics or
intermodulation products, and which may have been introduced by the recording system. I do not
want to treat every unexpected component as noise and throw it away. Some of it may be artefact,
but some of it may be part of what neural activity does to the state of the brain when
populations fire in synchrony, fall out of synchrony, and compete.

My hunch is that these byproducts and side effects may be more significant than they look. A
nonlinear system can produce harmonics and other mixing products when several inputs interact.
If neural populations do that, the resulting components may carry information about the
interaction, even when they are not independent source signals themselves. They would become
part of the footprint of ongoing competition or consideration of a stimulus, and therefore part
of the experience and its outcome.

What if part of the conscious brain's meta-analysis of thought appears in this mixing? The
harmonics or intermodulation products would not have to be thoughts in themselves. They might
instead be traces of the calculation: the result of combining, comparing, or choosing among
internally recalled and externally driven activity. Whether or not that interpretation survives,
the interaction still matters. The mixture changes the signal that every nearby neuron receives.

This is where I start thinking about neurons less as passive followers and more as individual
responders. I do not mean that each neuron is sentient or consciously aware. I mean that its
response depends on its current state, its past state, how it has habituated to similar signals,
and the mathematical structure of the activity arriving around it. In that limited sense, each
neuron is deciding which population to join, which signal to follow, or whether to remain caught
between them. The mathematics of the experience may be what causes it to attach to one stimulus
rather than another.

So the problem runs in both directions. Given several known stimuli, can I predict the harmonics,
intermodulation products, phase relationships, and other side effects that their competition
might produce? Given the recorded outcome, can I work backwards to a constrained set of source
signals and interactions that could have produced it? I am imagining something algebraic: a
forward model of how competition creates the measured mixture, paired with an inverse model that
tests which sources and interactions are compatible with that mixture.

The inverse direction is the dangerous one. A scalp recording does not contain a unique answer
to where every component came from, and the recording chain can create its own distortion. The
goal cannot be to divide the signal back down and declare that I have recovered the one true set
of sources. It would have to be a model that states its assumptions, separates biological
nonlinearity from instrumental distortion where it can, and returns plausible explanations with
uncertainty rather than certainty.

But even that would be useful. It could help distinguish an externally driven rhythm from an
internally recalled one, or show when their interaction is better explained by simple linear
superposition than by nonlinear mixing. It could also make the competition itself measurable:
not only identifying that two populations are active, but estimating the side effects and impact
of their synchrony, desynchrony, and changing rates of recruitment.

This is the tool I want to work toward: not a noise remover, but a way to read population
competition from EEG and other extracellular field recordings. It would ask what in the signal
is a source, what is a consequence of sources interacting, what belongs to the instrument, and
what cannot be known from the recording alone. The mixing may not be a distraction from the
activity I care about. It may be where some of the information is.

## Where I'd start

The first comparison I want to design is remembering a sound versus listening to one, then both
at the same time. I want to document it in the research project and, if simulations are needed,
keep those beside the rest of the simulation work. The useful tool would have to work forwards
and backwards: predict what known sources and interactions should produce, then test what can
and cannot be inferred from the mixture they leave behind.
