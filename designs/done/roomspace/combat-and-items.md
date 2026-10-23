# RoomSpace: damage, items, vehicles and performance guards

How things get hurt, what items are made of and how they work, temporary "visitor" objects (projectiles, effects, gibs), vehicles, collisions, and the chaos system that keeps it all running. Mostly notebook 1 (scans 182–210, 214). Numbers in brackets are scan numbers; the full wording is in `transcript/`. *(interpretation)* marks Claude's reading; **Proposal** sections are Claude's suggestions for gaps.

## Damage model

**Intentionality rule** (182). Anyone and anything can slam into walls without harm. Damage only happens when it is active and voluntary: a charged throw, a dash, a swing, a fired projectile. This applies to weapons too.

**Three integrity values** for every object (182):

| Value | Meaning | When exceeded |
|---|---|---|
| **HP**: general hit points | Health | 0 HP: dies or disconnects; below −X (−20 for limbs, 185): gibs |
| **IL**: (force) impulse limit | Max pressure, e.g. 1000 force | Gibs |
| **JS**: joint strength | Max pull force, e.g. 500 | Joint detaches |

Scan 185 labels the same limb values HP, IFT and JT.

**Three damage types** (182):

1. **HP damage**: Charged Kinetic Pressure, blades, status effects (fire, poison, electricity).
2. **Impulse stress**: crushing force, focused pressure, force impacts (against IL).
3. **Pull stress**: damaging drag, intentional centrifugal spin, ripping (against JS).

**Charged Kinetic Pressure (CKP)** (182). Simulates structural damage from blunt impacts: bullets, clubs, hammers, maces, charged throws, dashing bodies. It deals HP damage only and can be bundled with blade, impulse or pull damage. The final number can take speed, charge time, mass, target density, protection and the combined momentum of attacker and victim into account. **CKP acts on contact**, **blade damage acts on overlap** (without solid contact) and **hybrids** do both (202).

**Impulse Stress Damage (ISD)** (187). Below a minimum threshold, nothing. Past it, CKP damage starts every tick and grows with the stress. If the object's own max ISD is reached, it gibs. The more health damage an object has taken, the lower its max ISD (it grows brittle). Formula sketch (202): ISD = mass × speed × density × size/prominence.

**Blades** (184). Limbs have HP, a material (flesh/metal: penetration resistance) and softness; hits cause a wound particle burst and maybe a decal. Blade properties: mass/density, speed/momentum, sharpness (penetration threshold), integrity (a blade hitting something harder takes damage). Impact sequence: incoming → initial impact → **deflect** (little or no damage, momentum and recoil) or **penetrate** → past the threshold, **stuck** (no further damage) or **cut** → pull out, go through, fall out, or the victim gibs. Cut damage is applied per tick by the distance the blade travels inside the victim (record the local position, compare), with slow cuts doing slightly more and the blade dulling a little. A stuck blade that gravity can't pull is made dormant (performance). Only the blade part cuts; the hilt can get stuck. Blades can impale, get stuck, drag, cut, disconnect joints, eviscerate and gib.

**Temperature** (188). Below 0 °C things slow down, at 0 K they stop; 0–100 °C is the optimal range; above 100 °C objects take HP damage; around 1000 °C–10,000 °C they gib. Reactorcore's caution: this "lowers empowerment". (The note puts absolute zero at −200 °C; it's −273 °C.)

**Gnarlyness**, the damage multiplier (202, 208). Damage ≈ mass × speed × gnarlyness. The multiplier is built from density (foam to neutronium), roughness/hazardness (smooth = safe, jagged = more ISD for blades), volatility (more damage, more danger; transfers on touch and depletes) and LMB hold charge (player effort). Sharpness is a separate blade-only value, outside the multiplier. Fuel-powered items can convert fuel into extra damage or status effects. The range was "0.0–1.0?" but the worked example (50 kg × 40 km/h → 2200 CKP) implies 1.1.

**Dash and naked combat** (201). With no working hands, dashing is the last-ditch attack. Holding Dash tenses the body: every limb and held item gets CKP based on the combined direction and speed of attacker and victim. Worked examples (same mass): full-speed attacker into a still victim = maximum hit; victim fleeing at the same speed = no damage; half speed either way = 50%; a victim who dashes into the attacker ("retaliation on") negates the hit. Fleeing at an angle reduces damage (the note lists 45° → 50% and 22° → 25%, which looks inverted). The most aggressive character wins, with weight and density as big factors.

