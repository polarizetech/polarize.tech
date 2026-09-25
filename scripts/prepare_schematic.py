#!/usr/bin/env python3
"""The schematic-plate treatment — one recipe, so every archival plate matches.

Real historical engravings and drawings (public domain or openly licensed) are
turned into dark plates that sit inside long posts without fighting the page:

  crop (optional) -> grayscale -> flatten the paper (divide out uneven
  yellowing and foxing) -> levels, so paper goes to 0 and ink to 1 -> INVERT, so
  the ink becomes the light -> tone between a charcoal-teal ground and a
  bone-white line -> place on a 3:2 canvas of the same ground -> fine grain
  and a soft vignette -> 1600 px JPEG.

Nothing is drawn, generated or retouched: every line in the output is a line in
the source. The source, its licence and the crop used for each plate are
recorded in _data/schematics.yml; how to add one is in docs/schematic-visuals.md.

Usage:  python3 scripts/prepare_schematic.py SRC DEST [--crop L,T,R,B] [--seed N]
        --crop  fractions of the source (0-1) to keep, e.g. 0.08,0.03,0.62,0.5
Needs Pillow and NumPy (e.g. `uv run --with pillow --with numpy python3 ...`).
"""
import argparse

import numpy as np
from PIL import Image, ImageFilter

GROUND = np.array([17, 23, 25], dtype=np.float32)    # charcoal with a trace of teal
LINE = np.array([214, 207, 190], dtype=np.float32)   # bone white, slightly warm
WIDTH, ASPECT = 1600, 3 / 2


def treat(src, dest, crop=None, seed=0):
    im = Image.open(src).convert('L')
    if crop:
        l, t, r, b = crop
        im = im.crop((round(l * im.width), round(t * im.height),
                      round(r * im.width), round(b * im.height)))

    # Flatten the paper: divide by a heavy blur, which is the paper's own tone.
    a = np.asarray(im, dtype=np.float32) + 1
    paper = np.asarray(im.filter(ImageFilter.GaussianBlur(max(im.size) / 40)), dtype=np.float32) + 1
    flat = np.clip(a / paper, 0, 1.2)

    # Levels: paper (the bright bulk) to 0, ink to 1 — i.e. inverted.
    lo, hi = np.percentile(flat, [2, 60])
    ink = np.clip((hi - flat) / max(hi - lo, 1e-3), 0, 1) ** 0.85

    # Feather the crop's edges into the ground, so no box shows around it.
    h, w = ink.shape
    f = max(4, int(min(h, w) * 0.05))
    ramp = lambda n: np.minimum(1, np.minimum(np.arange(n), np.arange(n)[::-1]) / f)
    ink *= np.outer(ramp(h), ramp(w)) ** 1.5

    # Place on a 3:2 canvas of ground, the plate filling ~86% of the height
    # (or width), set a little off centre.
    h, w = ink.shape
    cw, ch = (w / 0.9, w / 0.9 / ASPECT) if w / h > ASPECT else (h / 0.86 * ASPECT, h / 0.86)
    cw, ch = int(cw), int(ch)
    canvas = np.zeros((ch, cw), dtype=np.float32)
    x0 = int((cw - w) * 0.46)
    y0 = (ch - h) // 2
    canvas[y0:y0 + h, x0:x0 + w] = ink

    # Resize to the output width.
    out = Image.fromarray((canvas * 255).astype(np.uint8)).resize(
        (WIDTH, round(WIDTH / ASPECT)), Image.LANCZOS)
    t = np.asarray(out, dtype=np.float32) / 255

    # Grain and vignette.
    rng = np.random.default_rng(seed)
    t = np.clip(t + rng.normal(0, 0.035, t.shape), 0, 1)
    yy, xx = np.mgrid[0:t.shape[0], 0:t.shape[1]]
    r = np.hypot((xx - t.shape[1] / 2) / (t.shape[1] / 2), (yy - t.shape[0] / 2) / (t.shape[0] / 2))
    vignette = 1 - 0.28 * np.clip(r - 0.35, 0, 1) ** 1.6

    rgb = (GROUND + (LINE - GROUND) * t[..., None]) * vignette[..., None]
    Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8), 'RGB').save(
        dest, 'JPEG', quality=82, optimize=True, progressive=True)
    return WIDTH, round(WIDTH / ASPECT)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('src')
    ap.add_argument('dest')
    ap.add_argument('--crop', type=lambda s: [float(x) for x in s.split(',')])
    ap.add_argument('--seed', type=int, default=0)
    a = ap.parse_args()
    w, h = treat(a.src, a.dest, a.crop, a.seed)
    print(f'{a.dest}  {w}x{h}')
