---
title: "Twelve ways to catch a green crab"
description: >-
  A screening exercise across sensory, biological and operational mechanisms for
  controlling an invasive crab — what each route would need to be true, what
  closed it, and the two that are still standing.
date: 2026-09-09 09:00:00 -0600
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
  - james2025
  - bedore2013
  - patullo2010
  - lohmann1984
  - boles2003
  - ernst2016
  - burke1954
  - garm2005
  - tautz1980
  - aimon2021
  - popper2001
  - jzquel2021
  - jury2024
  - coquereau2016
  - wethey2005
  - volkenborn2012
  - schmidt1989
  - hardege2011
  - rising2022
  - pearson1979
  - sugarman1983
  - young2019
  - holsman2006
  - defur1983
  - moksnes2003
  - moksnes2004
  - nicol2025
  - mcdonald2001
  - goddard2005
  - jeppesen2024
  - grosholz2021
  - turner2015
  - ens2022
  - grason2018
  - bergshoeff2018
  - bergshoeff2019
  - derivera2006
  - compton2010
  - rey2017
  - du2024
  - tepolt2020
  - thia2021
  - venkataraman2025
  - kasiouras2024
  - magee2013
summary: >-
  Twelve candidate mechanisms for preferentially removing an invasive crab,
  screened one at a time against the physics and the literature. Ten are closed,
  one is unreachable with available equipment, and two survive — neither of them
  a device. This is the ledger, including the errors made along the way.
---

This is a case study of a search that mostly returned no.

The subject is the European green crab (*Carcinus maenas*), an invasive
portunid established on the coast of British Columbia. The question I set out
with was narrow and, I thought, tractable: **is there any signal a green crab
can detect that a native crab cannot** — because if there is, you can build it
into a trap and catch one species without catching the other.

Twelve routes were screened. **Ten are closed. One is real but unreachable with
equipment I can obtain. Two survive, and neither of them is a device.**

None of this is novel. Every closure came from applying published work or
undergraduate physics to a specific question, and in one case the thing I
declared missing from the literature turned out to have been published, with
public code, four months earlier. **The value here, if there is any, is the
shape of the negative results and the order they arrived in** — so I am writing
it down in public rather than leaving it in a private repository. If any of it
saves somebody a month, take it.

## The constraint that governs everything

**A green crab trap that also catches Dungeness crab is worse than no trap.**
Dungeness supports British Columbia's most valuable crab fishery, and juvenile
Dungeness share estuarine nursery habitat with juvenile green crab. So
"attracts green crab" was never sufficient. The requirement was always
**differential** — something the target detects and the bycatch does not.

That single constraint is what killed most of the twelve.

## The ledger

| # | Route | Verdict | What closed it |
|---|---|---|---|
| 1 | **Electric prey mimicry** — a lure imitating prey bioelectric fields | **CLOSED** | Prey fields are a contact cue even for a shark; no crustacean electroreceptor has been identified |
| 2 | **Magnetic** — exploit a reported sex-specific field response | **OPEN, unreachable** | Real result, unreplicated, no located transducer, and an unresolved thermal confound |
| 3 | **Substrate vibration** from buried prey | **CLOSED** | Every catalogued prey sound sits outside the crab's measured mechanoreceptor band |
| 4 | **Water-borne prey sound** | **CLOSED** | Near-field falloff and displacement arithmetic put it at centimetres |
| 5 | **Acoustic reproductive interference** — mask mating signals | **CLOSED** | The water is too shallow to propagate the relevant frequencies at all |
| 6 | **Chemical prey odour** | **WORKS, NOT SELECTIVE** | Out-ranges every mechanical cue by orders of magnitude, and every crab there smells it |
| 7 | **Sex pheromone lure** | **WORKS, NOT SELECTIVE ENOUGH** | Attracts males of the target — and the bycatch problem is unaddressed |
| 8 | **Predator cue** — flush crabs out of refuge into gear | **CLOSED** | Requires a cue that moves the target and not the natives; same failure as 6 |
| 9 | **Parasite biocontrol** | **CLOSED, decisively** | Host-specificity testing against native Pacific crabs is the standing answer |
| 10 | **Native predator recovery** | **OPEN, not a lever** | One landscape-scale success exists; its agent is absent from the relevant water |
| 11 | **Gear** — trap type and entrance geometry | **SURVIVES** | Largest demonstrated effect anywhere in this exercise |
| 12 | **Place and schedule** — where and when the gear is set | **SURVIVES** | Two independent axes with real supporting evidence |

