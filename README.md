# POLARIZE — The Hidden Electricity of Life

A single-page, dark-themed educational site about **bioelectricity** and the phenomenon of **cellular polarization** (membrane potential). Documentary aesthetic — National Geographic / History Channel, with a modern typographic edge.

## What's inside

Four hand-built `<canvas>` animations (zero dependencies):

1. **Hero ion field** — drifting positive/negative ions connected by a faint bioelectric field.
2. **Polarization, Live** *(the centerpiece)* — an interactive slice of a cell membrane. Press **Stimulate** (or click the canvas) to fire a wave of **depolarization**: voltage-gated channels fling open, Na⁺ floods inward, and the membrane potential flips from the resting −70 mV toward +40 mV before repolarizing.
3. **Action-potential trace** — a live voltage-over-time graph synced to the membrane.
4. **Signal propagation** — a self-renewing depolarization wave racing down a nerve fibre, flipping charge polarity as it travels.

Respects `prefers-reduced-motion` and scales down to mobile.

## Run locally

It's a static site — no build step.

```bash
python3 -m http.server 4321
# then open http://localhost:4321
```

## Files

- `index.html` — structure & copy
- `styles.css` — dark documentary theme (Archivo / Oswald / Spectral)
- `app.js` — the four canvas animations

## Brand

| | |
|---|---|
| Background | near-black `#06080c` |
| Accent (banner gold) | `#f5c542` |
| Polarized / resting | cyan `#3fe0ff` |
| Depolarized | warm `#ff7a3c` |
| Display / body type | Archivo · Oswald · Spectral |

*An educational exploration. Figures are illustrative, not to scale.*
