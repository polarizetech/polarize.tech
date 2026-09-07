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
summary: >-
  The European green crab is a well-studied laboratory animal, which makes it a
  good test of a question worth asking about any organism: how much of its
  sensory front end can actually be computed rather than assumed? The answer
  turned out to be a tool that spends most of its time saying no.
---

The European green crab (*Carcinus maenas*) is unusual among invasive species in being a
classic laboratory animal. That makes it a good test of a question worth asking about any
organism: **how much of its sensory front end can be computed rather than assumed?**

The thing I built is not a simulator. A simulator implies you can turn a crank and get
behaviour out the other end. What this does is narrower and, I think, more useful: for a
given stimulus it answers **how much** arrives at a receptor, **in what format** that
receptor passes it on, and **where** it goes — and it refuses to answer when the number
underneath does not exist. Calling it a *screening tool* is more honest than calling it a
simulator, and the difference matters, because the most common output is a refusal.

## The design rule: every number carries where it came from

Each constant in the tool is tagged with its provenance — measured in this species, measured
in a surrogate species, derived from physics, or assumed. That sounds like bookkeeping. It
turned out to be the part that did the work.

Over the course of building it, the tags caught six errors that had already made it into the
model, every one of them from reading a summary instead of a source. Two examples, because
they are the kind of thing that is invisible without the discipline:

- A trap statistic entered the model as "entry success rises from 16% to 59%." Those are two
  different measurements — one is the fraction of attempts that succeed{% include cite.html key="bergshoeff2018" %}, the other is a
  percentage *increase in catch* from a modification{% include cite.html key="bergshoeff2019" %}. The second does not continue the
  first, and the best modification was not the one being quoted.
- A receptor threshold was carried in the model as a single value when the underlying study
  reports a range{% include cite.html key="schmidt1989" %}. The single number was the low end of it.

The rule that generates the rest: **an abstract is not a paper.** A source read only at
abstract can be cited as existing, but nothing may be said about what it measured. That
constraint is load-bearing in what follows, and I have marked where it bites.

## The mechanical senses — the part that is genuinely measured

The strongest ground is mechanoreception, because there is a real transfer function for this
species. Recordings from the mouthpart setae give displacement thresholds in micrometres,
and — more useful — the *coding*: spike count scales with displacement amplitude, interspike
interval with velocity, and roughly half the cells are directionally
sensitive{% include cite.html key="garm2005" %}.

That last detail is what made the first version of the tool wrong. Those setae are **tactile**
receptors for handling prey, not distance detectors, and I had been scoring far-field stimuli
against them. The tool now raises a scope flag on any far-field verdict from that row, because
the answer it would give is meaningless.

The receptor that *is* for water motion is a different one: sensory hairs on the chelae, studied
in crayfish{% include cite.html key="tautz1980" %}. A joint organ in the walking leg has been
described in green crab itself{% include cite.html key="burke1954" %}, the behavioural response of
intact animals to substrate vibration has been tested
directly{% include cite.html key="aimon2021" %}, and decapod acoustic detection has been reviewed
as a field{% include cite.html key="popper2001" %}. An evoked-potential study in the American
lobster asks which organ is actually responsible{% include cite.html key="jzquel2021" %}, and a
consolidated review of green crab sensory biology
exists{% include cite.html key="jury2024" %}.

**Where the abstract-only rule bites, and it bites here:** of the seven sources in this section I
have read two at full text. For the other five I can tell you they exist and what question they
asked — not what they found. **So the surrogate threshold the tool actually uses for the
water-motion channel is a number I am not in a position to attribute**, and the tool carries it
tagged as a surrogate for exactly that reason.

## The physics that decides most of it

Two pieces of arithmetic ended up governing nearly every conclusion.

**Near-field falloff.** A small oscillating body in water produces a field that falls off as
1/r³ if it oscillates back and forth, or 1/r² if it changes volume. The cube law is brutal: a
thousand times more source amplitude buys ten times the range. Working through plausible prey
sources, ordinary prey turns out to be a centimetre-scale cue; only a large struggling animal
or another crab reaches decimetres.

**Displacement is not pressure.** Particle displacement equals velocity divided by 2πf, so for
a given sound pressure a kilohertz signal carries far less displacement than a hundred-hertz
one. High-frequency sound is displacement-poor, and crabs detect displacement.

Those two together explain why the acoustic route keeps failing, and they are also why the
chemical route keeps winning: a plume falls off as 1/r and the olfactory threshold is low.

## What prey actually emit

Having built the receiver side, the obvious next question is what is available to receive.

The reference dataset for benthic invertebrate sound gives calibrated source levels for
scallops, limpets, urchins and crustaceans{% include cite.html key="coquereau2016" %}. Converting
each to particle displacement and solving for the crab's threshold, none of it reaches a crab
at more than millimetres — and every sound in that dataset peaks between 5 and 49 kHz, while
the analysis band was filtered from 2 kHz upward. **The corpus was built for hydrophone
monitoring, not for prey detection, and the crab's band was removed before analysis.** A null
there is unavailable, not absent.

