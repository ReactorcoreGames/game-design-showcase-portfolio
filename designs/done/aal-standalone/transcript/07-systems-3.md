# Standalone notebook transcript: Tutorial, database and scanning, debriefing, menus, profiles, options, game flow and SA gameplay

This chunk covers the front-end and support systems of the 2012-era design, in scan order: the VR tutorial plan (S37); the campaign flow diagram from Campaign button through Galaxy screen, Metagame screen, Briefing, Action and Debriefing (S38); the Database and scanning system, enemy designation codes and nicknames (S39, S41–S43); the Debriefing screen (S40); a menu-flow brainstorm with menu requirements and start-screen/profile sketches (S44); the full menu flowchart of the whole program (S45); the Database popup window and Briefing screen (S46); user profiles and what a profile holds, plus the "New?" helper popup (S47, S49); main menu layout concepts (S48); Start Game screens and the player character edit popup (S50); Options screens (S51); the campaign loop requirements (S52); the "Game Flow Logic" scene breakdown with a training build order and some engine study notes (S53); and a separate page on SA third-person gameplay, camera and environment scale (S54).

## S37 — Tutorial (`IMG_20191005_150542.jpg`)

Grid paper, blue pen, portrait, spiral binding on the left. Full page of text. Curly braces on the left group the bullet points into numbered stages 1, 2 and 3.

**Tutorial** (underlined heading)

The tutorial is a ~~linear campaign~~ *(above the strikethrough, inserted:)* "series of training lesson/challenges" / "sort of" *(an arrow from "sort of" points at the crossed words; "sort of campaign" appears to be the intended reading, with "series of training lesson/challenges" as an added alternative)* that all happens in a Virtual Reality (VR) simulation.

The purpose of the tutorial is:

Stage **1.** (brace around the first three bullets):
- What you are and your mission (Combat unit) — SLIDE SHOW
- Explain in detail (summary) about your combat unit, its composition and capabilities. Also introduce the user manual (which explains all functionality of all systems). Let the player know to refer to this manual (which is accessible at all times and pauses time.) whenever the player is uncertain what functionality is his/her unit having. — SLIDE SHOW
- Repeat the warning screen from pre-intro — SCREEN

Stage **2.** (brace):
- Do a quick set of scenarios where movement, aiming, shooting and basic commands are covered and done by the player — ACTION W/ GUIDANCE / NO DANGER, NO RUSH

Stage **3.** (brace):
- Finally, explain the game modes and remind the pre-intro screen and unit manual to the player. — SLIDE SHOW
  - (Do this ~~at the end of each action training~~) 2.5 *(the parenthetical is partly struck through; "2.5" written after it, i.e. this could become a stage 2.5)* *(interpretation)*

- Bonus: Present a choice for the impatient players
  1. Do the tutorial
  2. Play a predefined quick game match → let the player figure it out.

The second choice is also a refresher for old returning players. Before the match begins, the user manual is opened.

## S38 — Campaign flow: Campaign status, Galaxy, Metagame, Briefing, Action, Debriefing (`IMG_20191005_150609.jpg`)

Grid paper, blue pen, portrait, spiral binding on the right. A vertical flowchart of screen thumbnails down the left two-thirds of the page with labels and notes on the right; a small three-panel concept sketch at the top.

**Top concept sketch (top centre/right):** labelled "BIG BUTTON, MEATY" above a wide hatched bar (a large button). Below it, side by side: a "START" button, and under it an "M RESET" button; next to them a tall box "CURRENT STATUS" with a smaller strip "MISSION" at its bottom; to the right a box "WARNING!" with a triangle-and-exclamation-mark warning symbol, and a dashed empty box beneath it. A curved arrow runs from the "M RESET" button area to the dashed box under the warning *(interpretation: master reset is moved to a more isolated position near the warning)*. A note to the left, with a line to M RESET: "BIG CONFIRM REQUIRED (more isolated location".

**Flowchart, top to bottom:**

1. A box "CAMPAIGN" (a button) → arrow down to:
2. **Campaign status screen** (screen thumbnail): a big "START" button top-left, a large "STATUS" panel below it, a small "WARNING" box with the warning triangle at right with a small "M RESET" button under it; bottom bar with "HINT" at left, a centre button "C[?]MA[?]" *(unclear; possibly "C-MAP")*, and "D/E" *(possibly "B/E", back/exit)* at right. A line leads from this screen to the large notes on the right:
   - "Warning about permanent death and persistent world."
   - "Campaign Status"
   - "Continue Campaign button"
   - "Master Reset (Restart entire campaign, all campaign related stats and progress is erased (but not DB revealed entries, or maybe yes))"
   - To the left of this screen: "~~merge(?)~~ Nope" with a line from it down along the left side toward the Galaxy screen *(interpretation: considered merging the campaign status and Galaxy screens; decided no)*.
