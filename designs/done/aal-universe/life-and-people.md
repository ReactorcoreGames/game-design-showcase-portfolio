# AAL Universe: the player, people and minds

Who the player is, what happens on death, the group you play as, souls and psychic powers, and how NPCs think. Sources: `Planet Warfare.txt`, the 2011 docs, `PerformanceSimulations.rtf`, `WorldUniverseMetagame.rtf`, `PW_NVC Based AI System Musing.docx`, `PSRC Human Redux Plan.txt` and the clothing notes (read for their gameplay rules only), scans W1-29, W1-34, W2-37, PS-21.

## The player character

- **A regular yet malleable person** (`Planet Warfare.txt`): two arms with opposable thumbs that can use tools, interact with objects, pilot vehicles, operate machines, wear clothes and gadgets, carry and wield things, eat, make noise and speak. Equipment changes what you can do: scuba gear lets you dive, a jetpack lets you fly, climbing hooks let you cling to walls. Arms let you work machines and vehicles, which take you anywhere.
- **Controls**: WASD to move, mouse for menus, aiming and arms, Q to toggle inventory, E for a context-sensitive interaction, plus a few hotkeys; nothing that can't fit a console controller.
- **Start**: you are dropped anywhere in an already-alive universe as "someone's grown up child", with a generated backstory for that body.
- **No grind** after a start or a death: if a military spaceport with nuclear-armed ships is nearby, you can steal one at once; if all you have is primitives with swords, you tech up first.

## Two modes

- **Solo persona** (`Planet Warfare.txt`): you are one human who lives, dies and reincarnates after a time skip to finish what was started. You can gather a team that fights beside you, but you control only yourself.
- **Group of people**: switch freely to anyone in your group at any time. While one of them lives, a death passes you straight to another, with no time skip. If the last one dies, you reincarnate elsewhere with a new group after a longer, harsher time skip.
- **Earlier forms**: the 2011 "consensus of your faction" (direct control of any unit plus RTS orders over a finite population), and the 2014 **group mind** (`PerformanceSimulations.rtf`): control a group with broad RTS commands or take over any individual at will.

## Death, family and time skips

- As long as your group or family survives, death respawns you in its **sanctuary**. If it goes extinct, you are reborn elsewhere in the universe into a new family after a long time skip, during which factions and forces may change, retake or "remystify" places you knew.
- Your past lives' deeds remain part of the universe's history; you can go back and find the places you changed, aged by the time skip: overgrown and rusted if abandoned, an enemy's hive if conquered, a wasteland if eradicated. "Returning to an old location may evoke a sense of deja vu."
- You may reject your original family and found your own group with allies, friends and partners.

## Souls, the Astral Plane and psychic powers (`WorldUniverseMetagame.rtf`)

- The **Astral Plane** is an invisible, neutral background layer of the material world where souls and the astral collective reside. Matter can't enter it, but beings can connect to it to use psychic powers, and astral tension can burst into the world as strange anomalies.
- Anything that becomes able to form memories (feel, perceive, experience) gets an **Astral Being**, its "Me", whether biological or a robot. On confirmed death the Me disperses back into the universal pool. Resurrection is possible, with amnesia risk growing with time dead and damage repaired.
- **Reincarnation is half true**: the soul returns to the pool and may be born into a new being, but memories stay in the old body's atoms; only a body made partly from your previous one, plus psychic effort, can recover them. "Memory... is the underlying building block of existence" and the universe exists to create memories.
- **Psychic power** depends on the body's materials (rock and metal connect poorly; "astral conductive" organics connect well), size, and **connectivity** to the plane. Powers are an invisible **Astral Influence field** projected from the user (a square barrier, a tentacle), which ignores matter but tires the user faster with size and distance. Acting on something behind a wall forces a costly sensing power. Above 90% connectivity you sense everything everywhere, with severe overload risks (fainting, insanity, death). Every sentient being has an **Astral Barrier** protecting its memories; mind control, body swapping, memory transfer and cloning require breaking or sharing it. "There is no such thing as wireless psychic powers."
- W1-29 lists psychic aptitude by brain size, souls, reincarnation and spirit dynamics as topics; W2-37 notes that only characters capable of supporting sentience carry an Astral Being, beside "Memory" and "Memory Aquizition".
- **AAL lore** (`AAL Lore, Universe Basics.txt`) keeps this: no magic, rare and costly psychic abilities through the astral realm, souls resting there between lives. By the Exploration era Homo Mugen have digital immortality (timeline), which fits respawning.