The cue that does look promising is not a sound at all. Porewater pressure signals generated by
infaunal activity have been recorded directly in
sediment{% include cite.html key="wethey2005" %}, and the irrigation timing of three tellinid bivalves — including a Pacific Northwest clam that
is real green crab prey — has been measured in
detail{% include cite.html key="volkenborn2012" %}. That is a slow hydraulic signal, not an
acoustic one, and it is the only prey cue in this review with a field detection range measured
on relevant species.

## Chemistry, which out-ranges everything

Modelled as a plume, chemical detection spans roughly three orders of magnitude more distance
than any mechanical cue. The receptor side has two anatomically separate systems doing different jobs — olfaction on the
antennules, and contact chemoreception on the dactyls, where the gustatory organs of this species
have been characterised electrophysiologically{% include cite.html key="schmidt1989" %}. **I have
that paper at abstract only, so the threshold separation between the two — which is what the tool
actually runs on — is stated in the model as a sourced parameter and is not stated here.**

The tool refuses one thing here, deliberately. A chemical stimulus is not a scalar. You cannot
hand it a single "concentration" and get a receptor response, because mixtures cross-adapt and
receptors encode a ratio against background rather than an absolute. Single-compound
dose-response is enabled; mixtures raise an exception.

The female sex pheromone in this species has been the subject of an identification
study{% include cite.html key="hardege2011" %}, and later work using it produced the single
most interesting behavioural result in this review: males presented with a pheromone-treated
dummy female showed a mating response 87% of the time under ambient conditions and 40% under
ship-noise playback, a significant drop — while the *time taken to respond to the pheromone*
did not change significantly{% include cite.html key="rising2022" %}. Noise interfered with
completing the behaviour, not with detecting the signal. That dissociation is worth more than
either number alone.

## Electric and magnetic — where the tool says no

These are the two channels the tool refuses outright, and the refusals are the highest-confidence
outputs in it.

**Electric.** No electroreceptor has been identified in any crustacean, and none has been
sought in this species. That is not a modelling gap; it is the state of the field. The physics
side is unambiguous: prey bioelectric fields were measured at microvolt scale with the
electrode less than a millimetre from the tissue, and the authors state plainly that the
voltage from invertebrates was too weak to record away from the
source{% include cite.html key="bedore2013" %}. A behavioural sensitivity figure exists for a
freshwater crayfish{% include cite.html key="patullo2010" %} — a surrogate, from a different
order, in fresh water. The tool will quote named surrogates and will not produce a crab number.

**Magnetic.** There is a directly relevant result: juvenile green crabs were exposed to static
magnetic fields at strengths relevant to submarine power cables, and **females spent
substantially more time in the exposed zones while males showed no consistent
preference**{% include cite.html key="james2025" %}. That is a real, sex-specific response in
this species — and it is a static-field spatial preference, not a compass, and not a receptor.
Nobody has located the transducer.

**And there is a confound worth stating plainly, because it is the obvious one.** Helmholtz coils
dissipate heat, and crabs are thermotactic. Working the published coil geometry through a thermal
model gives, at the strongest field over the exposure period, roughly **20 W dissipated, a 0.58 K
gradient across the tank and a 0.30 K bulk rise** — small, but not obviously below what an animal
can detect, and I could not find a behavioural thermal-discrimination threshold for this species
to compare it against. So the model returns a number and refuses a verdict.

One thing does argue against the thermal explanation, weakly: ohmic heating scales with the square
of the current, so the confound is about ten times larger at the strongest field than at the
intermediate one — while the reported attraction was *strongest at the intermediate field*. The
confound and the effect run in opposite directions. **A thermocouple in the tank would settle it,
and that is the cheapest experiment anywhere in this review.**

The usual comparison is the spiny lobster, which is the standard invertebrate magnetoreception
system{% include cite.html key="lohmann1984" %}{% include cite.html key="boles2003" %}{% include cite.html key="ernst2016" %}.
**Here the abstract-only rule bites hardest:** I have read those three at abstract, so I will
not characterise their results. What I will say is a statement about the shape of the
literature rather than its contents — the receptor cells themselves have not been located and
characterised in that animal either. Mapping a mechanism from one order of crustaceans onto
another, across more than two hundred million years of divergence, when the source species'
anatomy is itself unresolved, produces a hypothesis wearing borrowed credibility. The tool
returns unavailable and says why.

## How the native crabs compare

Comparing green crab to the Pacific Northwest natives was the point at which the exercise
became most informative, because **the comparison cannot be run.**

Across eight receptor channels and five species, the green crab has measured values in five
channels and a described-but-unmeasured organ in two. For Dungeness crab, red rock crab,
graceful rock crab and yellow shore crab, I found **two** measured thresholds, both in Dungeness.
One establishes a behavioural detection threshold for a prey
extract{% include cite.html key="pearson1979" %}; the other, behavioural salinity detection
measured by antennular flicking{% include cite.html key="sugarman1983" %}. **I have both at
abstract only, so those are descriptions of what was measured, not of what was found** — the
model carries the values with the same tag. (A third record sits off this matrix entirely:
dactyl chemo- and mechanoreceptor recordings in the kelp crab, a species not among the five.)