3. Double-headed arrow (↕) between the campaign status screen and:
4. **Galaxy Screen** (thumbnail with a spiral galaxy drawn behind the contents): a "PROFILE" tab at the top-right corner; a "NEXT CAMPAIGN" button, a "STATUS" panel; bottom bar with a "STATUS" button centre and a "B" button right, labelled "Back".
5. Double-headed arrow between Galaxy and Metagame screen, labelled to the right "OR PLAYER CREATE IF DEAD". A save marker (circle with a dot) sits on this arrow, labelled "Save", with the note on the left "Progress save (Automatic)".
6. **Metagame Screen (Local Space)** (star system...) — thumbnail of a map with circles (planets/suns), small rectangles (ships), two fuzzy shaded areas (nebulae), a sun-like shape in the centre; a "DATAB." tab at top right labelled "Database/Profile"; bottom bar "HINT", "STATUS", "B".
7. From the Metagame screen a line runs down the left side through a second save marker "Save" to an "X" mark at the left edge of the Briefing screen *(interpretation: the save happens on entering briefing)*.
8. Bottom row, left to right, connected by arrows:
   - **BRIEFING** — screen thumbnail with several panels (a list at left, a picture with dots, text blocks), a "PLAY" button and a "back" button at the bottom. A curved arrow loops from "back" round under PLAY *(interpretation: back returns to the metagame)*. An arrow → to:
   - **ACTION** — thumbnail sketch of the mecha and mothership in combat. An arrow → to:
   - **DEBRIEFING** — thumbnail with a header "VICTORY / FAIL!", a text panel at left, a list with bullets at right, and an "OK" button bottom right. Under the Action→Debriefing arrow: "Even if fail or die".
   - From Debriefing a long curved arrow sweeps back up to the Metagame screen.

## S39 — The Database + Scanning System (`IMG_20191005_150617.jpg`)

Grid paper, blue pen, portrait, text only.

**The Database + Scanning System** (underlined)

The Db is a static encyclopedia of knowledge about the game's content, which includes:

- The Player
- The Enemies
- The World
- The Statistics (Player Char *(above: "(INDV.)")* & Overall stats)

The player may access this knowledge at any time and doing so will pause the game. The "player" section is 100% revealed from the start.

The "world" and "enemies" sections are empty initially. During gameplay, the player may scan enemies. ~~Th~~ If successful, the entry for the scanned entity will appear in the Database. Any modules/equipment aboard the successfully scanned entity will also appear in seperate entries within the Db. If certain requirements are met (scan certain entities), the overall description for said faction will be revealed. The entries provide backstory and useful information about scanned entities. Ultimately, it does nothing and is purely optional, but would add a lot of depth into the game.

## S40 — Debriefing screen (`IMG_20191005_150740.jpg`)

Grid paper, blue pen, portrait, spiral on the right. Text list at top, two layout sketches at the bottom.

**Debriefing screen** (underlined)

This screen evaluates the outcome of a battle and gives useful information to the player.

- Player status (Condition, RVs) — (Display images of MS and ReWaR) — Data collected (DB entries uncovered?)
- Enemy status (Destroyed, Escaped, Damaged) / (By category)
- Statistics (Time elapsed, targets destroyed, targets identified)
- World Status (Is area destroyed after battle or not?)
- Compliment (Victory/Mission Successful message)
  - ~~+ Mission evaluation? Maybe not. Score numbers are bad.~~ *(the whole line is struck through, but its content reads as a rejection of scoring anyway)*
- *(a scribbled-out word)*
- Compliment image (Badass pose of player char) — X-COM STYLE — (Either blended fullscreen in the background - reduced opacity or a smaller window with maximum opacity)

**Layout sketches:**

- **Type 1** (bottom left): a screen with a header "WIN/LOSE"; a large left panel labelled "SUMMARY" and "DETAILS" with a faint sketch of the mecha posing drawn behind/inside it (the compliment image); a right column "Player" then "Enemy" with entries "01", "02" and lines; bottom-right buttons "RETRY" and "OK". A label points at the buttons: "— continue/back to menu", and an arrow from RETRY reads "only in quick and training".
- **Type 2** (right, slightly higher): header "WIN/LOSE"; a picture strip at the top of the left area showing the units *(the compliment image as a smaller window)*; below it a panel "SUMMARY / DETAILS"; a tall right column with "Player" entries at top (labelled "Player") and "01", "02" further down (labelled "Enemies"); two buttons bottom right (illegible, presumably RETRY and OK).

