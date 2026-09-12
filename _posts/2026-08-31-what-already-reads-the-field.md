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
tier: C
claims:
citations:
  - kalmijn1971
  - clarke2013
  - sutton2016
  - morley2018
  - ortegajimenez2013
  - kennedy2014
  - bell1997
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
settled. Six of the twelve sources below were read at full text and are marked as such on
their cards. The other six could not be — paywalled or unindexed — and are entry points
only: where this post says a study *examined* something, or hedges a mechanism, that marks
pointing at a result rather than having checked it. The two flat statements that rest on an
unread source are textbook-level and carry nothing specific to those papers.

## Reading a field another body makes

Sharks, rays and skates detect the standing bioelectric field around another animal, using
jelly-filled canals in the head called the ampullae of Lorenzini. Seawater conducts, so the
field stays readable at a distance.

{% include source.html key="kalmijn1971" %}

Bumblebees detect the electric field around a flower, learn it as a reward cue, and
discriminate one field geometry from another. A flying bee carries about 32 pC, positive in
94% of individuals measured; a flower sits near ground potential through its stem and roots.
The difference is the signal.

{% include source.html key="clarke2013" %}

The sensor is body hair, not the antenna. Charged hairs move measurably at a stimulus around
twenty times weaker than antennae need, and hair deflection produces nerve firing where
antennal deflection produces none — with air-puff and scent controls confirming the antennal
recording was live.

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

Insects in flight carry charge. Held near a grounded orb web, charged honeybees, bottle
flies, fruit flies, aphids and water drops pull silk threads toward them by 1–2 mm at
0.7–1.9 m/s; uncharged controls produce no such deformation. Cross-spider mesh spacing is
about 2 mm, so the measured deflection is the size of the gap it would have to close. Roughly
30% of charged-insect trials produced no visible deformation and were kept in the analysis
anyway, which is where the large variance comes from.

{% include source.html key="ortegajimenez2013" %}

**Capture probability was not measured.** The deformation was. The effect on prey capture is
an inference from the deflection being mesh-sized, and the paper says so in those terms. The
charge a web carries in the wild has never been reported.

**There is no receptor anywhere in this.** No nerve, no organism doing anything. A passive
dielectric structure whose shape converts a static charge difference into mechanical motion.

A correction worth recording: the effect is **electrostatic, not optical.** Not photon
interaction, not amplification of light, not a quantum-optical property of the spiral. The
optical version circulates widely and has nothing behind it.

## Active electric sense

Some fish generate a field and read its distortion, rather than reading a field something
else made. That inverts the problem: the organism supplies the carrier — and then has to
subtract it. A mormyrid's own discharge reaches its passive electroreceptors too, and the
electrosensory lobe cancels it with a negative image assembled from granule-cell responses
that span the roughly 200 ms following the motor command.

{% include source.html key="kennedy2014" %}

The timing-dependent plasticity rule such a prediction would be learned through is an entry
point here, not something checked.

{% include source.html key="bell1997" %}

**Self-interference is part of the design, not a defect in it.** Any instrument that supplies
its own carrier inherits the same problem, and the biological answer is a learned model of
its own output rather than a better filter.

## Signals that travel

Distance kills most sensing ideas, so what biology manages is worth knowing.

Filamentous bacteria in marine sediment have been examined for electron transport along
their length, over distances described in centimetres — modest until held against the size
of a cell.

{% include source.html key="pfeffer2012" %}

Plants have been examined for a different long-range mechanism: whether a wound at one site
triggers a travelling calcium signal reaching undamaged tissue elsewhere.

{% include source.html key="toyota2018" %}

**These would not be the same transport.** Most of what this bench reasons about is ionic —
charge across a membrane. The cable-bacteria claim is electron transport, a different
mechanism, and it is a claim this bench has pointed at rather than checked. "Biological
conduction" is not one thing.

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

Some bacteria swim along the local geomagnetic field and carry iron-rich particles inside
intracytoplasmic vesicles. That those particles give the cell a magnetic moment which torques
it into alignment is how the original report proposed it — the word that report used was
"conceivably" — and it is settled textbook material today. It was not checked here.

{% include source.html key="blakemore1975" %}

**A compass needle, on the accepted mechanism.** No energy budget, no light, no computation,
no nervous system. The physics does the work.

Migratory songbirds are thought to do something else — a light-dependent reaction in a
retinal protein, where the field influences the chemistry of a short-lived radical pair.

{% include source.html key="xu2021" %}

**A chemical magnetometer, if the mechanism holds.** It would need a photon to start, and
would report the field as a change in reaction yield rather than as a force.

Copy the first and you have built a magnetometer. Copy the second and you have built a
spectrometer that happens to be field-sensitive. Same environmental quantity, two
instruments with nothing in common.

## What transfers

1. **A field sensor can be a motion sensor.** Two of the three organisms above read electric
   fields with hairs.
2. **Geometry alone can convert a field into motion**, with no receptor in the loop.
3. **Long-distance conduction may not always be ionic.** Electron transport is claimed too.
4. **Passive resonance buys single-digit gain.** Not orders of magnitude.

None of this is evidence for anything claimed here. It is a map of where the good ideas
already are, and every one was arrived at by something with no access to an amplifier.

## Correction — 2026-09-12

The original text said the spiderweb study tested "whether it changes capture probability."
It did not. That study measured thread deformation only; the effect on prey capture is the
authors' inference from the deformation being the size of the web's mesh spacing, and they
state it as such. The paragraph has been rewritten and the inference is now marked as one.

Two further statements were written flatter than their sources supported and have been
hedged: the torque mechanism in magnetotactic bacteria, which the 1975 report offers as
conjecture, and the radical-pair mechanism in songbirds, which remains a proposal.

This post published on 2026-08-31 with two of its twelve sources read at full text. Ten were
chased on 2026-09-12; four more could be read and are now marked on their cards, and the
bumblebee and mormyrid paragraphs were rewritten to report what those papers actually found.
The remaining six are paywalled or unindexed, and every statement resting on one of them is
pointing language by design, not by accident.

The post's tier has been lowered from B to C in the same change. Tier B requires that the
gate pass in strict mode, which fails on any source not read at full text; six of these
cannot be read at any price short of buying them individually. C is the tier whose rule this
post actually satisfies — unread sources are permitted, provided the prose that rests on them
is hedged, which is now the case for all six. Nothing in the findings above got weaker; the
label got honest.

## Corrections

If a statement above overreaches its source, that is a defect and worth reporting — the
point of citing by key is that you can check. The spider-web paragraph exists because the
wrong version was believed here first.