**Five independent lines of work converged on the bottom two rows.** That
convergence is the single most useful thing the exercise produced, and it took
about eight closures to get there.

---

## Where it started: the electromagnetic branch

The project began with a specific published result: juvenile green crabs
exposed to static magnetic fields at strengths relevant to submarine power
cables showed a **sex-specific** response, with females spending more time in
exposed zones and males showing no consistent
preference{% include cite.html key="james2025" %}.

That is exactly the shape of thing the constraint above demands — a
differential response, in the target species, in a channel you can generate
with a coil. It is why this project exists at all.

**Three things had to be true for it to become a trap, and I could establish
none of them.**

**First, a mechanism.** No transducer has been located. The obvious comparison
is the spiny lobster, the standard invertebrate magnetoreception
system{% include cite.html key="lohmann1984" %}{% include cite.html key="boles2003" %}{% include cite.html key="ernst2016" %}
— but the receptor cells have not been located and characterised in that animal
either. Mapping a mechanism from one order of crustaceans onto another, across
more than two hundred million years of divergence, when the source species'
anatomy is itself unresolved, produces a hypothesis wearing borrowed
credibility.

**Second, the field map has to reproduce.** It does not. No coil geometry I
could construct, at any separation or tank bearing, reproduces the published
zone table — best fit was 61% RMS error. That is a correspondence-with-the-authors
problem, not a finding, and it is recorded as one.

**Third, the confound.** Helmholtz coils dissipate heat and crabs are
thermotactic. Working the published geometry through a thermal model gives,
at the strongest field, roughly **20 W dissipated, a 0.58 K gradient across the
tank and a 0.30 K bulk rise** — small, but not obviously below what an animal
can detect, and I could not find a behavioural thermal-discrimination threshold
for this species to compare it against.

**One thing argues against the thermal explanation, and it is worth stating
because it cuts my way and I nearly missed it.** Ohmic heating scales with the
square of the current, so the confound is about ten times larger at the
strongest field than at the intermediate one — while the reported attraction
was *strongest at the intermediate field*. **The confound and the effect run in
opposite directions.** A thermocouple in the tank would settle it, and it is the
cheapest experiment anywhere in this review.

**Verdict: open, and unreachable here.** The claim is untouched. What closes it
is a replication with a sham coil and a temperature log, which needs a facility
and animals I do not have.

### And the electric branch is closed, which is a different answer

The original premise was electric, not magnetic — a lure imitating the
bioelectric field of buried prey. It is closed on two independent grounds.

**The physics.** Prey bioelectric fields were measured at **microvolt scale
with the electrode less than a millimetre from the tissue**, and the authors
state plainly that the voltage from invertebrates **was too weak to record away
from the source**{% include cite.html key="bedore2013" %}. Run through a
shark's own measured sensitivity, a natural prey field is readable at a few
centimetres. A crab is not a shark.

**The biology.** No electroreceptor has been identified in any crustacean, and
none has been sought in green crab. A behavioural sensitivity figure exists for
a freshwater crayfish{% include cite.html key="patullo2010" %} — a surrogate,
from a different order, in fresh water.

**That is not a modelling gap. It is the state of the field**, and the honest
output was to say so rather than to model around it.

**And the welfare evidence points the same way.** Green crabs have nociceptors in
every soft tissue tested{% include cite.html key="kasiouras2024" %}, and they
**learn to avoid a place where they receive electric shock** — some dropping a
wired leg even though the voltage was set below the single-shock level that
causes it{% include cite.html key="magee2013" %}. That was contact current, not a
field in water, so it sets no threshold. But it means an electric lure for this
animal should be expected to repel as well as attract.

---

## Prey signalling: vibration and sound

If the crab cannot be lured electrically, the next question is what its prey
actually broadcasts, and whether a trap can imitate it.