## S41 — Database: world entries, hierarchy, enemy designations (`IMG_20191005_150745.jpg`)

Grid paper, blue pen, portrait, text with a small tree diagram.

The world is much more simple. An entry for a world type and all its contents and hazards are revealed upon entering said respective world.

The Database is heavily categorized for the three parts "player", "enemies" and "world". The design supports infinite addons for both enemies and worlds.

**The rough hierarchy:** (tree diagram) A top box "The Database" with lines down to four boxes:

- **Player**: Overall; Mothership • Details; Robot • Details
- **Enemies**: Faction • Entity • Equipment
- **World**: ~~World~~ World Type 1 • Details
- **Stats**: Profile 1 stats; Overall stats

**Enemy Designations and Nicknames** (underlined)

Initially, when an entity is encountered the first time, it is "unknown". Upon destruction you get an incomplete entry that only contains an image and a designation code. This designation code is what you will ~~see~~ identify other entities of the same type in the future, instead of "unknown". It is in the following format:

`RS-1` — with brackets beneath: "RS" labelled "generic faction name", "1" labelled "nth of the type encountered".

This designation may be renamed through the Database at any time for any destroyed and/or scanned unit.

## S42 — Nicknames, world entries, savefile (`IMG_20191005_150805.jpg`)

Grid paper, blue pen, a half page (the lower part of the photo is the page edge). Text with one small sketch.

~~[scribbled word]~~ Besides a designation, the player also has an option to give a name (nickname) for the said type of enemy. This nickname will appear as a subtitle, under the designation code.

*(Sketch: a small angular enemy ship inside targeting corner brackets, with a label line to "RS-5" and beneath it "Bogey".)*

Forgot to mention. World types also recieve incomplete entries in Db if the player only passes near them. To get a complete entry, the player must actually enter them to gain the full information.

Designation and nicknames are saved ~~[?]~~ in the overall savefile.

## S43 — Scanning enemies (`IMG_20191005_150813.jpg`)

Grid paper, blue pen, portrait, text only.

**Scanning enemies** (underlined)

Depending on the controls, this might be automatic or a toggleable system. (scan mode)

Each enemy has a different scan integrity which determines how long must the player scan the target to get its full information.

The player may scan one entity at a time. ~~[?]~~ Attempting to scan another entity while another scan was already in progress, will cancel the old scan and begin the new one.

Scanning is simple; the player must only keep the larger, missile box-crosshair over the target to scan it. A scan is cumulative per enemy, so the player may try to scan it in short bursts instead of one single longer scan. If an enemy is destroyed before the scan is complete, the data will be lost.

If an enemy type that has already been scanned is loaded out with different equipment than the one that got scanned, the player may scan this enemy to gain the data of its equipment. Possibly at a faster rate than the original entity.

## S44 — Menu flow brainstorm, menu requirements, start screen sketches (`IMG_20191005_150825.jpg`)

Grid paper, blue pen, portrait, spiral on the right. Dense page: an outline-style menu flow at top-left with arrows, notes, a start-screen sketch at right, a title-screen sketch at lower right, a game-type screen sketch at bottom, and a requirements list at lower left.

Top: "right-click for descriptions (context-sensitive help popup) / r-click to close help too."

**Menu outline** (left half, with arrows):

- Pre-intro screen
- Intro
- Mainmenu
  - OPTIONS — a curved line to the note "(Player preferences)" / "Gameplay, Audio, Controls, Video, Misc (non gameplay preferences) (disable intro)"
  - EXIT
  - ABOUT/CREDITS
  - Campaign ↔ Character selection
  - Quick game ↔ Character selection
  - ~~Tutorial~~
  - VR Training ↔ Character selection, with "(?)"
- "Checkbox to disable these" with two arrows pointing at Pre-intro screen and Intro, and an arrow from Mainmenu back to that note.
- "Start game(?)" on the left with arrows to Campaign, Quick game and VR Training *(these three are grouped as the start-game options)*.
- **Character selection** has three vertical arrows down to a row: "Create/Edit/~~Delete~~" — the third arrow (to Delete) is crossed out with a big X.
- **Start screen AKA PROFILES** — arrows with "(?)" link it to Character selection and the Training group. Notes: "(similar to soldat start)" / "(If no chars, go to char creation) with possible assistance".
- A loop at the bottom left: a curved arrow from "VR Training" down to a circled group: "Briefing" — "Game IN"; "Gameplay"; "Debriefing" — "Game OUT", with arrows Briefing → Gameplay → Debriefing, and the circle's line looping back up.

