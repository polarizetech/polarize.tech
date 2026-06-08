/* ============================================================
   POLARIZE — bioelectric animations
   Pure canvas 2D, no dependencies.
   ============================================================ */
(() => {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const TAU = Math.PI * 2;

  /* Palette (kept in sync with styles.css) */
  const C = {
    gold:  "#f5c542",
    cyan:  "#3fe0ff",
    warm:  "#ff7a3c",
    mag:   "#ff4d8d",
    ink:   "#eef1f5",
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
        const col = p.pos ? C.gold : C.cyan;
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

  /* =========================================================
     2) MEMBRANE — the interactive polarization demo
     ========================================================= */
  function initMembrane() {
    const canvas = document.getElementById("membraneCanvas");
    if (!canvas) return;
    const { ctx, resize } = fitCanvas(canvas);
    const vis = makeVisibilityFlag(canvas);
    const readout = document.getElementById("voltReadout");

    const REST = -70, PEAK = 40;

    let channels = [];   // gated pores along the membrane
    let ions = [];       // free-floating ions on both sides
    let wave = null;     // active depolarization sweep {x, speed}
    let autoTimer = null;

    let memY = 0, memH = 0;

    function layout() {
      resize();
      const h = canvas._h;
      memY = h * 0.5;
      memH = Math.max(26, h * 0.085);

      const w = canvas._w;
      const n = Math.max(5, Math.round(w / 135));
      channels = Array.from({ length: n }, (_, i) => ({
        x: (w * (i + 0.5)) / n,
        open: 0,          // 0..1 gate openness
        v: REST,          // local membrane potential
        fired: false,
      }));

      const count = Math.round(Math.min(120, w / 7));
      ions = Array.from({ length: count }, () => spawnIon(w, h));
    }

    function spawnIon(w, h) {
      const outside = Math.random() > 0.4; // more ions outside
      // Na+ dominant outside, K+/anions inside
      let type;
      if (outside) type = Math.random() > 0.25 ? "na" : "k";
      else type = Math.random() > 0.55 ? "k" : "neg";
      const top = outside;
      const margin = 14;
      const y = top
        ? margin + Math.random() * (memY - memH / 2 - margin * 2)
        : memY + memH / 2 + margin + Math.random() * (h - (memY + memH / 2) - margin * 2);
      return {
        type, x: Math.random() * w, y,
        vx: (Math.random() - 0.5) * 0.25,
        vy: (Math.random() - 0.5) * 0.25,
        r: type === "neg" ? 2.4 : 3,
        flux: 0,           // >0 while rushing through a pore
        targetY: 0,
      };
    }

    function ionColor(t) { return t === "na" ? C.gold : t === "k" ? C.cyan : C.mag; }

    function stimulate() {
      if (wave) return;
      wave = { x: -30, speed: canvas._w / 95 };
      channels.forEach((c) => (c.fired = false));
    }

    function avgV() {
      let s = 0;
      for (const c of channels) s += c.v;
      return s / channels.length;
    }

    function frame() {
      const w = canvas._w, h = canvas._h;
      ctx.clearRect(0, 0, w, h);

      // ----- advance depolarization wave -----
      if (wave) {
        wave.x += reduceMotion ? wave.speed * 3 : wave.speed;
        if (wave.x > w + 60) wave = null;
      }

      // ----- update channels -----
      for (const c of channels) {
        if (wave && !c.fired && Math.abs(c.x - wave.x) < 36) {
          c.fired = true;
          c.open = 1;
        }
        // gate dynamics: snap open, ease closed
        if (c.open > 0.01) c.open *= 0.93; else c.open = 0;
        // local voltage: spike toward PEAK when open, decay to REST
        const target = c.open > 0.4 ? PEAK : REST;
        c.v += (target - c.v) * (c.open > 0.4 ? 0.5 : 0.06);
      }

      // ----- draw extracellular / intracellular tint by local voltage -----
      drawFluidTint(ctx, w, h, channels, memY, memH);

      // ----- ions -----
      updateIons(w, h);
      drawIons();

      // ----- membrane -----
      drawMembrane(ctx, w, channels, memY, memH);

      // ----- wave glow -----
      if (wave) {
        const g = ctx.createLinearGradient(wave.x - 70, 0, wave.x + 70, 0);
        g.addColorStop(0, hex(C.warm, 0));
        g.addColorStop(0.5, hex(C.warm, 0.5));
        g.addColorStop(1, hex(C.warm, 0));
        ctx.fillStyle = g;
        ctx.fillRect(wave.x - 70, memY - memH, 140, memH * 2);
      }

      // ----- charge labels -----
      drawChargeLabels(ctx, w, memY, memH, avgV());

      // ----- readout -----
      const v = Math.round(avgV());
      if (readout) {
        readout.textContent = (v > 0 ? "+" : "") + v + " mV";
        readout.style.color = v > -20 ? C.warm : C.cyan;
      }
      Trace.push(avgV());

      if (vis.visible) requestAnimationFrame(frame);
      else setTimeout(() => requestAnimationFrame(frame), 200);
    }

    function updateIons(w, h) {
      for (const p of ions) {
        // find nearest open channel to maybe rush through
        if (p.flux === 0 && p.type === "na" && p.y < memY) {
          for (const c of channels) {
            if (c.open > 0.5 && Math.abs(c.x - p.x) < 18) {
              p.flux = 1; p.vx = (c.x - p.x) * 0.05;
              p.targetY = memY + memH; break;
            }
          }
        }
        if (p.flux > 0) {
          // rush inward through pore
          p.y += 1.6;
          p.x += (snapChannelX(p.x) - p.x) * 0.2;
          if (p.y > p.targetY + 8) { p.flux = 0; p.vy = Math.random() * 0.3 + 0.1; }
        } else if (!reduceMotion) {
          p.x += p.vx; p.y += p.vy;
          // gentle brownian jitter
          p.vx += (Math.random() - 0.5) * 0.04;
          p.vy += (Math.random() - 0.5) * 0.04;
          p.vx *= 0.96; p.vy *= 0.96;
        }

        // wall + membrane confinement (unless mid-flux)
        if (p.x < 6) { p.x = 6; p.vx *= -1; }
        if (p.x > w - 6) { p.x = w - 6; p.vx *= -1; }
        if (p.flux === 0) {
          const topZone = p.y < memY;
          if (topZone && p.y > memY - memH / 2 - p.r) { p.y = memY - memH / 2 - p.r; p.vy *= -1; }
          if (!topZone && p.y < memY + memH / 2 + p.r) { p.y = memY + memH / 2 + p.r; p.vy *= -1; }
          if (p.y < 6) { p.y = 6; p.vy *= -1; }
          if (p.y > h - 6) { p.y = h - 6; p.vy *= -1; }
        }
      }
    }

    function snapChannelX(x) {
      let best = x, bd = 1e9;
      for (const c of channels) { const d = Math.abs(c.x - x); if (d < bd) { bd = d; best = c.x; } }
      return best;
    }

    function drawIons() {
      for (const p of ions) {
        const col = ionColor(p.type);
        const glow = p.flux > 0 ? 7 : 4.5;
        const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * glow);
        g.addColorStop(0, hex(col, 0.85));
        g.addColorStop(1, hex(col, 0));
        ctx.fillStyle = g;
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r * glow, 0, TAU); ctx.fill();

        ctx.fillStyle = col;
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, TAU); ctx.fill();

        // +/- sign
        ctx.strokeStyle = "rgba(10,10,14,.9)";
        ctx.lineWidth = 1.1;
        ctx.beginPath();
        ctx.moveTo(p.x - p.r * 0.5, p.y); ctx.lineTo(p.x + p.r * 0.5, p.y);
        if (p.type !== "neg") { ctx.moveTo(p.x, p.y - p.r * 0.5); ctx.lineTo(p.x, p.y + p.r * 0.5); }
        ctx.stroke();
      }
    }

    // controls
    const stimBtn = document.getElementById("stimulateBtn");
    const autoBtn = document.getElementById("autoBtn");
    if (stimBtn) stimBtn.addEventListener("click", stimulate);
    if (autoBtn) autoBtn.addEventListener("click", () => {
      if (autoTimer) { clearInterval(autoTimer); autoTimer = null; autoBtn.textContent = "Auto-pulse: Off"; }
      else { autoTimer = setInterval(stimulate, 2600); autoBtn.textContent = "Auto-pulse: On"; stimulate(); }
    });
    canvas.addEventListener("click", stimulate);
    canvas.style.cursor = "pointer";

    window.addEventListener("resize", layout);
    layout();
    frame();
  }

  /* ---- membrane drawing helpers ---- */
  function drawFluidTint(ctx, w, h, channels, memY, memH) {
    // sample local voltage across width → tint extracellular vs intracellular
    const n = channels.length;
    for (let i = 0; i < n; i++) {
      const c = channels[i];
      const x0 = i === 0 ? 0 : (channels[i - 1].x + c.x) / 2;
      const x1 = i === n - 1 ? w : (c.x + channels[i + 1].x) / 2;
      const depol = (c.v - (-70)) / 110; // 0 rest .. 1 peak
      // intracellular (bottom) glows warm as it depolarizes
      const gi = ctx.createLinearGradient(0, memY, 0, h);
      gi.addColorStop(0, hex(mix(C.cyan, C.warm, depol), 0.10 + depol * 0.22));
      gi.addColorStop(1, hex(mix(C.cyan, C.warm, depol), 0));
      ctx.fillStyle = gi;
      ctx.fillRect(x0, memY, x1 - x0, h - memY);
    }
  }

  function drawMembrane(ctx, w, channels, memY, memH) {
    const top = memY - memH / 2, bot = memY + memH / 2;
    const r = Math.min(7, memH * 0.26);
    const spacing = r * 2.05;

    // bilayer: two rows of phospholipid heads with tails inward
    ctx.save();
    for (let x = r; x < w; x += spacing) {
      // tails
      ctx.strokeStyle = "rgba(150,170,200,.18)";
      ctx.lineWidth = 1.1;
      ctx.beginPath(); ctx.moveTo(x, top + r); ctx.lineTo(x, memY - 1); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(x, bot - r); ctx.lineTo(x, memY + 1); ctx.stroke();
      // heads
      head(ctx, x, top + r, r);
      head(ctx, x, bot - r, r);
    }
    ctx.restore();

    // channels (gated pores)
    for (const c of channels) {
      const openW = 6 + c.open * 16;
      // pore body
      ctx.fillStyle = c.open > 0.4 ? hex(C.warm, 0.9) : "rgba(120,140,170,.5)";
      roundRect(ctx, c.x - openW / 2 - 4, top - 4, openW + 8, memH + 8, 5);
      ctx.fill();
      // channel lumen
      ctx.fillStyle = c.open > 0.4 ? hex(C.warm, 0.25) : "rgba(8,12,18,.85)";
      roundRect(ctx, c.x - openW / 2, top, openW, memH, 4);
      ctx.fill();
      if (c.open > 0.4) {
        ctx.strokeStyle = hex(C.warm, 0.8);
        ctx.lineWidth = 1.4;
        roundRect(ctx, c.x - openW / 2, top, openW, memH, 4);
        ctx.stroke();
      }
    }
  }

  function head(ctx, x, y, r) {
    const g = ctx.createRadialGradient(x - r * 0.3, y - r * 0.3, 0, x, y, r);
    g.addColorStop(0, "rgba(190,205,230,.55)");
    g.addColorStop(1, "rgba(70,90,120,.30)");
    ctx.fillStyle = g;
    ctx.beginPath(); ctx.arc(x, y, r, 0, TAU); ctx.fill();
  }

  function drawChargeLabels(ctx, w, memY, memH, v) {
    const h = memY * 2; // memY is vertical centre of the canvas
    ctx.save();
    ctx.font = "600 11px Oswald, sans-serif";
    ctx.fillStyle = "rgba(154,163,178,.55)";
    ctx.textBaseline = "top";
    ctx.fillText("EXTRACELLULAR · OUTSIDE", 14, 12);
    ctx.textBaseline = "bottom";
    ctx.fillText("INTRACELLULAR · INSIDE", 14, h - 12);
    ctx.restore();
  }

  /* =========================================================
     3) TRACE — action-potential voltage graph
     ========================================================= */
  const Trace = (() => {
    let canvas, ctx, vals = [], maxLen = 320;
    function init() {
      canvas = document.getElementById("traceCanvas");
      if (!canvas) return;
      const f = fitCanvas(canvas);
      ctx = f.ctx;
      window.addEventListener("resize", () => { f.resize(); maxLen = Math.round(canvas._w / 2); });
      maxLen = Math.round(canvas._w / 2);
      vals = new Array(maxLen).fill(-70);
      draw();
    }
    function push(v) { if (!ctx) return; vals.push(v); while (vals.length > maxLen) vals.shift(); }
    function vToY(v, h) {
      // map -90..+50 mV to bottom..top with padding
      const top = 18, bot = h - 18;
      const t = (v - 50) / (-90 - 50); // +50 -> 0, -90 -> 1
      return top + (bot - top) * t;
    }
    function draw() {
      if (!ctx) return;
      const w = canvas._w, h = canvas._h;
      ctx.clearRect(0, 0, w, h);

      // gridlines at key voltages
      const marks = [{ v: 40, l: "+40" }, { v: 0, l: "0" }, { v: -70, l: "−70 (rest)" }];
      ctx.font = "500 10px Oswald, sans-serif";
      for (const m of marks) {
        const y = vToY(m.v, h);
        ctx.strokeStyle = m.v === -70 ? "rgba(63,224,255,.22)" : "rgba(255,255,255,.07)";
        ctx.setLineDash(m.v === -70 ? [4, 4] : []);
        ctx.beginPath(); ctx.moveTo(40, y); ctx.lineTo(w - 8, y); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "rgba(154,163,178,.7)";
        ctx.fillText(m.l, 4, y - 4);
      }

      // the trace
      const step = (w - 48) / maxLen;
      ctx.beginPath();
      for (let i = 0; i < vals.length; i++) {
        const x = 44 + i * step;
        const y = vToY(vals[i], h);
        i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
      }
      ctx.strokeStyle = C.gold;
      ctx.lineWidth = 2;
      ctx.shadowColor = hex(C.gold, 0.7);
      ctx.shadowBlur = 8;
      ctx.lineJoin = "round";
      ctx.stroke();
      ctx.shadowBlur = 0;

      // leading dot
      if (vals.length) {
        const x = 44 + (vals.length - 1) * step;
        const y = vToY(vals[vals.length - 1], h);
        ctx.fillStyle = C.gold;
        ctx.beginPath(); ctx.arc(x, y, 3.2, 0, TAU); ctx.fill();
      }
      requestAnimationFrame(draw);
    }
    return { init, push };
  })();

  /* =========================================================
     4) AXON — a depolarization wave racing down a fibre
     ========================================================= */
  function initAxon() {
    const canvas = document.getElementById("axonCanvas");
    if (!canvas) return;
    const { ctx, resize } = fitCanvas(canvas);
    const vis = makeVisibilityFlag(canvas);
    window.addEventListener("resize", resize);

    let t = 0;
    const pulses = [0, 0.55]; // normalized positions along the fibre

    function frame() {
      const w = canvas._w, h = canvas._h;
      ctx.clearRect(0, 0, w, h);
      const cy = h / 2;
      const fibreH = Math.max(34, h * 0.22);

      if (!reduceMotion) t += 0.0045;

      // fibre body
      const bg = ctx.createLinearGradient(0, cy - fibreH, 0, cy + fibreH);
      bg.addColorStop(0, "rgba(40,70,95,.25)");
      bg.addColorStop(0.5, "rgba(20,40,60,.5)");
      bg.addColorStop(1, "rgba(40,70,95,.25)");
      ctx.fillStyle = bg;
      roundRect(ctx, 20, cy - fibreH, w - 40, fibreH * 2, fibreH);
      ctx.fill();
      ctx.strokeStyle = "rgba(120,150,180,.3)";
      ctx.lineWidth = 1.2;
      roundRect(ctx, 20, cy - fibreH, w - 40, fibreH * 2, fibreH);
      ctx.stroke();

      // resting polarization ticks (+ outside / - inside)
      ctx.font = "600 12px Oswald, sans-serif";
      ctx.textAlign = "center";
      for (let x = 50; x < w - 40; x += 46) {
        const np = nearestPulse(pulses, t, x, w);
        const depol = np; // 0..1
        ctx.fillStyle = hex(mix(C.cyan, C.warm, depol), 0.5 + depol * 0.5);
        ctx.fillText(depol > 0.5 ? "−" : "+", x, cy - fibreH - 6);
        ctx.fillStyle = hex(mix(C.cyan, C.warm, depol), 0.35 + depol * 0.5);
        ctx.fillText(depol > 0.5 ? "+" : "−", x, cy + fibreH + 16);
      }
      ctx.textAlign = "left";

      // travelling pulses
      for (let k = 0; k < pulses.length; k++) {
        let p = (t * 0.9 + pulses[k]) % 1.3;
        if (p > 1.05) continue;
        const px = 30 + p * (w - 60);
        const grd = ctx.createRadialGradient(px, cy, 0, px, cy, fibreH * 2.4);
        grd.addColorStop(0, hex(C.warm, 0.85));
        grd.addColorStop(0.4, hex(C.gold, 0.4));
        grd.addColorStop(1, hex(C.gold, 0));
        ctx.fillStyle = grd;
        ctx.beginPath(); ctx.ellipse(px, cy, fibreH * 1.5, fibreH * 1.4, 0, 0, TAU); ctx.fill();

        // bright core
        ctx.fillStyle = hex(C.warm, 0.95);
        ctx.beginPath(); ctx.ellipse(px, cy, fibreH * 0.45, fibreH * 0.92, 0, 0, TAU); ctx.fill();

        // trailing comet
        const tg = ctx.createLinearGradient(px - fibreH * 3, cy, px, cy);
        tg.addColorStop(0, hex(C.gold, 0));
        tg.addColorStop(1, hex(C.gold, 0.35));
        ctx.fillStyle = tg;
        roundRect(ctx, px - fibreH * 3, cy - fibreH * 0.5, fibreH * 3, fibreH, fibreH * 0.5);
        ctx.fill();
      }

      // direction hint
      ctx.fillStyle = "rgba(154,163,178,.45)";
      ctx.font = "600 11px Oswald, sans-serif";
      ctx.fillText("IMPULSE DIRECTION  →", 24, cy - fibreH - 18);

      if (vis.visible) requestAnimationFrame(frame);
      else setTimeout(() => requestAnimationFrame(frame), 220);
    }

    function nearestPulse(ps, time, x, w) {
      let best = 0;
      for (const off of ps) {
        let p = (time * 0.9 + off) % 1.3;
        if (p > 1.05) continue;
        const px = 30 + p * (w - 60);
        const d = Math.abs(px - x);
        const v = Math.max(0, 1 - d / 60);
        if (v > best) best = v;
      }
      return best;
    }
    frame();
  }

  /* ---------- shared draw utils ---------- */
  function roundRect(ctx, x, y, w, h, r) {
    r = Math.min(r, w / 2, h / 2);
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }
  function hex(h, a) {
    const n = parseInt(h.slice(1), 16);
    const r = (n >> 16) & 255, g = (n >> 8) & 255, b = n & 255;
    return `rgba(${r},${g},${b},${a})`;
  }
  function mix(h1, h2, t) {
    const a = parseInt(h1.slice(1), 16), b = parseInt(h2.slice(1), 16);
    const r = Math.round(((a >> 16 & 255) * (1 - t) + (b >> 16 & 255) * t));
    const g = Math.round(((a >> 8 & 255) * (1 - t) + (b >> 8 & 255) * t));
    const bl = Math.round(((a & 255) * (1 - t) + (b & 255) * t));
    return `#${((1 << 24) + (r << 16) + (g << 8) + bl).toString(16).slice(1)}`;
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
    Trace.init();
    initMembrane();
    initAxon();
  });
})();