**The receiver side is better documented than I expected.** There is a real
transfer function for the mouthpart setae — displacement thresholds, and the
coding: spike count scales with displacement amplitude, interspike interval
with velocity{% include cite.html key="garm2005" %}. **That paper is also
where I made my first substantive error** (below): those setae are *tactile*
receptors for handling prey, not distance detectors, and I spent a while
scoring far-field stimuli against them.

The organ that matters for substrate vibration is a joint organ in the walking
leg, described in green crab itself{% include cite.html key="burke1954" %},
with a measured band. Water motion is a different receptor
again{% include cite.html key="tautz1980" %}; the behavioural response of
intact animals to substrate vibration has been tested
directly{% include cite.html key="aimon2021" %}; decapod acoustic detection has
been reviewed as a field{% include cite.html key="popper2001" %}; an
evoked-potential study in the American lobster asks which organ is
responsible{% include cite.html key="jzquel2021" %}; and a consolidated review
of green crab sensory biology exists{% include cite.html key="jury2024" %}.

**The transmitter side is where it died.** The reference dataset for benthic
invertebrate sound gives calibrated source levels for scallops, limpets,
urchins and crustaceans{% include cite.html key="coquereau2016" %}. Converting
each to particle displacement and solving for the crab's threshold, **not one
of the nine sources reaches a crab at more than millimetres** — and every sound
in that dataset peaks between 5 and 49 kHz, while the analysis band was
filtered from 2 kHz upward.

**The corpus was built for hydrophone monitoring, not for prey detection, and
the crab's band was removed before analysis.** A null there is *unavailable*,
not absent, and the distinction is the whole point of recording it.

Two pieces of arithmetic govern all of this and are worth stating plainly,
because they close route 4 without any biology at all:

- **Near-field falloff.** A small oscillating body in water produces a field
  falling off as 1/r³ if it oscillates back and forth. The cube law is brutal:
  a thousand times more source amplitude buys ten times the range.
- **Displacement is not pressure.** Particle displacement equals velocity
  divided by 2πf, so for a given sound pressure a kilohertz signal carries far
  less displacement than a hundred-hertz one. **High-frequency sound is
  displacement-poor, and crabs detect displacement.**

**The one prey cue that survives is not a sound at all.** Porewater pressure
signals generated by infaunal activity have been recorded directly in
sediment{% include cite.html key="wethey2005" %}, and the irrigation timing of
three tellinid bivalves — including a Pacific Northwest clam that is real green
crab prey — has been measured in detail{% include cite.html key="volkenborn2012" %}.
That is a slow hydraulic signal, and it is the only prey cue in this review with
a field detection range measured on relevant species.

---

## Mating: pheromone, and interference

**Chemistry out-ranges every mechanical cue by two to three orders of
magnitude.** Modelled as a plume, prey odour reaches hundreds of metres where
the best mechanical cue reaches a couple. The receptor side has two
anatomically separate systems doing different jobs — olfaction on the
antennules, and contact chemoreception on the dactyls, where the gustatory
organs of this species have been characterised
electrophysiologically{% include cite.html key="schmidt1989" %}.

The female sex pheromone has been the subject of an identification
study{% include cite.html key="hardege2011" %}, and later work using it
produced the single most interesting behavioural result in this review: males
presented with a pheromone-treated dummy female showed a mating response 87% of
the time under ambient conditions and 40% under ship-noise playback, a
significant drop — **while the time taken to respond to the pheromone did not
change significantly**{% include cite.html key="rising2022" %}. Noise
interfered with completing the behaviour, not with detecting the signal. That
dissociation is worth more than either number alone.

**So chemistry works, and that is the problem.** It is the best-performing
channel in the whole review and it is the *least* selective one: a bait plume
is smelled by every crab in the basin. A pheromone lure is better — it targets
males of one species — but males are demographically close to irrelevant, and it
does nothing about Dungeness bycatch.

**Route 5, acoustic reproductive interference, closes on physics rather than on
biology, and cleanly.** Shallow water is a waveguide with a cutoff frequency
below which no mode propagates at all. At the 0.5–5 m depths where these
animals actually mate, the cutoff is **159–1594 Hz** — above the signal band
you would need to mask. **You cannot interfere with a signal in water that will
not carry your interference.**

---

## The selectivity problem, stated properly

