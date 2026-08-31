/* ============================================================
   POLARIZE — hero animation + scroll reveal
   Pure canvas 2D, no dependencies.

   The membrane, voltage-trace and axon demos were removed with the
   explainer sections they belonged to; see git history if they are
   ever wanted back.
   ============================================================ */
(() => {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const TAU = Math.PI * 2;

  /* Palette — read from the design system's tokens so the canvas follows the
     theme, including the light/dark pair design.css ships. Never hardcoded:
     design/tokens.json is the single source of truth for colour. */
  const cssVar = (name, fallback) =>
    getComputedStyle(document.documentElement).getPropertyValue(name).trim() || fallback;

  const C = {
    accent:    cssVar("--accent", "#5fd0c6"),
    measured:  cssVar("--measured", "#199e70"),
    exploring: cssVar("--exploring", "#c98500"),
    ink:       cssVar("--foreground", "#e8e9ea"),
  };

  /* High-DPI canvas helper. Returns a sizing fn; caller draws in CSS px. */
  function fitCanvas(canvas) {
    const ctx = canvas.getContext("2d");
    function resize() {
      const r = canvas.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.max(1, Math.round(r.width * dpr));
      canvas.height = Math.max(1, Math.round(r.height * dpr));
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      canvas._w = r.width;
      canvas._h = r.height;
    }
    resize();
    return { ctx, resize };
  }

  /* Only animate canvases that are on (or near) screen. */
  function makeVisibilityFlag(el) {
    const state = { visible: true };
    if ("IntersectionObserver" in window) {
      const io = new IntersectionObserver(
        (es) => es.forEach((e) => (state.visible = e.isIntersecting)),
        { rootMargin: "120px" }
      );
      io.observe(el);
    }
    return state;
  }

  /* =========================================================
     1) HERO — drifting field of charged ions
     ========================================================= */
  function initHero() {
    const canvas = document.getElementById("heroCanvas");
    if (!canvas) return;
    const { ctx, resize } = fitCanvas(canvas);
    const vis = makeVisibilityFlag(canvas);

    let ions = [];
    function seed() {
      const w = canvas._w, h = canvas._h;
      const count = Math.round(Math.min(90, (w * h) / 16000));
      ions = Array.from({ length: count }, () => {
        const positive = Math.random() > 0.45;
        return {
          x: Math.random() * w,
          y: Math.random() * h,
          r: 1.2 + Math.random() * 2.6,
          vx: (Math.random() - 0.5) * 0.18,
          vy: (Math.random() - 0.5) * 0.18,
          pos: positive,
          ph: Math.random() * TAU,
        };
      });
    }
    function onResize() { resize(); seed(); }
    window.addEventListener("resize", onResize);
    seed();

    let t = 0;
    function frame() {
      const w = canvas._w, h = canvas._h;
      ctx.clearRect(0, 0, w, h);
      t += 0.005;

      // soft connecting filaments (the "field")
      ctx.lineWidth = 1;
      for (let i = 0; i < ions.length; i++) {
        const a = ions[i];
        for (let j = i + 1; j < ions.length; j++) {
          const b = ions[j];
          const dx = a.x - b.x, dy = a.y - b.y;
          const d2 = dx * dx + dy * dy;
          if (d2 < 130 * 130) {
            const al = (1 - Math.sqrt(d2) / 130) * 0.16;
            ctx.strokeStyle = `rgba(63,224,255,${al})`;
            ctx.beginPath();
            ctx.moveTo(a.x, a.y);
            ctx.lineTo(b.x, b.y);
            ctx.stroke();
          }
        }
      }

      // ions
      for (const p of ions) {
        if (!reduceMotion) { p.x += p.vx; p.y += p.vy; }
        if (p.x < -20) p.x = w + 20; if (p.x > w + 20) p.x = -20;
        if (p.y < -20) p.y = h + 20; if (p.y > h + 20) p.y = -20;

        const pulse = 0.6 + 0.4 * Math.sin(t * 6 + p.ph);
        const col = p.pos ? C.accent : C.measured;
        const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 6);
        g.addColorStop(0, hex(col, 0.9 * pulse));
        g.addColorStop(1, hex(col, 0));
        ctx.fillStyle = g;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r * 6, 0, TAU);
        ctx.fill();

        ctx.fillStyle = col;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, TAU);
        ctx.fill();
      }

      if (vis.visible && !reduceMotion) requestAnimationFrame(frame);
      else setTimeout(() => requestAnimationFrame(frame), 240);
    }
    frame();
  }

  /* ---------- shared draw utils ---------- */
  function hex(h, a) {
    const n = parseInt(h.slice(1), 16);
    const r = (n >> 16) & 255, g = (n >> 8) & 255, b = n & 255;
    return `rgba(${r},${g},${b},${a})`;
  }

  /* ---------- scroll reveal ---------- */
  function initReveal() {
    const secs = document.querySelectorAll(".section");
    if (!("IntersectionObserver" in window)) { secs.forEach((s) => s.classList.add("in")); return; }
    const io = new IntersectionObserver((es) => {
      es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    secs.forEach((s) => io.observe(s));
  }

  /* ---------- boot ---------- */
  document.addEventListener("DOMContentLoaded", () => {
    initReveal();
    initHero();
  });
})();
