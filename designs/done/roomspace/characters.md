# RoomSpace: characters, controls and AI

The ragdoll body, how it moves and is controlled, how it holds things, how it gets hurt and heals, what it wears, and how NPCs think. Mostly from notebook 1 (scans 175–201). Numbers in brackets are scan numbers; the full wording is in `transcript/`. Notes marked *(interpretation)* are Claude's reading; sections headed **Proposal** are Claude's suggestions for gaps Reactorcore left open, not Reactorcore's design.

## The body

Every character is a physics ragdoll built from **limb types attached to a core** (185). The core has a prebuilt structure, monitors the status of every limb attached to it, and is the hub for repairs, healing and armor.

Limb types (180):

| Limb type | Examples | Role |
|---|---|---|
| **Core** (spine) | torso | Propulsion; back stash for stored items (size limit set by the core) |
| **Sensor Unit / AI Unit** | head, brain | Awareness; weak point; emergency manipulator (mouth); faces show AI state |
| **Auxiliary limbs** | legs, arms, tails | Mass, balance, reach, disposable damage sponge, passive offense. Feet can be built from a weaponized surface, active while dash-boosting |
| **Manipulator** | hands, claws, connectors | Grab, drop, use, rip, throw, active offense and defence |
| **Mounted item** | built-in gun or tool | Acts like a manipulator with reduced utility; cannot be dropped |
| **Vehicle interface** | console, port, saddle, nerve bond, membrane | Lets a character transfer control to another body as its pilot |

The same core + limbs + manipulator structure covers non-humans: worms, walkers, spider-like creatures (185 sketch).

**Head = mind.** A character with a head has **active AI** (thinks, targets, has emotions and needs, can go dormant, can generate power). Without a head it has **passive AI**: it repeats a pattern, cannot target, has no off switch, "jellyfish" (185).

**Limb status.** Each limb tracks its own HP, force limit, joint strength, alive/dead/paralyzed status and status effects (fire, acid, electricity) and reports to the core (185). The core can apply global effects such as paralysis or putting clothing on. A limb at **0 HP disconnects** (decapitation = joint disconnect) and at **−20 HP gibs**, so both kill and overkill exist. 0 HP on the core does not eject the limbs unless specified.

**Limb angle constraints** are defined per character (177). A limb pushed out of range rotates freely until it is back in range. Vehicles disable leg and arm constraints while in the cockpit; armor and clothes may change the ranges.

**Body sizes.** Human 1×2 m; the biggest character is 3×3 m (219). Room-size tables also list a "Longbig wielder" class in a 5×5 box (218), and an unpacked character holding long items can span about 10 m (223). The 3×3 m limit is the **packed** size used for doors (see `rooms.md`). Because the art is pixel art, human clothing assumes one body size (200), yet bigger and denser characters win dash fights (201): size differences come from non-human types and density, not scaled humans *(interpretation)*.