By this point the pattern was clear enough to test directly, so I built a
screening tool: for a given stimulus, how much arrives at a receptor, in what
format, at what range — and a refusal when the number underneath does not
exist. [That has its own write-up](/blog/green-crab-sensory-screening-tool/).

**Its most useful output was a comparison that cannot be run.**

Across eight receptor channels and five species, green crab has measured values
in five channels and a described-but-unmeasured organ in two. For Dungeness
crab, red rock crab, graceful rock crab and yellow shore crab, I found **two**
measured thresholds, both in Dungeness and both behavioural — a detection
threshold for a prey extract{% include cite.html key="pearson1979" %} and
salinity detection measured by antennular
flicking{% include cite.html key="sugarman1983" %}. Both are held at abstract
only, so those are descriptions of what was measured, not of what was found.

**Two filled cells out of thirty-two.** And they do not make the comparison
runnable, because they are behavioural thresholds in grams per litre while
every green crab value is single-unit electrophysiology in micrometres. Putting
them in one row would be a category error, not a comparison.

**That is the state of the literature, not a gap in the modelling.** Green crab
is a classic laboratory animal; the natives are commercially and ecologically
important animals whose sensory physiology has largely not been measured.

**And where the bands *are* known, they overlap.** Every crab whose
mechanoreception has been measured peaks around 100 Hz. There is no frequency
at which you can shout at a green crab and not be heard by a Dungeness.

What *can* be compared is everything except the senses, and there the
differences are substantial and well
documented{% include cite.html key="young2019" %}: salinity tolerance, depth
and zonation, body size, moult timing, tolerance of emersion and hypoxia.
Subadult Dungeness use the littoral zone in ways that matter for any comparison
drawn from trap data{% include cite.html key="holsman2006" %}, red rock crab
emersion physiology has been measured in
situ{% include cite.html key="defur1983" %}, settlement and emigration
behaviour has been studied in green crab{% include cite.html key="moksnes2003" %},
and predatory capability has been compared directly between green crab and red
rock crab on a native clam{% include cite.html key="nicol2025" %}.

**That list is the beginning of routes 11 and 12.** Selectivity does not have to
come from the signal. It can come from the calendar.

---

## Predators and parasites

**The complete answer to "why not biological control" is one paper.** The
host specificity of *Sacculina carcini*, the parasitic barnacle proposed as a
green crab agent, has been tested against native Pacific
crabs{% include cite.html key="goddard2005" %}, and the result is why nobody
deploys it. I am not going to characterise the numbers here — I hold it at
abstract level — but the conclusion is not controversial and it is the standing
reason route 9 is closed.

**Route 10 has the only landscape-scale evidence in this entire review**, and it
is not usable. A recovering sea otter population shows a strong negative
space-and-time relationship with green crab, with crabs persisting highest where
tidal restriction excluded the otters{% include cite.html key="jeppesen2024" %}.
That is the best result anywhere in the predator literature — and **the southern
sea otter has been absent from the Salish Sea since 1915.** It is an argument
for removing tidal barriers, not a lever anyone can pull.

So I built a register of everything else that might eat a green crab in British
Columbia: **24 agents, each carrying a status so the empty rows stay visible.**
The tally is the finding — **1 demonstrated, 1 failed, 3 with a measured diet
record, 4 plausible-untested, and 15 with no data at all.** Five of the top six
candidates are present in the Salish Sea. **None of the five has demonstrated
evidence there.**

Four survive three filters at once — present where the crabs are, capable of
taking one, and attached to a step someone could take this year: **giant Pacific
octopus, marine-foraging river otter, Pacific staghorn sculpin, and the
sunflower sea star.**

Building out their biology reordered them, and the reordering is the point.
Ranked on **being present and cheaply samplable**, the river otter comes first.
Ranked on **how strong the dietary prior actually is**, the octopus does. Those
are different questions and collapsing them into one ranking is how a project
talks itself into the wrong survey. The sunflower sea star has the **strongest
structural case on the list** — a recovering predator with funded recovery
programmes already running for their own reasons — and the **weakest dietary
case**, because its entire measured feeding ecology is urchins and molluscs.
Both statements are true at once.

