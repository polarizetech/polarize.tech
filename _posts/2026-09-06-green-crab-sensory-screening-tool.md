---
title: "Building a sensory screening tool for the European green crab"
description: >-
  A calculator that answers what a green crab can detect, in what units, at what
  range — and refuses to answer where nobody has measured. What it found about
  mechanoreception, chemistry, electric and magnetic fields, and how the native
  crabs compare.
date: 2026-09-06 09:00:00 -0600
project: invasive-species-bioelectric
status: published
inline_sources: true
tier: C
claims:
image: /assets/posts/european-green-crab.jpg
image_alt: >-
  A European green crab on wet sand, chelae raised, its carapace mottled green
  and its walking legs spread.
image_credit: Victor Heng
image_license: CC0
image_license_url: https://creativecommons.org/publicdomain/zero/1.0/
image_source_url: https://commons.wikimedia.org/wiki/File:Carcinus_maenas_138761951.jpg
citations:
  - bergshoeff2018
  - bergshoeff2019
  - schmidt1989
  - garm2005
  - tautz1980
  - burke1954
  - aimon2021
  - popper2001
  - jzquel2021
  - jury2024
  - coquereau2016
  - wethey2005
  - volkenborn2012
  - hardege2011
  - rising2022
  - bedore2013
  - patullo2010
  - james2025
  - lohmann1984
  - boles2003
  - ernst2016
  - young2019
  - holsman2006
  - pearson1979
  - sugarman1983
  - defur1983
  - moksnes2003
  - nicol2025
  - jeppesen2024
  - tepolt2020
  - thia2021
  - venkataraman2025
  - kasiouras2024
  - magee2013
summary: >-
  The European green crab is a well-studied laboratory animal, which makes it a
  good test of a question worth asking about any organism: how much of its
  sensory front end can actually be computed rather than assumed? The answer
  turned out to be a tool that spends most of its time saying no.
---

The European green crab (*Carcinus maenas*) is unusual among invasive species in being a
classic laboratory animal. That makes it a test of a question worth asking about any
organism: **how much of its sensory front end can be computed rather than assumed?**

Not a simulator. A simulator implies you turn a crank and get behaviour out. This is
narrower: for a given stimulus it answers **how much** arrives at a receptor, **in what
format** that receptor passes it on, and **where** it goes — and refuses when the number
underneath does not exist. The most common output is a refusal.

## The design rule

Every constant carries its provenance: measured in this species, measured in a surrogate,
derived from physics, or assumed. That sounds like bookkeeping. It did the work.

The tags caught six errors already in the model, every one from reading a summary instead of
a source. Two examples:

- A trap statistic entered as "entry success rises from 16% to 59%." Those are two different
  measurements — one the fraction of attempts that succeed, the other a percentage *increase
  in catch* from a modification. The second does not continue the first, and the best
  modification was not the one being quoted.

{% include source.html key="bergshoeff2018" %}
{% include source.html key="bergshoeff2019" %}

- A receptor threshold was carried as a single value where the study reports a range. The
  single number was the low end.

**The rule that generates the rest: an abstract is not a paper.** A source read only at
abstract may be cited as existing; nothing may be said about what it measured. That
constraint is load-bearing below, and it is marked where it bites.

## Mechanical senses — the measured part

The strongest ground, because there is a real transfer function for this species. Mouthpart
setae recordings give displacement thresholds in micrometres and, more usefully, the coding:
spike count scales with displacement amplitude, interspike interval with velocity, and
roughly half the cells are directionally sensitive.

{% include source.html key="garm2005" %}

**That detail is what made the first version wrong.** Those setae are **tactile** receptors
for handling prey, not distance detectors, and far-field stimuli were being scored against
them. The tool now raises a scope flag on any far-field verdict from that row.

The receptor that *is* for water motion is a different one — sensory hairs on the chelae,
studied in crayfish. A joint organ in the walking leg has been described in green crab
itself, the response of intact animals to substrate vibration tested directly, decapod
acoustic detection reviewed as a field, an evoked-potential study in American lobster asks
which organ is responsible, and a consolidated review of green crab sensory biology exists.

