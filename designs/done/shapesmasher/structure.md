# Shape Smasher: structure, metagame and wrapper

Back to [index.md](index.md).

## Metagame and campaigns

- **Campaigns** are a bunch of similarly themed levels grouped into a cohesive pack, made by both players and artists (SS3). The results screen tracks current campaign progress. Text notes: a random name generator for campaigns, and suggesting levels as bundles in a campaign.
- **Two kinds of progression** (SS16): player stats for infinite overarching progression, plus finite campaign progression. Text notes suggest tracking meta progress from local logs.
- **Artist stats** (SS16): how many people smashed your art and liked/disliked it.
- **Publishing order** (SS10): the server decides which levels players will play in campaigns.
- Random level fetch never serves a level the player has already played (SS3).

## Player log (SS3, SS12)

A log of all played levels, one row per level with its name/ID and a tag:
- Smash entries are red, spare entries are green.
- Bad entries are deleted and blocked for you.
- You can revisit and replay any level.
- One rating (feeling) per level.

## Feeling feedback (SS12)

The rating screen asks "How did you feel about this art by User####?" with a 3×3 emoji grid:

| | | |
|---|---|---|
| happy, satisfied (thumbs up) | neutral, useless | unsatisfied, violated (thumbs down) |
| surprise, shock, amazed | sad | angry, furious |
| loving, excited | "wut", confused, WTF | really makes you think |

The top row is "category 1" (basic like/neutral/dislike), the bottom two rows "category 2" (feelings). An open question: allow more than one feeling per rating? The text notes settle on like/neutral/dislike as the minimum, and **no written text feedback** on levels at all. The summary doc's list is happy, sad, shocked, confused, bored, angry.

## Server and storage (SS7)

- **Player storage** (PC, phone internal, SD card): old played levels, new fresh levels, screenshots, a personal copy of the account log.
- **Server storage**: published and updated levels, the list of all authors/IDs, stats and data of levels (status, monetization, users), ad circus / monetization / support info, sources, status, progress.
- **Level browsers**: "Browse individual levels from server/cloud" (SS8) and "Level browser (local, old/new)" (SS11) exist only as **titles**. The to-do list (SS9) separates an offline browser for old/local levels from an online server portal / "cloud hub" for new levels.
- Text notes: direct link sharing to levels, an offline mode for procgen, downloaded and self-made levels, data-plan cost awareness, an explicit content warning, "online interactions not rated", reporting and server-side deletion for bad manners (SS10: "reporting process and response protocols").

## Business model (SS1)

- Free / shareware: try to find a way not to impede creativity.
- An **ad circus** section.
- Season pass or microtransactions for access to new content (making content takes effort and time, so set expectations accordingly).
- A buyable **supporter badge** that says "I support free games with this business model".
- If total earnings exceed a target (10M net sales), make all content free for everyone, thank those who paid, and make them notice their effort gave a chance to play to those who couldn't afford it.
- The summary doc adds ideas for artists: gifts and donations, promoting their own sites, commissions for custom levels, premium levels in a monthly pass. The Simplified note drops all of this for an itch.io-style third-party paid product linked from the app.

## Ad circus (SS14)

A screen of ad tiles drawn as closed theatre curtains, "New ads every 6 hours!", with an "About the ad circus" section, a support data bar (e.g. 42/100) and a support disclaimer/notice button.

- Open a tile to view the ad content. Close at any time, no obligation to watch fully. Viewing for at least 5 seconds counts as a valid view and registers toward support progress. The viewer has a link, a "more info" button if applicable, a 5-second timer and a close button.
- The info popup covers: new features in development, data about server costs and data limits, expenses and funding goals, impact and communication.
- Rules: keep it out of the way and optional (not in the main menu, only as a submenu in Options or Extras). Communicate clearly what it is, why it's there and what it gives both sides. Keep it fun and casual, maybe gently poking fun at others in passing. Link to future developments, saying any support goes toward those aims.
- Entry types: (a) standardized ads from an ad network, (b) custom-made ads: image, text (title, description), links, video. No interactive content: a link can lead to some, but not inside the circus.
- Text notes: only urge people to watch if they want to for themselves. The Simplified note adds a way to break and destroy the ads in-game.

## Controls ergonomics (SS13, SS9)

- A comfortable one-hand thumb zone covers the lower part of the screen; the side strips need two-hand tap control (full area). Only tap, swipe, drag and hold are available.
- Grips sketched: one-hand thumb, one hand holding plus the other tapping, vertical two-hand "Game Boy grip", horizontal two-hand "GBA grip", and a supported one-thumb grip using two hands. The thumb's reach is drawn as a quarter-circle.
- A first-time option asks which hand the user plays with, which mirrors the menu, controls and interface positions.

## Credits page (SS15)

Scrollable, categorized, easy to read and browse. Links and images allowed. Useful, not celebratory: promote those who contributed in a concrete way, endorsing them with credits. Descriptions for entries. Easy exit at any time. Possibly collapsible tabs.

## Wrapper and production (text notes)

- Menu flow: start, exit, options, info, credits. A game tutorial and a level-creation tutorial.
- Floppy Heroes stock music optionally; destruction sound effects.
- A construction plan from MVP to final state; an initial prototype plan; a performance stress test (object count).

## Open to-dos (SS9, SS10)

Never designed in the notebook: the level browser (offline), level procgen heuristics, the random campaign metagame screen flow, the server level portal / cloud hub, the spawn/templates/multiselect panels, the reporting protocols, and tutorials/encouragement for level makers.
