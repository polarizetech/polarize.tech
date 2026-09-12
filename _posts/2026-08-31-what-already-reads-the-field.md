---
title: "What already reads the field"
description: >-
  Sharks, bumblebees, spiders, electric fish, sediment bacteria and migratory
  birds all solve sensing problems this bench keeps re-deriving. A survey of the
  biological precedent — and one popular story about spider webs that is wrong.
date: 2026-08-31 09:00:00 -0600
project: bioem-propagation
status: published
inline_sources: true
tier: B
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
  - kane2018
  - blakemore1975
  - xu2021
image: /assets/posts/peacock-crest.jpg
image_alt: >-
  A peafowl in profile, its fan-shaped head crest of narrow feathers with wide
  flags at the tips clearly visible against a paved background.
image_credit: Thomas Quine
image_license: CC BY 2.0
image_license_url: https://creativecommons.org/licenses/by/2.0/
image_source_url: https://commons.wikimedia.org/wiki/File:Peacock_crest_(24697301410).jpg
summary: >-
  Biology solved electric and magnetic sensing long before anyone built an
  instrument for it, and the solutions are stranger than the engineering ones.
  Two of the three field-sensing organisms here do it with *hair* rather than
  electrodes; one system does it with no receptor at all; and the two magnetic
  mechanisms are so different that copying one gives you a compass and copying
  the other gives you a spectrometer.
---

Survey of biological precedent. Phenomena are described at the level where they are
settled. Two sources below were read at full text and are marked as such on their cards;
the rest are entry points, and where this post says a study *tested* or *examined*
something, that marks pointing at a result rather than having checked it.

## Reading a field another body makes

Sharks, rays and skates detect the standing bioelectric field around another animal, using
jelly-filled canals in the head called the ampullae of Lorenzini. Seawater conducts, so the
field stays readable at a distance.

{% include source.html key="kalmijn1971" %}

Bumblebees detect the electric field around a flower.

{% include source.html key="clarke2013" %}
{% include source.html key="sutton2016" %}

Spiders detect the atmospheric potential gradient — the standing voltage between ground and
sky — and use it as a cue for ballooning.

{% include source.html key="morley2018" %}

**Both air cases use hair, not electrodes.** A charged filament in a field experiences a
force and moves; both animals already had an organ good at detecting hair movement, because
that is how they sense air currents and vibration. The field sense is a mechanical sense in
a different role.

For instrument design that reframes the problem: a field detector need not be a
voltage-measuring device in contact with anything. Anything charged, compliant, and watched
closely enough is a candidate.

## Geometry with no sensor in it

Insects in flight carry charge; a web does not. Whether that difference deforms the silk
toward a passing insect, and whether it changes capture probability, has been tested
directly.

{% include source.html key="ortegajimenez2013" %}

**There is no receptor anywhere in this.** No nerve, no organism doing anything. A passive
dielectric structure whose shape converts a static charge difference into mechanical motion.

A correction worth recording: the effect is **electrostatic, not optical.** Not photon
interaction, not amplification of light, not a quantum-optical property of the spiral. The
optical version circulates widely and has nothing behind it.

## Active electric sense

Some fish generate a field and read its distortion, rather than reading a field something
else made. That inverts the problem: the organism supplies the carrier.

{% include source.html key="bell1997" %}
{% include source.html key="kennedy2014" %}

## Signals that travel

Distance kills most sensing ideas, so what biology manages is worth knowing.

Filamentous bacteria in marine sediment have been examined for electron transport along
their length, over distances described in centimetres — modest until held against the size
of a cell.

{% include source.html key="pfeffer2012" %}

Plants have been examined for a different long-range mechanism: whether a wound at one site
triggers a travelling calcium signal reaching undamaged tissue elsewhere.

{% include source.html key="toyota2018" %}

**These are not the same transport.** Most of what this bench reasons about is ionic —
charge across a membrane. Cable bacteria move electrons. "Biological conduction" is not one
thing.

*On algae: giant algal cells are foundational in plant electrophysiology and carry
propagating electrical signals. No source for long-distance algal signalling is in the
ledger yet, so there is no entry. A gap, not a judgement.*

## A tuned mechanical receiver

Peafowl crest feathers have been measured for resonance against the frequencies of
conspecific display.

{% include source.html key="kane2018" %}

The relevant quantity is the gain a tuned passive resonator buys, and the reported values
are single-digit. Useful as a ceiling: a passive biological resonator in fluid at body
temperature is not a high-Q device.

## Two ways to feel the Earth

Some bacteria build chains of magnetic particles in membrane-bound compartments. The cell is
physically torqued into alignment.

{% include source.html key="blakemore1975" %}

**A compass needle, literally.** No energy budget, no light, no computation, no nervous
system. The physics does the work.

Migratory songbirds are thought to do something else — a light-dependent reaction in a
retinal protein, where the field influences the chemistry of a short-lived radical pair.

{% include source.html key="xu2021" %}

**A chemical magnetometer.** Needs a photon to start, and reports the field as a change in
reaction yield.

Copy the first and you have built a magnetometer. Copy the second and you have built a
spectrometer that happens to be field-sensitive. Same environmental quantity, two
instruments with nothing in common.

## What transfers

1. **A field sensor can be a motion sensor.** Two of the three organisms above read electric
   fields with hairs.
2. **Geometry alone can convert a field into motion**, with no receptor in the loop.
3. **Long-distance conduction is not always ionic.** Electrons travel too.
4. **Passive resonance buys single-digit gain.** Not orders of magnitude.

None of this is evidence for anything claimed here. It is a map of where the good ideas
already are, and every one was arrived at by something with no access to an amplifier.

## Corrections

If a statement above overreaches its source, that is a defect and worth reporting — the
point of citing by key is that you can check. The spider-web paragraph exists because the
wrong version was believed here first.
