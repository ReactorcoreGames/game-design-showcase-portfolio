# Cookbook: Text Over Images

Recipes for keeping titles and quotes legible on top of busy or bright images. Choose per page and per placement, matched to the page's look. A neon page wants a glow, a gritty one a hard outline, a soft painterly one a glass island. The original side-by-side demo is `workflow/legacy/text-visibility-demo.html`; open it in a browser to compare them.

Rule for quotes on images: separate the text from the image, but never dim or darken the image itself.

| # | Recipe | Best for | Core CSS |
|---|---|---|---|
| 1 | Full overlay card | Quotes on any image; the safest default | `background: rgba(0,0,0,.7); color:#fff; border-radius:4px` |
| 2 | Highlighter fill (MS Word style) | Short punchy lines, subtitles | `display:inline; background: rgba(0,0,0,.8); padding:.1em .4em; box-decoration-break: clone` |
| 3 | Hard outline via shadows | Big titles on bright, busy art | 8× `text-shadow: ±2px ±2px 0 #000` (all directions) |
| 4 | Layered soft shadows | Titles where an outline looks too harsh | `text-shadow: 0 0 3px #000, 0 0 6px #000, 0 0 9px #000, 2px 2px 0 #000` |
| 5 | CSS text stroke | Heavy display fonts only (thin fonts break up) | `-webkit-text-stroke: 2px #000` + `paint-order: stroke fill` |
| 6 | Box-shadow halo container | Quotes that should feel embedded, not boxed | `background: rgba(0,0,0,.3); box-shadow: 0 0 20px rgba(0,0,0,.8)` |
| 7 | Gradient card | Quote cards that fade into the image | `background: linear-gradient(135deg, rgba(0,0,0,.8), rgba(0,0,0,.4))` |
| 8 | Framed card | Retro, military or UI-styled pages | `border: 3px solid <accent>; background: rgba(0,0,0,.5)` |
| 9 | Glow | Neon, sci-fi or magic themes; doubles as the animated title effect | `text-shadow: 0 0 5px <c>, 0 0 10px <c>, 0 0 15px <c>, 0 0 20px <c>` |
| 10 | Inverted chip | Light, clean or toy-like pages | `background:#fff; color:#111; box-shadow: 0 0 0 2px #000` |
| 11 | Glass island | Painterly or atmospheric images | `background: rgba(255,255,255,.15); backdrop-filter: blur(10px); border:1px solid rgba(255,255,255,.2); text-shadow: 1px 1px 2px rgba(0,0,0,.8)` |
| 12 | Offset double layer | Comic, pop-art or arcade titles | `::before { content: attr(data-text); color:#000; transform: translate(2px,2px); z-index:-1 }` |

Notes:

- Tint the dark recipes (1, 2, 6, 7, 8) with the page's own background hue rather than pure black. It looks deliberate rather than generic.
- Combining two recipes is often best for hero titles. A glow (9) for the animated effect plus layered shadows (4) underneath keeps legibility even at the dimmest frame of the animation.
- `backdrop-filter` (11) is supported in all current browsers, but it costs GPU time. Use it on one or two elements per page, not on every card.
