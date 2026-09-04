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

First entry in a gear category. The format is deliberate: **specifications, then
what the physics of the delivery path allows, then a personal impression kept
separate from both.**

## Specifications

Checked 2026-08-27.

| | |
|---|---|
| Path | Bone conduction, open ear |
| Chip / Bluetooth | Qualcomm QCC3044, Bluetooth 5.2, multipoint |
| Codec | aptX Adaptive |
| Stated frequency range | 20 Hz – 20 kHz |
| Microphones | Dual, with cVc echo cancelling and noise suppression |
| Battery | 140 mAh, 10 h playtime; 5 min charge ≈ 90 min use; full charge ≈ 1 h |
| Weight | 30.6 g |
| Materials | Titanium alloy and silicone |
| Ingress | IP55 |
| Price | $149 USD at launch; $79 on the Suunto US store when checked |

One correction worth making, because it is easy to repeat. **"Dual" refers to the
microphones, not the transducers.** Every listing I checked says "Built-in Dual
Mics". Two bone transducers, one per side, is the standard arrangement for any
stereo bone-conduction headset and is not a distinguishing feature.

## The property that decides everything else

A sealed transducer at one ear gives roughly 40–60 dB of **interaural
attenuation** — the signal arriving at the far ear is far quieter than at the
near one, which is what makes two ears independent. A transducer on the skull
gives close to none. The skull couples both cochleae, so a bone-conducted signal
arrives at both at once.

This is not a shortcoming of this product. It is what bone conduction is.

It has a hard consequence for the work I do. My rulebase returns a laterality of
`undefined` — not "left", not "bilateral-ish" — for any delivery path with under
15 dB of interaural attenuation. A path that cannot deliver a left-ear stimulus
must not have downstream predictions made as though it did.

So, for this device:

| protocol | usable |
|---|---|
| Isochronic tones, AM envelopes, any shared signal | **yes** |
| Binaural beats | **no** |
| Interaural time differences, dichotic drive | **no** |
| Anything reporting a per-ear result | **no** |

Two further limits, neither disqualifying. The 20 Hz – 20 kHz figure is an
air-conduction-style specification and I have not verified it as *delivered*
through bone on a head — for evoked-potential work the delivered envelope is what
matters, and it is unmeasured. And the nearest measured air-versus-bone
separation I have is 22 dB, from tuning-fork work on a different transducer for a
different purpose.

## First impression

Mine, one person, one session, unblinded. Not evidence, and the tier on this post
reflects that.

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

That last point is the one I would actually defend, and it is about compliance
rather than acoustics: **a protocol that can run while you are present with your
family is a protocol that gets run.** Nothing here measures whether the delivered
signal is adequate for the purpose — only that the barrier to wearing it is much
lower.