## NPC minds: the NVC-based AI

From `PW_NVC Based AI System Musing.docx`:

- **Everything anyone does is to meet a need**, and everything anyone says is "please" or "thank you". Needs (after Manfred Max-Neef): subsistence; safety; freedom/power/participation; growth/learning/creation/variety; relaxation/fun; meaning/identity/belonging; equality/respect/understanding; love/giving/care. Each species has its own set and its own ways of expressing feelings.
- **Feelings** express urgency, from a smile or mild irritation to joy, anger or fear, shaped by context, memory and hope.
- **Strategies** aren't defined in advance; only vague "kickstarters" (for safety: "knowing the character can relax without care and harm"), and the AI works out the situation. Strategies range from worst (unmeets everything) to best (meets several needs with no downside). Domination structures favour the bad end, "power with people" the good end.
- **Memory**: simple records of sources and individuals (dangerous, safe, indifferent, unknown), areas and routes, and past strategies with success rates. Capacity is limited and old low-priority memories are overwritten, so NPCs forget. AIs guess causes from their senses and are sometimes wrong, on purpose. Memories spread by talking, terminals, posters, TV, radio and schools, so communities get smarter than individuals.
- **Paradigms**: beings with a soul (humans) can override need priorities for sustainability, equality and similar higher causes (sharing the loaf instead of eating it all). The deer-island story explains why animals lack this.
- **Delay**: AI decides on intervals rather than every frame, for performance and to make countless tireless AIs fair against one human. Under chaos the delay grows: the NPC is awestruck.
- **Dormancy**: under 1 km NPCs are fully loaded, 1–10 km simplified, beyond that abstract, far away shut down except for meta effects. **Pods** (a bed, an apartment, 1–10 person homes) meet some needs inside and let NPCs go dormant; destroy a pod and its occupants pop out, so pods can't be clown cars.
- **The bigger aim**: build the whole game (NPCs, UI, tutorials, community spaces) on nonviolent communication, so players absorb it; domination culture appears only as cautionary tales.

## Bodies and appearance (gameplay-relevant notes)

- **Human stages** (PS-21): baby 0–1 and infant 1–5 as single objects, child 5–15 as 6 pieces or a 4-piece version with floating Rayman hands, adult 15+ as a ragdoll of up to 14 pieces. Body types: thin, average, fat, skinny, muscular, dry, pustulous, mutated.
- **PSRC humans** can be a physics ragdoll, pre-rendered frames, an IK paper doll, or a mix. The foreword now accepts a single box or circle collider for every character.
- **Human Redux Plan** (2021, mostly art): adult ragdolls are 6–14 pieces where hands and feet don't collide; a simplified **6-limb** body (head/torso and each arm and leg as one piece) must also be supported. Clothes are flattened into the limb as data, so a clothed limb stays one collider; protection applies **per limb** (an exposed arm takes the hazard, which may spread to the body). Dropped clothes collapse into a generic folded pile. Backpacks, tools and guns are separate physics objects attached externally, with a soft carry limit (past it, chaos priority rises) and a hard one. The game centres on humans and human systems, so a creature with paws may not be able to work vehicles or tools. Physics hair, capes and chains are ruled out for this game.
- **Clothing categories** (`Cloth practicality PSRC.txt`): 1 vanity, fashion and indoor wear (optional in a dry 22 °C room); 2 basic everyday wear for -0 to +50 °C; 3 heavy protective gear for extremes; 4 specialised tactical gear for narrow hazards. Fashion may decorate categories 2–4 but never undermine their function (no feather flaps on a fire suit). Body hair is a limb overlay (density, coverage, pattern, colour, structure, material); free-flowing hair isn't supported by the universe sim.

## Open questions

- Solo versus group as two modes, or one model (the group, with solo as a group of one).
- How big a group is, and whether its members come from a finite population (2011) or are recruited.
- Whether psychic powers are playable, and how to show invisible astral fields (the musing says it needs "a specialized representation").