**Start screen / profiles sketch** (right middle): a screen box with header "welcome" (labelled above "(normally green) be bright yellow if no prof." with an arrow to the NEW button); a profile list box with lines and a scrollbar (labelled at left "~~[scribbled]~~ profiles"); buttons "NEW" and "DEL" to the right of the list; a checkbox "☐ Intro" (labelled "Checkbox for Intro Sequence"); a "Start" button (labelled "Greyout if no profiles (green if yes)"); at bottom-left "R-CLICK 4 HELP" next to an "EXIT" button (labelled "Crimson"); and a circled "New?" bottom right, labelled with a list: "USER PROFILE 0. / INTRO 1. / TRAINING 2. / MAKE CHAR 3." *(digits partly scribbled; interpretation)*. An arrow runs from this screen down to the title screen sketch.

**Title / main menu sketch** (lower right): a screen headed "TITLE" with a "PROFILES" tab at top right; menu items "Campaign", "Quickgame", "OPTIONS", "EXIT" with a "?" and an arrow to "ABOUT" *(reading uncertain, "A[?]UT")* in the bottom right; a circled "New?" bottom left with a note "Hint guide [POP UP]" and a small list "1. Intro / 2. Training / 3. [?]". A note to the left, struck through with diagonal lines: "Ask for confirmation (optional, set in Misc) (default: off)" with a line toward EXIT.

**Game-type screen sketch** (bottom centre): a tall box with small tab buttons at its left top: "P" labelled "Player Chars" and "T" labelled "VR Training"; main area "Game Type"; a "B" button bottom right labelled "Back to MM". A line connects it to the title screen's menu.

**Menu requirements:** (lower left, underlined)
- Fast & clear
- Organized
- Easy to learn/understand
- Does not enforce the tutorial or intro

Bottom: "Note: Training provides "Trainer player char"."

## S45 — Menu: full program flowchart (`IMG_20191005_150837.jpg`)

Grid paper, blue pen, portrait, spiral on the left. A full-page flowchart of boxes and arrows. Heading "Menu" top-left.

**Start sequence (top row):**
- "START PROG." (inside a faint circle) → (arrow with a small square on it, labelled "PRE-INTRO SCREEN") → box "INTRO SLIDES" (a faint circle around the pre-intro/intro area, labelled "can be disabled") → box "PROFILES / Start screen" ("Start screen" partly hatched over; an arrow off its right side ends in hatching). Note to the right: "~~necessary?~~ Yeah / Purpose: User profiles".
- PROFILES ↕ (double arrow) "Main Menu".

**Exit:**
- An ellipse "Exit PROG." at left. Arrows into it: from PROFILES/Start screen labelled "EXIT"; from Main Menu labelled "EXIT"; a thick arrow labelled "ALT+F4 (any time) (confirm if [?])" *(last word unreadable)*; a line from the left border edge of the Start-game group (with an X-hatched segment); and a long line "EXIT" running up the left margin from the Pause Menu.
- A scribbled, heavily looped line from Exit PROG. area to Main Menu *(interpretation: a crossed-out or "return" path)*.

**Main Menu branches:**
- Main Menu ↔ "START GAME" (double arrow).
- Main Menu ↔ "OPTIONS" (double arrow). OPTIONS fans out to a list "TABS: VIDEO*, AUDIO*, GAME*, MISC*, CONTROLS*".
- OPTIONS ↔ "PLAYER CHAR EDIT/CREATE" (labelled above "(POPUP WINDOW) or not").
- A curved line labelled "via profile link" goes from Main Menu's right side down to "The Database".

**Start Game group:** START GAME splits into three tabs in a long horizontal frame: "(tab) CAMPAIGN" ↔ "(tab) QUICK" ↔ "(tab) TRAINING" (each drawn as a tab with arrow-ends, double arrows between them).
- TRAINING ↔ PLAYER CHAR EDIT/CREATE (double arrow).
- TRAINING ↔ The Database (double arrow, labelled "(via profile link)").
- TRAINING ↔ "SLIDE SHOW" (double arrow).

