# Schematic plates on polarize.tech

How the site uses them, how to add one, then the original brief (below the rule).

## What is on the site

Six **real archival drawings** — Cajal, Galvani, Duverney, Milton, Vicq-d'Azyr — in
`assets/schematics/`, each registered in `_data/schematics.yml` with its source record, the exact
file downloaded, its licence and the crop used. All are public domain or CC BY. Nothing in them is
drawn or generated here: `scripts/prepare_schematic.py` only crops, flattens the paper, inverts,
tones to the site's charcoal-and-bone palette, and adds grain and a vignette.

(A first set of six plates, added 2026-09-25, turned out to be AI-generated in an archival style —
the brief below says so itself. They were removed the same day and replaced with these.)

Placement is automatic (`_includes/schematic-content.html`, used by `_layouts/post.html`):

- only posts with at least 800 words and 4 `##` sections get one;
- at most **one** plate per post, at the section break nearest the middle;
- the plate is one whose `projects` list includes the post's project, chosen stably from its
  publication date;
- `schematic: <id>` in a post's front matter picks the plate; `schematic: none` opts out;
- rants never get one (their layout does not use the include).

Each caption names the maker, work and date, and links the licence to the source record.

## Adding a plate

1. Find a real schematic you are allowed to show: public domain, CC0 or CC BY. Wellcome
   Collection (look for the Public Domain Mark) and Wikimedia Commons are the best sources; the
   brief below lists more. Check the licence on the individual file, not the collection.
2. Download the largest file (for Wellcome, the IIIF URL `…/full/2400,/0/default.jpg`).
3. Run the treatment, choosing a crop that frames one figure or a clean group:
   `uv run --with pillow --with numpy python3 scripts/prepare_schematic.py SRC
   assets/schematics/<id>.jpg --crop L,T,R,B`
4. Add the entry to `_data/schematics.yml` with every field filled in.

**Never generate the anatomy.** An image model may not redraw or invent a schematic for this site;
if one is ever used for surrounding texture, the plate must say so in its caption.

The same plates suit repo READMEs and social cards; reuse them from `assets/schematics/` with the
same credit.

---


# Polarize.tech Scientific Schematic Visual System

## Important provenance note

The earlier graphics in this chat **did not actually contain downloaded historical schematics**. The anatomical plates and handwritten-looking annotations were AI-generated in the visual style of old scientific atlases.

For future production, use **real archival/public-domain source images as the schematic layer**, then apply the Polarize visual treatment around them. The sources below are good candidates.

---

## Recommended schematic source library

### 1. Neurons — Santiago Ramón y Cajal

**Cajal–Retzius cell drawing (1891)**  
https://commons.wikimedia.org/wiki/File:Cajal-Retzius_cell_drawing_by_Cajal_1891.gif

- Original historical neuron drawing by Santiago Ramón y Cajal.
- Wikimedia Commons marks it as public domain.
- Best for: sparse neuron graphics, cortical-cell illustrations, dendritic morphology.
- Reuse confidence: **High**

**Cajal cortex drawings (1899)**  
https://commons.wikimedia.org/wiki/File:Cajal_cortex_drawings.png

- Three historical cortical drawings: adult visual cortex, adult motor cortex, and infant cortex.
- Public-domain status is clearly documented for the U.S.; check jurisdiction if needed for a commercial deployment outside the U.S.
- Best for: cortical layers, neuron populations, comparative morphology.
- Reuse confidence: **Medium–High**

**Cajal hippocampus drawing (1911)**  
https://commons.wikimedia.org/wiki/File:CajalHippocampus.jpeg

- Original drawing of rodent hippocampal neural circuitry.
- Wikimedia Commons identifies it as public domain in countries using life + 70 years or less.
- Best for: network/circuit illustrations, memory-related posts.
- Reuse confidence: **High**

**Historical isolated neuron / Deiters-type morphology**  
https://commons.wikimedia.org/wiki/File:NeuroneChauveau1890MeyCh.jpg

- Historical neuron illustration from the late 19th century.
- Marked as free of known copyright restrictions/public domain.
- Best for: single-neuron or axon/dendrite compositions.
- Reuse confidence: **High**

---

### 2. Brain anatomy — historical engraved plates

**Charles Bell — _The anatomy of the brain, explained in a series of engravings_ (1802)**  
https://wellcomecollection.org/works/be9879j5

