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
version stayed side by side. Then it was built with Claude Code. Six directions, oldest first, and then fourteen passes on the last one:

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

Both of the first two versions had a phone layout too, drawn as separate artboards.

<figure class="shot shot--pair">
  <a href="{{ '/assets/posts/homepage-redesign/01-light-mobile.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/01-light-mobile.jpg' | relative_url }}" alt="Version one on a phone: the light page, headline stacked above a smaller waveform card." loading="lazy" /></a>
  <a href="{{ '/assets/posts/homepage-redesign/02-dark-mobile.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/02-dark-mobile.jpg' | relative_url }}" alt="Version two on a phone: the same stacked layout in the dark palette." loading="lazy" /></a>
  <figcaption>Versions one and two at phone width.</figcaption>
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

### Fourteen passes on the hybrid

The hybrid itself changed fourteen times before it shipped, one request at a time. These are all
of them, in order, each shown where it changed the page.

<div class="shot-grid">
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h01-hero.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h01-hero.jpg' | relative_url }}" alt="Step 5.1 of the hybrid homepage: The first hybrid: brutalism's dark palette and specks, the first version's charts, and no stepper." loading="lazy" /></a>
    <figcaption><strong>5.1</strong> · The first hybrid: brutalism's dark palette and specks, the first version's charts, and no stepper.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h02-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h02-focus.jpg' | relative_url }}" alt="Step 5.2 of the hybrid homepage: Corners down to 4px." loading="lazy" /></a>
    <figcaption><strong>5.2</strong> · Corners down to 4px.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h03-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h03-focus.jpg' | relative_url }}" alt="Step 5.3 of the hybrid homepage: The specimen drawings replaced by the archival plates the site already had." loading="lazy" /></a>
    <figcaption><strong>5.3</strong> · The specimen drawings replaced by the archival plates the site already had.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h04-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h04-focus.jpg' | relative_url }}" alt="Step 5.4 of the hybrid homepage: Background fills taken off the cards." loading="lazy" /></a>
    <figcaption><strong>5.4</strong> · Background fills taken off the cards.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h05-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h05-focus.jpg' | relative_url }}" alt="Step 5.5 of the hybrid homepage: Rebuilt around the repositories: projects first, then the changelog, findings and notes." loading="lazy" /></a>
    <figcaption><strong>5.5</strong> · Rebuilt around the repositories: projects first, then the changelog, findings and notes.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h06-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h06-focus.jpg' | relative_url }}" alt="Step 5.6 of the hybrid homepage: “Merged this week” became “Recently merged”." loading="lazy" /></a>
    <figcaption><strong>5.6</strong> · “Merged this week” became “Recently merged”.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h07-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h07-focus.jpg' | relative_url }}" alt="Step 5.7 of the hybrid homepage: One WebGL field behind the whole page. At first the cells looked like bubbles." loading="lazy" /></a>
    <figcaption><strong>5.7</strong> · One WebGL field behind the whole page. At first the cells looked like bubbles.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h08-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h08-focus.jpg' | relative_url }}" alt="Step 5.8 of the hybrid homepage: Back to specks: smaller, clustered, of varying density." loading="lazy" /></a>
    <figcaption><strong>5.8</strong> · Back to specks: smaller, clustered, of varying density.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h09-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h09-focus.jpg' | relative_url }}" alt="Step 5.9 of the hybrid homepage: One colour: a faded white that polarises in opacity only." loading="lazy" /></a>
    <figcaption><strong>5.9</strong> · One colour: a faded white that polarises in opacity only.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h10-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h10-focus.jpg' | relative_url }}" alt="Step 5.10 of the hybrid homepage: Quieter still: lower peaks, softer firing." loading="lazy" /></a>
    <figcaption><strong>5.10</strong> · Quieter still: lower peaks, softer firing.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h11-hero.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h11-hero.jpg' | relative_url }}" alt="Step 5.11 of the hybrid homepage: The bracketed corner tags removed." loading="lazy" /></a>
    <figcaption><strong>5.11</strong> · The bracketed corner tags removed.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h12-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h12-focus.jpg' | relative_url }}" alt="Step 5.12 of the hybrid homepage: A Process section: three repositories that keep results honest." loading="lazy" /></a>
    <figcaption><strong>5.12</strong> · A Process section: three repositories that keep results honest.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h13-hero.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h13-hero.jpg' | relative_url }}" alt="Step 5.13 of the hybrid homepage: A simpler, centred hero; the numbers strip gone." loading="lazy" /></a>
    <figcaption><strong>5.13</strong> · A simpler, centred hero; the numbers strip gone.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h13-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h13-focus.jpg' | relative_url }}" alt="Step 5.13 of the hybrid homepage: The charts moved into a section for polarize-ui." loading="lazy" /></a>
    <figcaption><strong>5.13</strong> · The charts moved into a section for polarize-ui.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h14-hero.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h14-hero.jpg' | relative_url }}" alt="Step 5.14 of the hybrid homepage: A dedicated cell turning behind the heading, with buttons for the process and for getting in touch." loading="lazy" /></a>
    <figcaption><strong>5.14</strong> · A dedicated cell turning behind the heading, with buttons for the process and for getting in touch.</figcaption>
  </figure>
  <figure class="shot">
    <a href="{{ '/assets/posts/homepage-redesign/hybrid/h14-focus.jpg' | relative_url }}"><img src="{{ '/assets/posts/homepage-redesign/hybrid/h14-focus.jpg' | relative_url }}" alt="Step 5.14 of the hybrid homepage: Speculations as story cards, told like posts." loading="lazy" /></a>
    <figcaption><strong>5.14</strong> · Speculations as story cards, told like posts.</figcaption>
  </figure>
</div>

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