**What I can state, because these are my own search results rather than
somebody's findings:** no green-crab record exists in the diet literature for
*any* octopus species; there is no green-crab diet fraction for river otter
anywhere; there is nothing published on Pacific Northwest fish predation on
green crab; and I located **no crustacean predation record at all** for the
sunflower sea star. The diet numbers behind the ranking sit in the working notes
at abstract level, where they belong.

**And none of the four is measured on the size class that matters.** Which
brings up the thing that kept recurring.

---

## The two that survive

**Route 11 — gear.** Trap entrance modification has the largest demonstrated
effect of anything in this exercise{% include cite.html key="bergshoeff2018" %}{% include cite.html key="bergshoeff2019" %}.
It is a cable tie and a sinker. Nothing the sensory workstream produced comes
close.

There is also a peer-reviewed integrated population model for this species with
public code{% include cite.html key="keller2025" %}, fitted on a multi-year
removal time series — **which I confidently declared did not exist**, and which
puts shrimp traps well above the trap type used throughout British Columbia on
per-trap efficiency. That figure is not settled and I would not quote a
multiplier: reading the paper's own robustness appendix moves it by about a
third, and the model's observation process never tested whether catchability
varies through the season. **The defensible statement is that a paired
deployment — the two trap types fished side by side, same days, same sites,
same soak — would settle it cheaply with existing gear.**

**Route 12 — place and schedule.** Selectivity from the calendar rather than
from a device. Two axes came out strong: **trap the structured habitat rather
than the open flat**, and **fish the daytime flood tide**, because green crab
move up-shore on the flood regardless of light while the Dungeness incursion is
nocturnal. Others came out weaker, and the axis most often cited — tidal height
alone — was **downgraded** by a paper showing subadult Dungeness use the
littoral zone too{% include cite.html key="holsman2006" %}.

It costs nothing, because every axis is a decision about where and when to set
gear already in the water. It is falsifiable now, at a few hundred trap-sets,
with the kill condition written in advance.

**And here is the case against it, stated as strongly as I can.** It is bycatch
reduction, not control. The demographic work says only heavy size-selected
removal of *juveniles* drives the population down; composition does not. **And
the gear cannot execute that lever.** The smallest crab in one dataset of 17,615
animals was 21.1 mm across the carapace. Settling juveniles are 1.5 mm. **The
decisive size class and the available gear are mismatched, and no amount of
siting fixes it.**

That mismatch is also true of every predator in the register. **The size class
that decides the outcome is unmeasured for gear and for predators alike.** If
one sentence from this whole exercise is worth carrying forward, it is that one.

---

## Things that kept being true

- **Physics beats biology at range, every time.** Six of the twelve closures
  came from arithmetic done before any literature search — near-field falloff,
  waveguide cutoff, displacement-versus-pressure, ohmic heating. **Doing the
  arithmetic first would have saved weeks**, and the one branch where I built
  the apparatus before computing the gate is the branch that wasted the most
  time.
- **A cue that works is usually a cue everyone can hear.** Selectivity and
  efficacy pulled against each other in every sensory route. The channel with
  the best range was the least selective; the most selective idea was the one
  that would not propagate.
- **Absence of a measurement is not absence of the thing.** Repeatedly the
  honest output was *unavailable* rather than *absent* — a prey-sound corpus
  filtered before the relevant band, native species never tested, a receptor
  never sought. Collapsing those into a null manufactures a confident negative
  out of a test nobody ran.
- **The literature on the invader is far better than the literature on the
  natives.** Green crab is a laboratory animal. The commercially important
  Pacific crabs it competes with are not, and every cross-species comparison in
  this review foundered on that asymmetry rather than on modelling.
- **Removal suppresses locally and does not
  extirpate**{% include cite.html key="ens2022" %}. That is the consistent
  finding across jurisdictions, including a documented case of
  **stage-specific overcompensation — the hydra effect — following adult-only
  removal**{% include cite.html key="grosholz2021" %}, whose possibility had been
  assessed in advance{% include cite.html key="turner2015" %}.
  Early detection has a much better record{% include cite.html key="grason2018" %}.