- Full historical atlas with engraved brain plates.
- Wellcome explicitly marks the work **Public Domain** and allows use without restriction.
- Best for: sagittal brain, superior/inferior views, anatomical plates.
- Reuse confidence: **Very High**

**Richard H. Whitehead — _The anatomy of the brain_ (1900)**  
https://wellcomecollection.org/works/t8rfvckk

- Contains 112 digitized images.
- Wellcome Public Domain Mark.
- Best for: top-view, cross-sectional, and labeled brain anatomy.
- Reuse confidence: **Very High**

**J. G. Spurzheim — _The anatomy of the brain_ (1834)**  
https://wellcomecollection.org/works/tyxr39b4

- Large digitized historical brain/anatomy collection.
- Wellcome Public Domain Mark.
- Best for: unusual orientations, full-page plates, older handwritten/engraved feel.
- Reuse confidence: **Very High**

**Gray’s Anatomy — brain plate / lateral view**  
https://commons.wikimedia.org/wiki/File:Brain_diagram_without_text.svg

- Derived from the 1918 public-domain edition of Gray’s Anatomy.
- Available as SVG, useful for clean compositing.
- Best for: simple brain silhouette or lobe map with lots of negative space.
- Reuse confidence: **Very High**

**Gray’s Anatomy plate 517 — brain**  
https://commons.wikimedia.org/wiki/File:Gray%27s_Anatomy_plate_517_brain.png

- Historical Gray’s Anatomy plate.
- Explicitly identified as public domain.
- Best for: alternate brain sections/orientations.
- Reuse confidence: **Very High**

**NLM — human brain and upper torso, 1519**  
https://www.ncbi.nlm.nih.gov/nlmcatalog/101435106

- Very early anatomical woodcut with brain views from above.
- NLM states that it believes the item to be in the public domain.
- Best for: more unusual, archaic, top-down brain imagery.
- Reuse confidence: **High**

---

### 3. Auditory / cochlea / hearing

**Auditory pathway schematic — Jonathan E. Peelle**  
https://commons.wikimedia.org/wiki/File:Auditory_Pathway.png

- Modern but clean neuroscience schematic of the auditory neural pathway.
- Licensed CC BY 4.0.
- Best for: auditory pathway, cochlea-to-cortex posts, AEP/FFR material.
- Attribution required.
- Reuse confidence: **Very High**

**Public-domain auditory pathway diagram**  
https://commons.wikimedia.org/wiki/File:Aud_pathway.png

- Simple auditory pathway schematic released into the public domain by its author.
- Best for: minimal overlays or simplified auditory-route graphics.
- Reuse confidence: **Very High**

For a more antique cochlea/ear look, search the public-domain Gray’s Anatomy plate archive on Wikimedia Commons:
https://commons.wikimedia.org/wiki/Category:Gray%27s_Anatomy_plates

---

### 4. Bone / marrow / skeletal anatomy

**John Bell — _Engravings, explaining the anatomy of the bones, muscles, and joints_ (1794)**  
https://wellcomecollection.org/works/b3retmds

- 292 digitized images.
- Wellcome Public Domain Mark.
- Best for: bone cross-sections, long-bone structure, skeletal anatomy, marrow-adjacent visual concepts.
- Reuse confidence: **Very High**

**Jean-Joseph Sue / Edward Mitchell — _The anatomy of the bones of the human body_ (1829)**  
https://wellcomecollection.org/works/rf4g4unx

- Large collection of engraved bone plates.
- Wellcome Public Domain Mark.
- Best for: bone structure, trabecular forms, cross-sections, long-bone plates.
- Reuse confidence: **Very High**

**Edward Mitchell / John Barclay — human skeleton engravings (1819)**  
https://wellcomecollection.org/works/ajpy3dz6

- Historical skeleton and bone engravings.
- Public Domain Mark.
- Best for: skeletal anatomy, bone structure, broader anatomical fillers.
- Reuse confidence: **Very High**

---

## Best source hubs to browse

**Wellcome Collection**
https://wellcomecollection.org/

Search terms:
- brain anatomy engraving
- nervous system
- neuron
- cochlea
- auditory anatomy
- bones
- marrow
- histology
- cerebral cortex
- spinal cord

Look for the **Public Domain Mark** on the individual work.

**Wikimedia Commons**
https://commons.wikimedia.org/

Useful categories/searches:
- Santiago Ramón y Cajal
- Gray's Anatomy plates
- neuroanatomy
- auditory system
- histology
- skeletal anatomy

Check the license on each individual file.