**Cascading shockwave damage** and "how armor works" were open questions early on (183); armor was answered later (see `characters.md`).

## Objects and items

**Item anatomy** (183, 206). Items are built from:

- **Main body**: generic colliders (rect, triangle, circle, polygon).
- **Hand socket**: a snap anchor for a hand, shown on mouse-over in lime green.
- **Hand interface**: a solid grip; grabbing it gives control.
- **Weaponized surface (WS)**: like a main body, but its effect and collision can be switched off; deals CKP and/or blade damage or passive status effects.
- **Emission point**: where projectiles, beams or exhaust come out. Parameters: ammo reserve, launch speed, emission rate, angle range and direction, count, flags, recoil damping, charge-up, wind-up.

Every segment (main body, weapon surfaces) is individually destroyable; sockets and emission points vanish with the part they're attached to (208).

**Object types** (183): **passive** (main body only), **usable** (inert until picked up and used), **autonomous** (needs a "head" power supply: endless, volatile or repairable; works continuously, on a timer/charge/ammo, or on proximity/line of sight).

**Packed and unpacked items** (206, 209). Items can have a compact packed form; equipping one "unpacks" it onto the user and dropping it repacks it. Options include concealed weapons and items that attach to the core or head.

**Object properties** (188): mass, HP/gib limit, impulse limit, joint strength, density (blade resistance, toughness), brittleness (lowers the ISD limit), slipperiness, status ailments and resistances, momentum, CKP/ISD charge, surface area (not from sprites), position/rotation/enabled, volatility, safety rating, techscore (rarity), hazardness/roughness, damage mode lifetime, unreleased momentum.

**Object shaders** (188): colour (RGB), damage (noise), status (filter), light, saturation/lightness, vision modes (night vision as inverted heatmap, colourblind), time-of-day/mood tint, UI overlay. **Coverings/frostings** (276) are inert shader layers applicable to anything: snow, frost, oil, insects, goo, paint, dirt, moss, rust, soot, rad glow, barnacles, crystals, scales and more.

**Sprite states** (195). Item sprites have off/idle and on/active states, optionally animated. Muzzle flashes, beams and similar effects are **never baked into the sprite**; they are spawned as visitor objects.

**Crates and packaging** (195). Crates, boxes, cases and barrels store items behind themselves the same way a core does; oversized items stick out and can be shot. Grab a box and hold LMB: items that touch it (and pass the size check) go inside. "Reload" ejects everything (an earlier "suck mode" toggle was dropped). Storage objects might be derived from vehicles; "level refill equilibrium" is noted without detail.

**Ammo** (196). Guns hold an internal reserve (MAG/TOTAL); no ammo, no use, with audiovisual feedback (-EMPTY-). Guns emit only the projectile, no casings, for performance. Ammo boxes hold large reserves (e.g. 8000) and repair kits too (e.g. 2000); volatile boxes explode when broken. Two refill ideas, undecided: shove a held gun into an ammobox (the cheap version, not used if reloading exists), or pick up the ammobox and use it while holding or storing a matching gun.

**Fire modes** (205, 206). The player has one trigger (LMB): press, hold, release. Modes: semi-auto, full-auto, burst, toggle, charge (press charge, hold charge, continue previous charge; release when full, press again to fire, or cancel), multistage (manual or timed switching), pulse, repeat (infinite or x times). Extra balancing knobs (208): charge rate/amount/max/overcharge, rate-of-fire ramp up and down (affects accuracy), burst and projectiles per shot, recharging power cells shown as percent, cooldowns that vent heat. Camera shake is a result, never set by hand.

**Power and volatility** (206, 207). Everything needs power, fuel, ammo or work; player input is fuel too, with a cap. The power chain: reactor/generator → capacitor → fire/release → attack, with reserve banks fed by fuel/ammo, and recoil/heat/waste as the "tax". **Volatility** is stored, trapped power: reactor cycle, capacitor size ("armed matter"), current ammo, reserve size ("unarmed matter"), launch mechanism. More volatile means more damage and more danger if broken or misused. Mitigated by mass, density, surface area, and a **safety rating** (smart design; trading power for containment). Techscore was crossed out as a mitigator.

**External units, A/C/R + LM** (207). Ammo (reserve), capacitor (chamber), reactor (feeding) and launch mechanism can be split between the gun and an external unit worn on the core and wired to the gun: A outside, AR outside, or ACR outside (AC outside "makes no sense"). Destroying the gun drops the unit safely; destroying the unit makes the gun useless.