{% include source.html key="tautz1980" %}
{% include source.html key="burke1954" %}
{% include source.html key="aimon2021" %}
{% include source.html key="popper2001" %}
{% include source.html key="jzquel2021" %}
{% include source.html key="jury2024" %}

**Where the abstract-only rule bites:** of the seven sources in this section, two were read
at full text. For the other five: they exist, and the question they asked is stated, not what
they found. **So the surrogate threshold the tool uses for the water-motion channel is a
number I cannot attribute**, and it is tagged as a surrogate for that reason.

## The physics that decides most of it

**Near-field falloff.** A small oscillating body in water produces a field falling off as
1/r³ if it oscillates back and forth, 1/r² if it changes volume. The cube law is brutal: a
thousand times more source amplitude buys ten times the range. Ordinary prey is a
centimetre-scale cue; only a large struggling animal or another crab reaches decimetres.

**Displacement is not pressure.** Particle displacement equals velocity over 2πf, so for a
given sound pressure a kilohertz signal carries far less displacement than a hundred-hertz
one. High-frequency sound is displacement-poor, and crabs detect displacement.

Together these explain why the acoustic route keeps failing and the chemical route keeps
winning: a plume falls off as 1/r, and the olfactory threshold is low.

## What prey actually emit

The reference dataset for benthic invertebrate sound gives calibrated source levels for
scallops, limpets, urchins and crustaceans.

{% include source.html key="coquereau2016" %}

Converted to particle displacement and solved against the crab's threshold, none reaches a
crab at more than millimetres — and every sound in that dataset peaks between 5 and 49 kHz,
while the analysis band was filtered from 2 kHz upward. **The corpus was built for hydrophone
monitoring, not prey detection, and the crab's band was removed before analysis.** A null
there is unavailable, not absent.

The promising cue is not a sound. Porewater pressure signals from infaunal activity have been
recorded directly in sediment, and the irrigation timing of three tellinid bivalves —
including a Pacific Northwest clam that is real green crab prey — has been measured.

{% include source.html key="wethey2005" %}
{% include source.html key="volkenborn2012" %}

A slow hydraulic signal, not an acoustic one, and the only prey cue here with a field
detection range measured on relevant species.

## Chemistry, which out-ranges everything

Modelled as a plume, chemical detection spans roughly three orders of magnitude more
distance than any mechanical cue. Two anatomically separate systems do different jobs —
olfaction on the antennules, contact chemoreception on the dactyls, where the gustatory
organs of this species have been characterised electrophysiologically.

{% include source.html key="schmidt1989" %}

**Abstract only, so the threshold separation between the two — which is what the tool runs
on — is a sourced parameter in the model and is not stated here.**

One deliberate refusal: a chemical stimulus is not a scalar. You cannot hand it a single
concentration and get a receptor response, because mixtures cross-adapt and receptors encode
a ratio against background rather than an absolute. Single-compound dose-response is enabled;
mixtures raise an exception.

The female sex pheromone has been identified, and later work with it produced the most
interesting behavioural result in this review.

{% include source.html key="hardege2011" %}
{% include source.html key="rising2022" %}

Males presented with a pheromone-treated dummy female showed a mating response 87% of the
time under ambient conditions and 40% under ship-noise playback — while the *time taken to
respond to the pheromone* did not change significantly. **Noise interfered with completing
the behaviour, not with detecting the signal.** That dissociation is worth more than either
number alone.

## Electric and magnetic — where the tool says no

The two channels refused outright, and the refusals are its highest-confidence outputs.

**Electric.** No electroreceptor has been identified in any crustacean, and none sought in
this species. Not a modelling gap; the state of the field. The physics is unambiguous: prey
bioelectric fields measured at microvolt scale with the electrode under a millimetre from
tissue, and the authors state the voltage from invertebrates was too weak to record away from
the source.

{% include source.html key="bedore2013" %}