**Non-human characters** (180): animals (mouse up to elephant), robots (emitters, turrets, humanoids, mechs), mutants/cyborgs/monsters, ghosts/ethereals/spirits (single sprites that can't collide, spectate only) and immaterial beings (energy, EM fields, exotic matter; these can interact). Each has a **performance score**: about 2 for tiny critters, 6 for dogs/cats, 17 for horses/cows. Bigger creatures mean fewer entities per room; "prominence matters too".

**Non-conforming corrupt characters** (262): giants, worms, "weirdoes" that don't fit the packed form and so cannot travel room to room or use doors. Finding the centre point of irregular characters is listed as an open problem.

## Movement

**Gravity drive** (176). Primary movement applies directional force (WASD, 8 directions) to the torso/core. The limbs flop along behind. Gravity varies by room, but every living or powered thing can resist it and fly omnidirectionally, "like fish in an aquarium". The torso also rotates freely; RMB rotates it toward the cursor, and it has a preset aim bias, which matters when there are no hands.

**Secondary movement** comes from the manipulators: pointing hands or held items toward the cursor applies force and rotation, which also moves the body through momentum (176).

**Dash / Run, "Reckless Mode"** (175, 180, 201). A boost then acceleration, with a cooldown (stamina was considered). Dashing weaponizes the whole body with CKP (see `combat-and-items.md`). Boosting off terrain: hold Dash while pressed against a wall and an exponential acceleration multiplier charges up; when contact is lost, the multiplied acceleration fires in the opposite direction (175). Jumping in gravity rooms uses the same "dash toward terrain" charge (180). Dash appears to be bound to Shift (180).

**Grounded ragdolls** (180). In rooms with gravity, an idle character lies on the floor. Hold up to stand. Reversed: hold down to slump, tap once to crouch, tap twice for full ragdoll. As long as a limb or the core touches terrain, the core provides locomotion, so dragging a slumped ragdoll along the floor is a normal way to move ("lol").

**Mirror Turn** (186). A button flips the character to face the other way. The torso flips instantly toward the cursor; the limbs keep floating where they are, then travel back to their sockets over time that depends on size, mass and agility. Reactorcore revised whether limbs flip at the start ("maybe only at the end? Yeah this is better"). Everything stays usable during the turn, and a turn can be cancelled mid-turn. The point is to simulate the delay of a real body turning; cumbersome characters turn slower.

## Controls

Mouse + keyboard (175):

- **Mouse move**: cursor. **LMB**: pick up, use, grab, apply force (rip, crush). **RMB**: aim, orient, reach; rotate the torso; add swing speed to throws. **Wheel**: zoom.
- **WASD**: directional force on the core.
- **1 Let go** (tap to drop, tap + RMB to toss harmlessly, hold to charge a throw; called "B" on scan 178). **2 Dash/Run**. **3 Opposite aim**: pull hands in opposite directions (hold; 45° spread for a mild tear). **4 Flip items** (90° tap, 180° double tap, 270°; always clockwise). **5 Menu/Pause**. **6 Switch gear** (stash held items, bring out reserves; could become a Cortex Command style radial menu). **7 Limb selection** (hold to activate the closest hand; or a selection mode where the limb nearest the cursor highlights and LMB toggles it). **8 Mirror flip**. **9 Disable manipulator** (toggle). **10 Hand tandem/solo** toggle (all hands on one item, or each independent).
- Later notes add **R** reload/cycle and **T** drop/toss/throw (205), and the radial item-switch menu (209, in `combat-and-items.md`).

**Multi-handed characters** (177, marked "FUTURE ADDITION, not for initial release"): hands are laid out MechWarrior 4 style into groups. Keys 1–6 select a group, Shift+1–6 assigns; single-fire, link-fire, group-fire and alpha strike as advanced modes. Two-handed grips: pressing pulls hands and item to the centre, the item turns, hands return to their handles; with more than two hands, each goes to its nearest handle.

**Clamps** (262): angle −90° to 90°, "other clamps" 1–9, projectile speed 5–50. No context is given; probably parameter ranges for items *(interpretation)*.

Camera controls are in `rooms.md` (Camera).

## Holding things

**Grabbing** (179). Any operational manipulator can grab almost anything, pick up and equip usable items, and operate context-sensitive props, as long as the hand is empty.

**Slipperiness** (179). Hands and objects each have a slip (friction) value. On a force scale of 0–1000: below 500 the grip is 100% sturdy; between 500 and 800 it gradually fails; above 800 it is lost. Checked every tick.

**Ripping** (179): pulling with opposite hands, or pulling away while holding on. Tension builds, then kinetic damage applies each tick past a density-based threshold. Damage focuses on joints as impulse stress, mainly to dislocate limbs and connections.

**Crushing** (179): press/hold LMB. Raises grip strength but can damage weak items. Gradual pressure; impulse stress damage past a minimum. Weaker than ripping.

**Letting go** (178). Everything except mounted weapons can be dropped or thrown: tap to stop holding (one hand or all, via the limb selector); tap while swinging with RMB to toss harmlessly; **hold to charge a throw**, which imbues the item with Charged Kinetic Pressure. Throw damage depends on item mass/density, charge time (0–100%), hand strength, travel time and air friction (none in vacuum), and the combined launch velocity.

**Storing** (189). Characters store items at the core, behind the body. Stored items have collisions off and are unhittable unless they are long enough to poke out from behind the core. Item mass is added to the core, so carrying more makes the character slower. Size and mass limits apply. On death all items are released, and lots of dropped items form piles to sift through. Three storing schemes were listed without a choice:

1. Two items per hand (one held, one on the back).
2. A browsable inventory.
3. Cortex Command style cycling, previous/next through a first-in-last-out stack, with a "free hands" button.

A stapled note adds **three loadout sets** cycled with one button (1 → 2 → 3) (189), and the later radial menu (209) shows numbered sets of two hand slots each, where a two-handed item fills both slots of a set. That is the most developed version.

**Emergency head** (194, 199). When all hands are lost, the head becomes a "hand": a small mouth collider at the front of the head grabs things. Limits: can't store or switch, doesn't auto-snap items (it holds them as it picked them up), can't throw (only drop, or "spit out"), can flip/rotate/mirror, can crush and bite. LMB grab, LMB use/consume, RMB bite. It switches off as soon as one hand is back. This keeps a handless character in the fight and lets it heal back to full.

## Health and healing

**Healing items** (196). Repair kits, healthpacks, food and consumables give a number of HP to the core, which applies it to the limbs by the item's rule: heal all limbs (including lost ones), heal existing limbs only, or heal one limb (a specific type, all limbs of a type, or the next harmed or missing limb by a priority list such as core → head → arms → hands → legs → feet). How the HP is split was left open: 20 HP to every limb, or 20 HP shared across all limbs. Restored limbs pop back with a particle burst.

**Cannibal healing** (199). A head can grab and eat severed limbs or dead cores; heal amount = the HP-to-gib the eaten part had left.

**Core food reserve** (199). Food eaten (by hand or mouth) goes into a reserve in the core that regenerates damage over time at a limited rate. Regen heals all limbs equally; a lost limb needs 10 accumulated HP before it regrows, and comes back at 1 HP.

**Self-damage** (197). Items can hurt their user with recoil (a force kick or speed burst that throws the arm or the whole character) or by subtracting HP, using the same framework as healing items.

## Clothing and armor

**Clothing packages** (200). Clothing is an item. Using it moves the package to the torso, where the core registers it and dresses the matching body sectors; any clothing already worn comes back to the hand as a package to toss or re-equip. Humans have **4 sectors**: head, torso/arms/hands, legs, feet (first drafted as 5). Full suits cover all 4. Each piece is made for one character type; human clothing is the common case.

**Enhancements from armor/clothes** (200): core mobility (acceleration, force, top speed), regen rate and efficiency, armor (density, HP, status resistance, joint strength), rotation speed, gravity resistance, air friction mitigation, slipperiness, brittleness mitigation, damage multiplier. Clothes may also change limb angle ranges (177).

**Two ways to build armor** (200), not decided:

- **Sprite swap**: uses the limb's own collider; an if-statement runs armor logic before the limb's damage calculation. Cheap, easy armor penetration.
- **Attachment**: its own collider, HP and stats, sits on top and takes collision priority. Costs performance, risks ripping glitches; only benefit is crazier custom armor shapes.

Open item: "cheap cloth? (scarf, cape, coat)" (257).

## AI

**Emotions** (181). AI runs on needs, feelings and actions, plus stats. Circumstances affect needs, which cause feelings, which pick the next likely action (with random chance, a delay and execution time). The face changes to show the state.

| Needs | Feelings | Actions (sample) |
|---|---|---|
| Safety/confidence, success, efficiency, focus/stamina, awareness, play/fun/random | Fear/panic, anger/rage, shock/paralysis, frustration, curiosity/confusion, impatience, whimsy | Rush, melee, stabilize and aim, fire from cover, keep distance, flee, dodge, throw, grab nearest item, spray and pray, plus the full player control set (switch gear, mirror, tandem/solo...) |

Action choice depends on stats such as reflexes, intelligence, bravery, whimsy, patience, motivation, cautiousness and stamina. Stats can change temporarily or permanently through events, and can be randomized per NPC for "simple, yet very unique behaviours". AI emulates human vision and logic, including delays (178). Advanced AI (194) adds line of sight and stealth, memory, extended friendship and compassion, and non-combat facets with the full NVC (Nonviolent Communication) range of feelings and needs *(interpretation of "NVC")*.

**Opinions** (190, 197). When a character enters a room, it forms an opinion of everyone else: friend or foe (IFF), threat level for enemies, patience level for allies, and flags. Everyone does this to everyone (16 characters = 240 one-way links). Level generation sets groups, allegiances and patience; threat is judged by observing characters and their gear. In the simple version everyone is omniscient.

**AI flags** (190), labels toward a specific character X: **Loyal** (stay friendly whatever X does), **Protect** (stay close to X, attack whoever targets X), **Follow** (stay close, otherwise free), **Support** (attack X's target; for the player, the cursor position), **Nemesis** (focus on X, ignore others unless in the way), **Stalker** (like Nemesis but from afar), **Repulsed** (avoid X).

**Observation and judgement** (194, 197). Every attack carries its initiator's tag, so victims know instantly who hit them. Each NPC keeps a personal opinion list about every other character and shifts it when hit. Judgement weighs the severity (percentage of limb health, decapitation) and the number of offences (each one lowers patience). NPCs can broadcast an injustice to others who have a tag for the culprit ("the player hurt me, they're not our ally any more"). Anyone can be neutral, friendly or hostile toward anyone, individually, and can change.

**Navigation** (204). Nav nodes are numbered waypoints placed during room generation, forming paths the AI can walk either way. If the direct path to a target is blocked: go to the nearest unobstructed nav node, rescan, continue node to node until a direct path opens. AI reads global lists of characters, damage sources and environment items (position, velocity, power/danger rating), plus room borders, items, active hazards and passive obstacles.

## Proposals for open questions

These are Claude's suggestions, offered because Reactorcore left the topics undecided.

- **Proposal, storing scheme.** Use the three-set loadout from the radial menu (209) as the default: each set holds one item per hand or one two-handed item, so a human carries at most 3 sets, plus the core's stash for one oversized item on the back. It matches the "size limit defined by core" rule and keeps the radial menu simple. A browsable inventory would fit a building or vehicle storage room better than a body.
- **Proposal, healing split.** Healing items give a pool that is distributed by the item's priority rule (core first, then head, then whatever is most damaged), not a flat amount to every limb. That makes a 20 HP medkit always worth the same total, and lets special items (limb regrowth kits, armor patches) be defined by their rule alone.
- **Proposal, armor.** Default to sprite-swap armor (cheap, consistent with one collider per limb), and reserve attachment armor for rare special pieces such as shields and exotic suits, which can be modelled as items held in a socket instead.
- **Proposal, non-conforming characters.** Treat them as room-bound bosses or landmarks: generated inside one node, they never travel, which also makes them natural "remarkable points of interest" for that room (see `universe.md`).
