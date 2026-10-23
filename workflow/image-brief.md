# Image Brief

How to write the image prompts for a page (the five Klein images and the SDXL minis), and how they turn into files on the site. The prompts are written when the page is written. Generation happens later, locally, in batches, through the Batch AI Image Generator (BAIG) at `C:\ClaudeWorkspace\AI image gen batch program`.

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

**Rerolling on a paid model.** When Klein misses an image that needs stronger prompt adherence (complex, structured scenes), it can be rerolled on Nano Banana 2 Lite ($34 per 1000, prepaid credit, only with Reactorcore's go-ahead): `python tools/images.py gen <slug> --model nano-banana-2-lite --only 1,9`. Mark those images in the spec with `"model": "nano-banana-2-lite"` so `finish` takes them from that model's output. Nano Banana follows negations, so its prompts can end with "No text, lettering or signatures anywhere." Its 16:9 output is 1344×768, which `finish` scales to about 1270×726.

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
python tools/images.py collage <slug> ...             # numbered contact sheet into wip/shots/
python tools/images.py gen <slug> --only 1,4          # reroll some images (after rewording them)
python tools/images.py finish <slug> --only 5         # finish only some (a rewrite's new story image)
```

Raw BAIG output lands in `_work/<slug>/raw-<model>/` (gitignored). `finish` scales every image to the pixel area of 1280×720 (so 2:3 comes out at 784×1176), saves it as progressive JPEG at quality 82 under the exact name the page expects, and makes the 640×360 nexus thumbnail from the vignette. Look over the results before committing. To redo one bad image, use BAIG's `regenerate` on that prompt file, or edit the prompt and run `gen` again: a changed prompt gets a new file name, and `finish` takes the newest.

## Duds, flagged outputs and retries

Look at every result before committing: `collage` makes a numbered sheet of a spec's finished images in `wip/shots/` (gitignored), so a whole batch can be judged at once. Reroll a dud by rewording its prompt and running `gen --only <n>`. The prompt text is part of the `--only` run's file name, so a reworded retry is a fresh BAIG batch; an unchanged one is the same batch and BAIG won't rerun its finished or failed jobs (use `cli.py retry-failed` for that). `gen` carries on past a failed ratio group and lists what to rerun at the end. Give up on an image after two rerolls and use what's best.

Klein's provider sometimes rejects an image with "Your output has been flagged" (HTTP 400, code 3030). It's a check on the generated picture, not the prompt, so it repeats with similar wording, and it costs nothing. Klein has no filter setting. Change what the picture shows: in the Graviton pilot, a "tall sleek bipedal mecha" was flagged three times and passed as "a huge armored hovering war machine with no legs", and a "heap of wrecked tanks with smoke rising" box art passed once the wreck pile was gone. In batch 1, a hero punching an apartment block was flagged, and a reworded punch into an empty warehouse was flagged again; Nano Banana drew it first time.

Cartoon gore gets flagged too. In batch 3, a comic mosh pit with blood spurts and a flying severed arm was flagged on three of five images; two passed once the blood and loose limbs were taken out of the prompt (the page text can still describe them), and the third went to Nano Banana. Don't put gore in Klein prompts at all.

Cartoon people being hurt get flagged even without blood. On Jetboot Resistance (TF2 preset), guards blasted or knocked through the air were flagged twice and passed only as two startled guards stumbling, and a fighter with a rifle flying over an exploding base passed once as the title but was flagged three times as the 2:3 box art, even with the rifle and explosion taken out (it went to Nano Banana). Keep people and blasts apart: a hero beside an explosion can pass, people inside one don't.

Klein ignores small anatomical details it finds unusual. A "cyclops with one single large eye" came out with two eyes in the title shot while the box art, a close portrait, got it right. Check faces closely, and when a detail defines the character, frame it close or move that image to Nano Banana.

Heroic figures get flagged even when nothing is violent, probably by the output's nudity check. In batch 10 two box arts with a lone standing hero were flagged, along with every other image of the same hero: a "chunky humanoid robot in glossy white armor" (a smooth glossy body reads as skin) passed only as "a boxy, clearly mechanical robot with a square visor head and bolted armor plates", and a "ridiculously muscular hero in a torn bodysuit" was flagged on every wording and preset tried and went to Nano Banana. Describe figures as fully clothed or plainly mechanical from the first prompt, and keep "torn", "muscular" and "glossy" off people.

Nano Banana doesn't always obey its no-text line: on a 2:3 box art it painted a made-up title in big letters. Manga presets (Murata) add speech-bubble lettering on their own. Small lettering on plain sky can be removed with OpenCV inpainting (`cv2.inpaint`, masking only the strokes) on the finished JPG; note it in the manifest, because a later `finish` overwrites the fix.

Make every alt text describe what was actually generated, not what the prompt asked for.

## Mini images (SDXL)

Project pages also get up to ten small mood images beside their lore, layer and feature text (placement rules are in `workflow/page-brief.md`). They have their own free-form spec, `image-prompts/<slug>-mini.json`:

```json
{
  "slug": "<slug>-mini",
  "out": "site/projects/mini/<prefix>",
  "size": [320, 240],
  "quality": 70,
  "preset": "02 Photo - E - Cinematic",
  "lead": "Cinematic sci-fi film still, <the page's mood and palette in a few words>. ",
  "images": [
    {"n": 1, "name": "golden-age", "ratio": "3:2", "prompt": "<the section's opening line>"}
  ]
}
```

- `lead` goes in front of every prompt, because SDXL only reads about 300 characters and never sees the style suffix. Keep it to the page's mood and two or three palette words. A strong colour word tints the whole set (Graviton's "violet glow" turned all ten magenta), which is fine as long as the set stays coherent. A subject noun in the lead does the same to the content: Bunkership's "brutalist warships carved from moon rock" put a warship in all ten frames, even the hangar and the energy orb. Name the subject in the lead only if every mini should show it. Preset names must match BAIG's exactly (`02 Photo - S - Tilt Shift`, not "Tilt-shift"); `check` catches a wrong one.
- The prompt is the section's opening line, lightly trimmed of names SDXL can't know. Don't chase accuracy; it's flavor, and the thumbnail size hides flaws.
- `size` and `quality` make `finish` centre-crop to 4:3 and save at exactly 320×240, about 7 to 10 KB each.
- Run: `gen <slug>-mini --model sdxl --max 999`, then `finish <slug>-mini --model sdxl`, then `collage <slug>-mini`. SDXL is slow (several minutes for ten), so run it in the background while doing other work. Reroll duds (an image whose mood fights the section) at most twice. SDXL sometimes blocks one image of a set (`blocked=1` in the batch line), and `finish` then stops at that image without saving the ones after it: reword the blocked prompt, run `gen ... --only <n>` (a plain rerun reuses the old batch and changes nothing), and run `finish` again.

## SDXL fallback

When the Klein allowance is spent and pages are still waiting, SDXL (free, unlimited) can provide placeholders so no page ships without images. These are expected to be replaced with Klein images later.

- SDXL reads only about **300 characters**, and the style suffix comes last, so it's never seen. Use `--lead` to put a short style phrase at the **front** of every prompt.
- SDXL does badly at anime, comic, pixel, voxel, isometric and low-poly. Use **photography or watercolor** looks only, both in `--lead` and with `--preset`.

```
python tools/images.py gen <slug> --model sdxl --preset "02 Photo - E - Cinematic" --lead "Cinematic photograph. " --max 999
python tools/images.py finish <slug> --model sdxl
```

Mark SDXL-imaged projects in the manifest so they get a Klein pass later.