**Campaign branch (left column):**
- CAMPAIGN ↕ "Galaxy".
- Galaxy → "BRIEFING" small box labelled "first" → Local Space.
- Local Space → "DEBRIEF" small box labelled "last" → arrow back to Galaxy *(interpretation: first-campaign briefing on entering local space, final debrief returning to the galaxy)*.
- Galaxy ↕ "Local Space (metagame)".
- Local Space ↔ "Briefing" (main briefing box).
- An arrow from the left frame edge goes up to Exit PROG.

**Battle loop (centre):**
- QUICK ↕ Briefing (double arrow, long vertical).
- TRAINING ↕ Briefing (double arrow, diagonal).
- Briefing → "Action".
- Action ↔ "MAP/TACTICS" (double arrow).
- Action → "Debriefing".
- Debriefing → back up to Briefing via a line on the right, annotated with a circled note "Quick only" and "and training too" *(i.e. retry from debriefing goes back to briefing in quick and training modes)*.
- Debriefing → Local Space (metagame) (line going up the left).
- Action ↔ "PAUSE MENU" (double arrow).
- PAUSE MENU ↔ MAP/TACTICS (curved double arrow).
- PAUSE MENU ↔ The Database (long curved double arrow up the right side). A second double arrow from the Database goes down with an X crossing it *(interpretation: a struck direct link)*.
- PAUSE MENU note: "Ingame only thru Action".

**The Database** (right) with a wavy-edged list "Tabs: Player, Enemies, World, Stats".

**Bottom notes:**

Campaign → Continue
Campaign → New = Erase existing progress and stats ◎ [RESET]
Character can also reset (allow to change name)

## S46 — The Database popup; Briefing screen (`IMG_20191005_151048.jpg`)

Grid paper, blue pen, portrait, spiral on the right. Two UI sketches with notes, a hierarchy-structure doodle, and a text list at the bottom.

**The Database** (underlined)

Popup window (large, almost full screen ~90%)

**Sketch 1 (top left):** a large window. Top row of tab icons (small circle icons, a stick figure, a "55"-ish circled icon) and a "STATS" tab; label "TABS". A left column item list with bullet points (labelled "Itemlist"). Main area: a stick-figure image, two small boxes to its right, and text blocks. A "CLOSE" button at bottom right, labelled "CLOSE DB". Labels to the right with lines into the sketch:
- Code designation (changable)
- Nickname (changable)
- description w/ image
  - Summary
  - Details

**Sketch 2 (right):** a variant entry window: image box with an icon at top left, two short lines/boxes beside it (header), a large text area below, and two "CLOSE" buttons at bottom left and right.

**Itemlist / Hierarchy structure** (left): a bracketed list "A ~~~ / • B ~~~ / • B ~~~ / • • C ~~~ / • B ~~~ / • B ~~~ / A ~~~" showing nested levels (A > B > C).

**Briefing screen sketch (centre):** title "Briefing"; top-left a picture of a map with crossed lines and dots (labelled "generic image"); top-right text lines ("summary"); below, a large "details" text area; right column a list with bullets labelled "Unit listing and Status (Number of enemies is known always, but type might be unknown) Condition is shown too, if known"; bottom-right buttons "PLAY" and "B/E" labelled "play" and "back".

**Briefing/~~Debriefing~~** (underlined)
- Gives information prior battle ~~/ Evaluates outcome and situation~~ (By category)
- Possible information:
  - Mission objectives (What to do)
  - Location and environment (Hazards, RUs, Enviro-type)
  - Enemy amount and types (can be unknown if encountered in clouds)
  - Player Status (Condition & available RUs) (May be changed in previous battle)
  - Threat level (?)
  - Points of interest / Misc important info
  - Picture of location (General biome/enviro-type image)
- A note with a curved line linking the enemy and player status lines: "Shown in a hierarchy style listing with small icons and condition info if known."

## S47 — User Profiles (`IMG_20191005_151055.jpg`)

Grid paper, blue pen, portrait, text only.

**User Profiles:** (underlined)

A very big part of the game is persistent world and characters. As such, dying (Mothership is destroyed) will erase the character. This means its precious and relatively easy to fuck up. Even more so when a computer is shared by more than one person, even if for a brief moment (friend comes over).

Because of this fragility that the design inherently carries with, among other aspects and convinniences, there is a need for profiles. A user profile system. Nothing complicate, just individual saves and settings. Each profile holds individual game data, saves, preferences (control bindings), progress and statistics.

Basically a single person may have multiple profiles that progress differently or multiple people can play individual games with their own preferences, all without interfering with other profile.

There is an optional password that a user may *(inserted: "use to")* protect his profile, (with an ability to retrieve a lost password by telling it to send an email to a specified address), in case there is a need for such a measure.

