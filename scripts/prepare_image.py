#!/usr/bin/env python3
"""The house image treatment — one recipe, so every post image matches.

Post images are desaturated and contrast-shaped on purpose: the site is set in a
cool dark palette with a single accent, and full-colour photographs fight it.
Running every image through here rather than editing them by hand is what keeps
them looking like one set.

The recipe: grayscale -> mild contrast S-curve -> slight lift of the blacks so
nothing crushes to pure black against the page -> resize to a fixed width.

Usage:  python3 scripts/prepare_image.py SRC DEST [--width 1600]
"""
import argparse
from PIL import Image, ImageOps, ImageEnhance


def treat(src, dest, width=1600):
    im = Image.open(src).convert('L')          # grayscale
    im = ImageOps.autocontrast(im, cutoff=1)   # normalise the range, ignore outliers
    im = ImageEnhance.Contrast(im).enhance(1.18)
    # Lift the blacks: pure black reads as a hole in the page on a dark background.
    im = im.point(lambda v: int(18 + v * (255 - 18) / 255))
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.convert('RGB').save(dest, 'JPEG', quality=82, optimize=True, progressive=True)
    return im.size


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('src'); ap.add_argument('dest')
    ap.add_argument('--width', type=int, default=1600)
    a = ap.parse_args()
    w, h = treat(a.src, a.dest, a.width)
    print(f'{a.dest}  {w}x{h}')
