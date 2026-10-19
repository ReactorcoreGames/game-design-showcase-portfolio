/* Renders the nexus from projects.js: the hero's art mosaic and the designs grid, A–Z. */

(function () {
    const PROJECTS = (window.PROJECTS || []).slice().sort((a, b) => a.title.localeCompare(b.title));

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

    const mosaic = document.getElementById("mosaic");
    if (mosaic && PROJECTS.length) {
        const rows = [[], [], [], []];
        shuffled(PROJECTS).forEach((p, i) => rows[i % rows.length].push(p));
        mosaic.innerHTML = rows.map(row => {
            const tiles = row.map(p => `<img src="${thumb(p)}" alt="" width="640" height="360" decoding="async">`).join("");
            return `<div class="mosaic-row">${tiles}${tiles}</div>`; // doubled so the -50% drift loops seamlessly
        }).join("");
    }

    const grid = document.getElementById("tiles");
    if (!grid) return;
    grid.innerHTML = PROJECTS.map(p => `<a class="tile" href="${href(p)}" target="_blank" rel="noopener" style="--tint: var(--tint-${esc(p.tint || "cyan")})">
  <div class="tile-media"><div class="tile-img"><img src="${thumb(p)}" alt="" width="640" height="360" loading="lazy" decoding="async"></div>${p.icon ? `<span class="id-badge"><span class="icon" style="--icon: url(icons/${esc(p.icon)}.png)"></span></span>` : ""}</div>
  <div class="tile-body"><h3 class="tile-title">${esc(p.title)}</h3><p class="tile-sub">${esc(p.subtitle)}</p><p class="tile-blurb">${esc(p.blurb)}</p></div>
</a>`).join("");
})();
