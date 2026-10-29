# Digesting scan-based designs

Some projects (RoomSpace, Planet Warfare, Shape Smasher, TopVerse) have their design mostly in scanned notebook pages, with only a short condensed text doc beside them. Reading the scans costs roughly 4k tokens per large image, so a 100+ scan project is around 400k tokens: a lot, but a one-time cost if the scans are turned into text once and never read again. This doc is how to do that. Run it as its own session before the project's batch session, not inside one.

## The rule

Scans are read once. The output is a set of markdown digest files, and every later session (page brief, batch session) reads those instead of the scans.

## Steps

1. **Read the condensed docs first.** The text files in the project folder are small and give the vocabulary (acronyms, names of systems). That solves most of the "this page only makes sense if you read the earlier ones" problem before any scan is opened.
2. **Triage (for large sets, roughly 30+ scans).** Write a throwaway script that tiles the scans into contact sheets of about 12 thumbnails each and read those. Big handwritten titles are usually readable at that size. Mark each scan as core design, sidetrack, duplicate, or title-only, and read only the core ones at full size. Small sets skip this and read everything.
3. **Downscale.** Shrinking scans to about 1500 px on the long side cuts cost by roughly 40%. Do it by default for large sets; test on the two densest pages first and confirm the smallest text survives.
4. **Transcribe in order, in chunks.** For large sets, subagents each take 10 to 15 scans in order and write up both the text and the diagrams (described in words), with a running glossary handed from chunk to chunk. This keeps image tokens out of the main conversation. Small sets can be read directly. The rules for those subagents, because the AAL Standalone digest (2026-10-29) burned a whole usage window by breaking all of them:
   - **Sonnet, always.** Pass `model: "sonnet"` on every Agent call. Transcribing handwriting is grunt work and Sonnet reads it well. Haiku is fine for purely mechanical jobs (contact sheets, file lists, renaming). Never Opus for a subagent; the main session keeps the synthesis (the digest files), which is the part that needs judgement.
   - **At most two at a time.** Image reading is the expensive part, and seven agents in parallel spend a window in minutes. Run chunks one or two at a time and check each before starting the next.
   - **One pass per chunk.** No second "verification" pass and no re-reading of a chunk that already wrote its file. If a page came out doubtful, list it in the chunk's open questions instead. Never start a replacement agent for a chunk that is still running.
   - **Write to the final path.** Each agent writes its chunk straight into `designs/standby/<project>/transcript/NN-<name>.md`, glossary and open questions included, so a window running out loses nothing and no assembly step is needed.
   - **Brief once.** Write the shared brief (how to transcribe, output format, glossary so far) to a file and point each agent at it, instead of repeating it in every prompt.
5. **Write the digest as several files, not one.** In a folder per project:
   - `index.md`: summary of the whole design, glossary, list of the other files, and a scan-by-scan source table (which scan fed which file, which scans are title-only or unfinished).
   - One file per major part of the design, for example the core gameplay, an editor, the metagame/structure/wrapper. Pick the split that fits the project.
   - Mark clearly what is Reactorcore's notes versus Claude's interpretation of an unclear drawing, and list open questions rather than inventing answers.
6. **Save in two places.** The digest folder goes into `designs/standby/<project>/` (move the project's existing summary doc in there too) and a copy goes next to the scans in the project's own folder outside the repo. Update `designs/MANIFEST.md` so the project's design-file column points at the folder.

`designs/` is public in the repo, so the digest becomes public too. That matches how the other designs are treated.

## Budget notes

Reactorcore is on the Claude Pro plan, with usage on a 5-hour rolling window. A 100+ scan project likely spans two or three windows, so for those, do it in chunks across sessions: write each chunk's transcript to the digest folder as it's finished so nothing is lost when a window runs out, and note in `index.md` which scans are done. Plan the stopping points up front (for example: session 1 triage and the first three chunks, session 2 the rest, session 3 the digest files and the folder cleanup) and stop at one rather than pushing into the limit.

## Status

| Project | Scans | Digest |
|---|---|---|
| Shape Smasher | 16 | done, `designs/standby/shapesmasher/` (2026-10-22) |
| RoomSpace | 108 (`C:\08 Projects\Project_RoomSpace\Scan_RoomSpace`) | done, `designs/standby/roomspace/` (2026-10-22) |
| TopVerse | 49 (`C:\08 Projects\Project_Topverse\2 !scans`) | done, `designs/standby/topverse/` (2026-10-23) |
| AAL Universe: Perpetual Boundless Freedom (formerly Planet Warfare) | 132 (`C:\08 Projects\Project_Planet Warfare\1 FotoScan_Planet Warfare Misc`, `2 FotoScan_PSRC - needed an art system for PW`; 36 PSRC production pages listed by title only) | done, `designs/done/aal-universe/` (2026-10-24; page built 2026-10-26), plus `cohesive-design.md` |
| AAL Standalone | 127 (`C:\08 Projects\Project_Standalone\`, now sorted into version folders V0–V3 + spinoffs, scans renamed by code) plus 16 RTFs and the 2013 Unity demo | done, `designs/standby/aal-standalone/` (2026-10-29) |