**Recoil** (207, 197). Recoil = speed/size of the attack + volatility of release. Mitigated by gun weight, self-damage to the gun, safety rating, and power diverted to exhaust (weaker shots). Strong recoil throws the arm back or the whole character across the room.

**Heat** (205, experimental). Heat is a tax mitigated by weight, size and density; it can be vented as effects (muzzle flash, exhaust). Past a threshold, further use damages the item; cooling slows it, and freezing makes it inert.

**Weaponized surfaces and melee** (208). An item needs a WS to be a dedicated melee weapon (used with LMB); without one, it can only hurt by dashing (Reckless Mode). A passive WS (e.g. a bayonet) becomes the active function only when the primary is out of ammo, and not when held by a hand socket. Holding a hazardous WS can hurt the holder if something hits it. Catalogue: rocket hammer, sword, brass knuckles, laser sword (its blade is a line visitor), flame sword, beam sword, retractable blades, bayonet, pilebunker, ripsaw, flail (free joints), snapping jaws, automated spikes, motor-driven saws.

**Use cases sketched** (209): crossbow, AA-12 shotgun, grenade, energy-capacitor battle rifle, machine gun, pilebunker, rocket launcher, flamethrower.

**Radial context menu** (209). Holding the item-switch button opens a four-way menu around the character: top = func 1 (reload), left/right = previous/next item set, bottom = func 2 (purge all held items; activates the head if there are no items). Held over 2 seconds, it also shows stats: held and stored items (ammo, HP per segment), and the core (HP and statuses, food reserve, allies, features). A "current active items" panel shows each hand's item, or one shared two-handed item.

## Visitor objects

**Visitor objects** are temporary spawned things: projectiles, beams, explosions, fields, effects (202). Types: dots/pixels, solids, hitscans and rays, areas/fields/non-solid zones, lines and curves, waves, forces, emitters, projectors, spawners, nodes (embedded, attached, telepathic, remote), trails/tracers/afterimages. **All combine into composite prefabs.** Each has a collision type, representation type and interaction type; proximity detection (radius, hitscan, sensor collider); remote activation and guidance; timers.

Properties: mass, speed, rotation, position, lifetime-HP, impulse limit, status inflictions, size/prominence, friction, stickiness, density, hazardness, safety. Calculated: CKP, ISD, impulse, volatility (from the ammo), HP-lifetime. Modes: CKP, blade, or hybrid (e.g. explosive particle beams).

**Deployables** (202) either swap mode (same object) or release a payload (a different object), by gibbing into it, running a script or spawning it through emitters. Their contents may not exceed the parent's mass, fuel/power, techscore, density, volatility or lifetime ("never do anything arbitrary"); size can be traded for density. Gibs are limited to the parent's mass and energy budget.

**Gibs and effects** (203, 204). A reduced visitor object: collides only with terrain, informs the player and satisfies the senses, fades over time (bigger lasts longer), and impacts or idleness shorten its life. Cannot be weaponized. Properties: mass, lifetime points, impulse limit, friction, speed/position/rotation, size/prominence; a single simple component that nothing can attach to. A to-do note (257) ticks off "gib design limits: strictly visual effects" and "items as released gibs".

**Settling sketch** (203, untitled pencil). A free-floating circle collider (only its centre touches terrain) turns into a square of 1:1 density when pressed against a border, then flattens under gravity to a minimum height of 1 m and spreads sideways, losing density instead of getting thinner. Probably loose matter or blobs *(interpretation; see `environment.md`, blobs)*.

## Collisions

Collision layers (193): active characters (and traps), gibs/effects/projectiles, items and severed parts, room borders and terrain, AI nodes, world elements and volumes (explosions, gravity wells, smoke, gas, water). A character's own limbs never collide with each other until detached; other characters' limbs always do. Gibs, items and severed parts don't collide with each other, but do with terrain, characters and projectiles (189). Elements interact "ethereally" (overlap and forces, not solid contact).

**Rogue overlap fix** (193). When a limb is severed inside the torso, or someone grabs a long rifle still behind a corpse, the freed object overlaps a body and impales it. Fix: items and severed limbs carry a flag, `isCollisionsCleared`. Collisions stay off (and the item is unusable) until the object has moved clear of what it overlaps, then switch on.

## Vehicles