A behavioural sensitivity figure exists for a freshwater crayfish — a surrogate, different
order, fresh water.

{% include source.html key="patullo2010" %}

The tool quotes named surrogates and will not produce a crab number.

**Welfare, which is a different question from detection.** This species has nociceptors.
Acetic acid on every soft tissue tested — eyes, antennae, antennules, claws, leg joints —
produced a central nervous response, longer-lasting and lower in amplitude than a touch.

{% include source.html key="kasiouras2024" %}

And green crabs **learn to avoid a place where they are shocked.** Given two shelters, with a
10 V, 180 Hz, 200 ms shock delivered every 5 s through wires on the legs in one of them, they
learned to walk left or right to reach the other. The voltage was set below the level at
which a single shock made a crab drop a leg, and some dropped a wired leg anyway.

{% include source.html key="magee2013" %}

Both read in full. That shock was contact current through the legs, not a field in water, so
it gives the tool **no field threshold** and changes no number above. What it changes is the
expectation: current is aversive to this animal, so an electric lure should be expected to
repel as well as attract. The welfare limit the tool enforces — crayfish forced electrotaxis,
about 4 V/m — marks where current *forces* movement, not where it becomes unpleasant.

**Magnetic.** One directly relevant result: juvenile green crabs exposed to static magnetic
fields at strengths relevant to submarine power cables, **females spending substantially more
time in exposed zones while males showed no consistent preference.**

{% include source.html key="james2025" %}

A real, sex-specific response in this species — and a static-field spatial preference, not a
compass, and not a receptor. Nobody has located the transducer.

**The obvious confound, stated plainly.** Helmholtz coils dissipate heat and crabs are
thermotactic. Working the published coil geometry through a thermal model gives, at the
strongest field over the exposure period, roughly **20 W dissipated, a 0.58 K gradient across
the tank and a 0.30 K bulk rise** — small, but not obviously below what an animal can detect,
and no behavioural thermal-discrimination threshold for this species could be found to
compare against. The model returns a number and refuses a verdict.

One weak argument against the thermal explanation: ohmic heating scales with the square of
the current, so the confound is about ten times larger at the strongest field than at the
intermediate one — while the reported attraction was *strongest at the intermediate field*.
Confound and effect run in opposite directions. **A thermocouple in the tank would settle it,
and that is the cheapest experiment anywhere in this review.**

The usual comparison is the spiny lobster, the standard invertebrate magnetoreception system.

{% include source.html key="lohmann1984" %}
{% include source.html key="boles2003" %}
{% include source.html key="ernst2016" %}

**Here the abstract-only rule bites hardest:** all three read at abstract, so their results
are not characterised. What can be said is about the shape of the literature rather than its
contents — the receptor cells have not been located and characterised in that animal either.
Mapping a mechanism from one order of crustaceans onto another, across more than two hundred
million years of divergence, when the source species' anatomy is itself unresolved, produces
a hypothesis wearing borrowed credibility. The tool returns unavailable and says why.

## How the native crabs compare

The most informative part, because **the comparison cannot be run.**

Across eight receptor channels and five species, green crab has measured values in five
channels and a described-but-unmeasured organ in two. For Dungeness, red rock, graceful rock
and yellow shore crab: **two** measured thresholds, both in Dungeness — a behavioural
detection threshold for a prey extract, and behavioural salinity detection measured by
antennular flicking.

{% include source.html key="pearson1979" %}
{% include source.html key="sugarman1983" %}

**Both at abstract only, so those are descriptions of what was measured, not of what was
found** — the model carries them with the same tag. (A third record sits off the matrix
entirely: dactyl chemo- and mechanoreceptor recordings in the kelp crab, not among the five.)

**Two filled cells out of thirty-two, and the comparison still cannot be run** — for a
smaller reason than an empty literature. Those are *behavioural* thresholds, in grams per
litre and parts per thousand. Every green crab value is *single-unit electrophysiology*, in
micrometres or molar. Not the same quantity, so one row would be a category error rather than
a comparison.

