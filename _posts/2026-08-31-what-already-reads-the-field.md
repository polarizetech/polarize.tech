---
title: "What already reads the field"
description: >-
  Sharks, bumblebees, spiders, electric fish, sediment bacteria and migratory
  birds all solve sensing problems this bench keeps re-deriving. A survey of the
  biological precedent — and one popular story about spider webs that is wrong.
date: 2026-08-31 09:00:00 -0600
project: bioem-propagation
status: published
tier: A
claims:
citations:
  - kalmijn1971
  - clarke2013
  - sutton2016
  - morley2018
  - bell1997
  - kennedy2014
  - ortegajimenez2013
  - pfeffer2012
  - toyota2018
  - blakemore1975
  - xu2021
summary: >-
  Biology solved electric and magnetic sensing long before anyone built an
  instrument for it, and the solutions are stranger than the engineering ones.
  Two of the three field-sensing organisms here do it with *hair* rather than
  electrodes; one system does it with no receptor at all; and the two magnetic
  mechanisms are so different that copying one gives you a compass and copying
  the other gives you a spectrometer.
---

Three times now I have hit a sensing question on this bench — how weak a field can be
detected, across what distance, with what geometry — and found that something alive
had already settled it. This post is the survey I wish I had read first.

**What this post is, exactly.** It describes phenomena at the level where they are
settled and uncontroversial, and it is tiered accordingly. Each source below is
cited as *the entry point to its topic* — none of them has been read here at full
text, so nothing on this page reports what any individual paper measured or
concluded. Where I say something is known, I mean textbook-known, not
"this study showed."

## Reading a field another body makes

The oldest example is the one everybody has heard of. Sharks, rays and skates
detect the standing bioelectric field that surrounds another animal, using
jelly-filled canals in the head called the ampullae of
Lorenzini {% include cite.html key="kalmijn1971" %}. Seawater helps enormously
here: it conducts, so a body's field propagates through it and stays readable at
a distance.

The two examples that impressed me more happen in **air**, which is much harder,
because air does not conduct and there is no comparable field to swim through.

Bumblebees detect the electric field around a flower {% include cite.html key="clarke2013" %}.
Spiders detect the atmospheric potential gradient — the standing voltage difference
between the ground and the sky — and use it as a cue for
ballooning {% include cite.html key="morley2018" %}.

Both solve the air problem the same way, and this is the part worth taking:
**neither uses anything like an electrode.** They use hair {% include cite.html key="sutton2016" %}.
A charged filament sitting in an electric field experiences a force and moves, and both
animals already had an organ exquisitely good at detecting the movement of hairs, because
that is how they sense air currents and vibration. The field sense is a *mechanical* sense
wearing a different hat.

For anyone building an instrument, that reframes the problem. A field detector does
not have to be a voltage-measuring device in contact with something. It can be
anything charged, compliant, and watched closely enough.

## Reading a field you make yourself

Everything above is passive: the animal reads a field something else produced. There is a
second mode, and it is the one an instrument builder should look at hardest, because it is
the one where you supply the signal.

Weakly electric fish emit a discharge from a dedicated organ and read how nearby objects
perturb it. That is active sensing — the same idea as radar or sonar, arrived at
independently, in water.

What makes it worth studying is not that it works. It is what it costs. Four things have to
be present, and each is separately necessary:

1. An organ that produces a discrete, command-triggered discharge.
2. A receptor class tuned to that discharge, distinct from the receptors the same fish uses
   to sense other animals passively.
3. A cerebellum-like structure that learns a **negative image** of the animal's own
   discharge and subtracts it, through a plasticity rule that depends on the order in which
   the two inputs arrive {% include cite.html key="bell1997" %}.
4. A **corollary discharge** — a copy of the motor command that fired the organ — supplying
   the timing the negative image is built against
   {% include cite.html key="kennedy2014" %}.

Item 4 is the one I keep coming back to. The cancellation is not computed from the recorded
signal. It is timed from the *command that caused it*, before the signal arrives. An
instrument that emits and then tries to subtract its own contribution by measuring it is
solving a harder problem than the fish is, and the fish has had a long time to look for an
easier route.