**Two filled cells out of thirty-two, and the comparison still cannot be run** — but for a
different and much smaller reason than an empty literature. Those are *behavioural* thresholds,
in grams per litre and parts per thousand. Every green crab value is *single-unit
electrophysiology*, in micrometres or molar. They are not the same quantity, so putting them in
one row would be a category error rather than a comparison.

**That is the state of the literature, not a gap in the modelling.** Green crab is a classic
laboratory animal; the natives are commercially and ecologically important animals whose
sensory physiology has largely not been measured.

What *can* be compared is everything except the senses — and there the differences are
substantial and well documented{% include cite.html key="young2019" %}: salinity tolerance,
depth and zonation, body size, moult timing, and tolerance of emersion and hypoxia. Subadult
Dungeness use the littoral zone in ways that matter for any comparison drawn from trap
data{% include cite.html key="holsman2006" %}, red rock crab emersion physiology has been
measured in situ{% include cite.html key="defur1983" %}, settlement and emigration behaviour has
been studied in green crab{% include cite.html key="moksnes2003" %}, predatory capability has
been compared directly between green crab and red rock crab on a native
clam{% include cite.html key="nicol2025" %}, and the effect of a recovering apex predator on green
crab abundance has been examined{% include cite.html key="jeppesen2024" %}.

I have read the first of those at full text and the rest at abstract, which is why this
paragraph names questions rather than answers.

## The genetics, and what is actually there

I went looking for a genetic basis for the green crab's reproductive advantage — some
identified difference that would explain why it out-reproduces the natives. **There isn't
one, and the absence is informative.**

The adaptive-genomics literature for this species is real and substantial. What it is *about*
is temperature: cold tolerance, thermal adaptation, a chromosomal inversion, and the
relationship between genotype and thermal
plasticity{% include cite.html key="tepolt2020" %}{% include cite.html key="thia2021" %}{% include cite.html key="venkataraman2025" %}.
I have read these at abstract only and will not characterise their findings. But the
observation that the surveyed literature concerns thermal physiology and not reproduction or
sensory biology is an observation about the literature, and I can make it.

So the honest account of why green crab out-reproduce the natives is life-history and
tolerance, not a gene: a longer breeding season, earlier maturity at smaller size, two broods
a year where conditions allow, and sperm storage such that one fertilisation can serve more
than one clutch{% include cite.html key="young2019" %}. Note also that *reproducing* more is not
the same as *mating* more — with sperm storage, the two can move in opposite directions.

## What the tool is for

The most-used outputs are refusals: no electric readout, no magnetic readout, no mixture
readout, no cross-species comparison, no sex difference in transduction. Sex enters the model
in exactly one place — body size — because no measured threshold in this species differs by
sex, and the tool will not invent one.

That is a strange thing to build on purpose, and it is the part I would defend. The value is
not in the numbers it produces. It is that the numbers cannot drift: every constant is pinned
by a test that fails if the figure is misquoted, and in one working session those tests caught
four errors that had entered the model from secondary summaries of paywalled sources — which
is exactly how this literature is normally read.

**The most instructive failure, though, was mine and not the literature's.** The claim above —
that no native species had a single measured sensory channel — was a strong negative drawn from
a shallow search, and it was wrong; a deeper search turned up the two Dungeness thresholds
immediately. **A test had been pinning the wrong number in place**, with a comment beside it
admitting the value was known to be stale. That is worse than an unchecked number, because it
looks checked.

And correcting it nearly introduced a new error. The function answering *which channels are
comparable across species* tested only whether a cell was marked measured. Filling the two
Dungeness cells would have made two channels report as comparable when the underlying
quantities are not the same thing. It compares units now. **A test that counts statuses will
happily certify a category error**, and the correction is what exposed it.

**What would make it wrong:** if a measured audiogram for *Carcinus maenas*, Dungeness and red
rock crab on one rig showed the receptor bands to be substantially different from the surrogate
values used here, most of the mechanical conclusions would need redoing. That measurement does
not exist, and it is the single experiment that would change the most.

---

## Corrections

**2026-09-06.** Three changes, none of which erase anything above.

- The native-comparison section originally said I had found *"two measured chemosensory
  thresholds in a single species and nothing else."* The two are now **cited by
  key**{% include cite.html key="pearson1979" %}{% include cite.html key="sugarman1983" %}, one
  of them is a salinity threshold rather than a prey-odour one, and **"nothing else" was an
  overreach** — a third native record exists off the matrix. Both are held at abstract only, so
  the post names what they measured and not what they measured it to be. The count of filled
  cells is unchanged at two of thirty-two, and the comparison remains un-runnable.
- The **"What the tool is for"** section gains the account of how that error survived a test,
  and of the second defect that correcting it exposed.
- The correction has been applied to the model itself, not only to this post.
