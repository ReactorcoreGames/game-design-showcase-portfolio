/* Reactorcore theme effects, shared by every page (load with defer, after theme.css).

   - Reactor wave: glowing cyan strands flowing across a fixed canvas behind the page.
   - Startup burst: a reactor-pulse flash when a visit starts, on the front page (site/index.html) only (once per visit, sessionStorage
     "rc-burst"). Click or any key skips it. The page opts in with this in <head>:
       <script>try{if(!sessionStorage.getItem("rc-burst"))document.documentElement.classList.add("burst-pending")}catch(e){}</script>
     The element marked data-burst-origin (usually the logo) is where the pulse starts.
   - prefers-reduced-motion: the wave is drawn once and holds still; the burst is a plain fade.

   window.RCFX.replayBurst() and window.RCFX.wave(on) exist for the look-test page. */

(function () {
    "use strict";

    var root = document.documentElement;
    var reduced = window.matchMedia("(prefers-reduced-motion: reduce)");
    var BG = "4, 11, 22";
    var CYAN = "19, 255, 230";
    var BLUE = "79, 184, 255";
    var energy = 0;   // 0..1, raised by the burst, boosts the wave while it decays

    function makeLayer(cls) {
        var c = document.createElement("canvas");
        c.className = "fx-layer " + cls;
        c.setAttribute("aria-hidden", "true");
        document.body.prepend(c);
        return c;
    }

    function fit(canvas) {
        var dpr = Math.min(window.devicePixelRatio || 1, 1.5);
        var w = window.innerWidth, h = window.innerHeight;
        canvas.width = Math.round(w * dpr);
        canvas.height = Math.round(h * dpr);
        return { w: w, h: h, dpr: dpr };
    }

    /* ---------- Reactor wave ---------- */

    var wave = (function () {
        var canvas = makeLayer("fx-wave");
        var ctx = canvas.getContext("2d");
        var size = fit(canvas);
        var running = false, enabled = true, frame = 0, last = 0, t = 0;

        // Each strand: vertical position (fraction of height), amplitude, two wavelengths, speeds,
        // colour, and a pulse of light travelling along it.
        var strands = [
            { y: 0.58, a: 70, k1: 0.0042, k2: 0.0110, s1: 0.45, s2: 0.27, p: 0.0, c: CYAN, alpha: 0.55, pulse: 0.00, ps: 0.16 },
            { y: 0.62, a: 95, k1: 0.0031, k2: 0.0085, s1: 0.32, s2: 0.41, p: 1.7, c: BLUE, alpha: 0.40, pulse: 0.45, ps: 0.11 },
            { y: 0.55, a: 55, k1: 0.0057, k2: 0.0140, s1: 0.58, s2: 0.20, p: 3.1, c: CYAN, alpha: 0.34, pulse: 0.80, ps: 0.21 },
            { y: 0.66, a: 120, k1: 0.0024, k2: 0.0068, s1: 0.25, s2: 0.33, p: 4.4, c: BLUE, alpha: 0.24, pulse: 0.25, ps: 0.08 },
            { y: 0.60, a: 40, k1: 0.0070, k2: 0.0170, s1: 0.70, s2: 0.52, p: 5.2, c: "220, 255, 252", alpha: 0.20, pulse: 0.62, ps: 0.27 },
            { y: 0.30, a: 50, k1: 0.0036, k2: 0.0095, s1: 0.22, s2: 0.30, p: 2.4, c: BLUE, alpha: 0.10, pulse: 0.10, ps: 0.06 }
        ];

        function yAt(s, x, scale) {
            return s.y * size.h + s.a * scale * (
                0.62 * Math.sin(x * s.k1 + t * s.s1 + s.p) +
                0.38 * Math.sin(x * s.k2 - t * s.s2 + s.p * 1.3));
        }

        function trace(s, x0, x1, scale) {
            var step = 8;
            ctx.beginPath();
            for (var x = x0; x <= x1 + step; x += step) {
                var y = yAt(s, x, scale);
                if (x === x0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
            }
        }

        function draw() {
            var d = size.dpr;
            ctx.setTransform(d, 0, 0, d, 0, 0);
            ctx.clearRect(0, 0, size.w, size.h);
            ctx.globalCompositeOperation = "lighter";
            ctx.lineCap = "round";
            ctx.lineJoin = "round";
            var scale = Math.min(1, size.w / 1100) * (1 + energy * 0.9);
            var boost = 1 + energy * 2.2;

            strands.forEach(function (s) {
                trace(s, 0, size.w, scale);
                ctx.strokeStyle = "rgba(" + s.c + "," + (s.alpha * 0.2 * boost) + ")";
                ctx.lineWidth = 9;
                ctx.stroke();
                ctx.strokeStyle = "rgba(" + s.c + "," + Math.min(1, s.alpha * boost) + ")";
                ctx.lineWidth = 1.3;
                ctx.stroke();

                // the travelling pulse: a bright segment with a fading tail
                var len = Math.max(160, size.w * 0.18);
                var head = ((s.pulse + t * s.ps) % 1.4) * (size.w + len) - len * 0.2;
                var g = ctx.createLinearGradient(head - len, 0, head, 0);
                g.addColorStop(0, "rgba(" + s.c + ",0)");
                g.addColorStop(1, "rgba(" + s.c + "," + Math.min(1, 0.95 * boost * s.alpha / 0.55) + ")");
                trace(s, Math.max(0, head - len), Math.min(size.w, head), scale);
                ctx.strokeStyle = g;
                ctx.lineWidth = 2.2;
                ctx.stroke();
            });
            ctx.globalCompositeOperation = "source-over";
        }

        function tick(now) {
            if (!running) return;
            var dt = last ? Math.min(0.05, (now - last) / 1000) : 0;
            last = now;
            t += dt * (1 + energy * 1.5);
            energy = Math.max(0, energy - dt * 0.35);
            draw();
            frame = requestAnimationFrame(tick);
        }

        function start() {
            if (running || !enabled || reduced.matches || document.hidden) return;
            running = true; last = 0;
            frame = requestAnimationFrame(tick);
        }
        function stop() { running = false; cancelAnimationFrame(frame); }

        function refresh() {
            size = fit(canvas);
            if (!enabled) { ctx.clearRect(0, 0, canvas.width, canvas.height); return; }
            draw();
            start();
        }

        window.addEventListener("resize", refresh);
        document.addEventListener("visibilitychange", function () { if (document.hidden) stop(); else start(); });
        reduced.addEventListener("change", function () { stop(); refresh(); });
        t = 7.3;  // a pleasant shape for the still frame under reduced motion
        refresh();

        return {
            set: function (on) { enabled = on; canvas.hidden = !on; if (on) refresh(); else stop(); }
        };
    })();

    /* ---------- Startup burst ---------- */

    function burst() {
        var canvas = makeLayer("fx-burst");
        var ctx = canvas.getContext("2d");
        var size = fit(canvas);
        root.classList.remove("burst-pending");

        var origin = { x: size.w / 2, y: size.h * 0.4 };
        var mark = document.querySelector("[data-burst-origin]");
        if (mark) {
            var r = mark.getBoundingClientRect();
            if (r.width && r.bottom > 0 && r.top < size.h) origin = { x: r.left + r.width / 2, y: r.top + r.height / 2 };
        }

        var CHARGE = 420, FLASH = 640, END = 1900, FADE = reduced.matches ? 500 : 0;
        var start = 0, skippedAt = 0, ignited = false, frame = 0;
        var diag = Math.hypot(Math.max(origin.x, size.w - origin.x), Math.max(origin.y, size.h - origin.y));

        // streaks of light drawn in toward the core while it charges
        var streaks = [];
        for (var i = 0; i < 28; i++) {
            var ang = Math.random() * Math.PI * 2;
            streaks.push({ ang: ang, dist: diag * (0.35 + Math.random() * 0.6), len: 40 + Math.random() * 120, delay: Math.random() * 0.45 });
        }

        function skip() { if (!skippedAt) skippedAt = performance.now(); }
        canvas.addEventListener("pointerdown", skip);
        window.addEventListener("keydown", skip);

        function ignite() {
            if (ignited) return;
            ignited = true;
            energy = 1;
            root.classList.add("fx-ignite");
            setTimeout(function () { root.classList.remove("fx-ignite"); }, 2000);
        }

        function done() {
            cancelAnimationFrame(frame);
            window.removeEventListener("keydown", skip);
            canvas.remove();
            ignite();
            try { sessionStorage.setItem("rc-burst", "1"); } catch (e) {}
        }

        function radial(r0, stops, alpha) {
            var g = ctx.createRadialGradient(origin.x, origin.y, 0, origin.x, origin.y, r0);
            stops.forEach(function (s) { g.addColorStop(s[0], "rgba(" + s[1] + "," + (s[2] * alpha) + ")"); });
            ctx.fillStyle = g;
            ctx.fillRect(0, 0, size.w, size.h);
        }

        function plainFade(e) {
            ctx.fillStyle = "rgba(" + BG + "," + (1 - Math.min(1, e / FADE)) + ")";
            ctx.fillRect(0, 0, size.w, size.h);
            return e >= FADE;
        }

        function step(now) {
            if (!start) start = now;
            var e = now - start;
            if (skippedAt) {   // a skip jumps ahead into a quick fade
                e = Math.max(e, FLASH) + (now - skippedAt) * 4;
                start = now - e;
                skippedAt = now;
            }
            ctx.setTransform(size.dpr, 0, 0, size.dpr, 0, 0);
            ctx.clearRect(0, 0, size.w, size.h);

            if (FADE) {
                if (plainFade(e)) return done();
                frame = requestAnimationFrame(step);
                return;
            }

            // dark cover that lifts after the flash
            var cover = e < FLASH ? 1 : Math.max(0, 1 - Math.pow((e - FLASH) / (END - FLASH - 300), 0.7));
            ctx.fillStyle = "rgba(" + BG + "," + cover + ")";
            ctx.fillRect(0, 0, size.w, size.h);
            ctx.globalCompositeOperation = "lighter";

            if (e < FLASH) {
                // charge: the core flickers up and streaks converge on it
                var c = e / FLASH;
                var flicker = 0.75 + Math.random() * 0.25;
                radial(20 + 140 * c * c, [[0, "255,255,255", 1], [0.25, CYAN, 0.9], [1, BLUE, 0]], c * flicker);
                ctx.lineWidth = 1.5;
                streaks.forEach(function (s) {
                    var p = Math.min(1, Math.max(0, (c - s.delay) / (1 - s.delay)));
                    if (p <= 0) return;
                    var d = s.dist * (1 - p);
                    var x1 = origin.x + Math.cos(s.ang) * d, y1 = origin.y + Math.sin(s.ang) * d;
                    var x2 = origin.x + Math.cos(s.ang) * (d + s.len), y2 = origin.y + Math.sin(s.ang) * (d + s.len);
                    var g = ctx.createLinearGradient(x1, y1, x2, y2);
                    g.addColorStop(0, "rgba(" + CYAN + ",0.9)");
                    g.addColorStop(1, "rgba(" + CYAN + ",0)");
                    ctx.strokeStyle = g;
                    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
                });
            }

            if (e >= CHARGE) {
                ignite();
                var f = (e - CHARGE) / (END - CHARGE);               // 0..1 over the rest of the burst
                var flash = Math.exp(-Math.pow((e - FLASH) / 150, 2));  // white-blue peak at FLASH
                var glow = Math.max(0, 1 - f) * 0.8;                     // the lingering Cherenkov blue
                radial(diag * 1.1, [[0, "255,255,255", 1], [0.12, "200,255,250", 0.95], [0.35, CYAN, 0.7], [1, BLUE, 0.35]], flash);
                radial(diag * (0.5 + f), [[0, CYAN, 0.5], [0.4, BLUE, 0.35], [1, BLUE, 0]], glow);

                // shock rings racing outward
                [0, 110].forEach(function (lag, i) {
                    var re = e - CHARGE - lag;
                    if (re < 0) return;
                    var rr = diag * 1.15 * (1 - Math.pow(1 - Math.min(1, re / 1100), 3));
                    var ra = Math.max(0, 1 - re / 1100) * (i ? 0.45 : 0.9);
                    ctx.strokeStyle = "rgba(" + (i ? BLUE : CYAN) + "," + ra + ")";
                    ctx.lineWidth = (i ? 10 : 3) * (1 - re / 1400);
                    ctx.beginPath(); ctx.arc(origin.x, origin.y, rr, 0, Math.PI * 2); ctx.stroke();
                });
            }
            ctx.globalCompositeOperation = "source-over";

            if (e >= END) return done();
            frame = requestAnimationFrame(step);
        }
        frame = requestAnimationFrame(step);
    }

    if (root.classList.contains("burst-pending")) burst();

    window.RCFX = {
        replayBurst: function () { try { sessionStorage.removeItem("rc-burst"); } catch (e) {} burst(); },
        wave: function (on) { wave.set(on); }
    };
})();