## S48 — MM concepts (main menu layouts) (`IMG_20191005_151116.jpg`)

Grid paper, blue pen, portrait, spiral on the right. Several main menu (MM) layout sketches, numbered.

**MM concepts** (heading)

- **Concept A (top left):** a screen with "Profiles ☐ / [?]" *(tiny text, partly struck: "PG1 BCE"?)* at the top right; buttons "campaign" and "quickgame" side by side; below them "OPTIONS" and "EXIT"; "r-click 4 help" at bottom left; a circled "NEW?" at bottom centre.
- **Concept B (top right):** a screen with a vertical stack of buttons of decreasing size, each with a scale number beside it: "CAMPAIGN" 1.3, "QUICK" 1.1, "OPTIONS" 1.0, "EXIT" 1.0 *(last digit unclear)*. Note: "Larger button to signify importance and revelance".
- **Concept 2 (middle left):** a screen with "NEW" top left and "PROFILE" top right; a centred list "CAMPAIGN / QUICK / OPTIONS / ABOUT"; "Hint" bottom left; "B/E" button bottom right labelled "Back/Exit". Note from PROFILE: "Profile has a link to "The Database". (The available entries are tied to profiles anyway)".
- A small separate sketch (middle right): a box with "START GAME", "OPTIONS", ~~ABOUT~~ (crossed out with a scribble).
- **Concept 1 (lower left, two stacked screens):** upper: a screen with circled "NEW?" top left and "USER A ONLINE" top right; menu "START GAME / PROFILES / OPTIONS"; bottom "hint ~~NEW~~ ABOUT" and an "E/B" button. Lower: a profile select screen with circled "NEW?" and header "welcome"; a list box "USER A / USER B / USER C"; buttons "NEW" / "DEL" (labelled "grey, with yellow pulsing glow (if no profiles)"); "hint" bottom left; "ABOUT (or credits)"; an "EXIT" button labelled "EXIT - LOADED START / BACK - IF THRU MM". An arrow goes from the profile list up to the menu screen. Note at the bottom: "Each user is listed as a button to MM".
- **Concept 3 (lower right):** "tabs" — a tab row coloured by label: "Red: Campaign", "Yellow: Quick", "Green: Training", and a "Profile" tab at the right end; a large content area (labelled "CONTENT") and an "E/B" button bottom right. Arrows from Concept 1's menu point into it.

Bottom right: "Important: Consistent and streamlined"

## S49 — User profile data; "New?" popup (`IMG_20191005_151125.jpg`)

Grid paper, blue pen, portrait, spiral on the left. Text only.

The data a user profile hold is the following:
- Player Character (One per profile, name not modifiable) (As in, one at a time.)
- Campaign World (Each profile is fully individual)
- Database Progress (revealed entries, stats accumulated, log...)
- Control Bindings
- 1 Automatic progress save (plus 2 emergency saves)
- Profile name
- Profile password (optional)
- Profile password recovery address (optional, even with passw.)

**"New?" Popup** (underlined)
1. Create a profile (no link, profile is mandatory to continue.) — with an annotation line: "(If accessed thru MM, is greyed out)"
2. Create a character (This gives a link to "start game" with training tab to the char edit. Once leaving char edit, user will find himself at training)
3. Play Training
4. Customize options
5. Play quick or campaign (suggestion) (two links to respective targets)

Note on 2.: The link does not instantly transfer the user to target. Instead, it engages a guided autopilot (to show how it works)

## S50 — Start Game Screens; Player Char edit (`IMG_20191005_151154.jpg`)

Grid paper, blue pen, portrait, spiral on the right.

**Start Game Screens** (underlined)

**Overall Layout** — sketch: a screen with a "TABS" row at the top and a "PROFILE" tab top right (labelled "LINK TO DB."); two small stacked buttons at the top-left of the content area ("PLA[YER]" and a hatched one); bottom bar "Hint", "[PLAYER CHAR]", and an "E/B" button labelled "to MM". Under [PLAYER CHAR]: "[NONE]" — "pulsing glow if no char".

Tabs:
- Campaign
- Quick
- Training

**Targeting reticle sketch (right, in a wavy cloud outline):** a circled target (a round object) inside left and right bracket scales with tick marks; small tick marks above and below; on the right scale the numbers "5:3.00" and "H.3.04" *(unclear)*; a line from the top of the right bracket to the label "name target". Caption: "As UI targetting identifier elements". A line runs from this cloud down to the preview note below *(interpretation: the character preview should show the name in this targeting-label style)*.

