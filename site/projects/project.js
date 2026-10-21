/* Shared behaviour for the showcase pages in site/projects/ (load with defer, after project.css).

   - Fork as Markdown: any [data-fork-md] button downloads the page's design as a .md file, a
     1:1 text copy of the page (no images, no styling) that someone can hand to an AI or keep as
     the start of their own design document. Elements marked data-md="skip" are left out.
   - Box art sizing: the send-off's box art is made exactly as tall as the card beside it.

   Markdown rules: h2/h3 become headings, paragraphs keep bold, italics and links, lists stay
   lists, tables stay tables, quotes on images become blockquotes, the step chains become
   numbered lists and the nested structure diagram becomes a nested list. */

(function () {
    "use strict";

    var NOTE = "Forked copy of an original design by https://reactorcoregames.github.io, rename this project under a new name to continue working on it.";

    /* ---------- Fork as Markdown ---------- */

    function squash(s) { return s.replace(/\s+/g, " "); }

    // Inline content: text with **bold**, *italics*, links and `keys`.
    function inline(node) {
        var out = "";
        node.childNodes.forEach(function (n) {
            if (n.nodeType === 3) { out += squash(n.textContent); return; }
            if (n.nodeType !== 1 || skipped(n)) return;
            var tag = n.tagName.toLowerCase(), inner = inline(n);
            if (!inner.trim()) return;
            if (tag === "strong" || tag === "b") out += wrap(inner, "**");
            else if (tag === "em" || tag === "i") out += wrap(inner, "*");
            else if (tag === "kbd" || tag === "code") out += "`" + inner.trim() + "`";
            else if (tag === "a") out += "[" + inner.trim() + "](" + n.href + ")";
            else if (tag === "cite") out += " (" + inner.trim() + ")";
            else if (tag === "br") out += " ";
            else out += inner;
        });
        return out;
    }

    // Keep the spaces outside the markers, so "**bold** text" never becomes "**bold **text".
    function wrap(s, mark) {
        var m = s.match(/^(\s*)([\s\S]*?)(\s*)$/);
        return m[1] + mark + m[2] + mark + m[3];
    }

    function skipped(el) {
        return el.dataset.md === "skip" || el.tagName === "IMG" || el.tagName === "SCRIPT" ||
            el.classList.contains("icon") || el.classList.contains("btn") || el.hidden;
    }

    function line(s) { return squash(s).trim(); }

    function table(el) {
        var rows = [];
        el.querySelectorAll("tr").forEach(function (tr) {
            rows.push(Array.prototype.map.call(tr.children, function (c) { return line(inline(c)).replace(/\|/g, "\\|"); }));
        });
        if (!rows.length) return "";
        var head = el.tHead ? rows.shift() : rows[0].map(function () { return " "; });
        return ["| " + head.join(" | ") + " |", "|" + head.map(function () { return " --- "; }).join("|") + "|"]
            .concat(rows.map(function (r) { return "| " + r.join(" | ") + " |"; })).join("\n");
    }

    function chain(el) {
        return Array.prototype.map.call(el.children, function (li, i) {
            var copy = li.cloneNode(true), b = copy.querySelector("b"), title = b ? line(b.textContent) : "";
            if (b) b.remove();
            var rest = line(inline(copy));
            return (i + 1) + ". **" + title + "**" + (rest ? ": " + rest : "");
        }).join("\n");
    }

    function nest(el, depth) {
        var out = [];
        Array.prototype.forEach.call(el.children, function (box) {
            if (box.tagName !== "DIV") return;
            var name = box.querySelector(":scope > span"), note = box.querySelector(":scope > small");
            out.push("  ".repeat(depth) + "- **" + (name ? line(name.textContent) : "") + "**" + (note ? ": " + line(note.textContent) : ""));
            var inner = nest(box, depth + 1);
            if (inner) out.push(inner);
        });
        return out.join("\n");
    }

    function list(el, ordered) {
        return Array.prototype.map.call(el.children, function (li, i) {
            return (ordered ? (i + 1) + ". " : "- ") + line(inline(li));
        }).join("\n");
    }

    function keys(el) {
        var out = [];
        el.querySelectorAll(".p-keygroup").forEach(function (g) {
            var h = g.querySelector("h3");
            if (h) out.push("**" + line(h.textContent) + "**");
            g.querySelectorAll("dl > div").forEach(function (row) {
                out.push("- `" + line(row.querySelector("dt").textContent) + "`: " + line(inline(row.querySelector("dd"))));
            });
            out.push("");
        });
        return out.join("\n").trim();
    }

    // Block content: walks an element and returns a list of Markdown blocks.
    function blocks(el) {
        var out = [];
        Array.prototype.forEach.call(el.children, function (n) {
            if (skipped(n)) return;
            var tag = n.tagName.toLowerCase(), cls = n.classList, text;
            if (tag === "h1" || tag === "h2") out.push("## " + line(n.textContent));
            else if (tag === "h3") out.push("### " + line(n.textContent));
            else if (tag === "p" && cls.contains("p-kicker")) out.push("*" + line(n.textContent) + "*");
            else if (tag === "p") { text = line(inline(n)); if (text) out.push(text); }
            else if (tag === "figure") {
                var cap = n.querySelector("figcaption");
                if (cap) out.push("> " + line(inline(cap)));
            }
            else if (tag === "table") out.push(table(n));
            else if (cls.contains("p-chain")) out.push(chain(n));
            else if (cls.contains("p-nest")) out.push(nest(n, 0));
            else if (cls.contains("p-keys")) out.push(keys(n));
            else if (tag === "ul") out.push(list(n, false));
            else if (tag === "ol" && !cls.contains("p-stack")) out.push(list(n, true));
            else out = out.concat(blocks(n));   // sections, cards, stacks, wrappers
        });
        return out;
    }

    function toMarkdown() {
        var name = document.querySelector(".p-name"), sub = document.querySelector(".p-sub");
        var title = line(name ? name.textContent : document.title) + (sub ? ": " + line(sub.textContent) : "");
        var body = blocks(document.querySelector("main"));
        return ["*" + NOTE + "*", "# " + title].concat(body).join("\n\n").replace(/\n{3,}/g, "\n\n") + "\n";
    }

    function download() {
        var file = (location.pathname.split("/").pop() || "design.html").replace(/\.html?$/i, "") + "-design.md";
        var url = URL.createObjectURL(new Blob([toMarkdown()], { type: "text/markdown;charset=utf-8" }));
        var a = document.createElement("a");
        a.href = url; a.download = file;
        document.body.appendChild(a); a.click(); a.remove();
        setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    }

    document.querySelectorAll("[data-fork-md]").forEach(function (btn) {
        btn.hidden = false;
        btn.addEventListener("click", download);
    });

    /* ---------- Box art as tall as its card ---------- */

    // The art's width decides the card's width, and so its height, so settle it in a few passes.
    // On phones the art never takes more than half the row.
    var sendoff = document.querySelector(".p-sendoff");
    if (sendoff) {
        var card = sendoff.querySelector(".p-card"), art = sendoff.querySelector("img");
        var fit = function () {
            sendoff.style.removeProperty("--box-w");
            if (!card || !art) return;
            var gap = parseFloat(getComputedStyle(sendoff).columnGap) || 0;
            var max = (sendoff.clientWidth - gap) / 2, w = max;
            for (var i = 0; i < 4; i++) {
                sendoff.style.setProperty("--box-w", w + "px");
                w = Math.min(max, card.offsetHeight * 2 / 3);
            }
            sendoff.style.setProperty("--box-w", w + "px");
        };
        fit();
        window.addEventListener("resize", fit);
        if (document.fonts) document.fonts.ready.then(fit);
    }
})();
