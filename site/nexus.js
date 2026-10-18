/* Renders the nexus from projects.js: hero mosaic, stats, browse bar and project cards.
   Filter state lives in the URL hash (#genre=mecha&aal=1&q=ragdoll&sort=az) so views can be linked. */

(function () {
    const PROJECTS = window.PROJECTS || [];
    const GENRES = window.GENRES || [];
    const ARTICLES = window.ARTICLES || [];
    const genreLabel = Object.fromEntries(GENRES.map(g => [g.id, g.label]));

    const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
    const href = p => "projects/" + encodeURIComponent(p.page);
    const thumb = p => "projects/thumbnails/" + encodeURIComponent(p.thumb || p.prefix + "_2_vignette_thumb.jpg");

    function shuffled(list) {
        const a = list.slice();
        for (let i = a.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [a[i], a[j]] = [a[j], a[i]];
        }
        return a;
    }

    /* ---- Hero ---- */

    const mosaic = document.getElementById("mosaic");
    if (mosaic && PROJECTS.length) {
        const pool = shuffled(PROJECTS);
        const rows = [[], [], [], []];
        pool.forEach((p, i) => rows[i % rows.length].push(p));
        mosaic.innerHTML = rows.map(row => {
            const tiles = row.map(p => `<img src="${thumb(p)}" alt="" width="640" height="360" decoding="async">`).join("");
            return `<div class="mosaic-row">${tiles}${tiles}</div>`; // doubled so the -50% drift loops seamlessly
        }).join("");
    }

    const setText = (id, v) => { const el = document.getElementById(id); if (el) el.textContent = v; };
    setText("stat-designs", PROJECTS.length);
    setText("stat-articles", ARTICLES.length);
    setText("stat-genres", GENRES.length);
    setText("stat-aal", PROJECTS.filter(p => p.universe === "aal").length);

    /* ---- Catalog ---- */

    const grid = document.getElementById("grid");
    if (!grid) return;
    const chipsEl = document.getElementById("chips");
    const search = document.getElementById("search");
    const sortEl = document.getElementById("sort");
    const countEl = document.getElementById("result-count");

    const state = { genre: "", aal: false, released: false, q: "", sort: "featured" };
    let shuffleOrder = null;

    function readHash() {
        const h = new URLSearchParams(location.hash.slice(1));
        state.genre = genreLabel[h.get("genre")] ? h.get("genre") : "";
        state.aal = h.get("aal") === "1";
        state.released = h.get("released") === "1";
        state.q = h.get("q") || "";
        state.sort = ["featured", "newest", "az", "shuffle"].includes(h.get("sort")) ? h.get("sort") : "featured";
    }

    function writeHash() {
        const h = new URLSearchParams();
        if (state.genre) h.set("genre", state.genre);
        if (state.aal) h.set("aal", "1");
        if (state.released) h.set("released", "1");
        if (state.q) h.set("q", state.q);
        if (state.sort !== "featured") h.set("sort", state.sort);
        const s = h.toString();
        history.replaceState(null, "", s ? "#" + s : location.pathname + location.search);
    }

    function matches(p) {
        if (state.genre && !p.genres.includes(state.genre)) return false;
        if (state.aal && p.universe !== "aal") return false;
        if (state.released && p.status !== "released") return false;
        if (state.q) {
            const hay = [p.title, p.subtitle, p.blurb, ...(p.tags || []), ...p.genres.map(g => genreLabel[g] || g),
                p.universe === "aal" ? "aal armored assault league" : "", p.status].join(" ").toLowerCase();
            if (!state.q.toLowerCase().split(/\s+/).filter(Boolean).every(w => hay.includes(w))) return false;
        }
        return true;
    }

    function sorted(list) {
        if (state.sort === "az") return list.slice().sort((a, b) => a.title.localeCompare(b.title));
        if (state.sort === "newest") {
            const idx = new Map(PROJECTS.map((p, i) => [p, i]));
            return list.slice().sort((a, b) => (b.added || "").localeCompare(a.added || "") || idx.get(a) - idx.get(b));
        }
        if (state.sort === "shuffle") {
            if (!shuffleOrder) shuffleOrder = new Map(shuffled(PROJECTS).map((p, i) => [p, i]));
            return list.slice().sort((a, b) => shuffleOrder.get(a) - shuffleOrder.get(b));
        }
        return list;
    }

    function renderChips() {
        const counts = {};
        PROJECTS.forEach(p => p.genres.forEach(g => { counts[g] = (counts[g] || 0) + 1; }));
        const aalCount = PROJECTS.filter(p => p.universe === "aal").length;
        const relCount = PROJECTS.filter(p => p.status === "released").length;
        let html = `<button type="button" class="chip" data-genre="" aria-pressed="${!state.genre}">All<span class="n">${PROJECTS.length}</span></button>`;
        for (const g of GENRES) {
            if (!counts[g.id]) continue;
            html += `<button type="button" class="chip" data-genre="${g.id}" aria-pressed="${state.genre === g.id}">${esc(g.label)}<span class="n">${counts[g.id]}</span></button>`;
        }
        if (aalCount) html += `<button type="button" class="chip chip-aal" data-toggle="aal" aria-pressed="${state.aal}" title="Armored Assault League universe">AAL universe<span class="n">${aalCount}</span></button>`;
        if (relCount) html += `<button type="button" class="chip chip-released" data-toggle="released" aria-pressed="${state.released}">Released<span class="n">${relCount}</span></button>`;
        chipsEl.innerHTML = html;
    }

    function cardHTML(p) {
        const aal = p.universe === "aal";
        const badges = [
            p.status === "released" ? '<span class="badge badge-released">Released</span>' : '<span class="badge">Concept</span>',
            aal ? '<span class="badge badge-aal">AAL</span>' : ""
        ].join("");
        const genres = p.genres.map(g => `<button type="button" class="chip" data-genre="${g}" aria-pressed="${state.genre === g}">${esc(genreLabel[g] || g)}</button>`).join("");
        const play = p.status === "released" && p.play
            ? `<a class="btn btn-primary play" href="${esc(p.play)}" target="_blank" rel="noopener">▶ Play it</a>` : "";
        return `<article class="card${aal ? " is-aal" : ""}">
  <div class="card-media"><img src="${thumb(p)}" alt="" width="640" height="360" loading="lazy" decoding="async"><div class="badges">${badges}</div></div>
  <div class="card-body">
    <h3><a href="${href(p)}" target="_blank" rel="noopener">${esc(p.title)}</a></h3>
    <p class="subtitle">${esc(p.subtitle)}</p>
    <p class="blurb">${esc(p.blurb)}</p>
    <div class="card-genres" aria-label="Genres">${genres}</div>
    ${play}
  </div>
</article>`;
    }

    function render() {
        const list = sorted(PROJECTS.filter(matches));
        grid.innerHTML = list.length ? list.map(cardHTML).join("")
            : '<p class="empty">No designs match that. <button type="button" class="chip" data-reset>Clear filters</button></p>';
        countEl.textContent = list.length === PROJECTS.length ? `${list.length} designs` : `${list.length} of ${PROJECTS.length}`;
        chipsEl.querySelectorAll("[data-genre]").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.genre === state.genre)));
        chipsEl.querySelectorAll("[data-toggle]").forEach(b => b.setAttribute("aria-pressed", String(state[b.dataset.toggle])));
        if (search.value !== state.q) search.value = state.q;
        sortEl.value = state.sort;
    }

    function update(scroll) {
        writeHash();
        render();
        if (scroll) {
            const top = document.getElementById("designs").getBoundingClientRect().top;
            if (top < 0) document.getElementById("designs").scrollIntoView();
        }
    }

    document.addEventListener("click", e => {
        const g = e.target.closest("[data-genre]");
        if (g && (chipsEl.contains(g) || grid.contains(g))) {
            state.genre = state.genre === g.dataset.genre && g.dataset.genre ? "" : g.dataset.genre;
            update(grid.contains(g));
            return;
        }
        const t = e.target.closest("[data-toggle]");
        if (t && chipsEl.contains(t)) { state[t.dataset.toggle] = !state[t.dataset.toggle]; update(false); return; }
        if (e.target.closest("[data-reset]")) {
            Object.assign(state, { genre: "", aal: false, released: false, q: "" });
            update(false);
        }
    });

    let typing;
    search.addEventListener("input", () => {
        clearTimeout(typing);
        typing = setTimeout(() => { state.q = search.value.trim(); update(false); }, 120);
    });
    sortEl.addEventListener("change", () => {
        state.sort = sortEl.value;
        if (state.sort === "shuffle") shuffleOrder = null;
        update(false);
    });
    window.addEventListener("hashchange", () => { readHash(); render(); });

    readHash();
    renderChips();
    render();
})();