**That is the state of the literature, not a gap in the modelling.** Green crab is a classic
laboratory animal; the natives are commercially and ecologically important animals whose
sensory physiology has largely not been measured.

What *can* be compared is everything except the senses, and there the differences are
substantial and documented: salinity tolerance, depth and zonation, body size, moult timing,
tolerance of emersion and hypoxia.

{% include source.html key="young2019" %}
{% include source.html key="holsman2006" %}
{% include source.html key="defur1983" %}
{% include source.html key="moksnes2003" %}
{% include source.html key="nicol2025" %}
{% include source.html key="jeppesen2024" %}

The first was read at full text and the rest at abstract, which is why this section names
questions rather than answers.

## The genetics, and what is actually there

Looking for a genetic basis for the reproductive advantage — some identified difference
explaining why it out-reproduces the natives. **There isn't one, and the absence is
informative.**

The adaptive-genomics literature for this species is real and substantial. What it is *about*
is temperature: cold tolerance, thermal adaptation, a chromosomal inversion, and the
relationship between genotype and thermal plasticity.

{% include source.html key="tepolt2020" %}
{% include source.html key="thia2021" %}
{% include source.html key="venkataraman2025" %}

Read at abstract only, so their findings are not characterised. But that the surveyed
literature concerns thermal physiology and not reproduction or sensory biology is an
observation about the literature, and it can be made.

So the honest account of why green crab out-reproduce the natives is life-history and
tolerance, not a gene: longer breeding season, earlier maturity at smaller size, two broods a
year where conditions allow, and sperm storage such that one fertilisation can serve more
than one clutch. Note that *reproducing* more is not the same as *mating* more — with sperm
storage the two can move in opposite directions.

## What the tool is for

The most-used outputs are refusals: no electric readout, no magnetic readout, no mixture
readout, no cross-species comparison, no sex difference in transduction. Sex enters in one
place — body size — because no measured threshold in this species differs by sex, and the
tool will not invent one.

The value is not in the numbers. It is that they cannot drift: every constant is pinned by a
test that fails if the figure is misquoted, and in one session those tests caught four errors
that had entered from secondary summaries of paywalled sources — which is how this literature
is normally read.

**The most instructive failure was mine, not the literature's.** The claim that no native
species had a single measured sensory channel was a strong negative drawn from a shallow
search, and it was wrong; a deeper search turned up the two Dungeness thresholds immediately.
**A test had been pinning the wrong number in place**, with a comment beside it admitting the
value was stale. That is worse than an unchecked number, because it looks checked.

Correcting it nearly introduced a new error. The function answering *which channels are
comparable across species* tested only whether a cell was marked measured. Filling the two
Dungeness cells would have made two channels report comparable when the underlying quantities
are not the same thing. It compares units now. **A test that counts statuses will happily
certify a category error**, and the correction is what exposed it.

**What would make it wrong:** a measured audiogram for *Carcinus maenas*, Dungeness and red
rock crab on one rig, showing receptor bands substantially different from the surrogate
values used here. Most mechanical conclusions would need redoing. That measurement does not
exist, and it is the single experiment that would change the most.

## Corrections

**2026-09-06.** Three changes, none erasing anything above.

- The native-comparison section originally said *"two measured chemosensory thresholds in a
  single species and nothing else."* The two are now cited by key, one is a salinity threshold
  rather than a prey-odour one, and **"nothing else" was an overreach** — a third native
  record exists off the matrix. Both are held at abstract only, so the post names what they
  measured and not what they measured it to be. The count of filled cells is unchanged at two
  of thirty-two, and the comparison remains un-runnable.
- **"What the tool is for"** gains the account of how that error survived a test, and of the
  second defect that correcting it exposed.
- The correction has been applied to the model itself, not only to this post.

**2026-09-16.** One addition, nothing erased: the electric section now carries the
green-crab welfare evidence — nociceptive responses and learned shock avoidance — with a
note that neither supplies a field threshold, so no number in the tool changed.