The other half of the lesson is a warning about copying it. This works in water because
water conducts, so the fish drives a current through the medium and objects perturb the
current density at its skin. Air does not conduct. The nearest thing in air is capacitive —
a nearby object changes how much charge sits where — which is a different quantity, with a
different distance dependence, and it responds to a different property of the object. The
intuition transfers; the arithmetic does not.

## The spider web — and the story that is wrong

There is a well-travelled claim that a spider web's geometry does something clever
with *light* — that the web amplifies a fly's photons, or exploits some optical
property of the spiral. I went looking for it because it is a good story.

It is not what happens. What actually happens is
**electrostatic** {% include cite.html key="ortegajimenez2013" %}. Insects in flight
carry charge. A web does not. When a charged insect passes close, the silk is pulled
toward it — the threads physically deform in its direction, which makes contact more
likely than the geometry alone would predict.

That is a better story than the optical one, for a reason worth stating plainly:
**there is no sensor anywhere in it.** No receptor, no nerve, no organism doing
anything. It is a passive dielectric structure whose shape converts a static charge
difference into mechanical motion. Everything else in this post is an animal reading
a field. This is geometry alone doing the work.

I mention the correction rather than quietly writing the right version because the
two ideas get conflated constantly, and only one of them has a source behind it.

## Signals that travel

Distance is the constraint that kills most sensing ideas, so it is worth knowing what
biology manages.

In marine sediment there are filamentous bacteria that move **electrons** along their
length, through conductive structures running the length of the
filament {% include cite.html key="pfeffer2012" %}. The distances involved are
centimetres — which sounds modest until you hold it against the size of a cell, where
it is enormous.

Plants do something different and just as long-ranged: a wound at one site produces a
travelling calcium wave that reaches undamaged tissue elsewhere in the
organism {% include cite.html key="toyota2018" %}.

The reason to keep these two apart is that they are not the same kind of transport.
Most of what I reason about on this bench is ionic — the action potential, charge
moving across a membrane. **Cable bacteria are not doing that.** They are moving
electrons, which is a different mechanism with different limits, and it is a useful
reminder that "biological conduction" is not one thing.

*(On algae specifically: giant algal cells are a foundational preparation in plant
electrophysiology and do carry propagating electrical signals. I have not put a source
for long-distance algal signalling into the ledger yet, so there is no entry for it
here. That is a gap, not a judgement.)*

## Two ways to feel the Earth

Magnetoreception is where the divergence gets sharpest, because the two best-known
mechanisms have almost nothing in common.

Some bacteria build chains of magnetic particles inside membrane-bound
compartments {% include cite.html key="blakemore1975" %}. The cell is then physically
torqued into alignment by the Earth's field. This is a **compass needle** in the most
literal sense: no energy budget, no light, no computation, no nervous system. The
physics does the work and the organism goes along with it.

Migratory songbirds are thought to do something entirely different — a light-dependent
reaction in a protein in the eye, where the magnetic field influences the chemistry of
a short-lived pair of radicals {% include cite.html key="xu2021" %}. This is a
**chemical magnetometer**. It needs a photon to start, and it reports the field as a
change in how a reaction turns out.

Copy the first and you have built a magnetometer. Copy the second and you have built a
spectrometer that happens to be field-sensitive. Same environmental quantity, two
instruments with nothing in common — which is a useful thing to have internalised
before deciding what "detecting the field" is going to mean for a given design.

## What I take from it

Three things, all structural, none of them a finding of mine:

1. **A field sensor can be a motion sensor.** Two of the three organisms above read
   electric fields with hairs. Any charged, compliant surface is a candidate transducer.
2. **Geometry alone can convert a field into motion**, with no receptor in the loop at all.
3. **Long-distance conduction in biology is not always ionic.** Electrons travel too.
4. **If an instrument emits, cancelling its own signal is most of the work** — and the one
   animal that does this times the cancellation from the command, not from the recording.

None of this is evidence for anything I am claiming. It is a map of where the good
ideas already are, and every one of them was arrived at by something with no access to
an amplifier.

## Corrections

If any statement above overreaches its source, that is a defect and I want it reported
— the whole point of citing by key is that you can go and check. The spider-web
paragraph exists because I believed the wrong version myself.
