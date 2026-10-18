/* Shared by index.html and articles.html: the "See my work" links drawer and the footer year.
   The drawer's links live here so every page shows the same list. */

(function () {
    const LINKS = [
        { group: "See my work" },
        { label: "Game design articles", desc: "16 essays on why games matter and how to design them", href: "articles.html", accent: true },
        { label: "Reactorcore homepage", desc: "Everything I make, in one catalog", href: "https://reactorcoregames.github.io/" },
        { label: "Releases on itch.io", desc: "Games, software, tools and experiments", href: "https://reactorcore.itch.io/" },
        { label: "Devblog & membership perks", desc: "Patreon: updates, articles, early access", href: "https://www.patreon.com/ReactorcoreGames" },
        { label: "RCG Discord community", desc: "Hang out, ask, follow along", href: "https://discord.gg/UdRavGhj47" },
        { label: "All my links", desc: "Linktree: socials, galleries, mods, assets", href: "https://linktr.ee/reactorcore" },
        { label: "GitHub", desc: "This portfolio's source, designs and design bible", href: "https://github.com/ReactorcoreGames/game-design-showcase-portfolio" },
        { group: "Contact or hire me" },
        { label: "reactorcoregames@gmail.com", desc: "Advanced game design plans and consulting, standalone offline web apps, automation software with Python", href: "mailto:reactorcoregames@gmail.com", accent: true },
        { label: "Resume / CV", desc: "What I can work on, and how", href: "hire_me/hire_me.html" }
    ];

    const root = document.documentElement;
    const wide = () => window.innerWidth >= 1400;

    const drawer = document.createElement("aside");
    drawer.className = "drawer";
    drawer.id = "links-drawer";
    drawer.setAttribute("aria-label", "Links");
    let html = '<h2>Links <button class="drawer-close" type="button" aria-label="Close links">✕</button></h2>';
    let open = false;
    for (const item of LINKS) {
        if (item.group) {
            if (open) html += "</ul>";
            html += `<p class="drawer-group-label">${item.group}</p><ul class="link-list">`;
            open = true;
            continue;
        }
        const external = /^https?:/.test(item.href);
        html += `<li><a href="${item.href}"${item.accent ? ' class="ll-accent"' : ""}${external ? ' target="_blank" rel="noopener"' : ""}>` +
            `<span class="ll-label">${item.label}</span><span class="ll-desc">${item.desc}</span></a></li>`;
    }
    html += "</ul>";
    drawer.innerHTML = html;

    const backdrop = document.createElement("div");
    backdrop.className = "drawer-backdrop";
    document.body.append(drawer, backdrop);

    const toggles = document.querySelectorAll("[data-drawer-toggle]");
    function setOpen(state, remember) {
        root.classList.toggle("links-open", state);
        toggles.forEach(t => t.setAttribute("aria-expanded", String(state)));
        if (remember && wide()) {
            try { localStorage.setItem("rc-links", state ? "open" : "closed"); } catch (e) { /* storage unavailable */ }
        }
    }
    setOpen(root.classList.contains("links-open"), false);

    toggles.forEach(t => t.addEventListener("click", () => setOpen(!root.classList.contains("links-open"), true)));
    drawer.querySelector(".drawer-close").addEventListener("click", () => setOpen(false, true));
    backdrop.addEventListener("click", () => setOpen(false, false));
    document.addEventListener("keydown", e => {
        if (e.key === "Escape" && root.classList.contains("links-open") && !wide()) setOpen(false, false);
    });

    document.querySelectorAll("[data-year]").forEach(el => { el.textContent = new Date().getFullYear(); });
})();
