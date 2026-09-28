---
title: "Redesigning the homepage, one version at a time"
description: >-
  Six versions of the polarize.tech homepage, from a post list in a sidebar to a
  lab's front door drawn over a field of polarising cells: what each one tried,
  what was kept, and how the result became components in the design system.
date: 2026-09-28 10:00:00 -0600
project: method
status: published
tier: A
claims:
citations:
schematic: none
# About the site, not the research: kept out of the homepage's Findings.
findings: false
summary: >-
  The homepage went through six versions in a day, each one kept. The first tried a
  familiar product-site layout, the fourth threw out every rule, and the one that
  shipped took pieces from all of them. What survived became polarize-ui's landing
  layer, so every page on the site now uses it.
image: /assets/posts/homepage-redesign.jpg
image_alt: >-
  The redesigned polarize.tech homepage: the heading "Reading and writing the body
  electric" centred over a faint field of specks, with "Our process" and "Get in
  touch" buttons beneath.
image_credit: Screenshot of polarize.tech. Desaturated for this site.
---

Until this week the homepage was a list. It showed the four latest posts, the speculations and
the most recently active repositories, inside the same sidebar layout as every other page. It
was accurate, and it said nothing about what this lab is for.

<figure class="shot shot--wide">
  <a href="{{ '/assets/posts/homepage-redesign/00-before.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/00-before.jpg' | relative_url }}" alt="The old homepage: a sidebar with the brand, a menu and counts, beside a list of the latest posts with thumbnails." loading="lazy" /></a>
  <figcaption>Before: the homepage as a post list inside the blog's sidebar layout.</figcaption>
</figure>

The redesign was done in the open, in conversation with Claude on a design canvas where every
version stayed side by side. Then it was built with Claude Code. Six versions, oldest first:

<figure class="shot shot--strip">
  <div class="shot__scroll"><a href="{{ '/assets/posts/homepage-redesign/07-filmstrip.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/07-filmstrip.jpg' | relative_url }}" alt="The top of every homepage version side by side: the old post list, the light version, the dark version, the brutalist version, the no-rules version and the final hybrid." loading="lazy" /></a></div>
  <figcaption>The top of each version, oldest first: before, light, dark, brutalist, no rules, and the one that shipped. Scroll sideways on a phone.</figcaption>
</figure>

## 1. A familiar front door