**Rules** (210). Vehicles are characters with sockets and/or interfaces. They need a "head" (which gives limited ambient power) and at least one interface or socket; powerful functions need compatible fuel. The pilot's controls are remapped to the vehicle's; a saddled living mount keeps regular controls and its head can be the control interface. Internal cockpits link the pilot to the vehicle (no collision between them) and need an exit zone: leaving pushes anything in the way out with a force set by the door's strength, and if the obstacle is too heavy, the vehicle itself is pushed away.

**Entry types** (210): A external control surface (free-form grab), B external socket (auto-aligned), C internal via a handle and door (exit area must stay clear; limbs fold to the centre while linked), D internal via a socket button. The vehicle radial menu puts EXIT on top and RELOAD at the bottom, the reverse of the on-foot layout, so a panicked press right after ejecting doesn't purge your gear. Losing control: pilot knocked out or killed, vehicle core or interface destroyed, pilot disconnects, or the pilot's hands are destroyed (180).

**Use cases** (210): HEV-style pilot protection, transport and carry-alls, special utility, armor, mobility, oversized items, mind control and remote operation ("there's a little bit of vehicle in all of us"), construction and demolition (with custom binds), operable stationary machines, temporarily tamed animals and robots. Topic list (195): remote control, operator compatibility, recursive piloting, pilot loss and entry, repair and refuel, vehicle-specific hands, usage permissions and locks, hijacking, control remapping.

**Stationary devices** (210): elevators, moving platforms, doors, bridges, cranes, hatches, pumps, conveyors, large storage, turrets, traps, emitters, all "context sensitive operable objects".

Big vehicles (starships, mobile bases) became **MDRCs** in notebook 2; see `universe.md`.

## Performance guards

**Chaos Intervention System** (203), the "low effort mode": speed up gib/effect fading, use template values instead of full calculations, put AI into "shock" (paused or simplified), drop shaders, delay AI, events and gibs, randomly erase items, gibs or effects as visible "anomalies", and globally jam usable items, emitters and active terrain. Later the same system (the "Glitch-Chaos system") resolves stuck or out-of-bounds objects and can warp or reassemble terrain (237, 277; see `rooms.md`, `environment.md`).

**Chaos Curse** (203). Each usable item gets a rating from rate of fire, projectiles per shot, and the lifetime, size and payload of its visitors. Under heavy load (many characters, many visitors or terrain objects, the item used heavily) the curse can activate: the item jams, malfunctions, "glitches out of reality", vanishes, explodes, slips out of the hand, or spawns dangerous anomalies around the user. An in-fiction way to cap performance cost.

**Budget** (214). Max 16 characters (a human with armor and items is about 34 objects), 500 limbs, 100 items (6-part composites = 600 objects), 700 visitors per second from item use (32 sources × 20/s) plus 200 per second from character emissions. Only the dot rate (20/s per handheld device) is filled in on the visitor table; hitscans, solids, lines, areas, rays and emitters are blank. The worst case to design for: 16 fully loaded characters dual-wielding full-auto weapons in a large open room with 40–50 destructible terrain objects (3–8 nuggets each), rain, wind, geofire, a gravity well, and a flood about to arrive.

## Proposals for open questions

Claude's suggestions, not Reactorcore's design.

- **Proposal, ammo refill.** Use "pick up the ammobox and use it while holding or storing a matching gun", since it needs no new collision rule and works with the emergency head. Shoving a gun into a box can stay as a fast shortcut for the same action.
- **Proposal, dash angle table.** Make damage scale with the closing speed along the attacker's direction, i.e. the cosine of the escape angle: 0° escape at full speed = 0%, 45° ≈ 29%, 90° (sideways) = 100% of the attacker's speed. This matches the "no damage when fleeing at the same speed" example and fixes the inverted 22°/45° pair.
- **Proposal, Gnarlyness range.** Let the multiplier run 0.1–2.0 with 1.0 as neutral (a plain club), so the 1.1 worked example fits and foam (low) to neutronium spikes (high) both have room.
- **Proposal, visitor rate table.** Fill the blanks relative to the dot's 20/s by cost: hitscan 20/s (cheap, instant), solids 10/s, lines 10/s, overlap areas 4/s, rays (bouncing) 4/s, emitters 2/s (each spawns children counted against the same budget).
- **Proposal, temperature.** To keep the "empowerment" Reactorcore worried about, apply temperature damage only to objects and unprotected limbs, and let suits and vehicles define their own safe range. Extreme rooms then become places you gear up for rather than places you avoid.