**Player Char** (underlined) — "Name (perm.) (Grey if edit)"

Sketch "CHAR EDIT": a popup with rows labelled at left "Name", "nicks" (two rows), "color" (three colour swatches) and a "RAND" button under the colours; small icons beside the rows; a preview panel on the right showing the mecha and mothership; an "OK" button at the bottom with two labels: "CREATE (if none)" and "DONE (if char)".

Notes:
- [OPTIONAL] preview? (ReWaR/MS pose?) (Reflect color and name choices)
- New popup window over game screen

| IF NO CHAR | IF CHAR |
|---|---|
| - Enter name | + Name cannot change |
| - Give nickname (optional) • Mothership • ReWaR | + All others are editable |
| - Select Color(s) (default random color) | |
| - Seperate colors for each unit (?) | |

*(In "IF NO CHAR", "NO" is written above the line as an insertion; in "IF CHAR" a word before CHAR is scribbled out.)*

## S51 — Options Screens (`IMG_20191005_151200.jpg`)

Grid paper, blue pen, portrait.

**Options Screens** (underlined)

Sketch (top left), "overall layout": a screen with "tabs" across the top (several short tab dividers) and "PROFILE" top right; "Hint" bottom left; an "E/B" button bottom right labelled "Back to MM".

Tabs:
- Gameplay (maybe unnecessary)
- Video
- Audio
- Controls
- Misc (non-gameplay misc options)

**options (V, A, G, M)** — sketch: a column with checkboxes (checked, unchecked, checked) each followed by a wavy label, then two labelled sliders with handles.

**Options (controls)** — sketch: a two-column table "Action | key" with rows (wavy action names) bound to: A, D, W, S, SPACE, MOUSE1, MOUSE2. Under it two buttons "DEF" labelled "DEFAULT" and "E/B" labelled "Back".

Options are automatically saved when leaving an option menu (save options button optional) User is notified of this briefly, to make him understand how the system functions.

## S52 — Requirements: Campaign (`IMG_20191005_151344.jpg`)

Grid paper, blue pen, portrait; mostly empty page, cropped at the bottom.

**Requirements:** / **Campaign** (both underlined, top left)

