---
title: "Gear: Suunto Sonic bone conduction headphones"
description: >-
  Specs, a first impression, and the one property that decides which protocols
  can run on them at all.
date: 2026-08-27 09:00:00 -0600
project: audio-evoked-potentials
category: gear-review
status: published
tier: C
claims:
  - AEP-0005
citations:
image: /assets/posts/suunto-sonic.jpg
image_alt: >-
  The Suunto Sonic, a bone-conduction headset: a wraparound neckband with two
  transducer pads that sit on the cheekbones rather than over the ear canals.
image_credit: >-
  Manufacturer product image, Suunto. Reproduced to illustrate a review of the
  product. Desaturated for this site.
---

Gear entry. Specifications, then what the delivery path allows, then an impression kept
separate from both.

## Specifications

Checked 2026-08-27.

| | |
|---|---|
| Path | Bone conduction, open ear |
| Chip / Bluetooth | Qualcomm QCC3044, Bluetooth 5.2, multipoint |
| Codec | aptX Adaptive |
| Stated frequency range | 20 Hz – 20 kHz |
| Microphones | Dual, cVc echo cancelling and noise suppression |
| Battery | 140 mAh, 10 h; 5 min charge ≈ 90 min use; full ≈ 1 h |
| Weight | 30.6 g |
| Materials | Titanium alloy, silicone |
| Ingress | IP55 |
| Price | $149 USD at launch; $79 on the Suunto US store when checked |

**"Dual" is the microphones, not the transducers.** Every listing checked says "Built-in
Dual Mics." Two bone transducers, one per side, is standard for any stereo bone-conduction
headset and not a distinguishing feature.

## The property that decides the rest

A sealed transducer at one ear gives roughly 40–60 dB of interaural attenuation. That
separation is what makes two ears independent.

A transducer on the skull gives close to none. The skull couples both cochleae, so the
signal arrives at both at once.

{% include fig-bone-vs-air.html %}

This is what bone conduction is, not a fault in the product.

Consequence for protocol selection: the rulebase returns laterality `undefined` — not
"left", not "bilateral-ish" — for any path under 15 dB of interaural attenuation. A path
that cannot deliver a left-ear stimulus gets no downstream per-ear predictions.

| protocol | usable |
|---|---|
| Isochronic tones, AM envelopes, any shared signal | **yes** |
| Binaural beats | **no** |
| Interaural time differences, dichotic drive | **no** |
| Anything reporting a per-ear result | **no** |

Two further limits, neither disqualifying:

- 20 Hz – 20 kHz is an air-conduction-style specification. Not verified as *delivered*
  through bone on a head. For evoked-potential work the delivered envelope is what matters,
  and it is unmeasured.
- Nearest measured air-versus-bone separation on hand is 22 dB, from tuning-fork work on a
  different transducer for a different purpose.

## First impression

One person, one session, unblinded. Not evidence; the tier reflects that.

> The headphones were extremely easy to get set up, and this is the first time
> that I've used bone conduction headphones, so it truly blew my mind experiencing
> them. I couldn't believe how high resolution they were, even though it's not
> even sound directly through the ears. Still trying to wrap my head around it.
> But regardless, this is a great buy.
>
> Also, just as a side note, it's a really great way to have audio-evoked
> potentials or something like Brain.fm running during family time so that my ears
> aren't covered, and I'm more aware and more present, but can still be running a
> therapeutic music solution.

The defensible part of that is about compliance, not acoustics: a protocol that runs while
you are present with your family is a protocol that gets run. Nothing here measures whether
the delivered signal is adequate — only that the barrier to wearing it is lower.