- **The temperature literature is where the actual predictive signal is.**
  Adult thermal tolerance does not discriminate sites — it is broad enough to
  make the whole coast suitable{% include cite.html key="compton2010" %}. The
  discriminator is larval recruitment
  temperature{% include cite.html key="derivera2006" %}, with warmer winters
  adding a second brood{% include cite.html key="rey2017" %} and a modelling
  result finding a large increase in larval arrival for a small temperature
  rise{% include cite.html key="du2024" %}. The adaptive-genomics literature for
  this species is likewise about
  temperature{% include cite.html key="tepolt2020" %}{% include cite.html key="thia2021" %}{% include cite.html key="venkataraman2025" %},
  not about reproduction or sensory biology — an observation about what the
  literature is *about*, which is a claim I can make from titles and abstracts.

---

## The method, and the errors it caught

The part of this I would actually defend is not any of the twelve verdicts. It
is that **every constant is pinned by a test that fails if the figure is
misquoted**, every number carries a tag saying whether it was measured, derived,
assumed or unavailable, and **a source read only at abstract may be cited as
existing but may not have findings attributed to it.**

That last rule is unpopular with my own drafts. It caught five violations in the
first version of the companion post, and it is why several paragraphs above name
what a study measured rather than what it found.

**Here is what those rules caught. I think this table is the most useful thing
on the page.**

| The error | How it was caught | What it cost |
|---|---|---|
| A turbulent-diffusion constant **10× wrong** | Checked against a field measurement | Chemical detection range was off by an order of magnitude in the *conservative* direction |
| Scored far-field stimuli against a **tactile** receptor | Reading the paper properly | Invalidated a whole class of range estimates |
| Attributed a vibration organ to the **wrong joint**, then used a surrogate band from the wrong genus | Re-reading the 1954 source | Reversed a result: "1 of 9 prey sounds rescued" became **0 of 9** |
| Conflated a trap's **entry success** with its **catch increase** | A test asserting the two figures | The best modification is +81%, not the number I had |
| Collapsed a lab mechanism into a **population-level** claim | The operator asked what a phrase meant | Split into two claims; pinned that no population-level effect has been demonstrated{% include cite.html key="mcdonald2001" %} |
| "**Zero** native sensory channels have ever been measured" | Searching again, less shallowly | A strong negative from a shallow search. Overturned within minutes |
| "**No population model exists** for this species" | Searching by *author* instead of by topic | It existed, with public code. The repos are named after the method, not the species |
| Read a gear ratio **off a log axis by eye** | Reading the printed posterior table | Both comparison gears understated, **always in the direction that flattered my preferred answer** |

**Two patterns in that table are worth more than the individual entries.**

The first: **most of these errors ran in the direction that made the result
look better.** Not one of them was random. That is what a bias looks like from
the inside, and it is the argument for tests that pin numbers rather than
vigilance.

The second: **a test can hold a wrong number in place.** The "zero native
channels" claim survived two days after I knew it was wrong, because a test was
asserting it, with a comment beside it saying the value was known to be stale.
That is worse than an unchecked number — it looks checked. And when I finally
corrected it, the fix nearly introduced a new error: the function answering
*which channels are comparable across species* tested only whether a cell was
marked "measured", so filling the two Dungeness cells would have certified a
category error as a comparison. **A check that counts statuses will happily
certify nonsense.**

---

## What would change the picture

- **A thermocouple in a Helmholtz coil tank**, during a replication with a sham
  coil. Settles route 2 either way, and it is the cheapest decisive experiment
  in the review.
- **A measured audiogram for green crab, Dungeness and red rock crab on one
  rig.** It does not exist. It is the single measurement that would change the
  most, and if the bands turned out to differ substantially, most of the
  mechanical conclusions above would need redoing.
- **A paired deployment of two trap types**, same days and sites. Settles the
  gear question with equipment already in the water.
- **Any diet study at all** on the four shortlisted predators — two of which
  need no collection permit, because middens and scat are lying on the ground.
- **Gear that reaches sub-20 mm crabs.** Nothing in this review addresses the
  size class that the demography says decides the outcome. That is the open
  problem, and I do not have an answer to it.

If any of this is useful to somebody working on a real protocol, it is yours —
that is why it is here rather than in a private folder. The working notes,
including the numbers I have held back above because I have only read their
abstracts, are more detailed than this post and I am happy to share them.