A vertical flow at the right, with numbered brackets on its left:
- **0** [ Setup game/go (continue campaign) ↓
- **1** [ Briefing screen ↓
- **2** [ Launch ↓ Game ↓ End
- **3** [ Debriefing (allow retry if quick game)

A long curved arrow on the left loops from 3 (Debriefing) back up to 0 (Setup game/go).

## S53 — Game Flow Logic: scenes; training build order; engine notes (`IMG_20191005_151351.jpg`)

Grid paper, blue pen, portrait, spiral on the left.

**Game Flow Logic** (underlined). Beneath it, a struck-out first attempt: "Campaign", "Quick", "Training" each with an arrow down, the whole area crossed out with many diagonal lines.

**Scenes** (underlined)
1. ( Pre-intro / Intro ) — Start/Intro
2. ( Profile Select / Main Menu / About ) — Menu (Main)
3. ( Brief/Debrief (Q/C) / Galaxy/Local (Metagame) ) — Game Prep
4. ( Action / Tactics / Pause ) — Action
X. ( Options / Database / Char edit / Brief/Debrief (Q/T) / Alt+F4 confirm ) — Standalone Components

*(Here "Standalone Components" seems to mean scenes/popups that stand on their own, not the game title.)* *(interpretation)*

**Numbered list (right side)**, with lines from items 1 and 2 to scenes 1 and 2, and a big curved bracket around items 3–7 *(interpretation: an implementation/build order)*:
1. Intro
2. Main menu
3. Action (Bare bones basics)
4. Quick Game system + page enabled
5. Brief + Debrief enabled
6. Pause menu
7. *(blank)*

**Lower right, separate notes:**

(unlocker alternative)
Lockhunter.com

A bracketed list, all struck through *(interpretation: Unity documentation topics read and ticked off)*:
- ~~Forward Rend Path Dem[o]~~
- ~~Optimizing gfx perf.~~
- ~~Execution Order~~
- ~~Rendering Paths~~
- ~~Player Settings~~
- ~~Settings Managers~~
- ~~Render Settings~~
- ~~Scripting Concepts~~

Bottom, small: "DNB Eveson (dj)" *(a music note, unrelated to the design)*.

## S54 — SA gameplay (`IMG_20191005_152459.jpg`)

Grid paper, blue pen, portrait, spiral on the right. Text with one small sketch. *(Different from the rest of the chunk: here "SA" is a single piloted mech with hover legs, no mothership mentioned.)*

**SA gameplay:** (underlined)

- Dynamic TPS view during piloting (Camera moves as the player moves.)
- OPTIONAL: FPS view while mech startup/shutdown
  - \* This could be just the opening/~~intro~~ cinematic.
- Ground movement of SA very similar to M-44 hammerhead from Mass Effect 2. Hover legs. *(a word above "legs" is struck)*
- Enviroments very large, details semilow (optimization)
  - \* Game will function on a large scale
  - \* Player has extreme mobility and speed at his disposal so the enviroments must feel limitless or atleast extremely large to allow the player to use the SA to its maximum potential and "feel" the speed. The SA is capable of very long sustained flight so the world should not have an upper limit.
- Camera is fairly far from player, and ~~[?]~~ depending on speed ~~[?]~~ it moves accordingly, back and forth.
  - *(Sketch: the mech seen from behind, a humanoid robot with bulky shoulders and legs, labelled "(back side)".)*
- Vapor trails are a must. (not in space though!)

## Glossary additions

- **VR Training / Training**: the tutorial as a series of lessons/challenges in a VR simulation; also a game mode tab next to Campaign and Quick. Provides a "Trainer player char".
- **Pre-intro screen**: a warning screen before the intro (repeated in the tutorial; content implied as the permadeath/persistent world warning). Can be disabled by checkbox.
- **User manual / unit manual**: in-game manual explaining all unit functionality, accessible at all times, pauses time.
- **Master Reset (M RESET)**: restarts the entire campaign, erasing campaign stats and progress (DB entries maybe kept). Needs a big confirm.
- **Galaxy screen**: screen above Local Space, with "Next Campaign" and status; campaign = one local star system.
- **Local Space**: the metagame screen (star system map).
- **MAP/TACTICS**: the in-action tactics map, reachable from Action and the Pause Menu.
- **Scan integrity**: per-enemy value determining how long a scan takes; scans are cumulative, lost if the target dies first.
- **Missile box-crosshair**: the larger crosshair used for scanning (and presumably missile lock).
- **Designation code**: `RS-1` format, faction code + nth type encountered; renamable. **Nickname**: optional player-given subtitle under the code (example "RS-5 / Bogey").
- **MM**: Main Menu. **B/E, E/B**: Back/Exit button. **DEF**: Default button (controls).
- **"New?" popup**: a circled helper button giving a guided 5-step start (profile, character, training, options, quick/campaign), with links that run a "guided autopilot".
- **Profile**: per-user save container (one character, campaign world, DB progress, bindings, 1 auto save + 2 emergency saves, name, optional password + recovery address).
- **Q/C, Q/T**: Quick/Campaign, Quick/Training (on S53).
- **Standalone Components**: S53 scene group for popups usable from anywhere (options, database, char edit, brief/debrief for quick/training, Alt+F4 confirm).
- **TPS / FPS**: third-person / first-person view.
- **M-44 Hammerhead**: Mass Effect 2 hover tank, the reference for SA ground movement.
- **X-COM style**: reference for the debriefing compliment image.
- **Soldat**: game referenced as the model for the start/profile screen.

## Open questions

- S37: is "sort of campaign" or "series of training lesson/challenges" the intended wording for the tutorial? What is the "2.5" next to the struck-out "(Do this at the end of each action training)"?
- S38: what is the bottom-centre button on the Campaign status screen ("C[?]MA[?]", maybe "C-MAP")? Was "merge? Nope" about merging the campaign status and Galaxy screens?
- S38/S45: what is the exact role of the Galaxy screen vs. a campaign: is each "campaign" one star system, with "Next Campaign" moving to the next system?
- S45: what does "confirm if [?]" after ALT+F4 say? What is the scribbled looping line between Exit PROG. and Main Menu, and the crossed-out second arrow from the Database?
- S44: the circled "New?" list ("USER PROFILE 0. / INTRO 1. / TRAINING 2. / MAKE CHAR 3.") differs in order from S49's 5-step list; which was final?
- S48: the tiny text under "Profiles" in Concept A (looks like "PG1 BCE") is unreadable.
- S50: what are the numbers "5:3.00" and "H.3.04" on the targeting reticle sketch?
- S53: is the numbered list 1–7 a build/implementation order for a first playable? Are the struck-out items Unity manual topics?
- S54: which version of the design does this page belong to? It treats SA as a single hover-legged piloted mech with a startup/shutdown cockpit view, unlike the mothership+ReWaR tandem elsewhere.
