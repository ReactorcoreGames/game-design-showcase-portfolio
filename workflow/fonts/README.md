# Font samples

A ready-made look at the display fonts in `assets/fonts/` that are safe to self-host, so a page can pick its fonts without re-rendering samples every session.

- `licences.txt`: every font file in `assets/fonts/` with its embedded licence (name IDs 13/14) and `fsType`, one per line as `class|fsType|file|licence|url`. The class column marks `OFL` and `CC0` fonts; the rest are blank (freeware, CC BY-SA/ND, unknown), which the page brief says to avoid.
- `samples-1.png`, `samples-2.png`: the CC0 and OFL candidates rendered with the same test line (it includes `&`, digits and `Qg`, the glyphs that most often surprise).
- `samples-0-in-use.png`: fonts already taken by a page. Which page uses which is in the `FONTS` list in `tools/brand.py`; check it before choosing, so no two pages share a pair.

If fonts are added to `assets/fonts/`, rerender the samples and the table and replace these files.

Gotchas found so far: Zero Hour's `&` looks like an 8; the Zeroes family draws capital C like a lowercase one, so "City" reads "city"; Zector is a hairline face that vanishes over a busy or pale image, so keep it out of subtitles; the pixel fonts (6809 Chargen, Jersey 10, Micro5) need about 1–1.25rem to read as kickers. Motion Control's WOFF2 fails to decode in Edge and Chrome (the page falls back to Segoe UI), so it's unusable as built; Hydrogen Whiskey draws A without a crossbar (Λ), which stays legible in titles. Check `document.fonts` statuses in headless Edge rather than trusting a screenshot.