**National Library of Medicine / NLM**
https://collections.nlm.nih.gov/

Useful for:
- early anatomical plates
- medical illustration
- historical neuroanatomy
- unusual archival diagrams

Check the copyright statement on each record.

---

# Reusable image-generation prompt

Use this prompt after attaching or otherwise supplying the **actual archival schematic** you want incorporated.

```text
Create a high-resolution landscape editorial image for Polarize.tech using the supplied historical scientific schematic as the authentic primary visual source.

SUBJECT:
[SUBJECT — e.g. pyramidal neuron / cochlea / coronal brain section / bone marrow / auditory pathway]

SOURCE SCHEMATIC:
[ARCHIVAL SOURCE NAME + URL OR ATTACHED IMAGE]

COMPOSITION:
- landscape orientation, approximately [ASPECT RATIO — default 16:9]
- preserve the identifiable structure, linework, proportions, imperfections, labels, handwritten marks, and engraving character of the supplied source
- do not redraw the anatomy into a generic AI version
- position the schematic off-center or asymmetrically
- leave approximately 35–50% of the image as quiet negative background space
- one primary schematic only, with at most 1–2 small secondary details/insets
- avoid collage density and avoid filling every region of the canvas

VISUAL STYLE:
- dark archival scientific photograph / aged technical plate
- deep charcoal-black and very dark desaturated teal-green base
- faded warm-gray, bone-white, graphite, oxidized brown, or extremely muted rust linework
- color should feel embedded in aged photographic chemistry, not digitally overlaid
- almost monochrome
- no bright gradients, neon glows, saturated cyan, hot magenta, purple bloom, or vivid blue lighting
- extremely restrained color contrast
- soft uneven exposure, subtle vignette, faded edges, dust, scratches, paper texture, emulsion grain, and minor archival wear
- schematic itself slightly darkened so it emerges from the surface rather than sitting brightly above it

TECHNICAL OVERLAYS:
- add only a sparse layer of thin drafting geometry
- subtle measurement ticks
- one or two circles/arcs
- a few crosshairs, guide lines, coordinate marks, scale bars, or waveform traces where conceptually relevant
- overlays should be dimmer than the primary schematic
- typography/annotations should feel like original scientific notation or restrained drafting marks
- avoid fake dense equations or decorative pseudo-science

MOOD:
- archival
- experimental
- precise
- understated
- slightly mysterious
- scientific rather than science-fiction
- should feel scanned, photographed, or printed rather than freshly digitally rendered

NEGATIVE CONSTRAINTS:
- no people
- no 3D glossy anatomy
- no photorealistic medical render
- no bright gradient wash
- no cyberpunk neon
- no glowing UI
- no dense HUD
- no excessive labels
- no multiple competing focal points
- no generic AI neuron/brain replacing the supplied archival drawing
- no invented technical text when real labels from the source can be retained

OUTPUT:
- high-resolution landscape image suitable for blog headers, GitHub repositories, article cards, and editorial filler graphics
- preserve enough empty space that title text could be placed over the image later
```

---

## Short reusable version

```text
Use the supplied real public-domain scientific schematic as the authentic foreground source. Create a high-resolution 16:9 Polarize.tech editorial image: dark charcoal/desaturated-teal aged photographic plate, faded graphite/bone-white engraving, subtle oxidized-brown accents, low contrast, archival grain, dust, scratches and vignette. Keep the schematic slightly dark and embedded into the background. Add only sparse drafting geometry, measurement ticks, one or two arcs/crosshairs, and minimal handwritten/scientific annotations. Leave 35–50% quiet negative space. Nearly monochrome. No bright gradients, neon, glossy 3D anatomy, busy HUDs, fake equations, or generic AI-redrawn anatomy. Preserve the supplied source's actual linework and historical imperfections.
```

---

## Suggested subject rotation

To avoid the “all brains” problem, rotate across:

1. Cajal pyramidal neuron
2. Cajal hippocampal circuitry
3. Brain viewed from above
4. Coronal brain section
5. Cochlea / organ of Corti
6. Auditory pathway
7. Synapse / terminal bouton
8. Spinal cord cross-section
9. Long-bone / trabecular structure / marrow cavity
10. Skeletal plate
11. Peripheral nerve bundle
12. Retina / optic pathway
13. Muscle spindle
14. Histological tissue plate
15. EEG / physiological waveform plate

The archive source should change with the subject instead of repeatedly restyling the same sagittal brain.