The first brief was a proper homepage for a research lab, borrowing the feel of product sites
like [DigitalOcean](https://www.digitalocean.com) and [Intercom](https://www.intercom.com):
a big headline, a product shot, and sections for what the lab does. It was built strictly on
[polarize-ui](https://github.com/polarizetech/polarize-ui), the design system these pages
already used: the display serif for headings, the mono face for labels, and never bold.

The product shot was a mock recording workbench, with three channels and a time–frequency map.
It carried a TASTE badge saying it was an illustration and not a recording. Even as decoration,
the page kept the rule every page here follows: a label may never be hidden.

<figure class="shot shot--wide">
  <a href="{{ '/assets/posts/homepage-redesign/01-light.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/01-light.jpg' | relative_url }}" alt="Version one: a light page, the heading on the left, a card of waveforms and a heatmap on the right, a claim card overlapping it." loading="lazy" /></a>
  <figcaption>Version one: light, conventional, and entirely inside the design system's rules.</figcaption>
</figure>

## 2. Dark

The same page in the design system's dark palette. It was an easy change, because every colour
is a token. It was also the first sign that the lab reads better at night.

<figure class="shot shot--wide">
  <a href="{{ '/assets/posts/homepage-redesign/02-dark.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/02-dark.jpg' | relative_url }}" alt="Version two: the same layout in a dark palette with a teal accent." loading="lazy" /></a>
  <figcaption>Version two: the same page, dark.</figcaption>
</figure>

## 3. Brutalism, and specks

Next came a push towards brutalism, after the sound-therapy site [Byotōne](https://byotone.com):
fields of animated specks, bracketed mono tags, a huge headline, and a lettered step-through
navigation. The specks took several forms: a ring around the headline, a slowly turning cell, a
helix, and an evoked-response wave. The page labelled them decoration, not data.

One thing from the reference was deliberately not copied: its all-caps serif. Here uppercase is
always the mono face, so the big headings stayed in regular case.

<figure class="shot shot--wide">
  <a href="{{ '/assets/posts/homepage-redesign/03-brutalist.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/03-brutalist.jpg' | relative_url }}" alt="Version three: a dark page with a ring of specks around a spread-out serif headline, bracketed frequency-band tags and a lettered step navigation." loading="lazy" /></a>
  <figcaption>Version three: specks, bracketed tags, and a stepper that did not survive.</figcaption>
</figure>

## 4. No rules

To see what the rules were costing, one version dropped all of them: a condensed grotesque, acid
green, 1px grid lines everywhere, and a simulated network of about five thousand cells behind the
whole page. Those cells fire on their own, set off their neighbours, and sometimes fire together
as waves, synchronised colonies or rhythmic bursts. A live counter in the top bar says how many
are firing, and the footer says it is a simulation.

It was the loudest version and the least like the lab, but the cells stayed.

<figure class="shot shot--wide">
  <a href="{{ '/assets/posts/homepage-redesign/04-no-rules.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/04-no-rules.jpg' | relative_url }}" alt="Version four: an enormous condensed uppercase headline in white and acid green, a grid of mono labels, and clusters of green squares firing in the background." loading="lazy" /></a>
  <figcaption>Version four: no rules. The top bar counts how many simulated cells are firing.</figcaption>
</figure>

## 5. The one that shipped

The final version took something from each of the others. It has the dark palette and the design
system's type. From brutalism it took hard rules and square-ish corners, and from the first
version it took the charts. The cells moved into a single WebGL field behind the entire page, one
that looks like cells polarising rather than confetti. They are small, white, dim, sometimes
grouped, occasionally firing together. The stepper and the bracketed tags went, and so did the
background fills on cards.

The content changed more than the look. Looking at how other labs present themselves helped,
especially [Michael Levin's lab site](https://drmichaellevin.org) and his separate essay site,
[Thoughtforms](https://thoughtforms.life). They pointed to an order: lead with the work, let the
articles report what it found, and give speculation its own quieter room. So the homepage now opens
with the process that keeps results honest. Then come the projects, the changelog, the findings,
the speculations and the design system.

<figure class="shot shot--wide">
  <a href="{{ '/assets/posts/homepage-redesign/05-hybrid.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/05-hybrid.jpg' | relative_url }}" alt="Version five on the canvas: the centred serif headline over a field of faint white specks." loading="lazy" /></a>
  <figcaption>The shipped design, as it stood on the canvas.</figcaption>
</figure>

## 6. From canvas to components

A design that lives only on a canvas has to be rebuilt by hand for every page, and it drifts. So
it went into polarize-ui as components, in both of its forms: a zero-build stylesheet and custom
element for plain HTML sites like this one, and React components that render the same classes.

The new landing layer covers the top bar, hero, section heads, process steps, project features,
repository cards, the changelog feed, article cards, story cards, archival plates and the footer.
The cell field is `<ui-cellfield>`. It draws nothing a reader needs, and it stops for anyone who
has asked their system to reduce motion. The design system's own checks hold the new stylesheet
to the same rules as the rest: no raw colours, never bold, and uppercase only in the mono face.

It shipped as polarize-ui v0.5.6, and this site then adopted it everywhere. Every page now has the
new top bar, the new footer and the dark palette, and the speculations page uses the new story
cards.

<figure class="shot shot--wide">
  <a href="{{ '/assets/posts/homepage-redesign/06-live-process.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/06-live-process.jpg' | relative_url }}" alt="The live Process section: three numbered cards for adaptive-preregistration, scientific-research-scaffold and scientific-research-rag, joined by arrows." loading="lazy" /></a>
  <figcaption>Live: the Process section, three repositories that keep results honest.</figcaption>
</figure>

<figure class="shot shot--wide">
  <a href="{{ '/assets/posts/homepage-redesign/06-live-findings.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/06-live-findings.jpg' | relative_url }}" alt="The live Findings section: a featured article with its photograph beside its title and summary." loading="lazy" /></a>
  <figcaption>Live: Findings, built from the posts themselves, with their own images and credits.</figcaption>
</figure>

The same components hold up on a phone. The top bar folds into a menu that works without script,
the process steps stack with downward arrows, and the story cards scroll sideways.

<figure class="shot shot--pair">
  <a href="{{ '/assets/posts/homepage-redesign/06-live-mobile.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/06-live-mobile.jpg' | relative_url }}" alt="The live homepage on a phone: the heading, description and two buttons over the cell field." loading="lazy" /></a>
  <a href="{{ '/assets/posts/homepage-redesign/06-live-mobile-process.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/06-live-mobile-process.jpg' | relative_url }}" alt="The Process section on a phone: one numbered card per row." loading="lazy" /></a>
  <figcaption>On a phone: the hero, and the process steps stacked.</figcaption>
</figure>

## What was kept

Every version is still on the canvas, and the rules did most of the work. The versions that broke
them were useful for finding out what the rules cost, and each time the answer was less than it
first looked. These are the ones that survived:

- **The type rules.** The display serif is for headings, the sans is never bold, and uppercase is
  always mono.
- **The label rule.** Decoration says it is decoration. A tier badge can never be hidden.
- **Real content only.** Every card is built from the site's own data: posts, essays, repositories
  and the changelog. A project's finding is always its own post's summary, never a line written for
  the homepage.
- **The cells.** Only these came from the version with no rules.

The components are in [polarize-ui](https://github.com/polarizetech/polarize-ui), and the live
Storybook shows the whole homepage at desktop and phone width.
