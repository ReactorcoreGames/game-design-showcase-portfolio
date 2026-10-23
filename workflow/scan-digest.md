# Digesting scan-based designs

Some projects (RoomSpace, Planet Warfare, Shape Smasher) have their design mostly in scanned notebook pages, with only a short condensed text doc beside them. Reading the scans costs roughly 4k tokens per large image, so a 100+ scan project is around 400k tokens: a lot, but a one-time cost if the scans are turned into text once and never read again. This doc is how to do that. Run it as its own session before the project's batch session, not inside one.

## The rule

Scans are read once. The output is a set of markdown digest files, and every later session (page brief, batch session) reads those instead of the scans.

## Steps

1. **Read the condensed docs first.** The text files in the project folder are small and give the vocabulary (acronyms, names of systems). That solves most of the "this page only makes sense if you read the earlier ones" problem before any scan is opened.
2. **Triage (for large sets, roughly 30+ scans).** Write a throwaway script that tiles the scans into contact sheets of about 12 thumbnails each and read those. Big handwritten titles are usually readable at that size. Mark each scan as core design, sidetrack, duplicate, or title-only, and read only the core ones at full size. Small sets skip this and read everything.
3. **Optional downscale.** Shrinking scans to about 1500 px on the long side cuts cost by roughly 40%. Test on the two densest pages first and confirm the smallest text survives.
4. **Transcribe in order, in chunks.** For large sets, fresh subagents each take 10 to 15 scans in order and write up both the text and the diagrams (described in words), with a running glossary handed from chunk to chunk. This keeps image tokens out of the main conversation. Small sets can be read directly.
5. **Write the digest as several files, not one.** In a folder per project:
   - `index.md`: summary of the whole design, glossary, list of the other files, and a scan-by-scan source table (which scan fed which file, which scans are title-only or unfinished).
   - One file per major part of the design, for example the core gameplay, an editor, the metagame/structure/wrapper. Pick the split that fits the project.
   - Mark clearly what is Reactorcore's notes versus Claude's interpretation of an unclear drawing, and list open questions rather than inventing answers.
6. **Save in two places.** The digest folder goes into `designs/standby/<project>/` (move the project's existing summary doc in there too) and a copy goes next to the scans in the project's own folder outside the repo. Update `designs/MANIFEST.md` so the project's design-file column points at the folder.

`designs/` is public in the repo, so the digest becomes public too. That matches how the other designs are treated.

## Budget notes

Reactorcore's usage runs on a 5-hour rolling window. A 100+ scan project likely spans two or three windows, so for those, do it in chunks across sessions: write each chunk's transcript to the digest folder as it's finished so nothing is lost when a window runs out, and note in `index.md` which scans are done.

## Status

| Project | Scans | Digest |
|---|---|---|
| Shape Smasher | 16 | done, `designs/standby/shapesmasher/` (2026-10-22) |
| RoomSpace | 108 (`C:\08 Projects\Project_RoomSpace\Scan_RoomSpace`) | done, `designs/standby/roomspace/` (2026-10-22) |
| Planet Warfare | ? | not started |
