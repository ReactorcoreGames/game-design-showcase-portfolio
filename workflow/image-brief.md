# Image Brief

How to write the five image prompts for a page, and how they turn into files on the site. The prompts are written when the page is written. Generation happens later, locally, in batches, through the Batch AI Image Generator (BAIG) at `C:\ClaudeWorkspace\AI image gen batch program`.

## Budget and model

- **Model:** FLUX.2 klein 4B (`klein4b`), **Standard** tier: 1536×864 at 16:9, 1024×1536 at 2:3.
- **Budget:** about 75 free Klein images a day, but **plan for 70**. Using the full allowance also locks out the free SDXL lane, which is the fallback. That's 14 projects a day at five images each. `tools/images.py gen` refuses a batch over 70.
- Each project's prompts must be locked before generating. The goal is one run per project with no retries, so the prompts carry the quality.

## The spec file

One file per project at `image-prompts/<slug>.json`:

```json
{
  "slug": "punk-orphans",
  "prefix": "punk-orphans",
  "preset": "08 Games - C&C Allies (RTS/Isometric 2D)",
  "style": "Palette of scorched rust orange, gunmetal and toxic lime accents.",
  "images": [
    {"n": 1, "role": "title",    "ratio": "16:9", "prompt": "..."},
    {"n": 2, "role": "vignette", "ratio": "16:9", "prompt": "..."},
    {"n": 3, "role": "feature",  "ratio": "16:9", "prompt": "..."},
    {"n": 4, "role": "boxart",   "ratio": "2:3",  "prompt": "..."},
    {"n": 5, "role": "story",    "ratio": "16:9", "prompt": "..."}
  ]
}
```

- `prefix` defaults to `slug`. Set it only for published pages, whose image prefixes differ (see the manifest).
- `preset` is the exact name of a BAIG style preset. Its text is read live from BAIG's `config.json` and appended to every prompt.
- `style` is optional extra style text appended after the preset. Use it for the color scheme, taken from the page's CSS palette, plus anything the preset lacks.
- **Length:** prompt + preset + style must stay within **1800 characters** per image. Klein's encoder silently drops text past roughly 2000, and the style is the part that gets lost because it comes last. `tools/images.py check` enforces the limit. A 400–900 character prompt is usually right.

**Section specs.** Pages that aren't project showcases (the AAL universe page) use a free-form spec instead: add `"out": "site/aal/images"` and give each image a kebab-case `name` instead of a `role`. Any number of images is allowed, numbered from 1. `finish` saves them as `<out>/<NN>-<name>.jpg` and makes no thumbnail. `image-prompts/aal.json` is the example.

## Choosing a style preset

BAIG has ~110 presets (`python tools/images.py check` shows the one in use; the full list is in BAIG's `config.json` → `style_presets`). Families include `01 Main` (digital painting, comic, 3D high/low poly, Frazetta oil, 90s anime), `02 Photo` (cinematic, gritty, dystopian, noir, tilt-shift, long exposure…), `03 Style` (sketch, watercolor, retro, vector, pop art, pixel), `04 Special` (glitch, splash, ghostly), `06 Cool`, `08 Games` (named game art styles: Homeworld, Super Metroid, C&C, Battletech, Einhander, Daemon X Machina…) and `09 Artist` (Nihei, Frazetta-era cover painters, Murata…).

Pick the preset that best expresses **this** game. **Spread presets across projects** so the portfolio doesn't become one look repeated 60 times. Before choosing, check which presets other specs in `image-prompts/` already use. One preset per project keeps its five images visually coherent.

## Writing the prompts

- **Structure:** camera framing, angle and lens first; then the main subject with its key details; then secondary details and surroundings. The style comes from the preset, so don't repeat it in the prompt.
- **One clear focal point** per image.
- **No text in images.** No signs, labels, titles or logos, and no quoted words.
- **No names the model can't know.** Describe instead: not "Super Mario" but "a cartoony plumber in red and blue overalls". The same goes for invented names from the design. The model doesn't know what a "Halberd Suit" is, so describe what one looks like.
- **Avoid words with a stronger default meaning than the one intended.** "Drone" produces a quadcopter even when the design means an unmanned submarine robot. Say what the thing *looks* like.
- **Recurring subjects are described identically every time.** If the hero is "a teal abyssal frogman guardian in glowing armor", write that full phrase in every prompt it appears in. A shortened "the guardian" becomes a generic human knight.
- **Match the page.** Each image depicts what its quote and section claim: the vignette shows the gameplay feel described, the feature image shows the feature it sits beside, the story image shows the world from the Lore section.
- **Box art is portrait (2:3).** Compose for a tall cover: a strong central subject, with room at the top where a title would go (but no title).

## Running it (local session only)

```
python tools/images.py check                          # every spec valid, total count
python tools/images.py gen <slug> <slug> ... --dry-run
python tools/images.py gen <slug> <slug> ...          # spends the daily allowance
python tools/images.py finish <slug> <slug> ...       # resize + JPEG + thumbnail into site/
```

Raw BAIG output lands in `_work/<slug>/raw-<model>/` (gitignored). `finish` scales every image to the pixel area of 1280×720 (so 2:3 comes out at 784×1176), saves it as progressive JPEG at quality 82 under the exact name the page expects, and makes the 640×360 nexus thumbnail from the vignette. Look over the results before committing. To redo one bad image, use BAIG's `regenerate` on that prompt file, or edit the prompt and run `gen` again: a changed prompt gets a new file name, and `finish` takes the newest.

## SDXL fallback

When the Klein allowance is spent and pages are still waiting, SDXL (free, unlimited) can provide placeholders so no page ships without images. These are expected to be replaced with Klein images later.

- SDXL reads only about **300 characters**, and the style suffix comes last, so it's never seen. Use `--lead` to put a short style phrase at the **front** of every prompt.
- SDXL does badly at anime, comic, pixel, voxel, isometric and low-poly. Use **photography or watercolor** looks only, both in `--lead` and with `--preset`.

```
python tools/images.py gen <slug> --model sdxl --preset "02 Photo - E - Cinematic" --lead "Cinematic photograph. " --max 999
python tools/images.py finish <slug> --model sdxl
```

Mark SDXL-imaged projects in the manifest so they get a Klein pass later.
