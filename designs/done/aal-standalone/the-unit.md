# Standalone: the unit (mothership and ReWaR)

The player's tandem combat unit: the mothership that carries the AI, and the ReWaR mecha it remote-controls and rebuilds. Their systems, flight, weapons, controls, and the V3 arsenal. Mostly V2 (2011–2012); V0, V1 and V3 differences are marked. Sources: R1–R34, A17–A18, the AoY content lists (player, 2011-08), the ReWaR developer log (2011-10), the 2013 demo renders, the 2023 pitch (`Standalone.txt`) and the 2024 multi-weapon note.

## The tandem

- **The AI is the character.** It lives in the mothership's AI core; the ReWaR is "a semi-expendable proxy warrior, an unmanned remote vehicle" (content lists). Lose the ReWaR and the mothership builds another; lose the mothership and the AI dies with it.
- **Switching**: the player controls one machine at a time and switches at will. The other runs on its own: the mothership goes on autopilot (V3 pitch) and takes orders from the tactics screen (move, fire A at B, harvest, dock the ReWaR, retreat; see [campaign-and-modes.md](campaign-and-modes.md) and [interface-and-demo.md](interface-and-demo.md)). The ReWaR is the main fighter; the mothership supports it and is "very powerful itself".
- **Unit ID**: each unit has a code painted on the hull, e.g. "SA-56" (R1).
- **Double AI co-op** (R1): two players share one SA, one in each machine. "Both AI cores reside in both the MS and RWR, but only one may be active at a time." Switching places needs both players to agree. (V3 instead suggests co-op as two Standalone units side by side.)
- **Colours**: the core/energy colour tints shields, thrusters and weapon effects; ship and mech have their own colours (character edit, S1/S50).

**V0** had no tandem: you *pilot* one Standalone with life support, a central super reactor and a supply dropship (R35–R37, E5; see [versions.md](versions.md)). **V1** introduced the AI "You", the mothership and a "robot warrior" with no name yet; there the wrecked robot split into 5 pieces the mothership had to collect with a tractor beam before rebuilding.

## The mothership (MS)

### What it is

A large, armoured, heavily armed ship, part carrier and part harvester (content lists). In the V3 pitch: "an all-environment self-sustainable deep-space von-neumann probe assault battleship superweapon" with a mecha bay and a linear catapult, FTL travel, "more armor and bigger guns" than the mecha but less agility, and a main cannon "that can wipe out an entire fleet in one shot".

### Layout (R2, R13)

R13's feature list ("AoY - Mothership"): repair bay (exposed, or an entry hatch near the exterior); linear catapult, connected to or near the repair bay; resource storage / cargo bay; harvesting equipment (turret, molecular ray); multi-directional propulsion; heavy armour with reinforced atmospheric armour on the bottom; reactor/engine; AI core; sensor array; repair drone slots; cameras.

R2's "interior system" cutaway: a **launcher** rail along the top with a **top hatch**; the **AI core** linked to the **sensors**; the **reactor** below the core; a **resource processor**; a **LAB basement** with a bottom exit; a **tractor beam** reaching down from the hull with a robotic claw unit. A vertical shaft holds the ReWaR in its bay below the top hatch *(interpretation)*. A top view adds an **FTL engine**, an **artillery mount** with a long swinging cannon, and a **shield generator**. Other sketches show the ship harvesting rock with claw legs ("Harvester") and a catapult ("CATA").

### The ecosystem (R5)

- Armour is repairable; the barrier is self-charging.
- The MS stores resources harvested from stones and minerals. **Drones** do the harvesting; the **LAB** builds the drones. Building drones and repairing the ship cost **RVs**; drone repairs are free ("fragile anyway").
- Diagram: **storage**, **drone store** and an **exit airlock** in a row with the LAB below them. Drones leave through the airlock to mine a rock ("+RES 22/100") or to sit in one of six numbered **repair positions** on the hull. The ReWaR also comes and goes through the airlock.
- In V3 the mothership also "can print a new mecha" with gathered resources, and repairs, refuels and rearms both machines at a resource cost.

### Sensors and electronics (R4)

Fire control system; long-range sensors (a dish); an ECM suite that reveals cloaked enemies; multiple "exterior eyes" that watch targets near the ship; defence barrier projectors. The sensor ranges from galaxy level down to the tactics screen are in [world-and-combat.md](world-and-combat.md).

### Flight systems (R9)

- Main thruster (back) L5; bottom hover thrusters L4; retro thrusters (front) L3; turn thrusters (side) L2; pitch thrusters (top/bottom) L2. The L-numbers are unexplained, probably size or power *(interpretation)*.
- A **frontal energy projector**: a shield during atmospheric re-entry and an acceleration field during liftoff.
- Manoeuvring fins: 3–4 large at the back near the main thruster, 3–4 small mid-front.
- A sketched flight path: fiery re-entry, a curved descent, low level flight, a steep climb back to space.

### Armaments (R8, R10, R11)

- **Coverage** (R10): full 360×360°; 1–4 rotating general turrets with variable energy weapons; 2–6 rotating point-defence turrets; one huge frontal cannon.
- **Main turrets** (R8): rapid fire (small shots, high rate of fire), cannon fire (large shot, low rate of fire), exploding blaster bolts, an AA-style AoE effect, a heavy tractor beam. "+Extra!": the main turrets are **railguns** that use ammo made from RVs, so the ship must move to resource spots to replenish, which suits it to a support role.
- **PD turrets** (R8): a "GRS1 style laser system", a constant weak beam, a full discharge beam that pierces, a light tractor beam.
- **Weapon pod** (R11): a guided **megabomb**, a manipulator arm and a **CM gun**; a gun with targeting optics, a camera sensor and a laser, its projectile marked "flare gun behaviour / magnetic / extreme heat".
- **V1**: the mothership auto-fires and takes support orders: artillery, covering fire, area denial.
- **2013 demo**: the tactics screen lists mothership ammo as "MSSL 43, RAILG 220, MAING 40% charge" (missiles, railguns, a charged main gun, *interpretation*).
- **V3** (2024 note): megabeam frontal cannon; multiple multigun railgun turrets on all sides; a missile launcher array; a defence laser matrix; multipurpose drones armed with a basic railgun multigun; bomb, torpedo and mine munitions bays.

Open: R10's energy turrets vs R8's railguns. The V3 list keeps railgun turrets, so railguns probably won.

### Controls (R34)

- **Basic (auto)**: forward, backward, up, down, turn left/right, strafe left/right.
- **Advanced (manual only)**: roll, pitch, no acceleration or speed limits, no auto-brakes except auto-hover on planets ("Don't want to fall down!").
- **Functions**: turret aim mode (manual, with lock-on); catapult launch; tertiary special weapons (missiles, CM, bombs, torpedoes, nukes, super nukes, maybe mines); repair on/off; harvest on/off; autofire turrets at threats (toggle); switch optical/infrared; camera mode toggle; auto-dock the ReWaR; target lock-on and scan; main gun control (mode select, firing); RV management (tactics screen only); light modes; full stop; engine kill ("Don't do this on planet!!"); quick 360° look; manual harvest; tractor/gravity beam control with the turrets (circled).
- **Control states**, a scale in two steps:
  - **Automatic**: stable and restricted; holds 0 roll and 0 pitch, bottom pointed down; docking the ReWaR is easy.
  - **Semiauto**: keeps stability but lets the player steer, like the Raptor in UT2004; emphasis on aiming; a more zoomed-out camera.
  - **Manual**: full freedom, roll and pitch, the catapult can be aimed; docking may be confusing; Freelancer-style controls. Rolling 180° on a planet and then handing control to the AI reverts it to auto.
- "Note to self: include aiming guides in the GUI for the MS."

### Scale and look

- **A17** ("too small scale oops"): a 16 m long mothership, 6–8 m wide, 3.4 m high, a 9 m deck, two main defence turrets and a sideways positron cannon. The page was later judged too small; the replacement scale is not recorded (open question in [index.md](index.md)).
- **2011-10 line sketch**: a long gun-like carrier with a big multi-barrel nose cannon and an internal compartment labelled "STOMACH".
- **2013 demo renders**: a long, flat, boxy grey carrier with a white launch deck along the top, a red-and-white bow, hazard stripes, swept red-tipped fins and twin rear engines; the STANDALONE logo is painted on the catapult deck.

## The ReWaR (Remote Warrior Robot)

### Requirements (developer log, 2011-10-24)

- **Movement**: high speed, high manoeuvrability, atmospheric re-entry, high-yield thrusters, transforms from biped to jet for extreme linear speed, multidirectional thrusters for strafing, dodging and turning, automatic alignment for docking with surfaces.
- **Defence**: a shield that absorbs bursts of massive damage, a low-threshold energy barrier, strong armour plating.
- **Offence**: the variable energy weapon system (rifle, cannon, sword, grapple, shield), directed or dropped countermeasures, area-denial/bombardment micromissiles, a point-defence/sidearm laser turret.
- **Experimental**: guided large fusion bombs/missiles, a **Buster cannon** (ultimate ranged weapon), a **Buster sword** (ultimate close-quarters weapon), an overcharge / "limit cancel" feature.
- **General**: full 360° camera view; sensor suite, IFF, ECM, targeting and fire control; manipulator arms; powerful heat management; launchable from a linear catapult.
- Two setups: **Type 1 "Spartan"**, a large shield with a large rifle/sword; **Type 2 "Standalone"**, two large variable arm cannons with shield functionality. The notebook and the demo follow Type 1.

R12's earlier feature list ("AoY - Robot"): reactor; arm rifle (MG, cannon and shotgun) plus Buster rifle, mega sword and bayonet; control unit and light ECM; shield; CM bomblet launchers; micromissile launchers.

### Health (content lists, 2011-08)

Two layers. The **passive barrier** is weak and rechargeable: it soaks minor damage, recharges when not under fire, and after failing waits a short delay and powers back up to full before reactivating. **Armour integrity** is the last line and does not regenerate in the field; the mothership repairs it, but the ReWaR must shut down for that, leaving the mothership on its own. The **auto maintenance** system in the torso is explicitly "NOT HP regen" (R19).

### Body (R14, R17–R20)

- **Torso, internal** (R19): main computer (fire control, image/data processing, system management, anti-hack hardware), reactor, environmental hazard sensors ("instincts": heat/cold, radiation, EMP, weather), an energy barrier generator for heat and cold, a communicator/receiver (the remote-control hardware), cooling and heatsinks, auto-maintenance, passive/active radar, capacitors.
- **Torso, external** (R19, R18): chest reactor port; chest rifle/shield mount; landing gear (more in the legs); cooling vents, which disperse heat and make **after-images**; area lights and a frontal chest light; waist side thrusters; the back missile system; the back main biped thruster array; chest retro thrusters; small cameras scattered over torso and legs for a 360° view. R18 suggests experimenting with a 360° spherical camera.
- **Shoulder units** (R20): missile system, thrusters (forward, up, down, side), heat vents front and back, a shield generator on the side. "Tighter tho": the shoulder-to-arm gap should be tighter. R14 had shoulder missiles under a lid, crossed out "nope".
- **Legs** (R17, R20): **Gerwalk-type legs** that swing forward in jet mode *(interpretation)*; knee plates with a thruster and 3 CM guns (front and back); side pieces with an RCS thruster and 2 CM guns; knee-cap thrusters; feet that unfold.
- **Head** (R16, R23): main aim (optical camera), zoom for a first-person/telescope mode, sensors (IFF with automatic target recognition, hazard detection, motion, collision/proximity), light amplifiers (night vision), infrared (thermal), a scanner, a camera flash, flight lights, search and floodlights. A **head turret** covers a wide arc (R23). Head styles considered: flag, Gundam, hardballer, Votoms, Armored Core, crusader, Iron Giant, big red eye, camera array. The 2013 model has a square head with round red sensors.
- **Back pack** (R23): a central fan-like unit between two side pods with round launchers and angled nozzles; missile options of a few, many small, or one big one with no reload; a sliding cover.

### Thrusters (R15)

| Group | Role |
|---|---|
| Shoulder (RCS) | turning and adjustments, roll and yaw |
| Waist | sideways movement, strafing, dodging |
| Back unit | balance control ("tail binder"); main forward thrust in biped; downward movement (biped, secondary; jet in space, maybe a separate device); extra forward thrust in jet; unfolding wings with flaps for jet flight in atmosphere |
| Top/front (jet) | downward movement in biped; RCS in jet |
| Breast | VTOL thrust (hovering in jet mode); backward thrust in biped |
| Knee | as the breast thrusters, plus the jet ↔ biped transition |
| Leg | main forward propulsion in jet; levitation over surfaces; upward thrust in biped |

The jet can land by levitating over a surface. V3 frames the whole thing as momentum physics: no air friction or speed caps, you brake actively, and you "throw" yourself around by adding force, skating and gliding over surfaces, turning on a dime (the design intent is in [campaign-and-modes.md](campaign-and-modes.md)).

### Biped and jet (R18, R30, R31)

Jet form ("combat jet mode") puts the robot behind its round shield with the rifle mounted down the shield's centre, flying shield-first ("SUPER MAN!"). R30 storyboards four ways to shift:

- **A**: one at a time: rifle to the centre of the body (click), shield moved (remove), shield over the rifle (click).
- **B**: combine the rifle with the shield, then attach the pair.
- **C**: attach only the rifle and move the left hand to the centre; maybe a dual E-port connection.
- **D**: simply move the arms into position. "No reactor connection this way :("

Which one was chosen is not recorded. The shield's features include a jet mode connector ("attach self under rifle") and launch ports for bombs at its top for jet use (R31).

### Scale (A18)

A 2 m tall ReWaR (1.2 × 2 × 0.5 m), a 0.6 m rifle, a 1.1 m shield, a 0.4 m fusion bomb, 0.1 m missiles and 1 cm CM bomblets, in a 90 km stable world with 1 cm precision; supersonic is 360 m/s. Like A17, this scale was later marked "too small".

## The arm rifle

The ReWaR's main weapon, called the **Variable Energy Rifle** in V1 and the **arm rifle** from 2011-08; the **temgrav variable rifle/blade** in 2024. In V0 it was two arm guns that merge into a super rifle (R35–R37).

### What it does (R21, content lists)

- A **particle gun** with unlimited ammunition drawn from the reactor; kinetic, thermal and EMP damage; variable output; an explosive AoE on hard surfaces; vaporises soft targets (or cuts large ones); generates heat and recoil.
- The output is capped: the content lists give 100 rounds in rapid-fire mode; firing 50 and reloading leaves the rifle unable to fire until all 100 recharge. R25 adds a **forced recharge** that refills the whole particle tank while firing is blocked.
- **V1/2011-08 modes**: 3×2 projectile options, piercing or explosive × rapid fire, charge cannon or spread fire; plus an energy blade and a utility tractor beam.

### How it works (R21, R22, R25, R28)

Components: a **particle generator** fed by the ReWaR's reactor through an arm power port; a particle intake and **mutator**; an internal battery; an excess energy store (**E-cap**) and a **particle capacitor** (P-cap); an initial acceleration coil; the **activator**; **magnetic field generators / rails** (retractable, variable: main acceleration, speed, shape, spread); a variable projector nozzle; an **atmospheric annihilation laser** that clears the air ahead to extend range; heatsinks and vents; a normal handle and secondary handles for Buster mode; an arm power port, a back reactor port for Buster mode and a second reactor port for jet use (maybe the same port). Reactor connection "still allows minimal arming capability"; the jet connection allows "even less".

Firing sequence (R25): 1. mode selection; 2. aim/lock-on; 3. trigger; 4. particles move into the activator, the amount set by the mode; 5. the activator weaponises, charges and stabilises them; 6. the shot launches; 7. steps 4–6 repeat while the trigger is held and particles remain; 8. on release, back to step 1 or 2. Particles regenerate when not firing. Preparation per mode: charge time (sets rate of fire) and the field controller's spread, shape and velocity. Normal activator: limited capacity. Buster activator: opens out spiky, unlimited capacity, but vulnerable, and switching mode takes a delay with no firing.

### Modes (R22, R24)

| Mode | Notes |
|---|---|
| Heavy MG + burst function | small shots with AoE bursts; 1/100 energy per shot |
| Flamer | chargeable; 10/100 energy; later replaced in melee by the blowtorch |
| Long range cannon / charge cannon | a long beam or bolt; the charge shot pierces a barrier and explodes. A constant beam was crossed out |
| Shield | a barrier mode; the grappling beam / gravity gun was crossed out here and moved to a "seperate device" (the left arm's grappling beam, R31) |
| Melee: charged burst slash | a big curved energy arc |
| Melee: blowtorch | continuous short tight jet, chosen over the flamer |
| **Buster: wide raw particle beam** | 20–40° cone, 2–3 s, aimable while firing, vaporises groups of small enemies |
| **Buster: concentrated cutting beam** | "aka massive laser sword", 3–5 s, pinpoint, pierces the hardest targets |
| **Buster: buster bolt** | "aka nuke": an ultra powerful shot that vaporises soft targets, makes a massive AoE blast on hard ones, and leaves a dangerous "bleeding trail" that hurts near misses |

Buster mode mounts the rifle on the back reactor port, pointing forward from the body's centre, and makes it "more bulky, longer, wider" (R29). Mount requirements: arm, Buster mount, jet mount (R29). R28 marks one of its rifle sketches "This one"; parts fold away up to 90° and 180° to be concealed.

### Appearance (R26)

An energy particle beam: extremely hot, so bright, with long trails, a residual glow and a heat-mirage distortion; **EM bleeding** sheds lesser charged particles and small electric arcs along the trail, stronger at the tip; made of solid matter, so **opaque, not transparent**; a strong magnetic field repels weak matter, so near misses take damage from both the field and the bleeding. Colours: main beam yellow, white, red or orange (or blue); EM particles blue, white, purple or pink.

### Add-ons (R27)

A variable **targeting laser** (rangefinder, paints targets for the mothership "in fog only", laser sight, remote control, a low-power precise non-weapon). A **gun camera** (optical and infrared; reflex/ironsight aiming; better accuracy with the main camera; the zoom is crossed out: "head provide telescope"). A **flashlight** (adjustable, with Morse signal flashing). Rejected: independent RCS thrusters and cameras so the rifle can fly by remote ("Nah.").

## The shield and left arm (R30, R31)

- **Shield** (R31, dated 11.1.2012): full body coverage; a particle-based **barrier generator** as the first line of defence; maybe an inner rifle port for a barrier boost; the jet mode connector; landing gear compatible with the linear catapult; heatsinks along its edges; a slow arm connector; works as a heat shield for atmospheric re-entry. Front: mostly solid, dull and hard-looking, with concealed landing gear. Side: thick yet lightweight, 2 or 4 bomb launch ports at the top for jet use. Back: the arm connector, a rifle rail, the fusion bomb dispenser. R30 notes a "higher connection point" and a taller shield.
- **Content lists**: large enough to cover the body and able to take "a direct nuclear blast or a deathray beam"; it has its own armour integrity, far more durable than the robot's, and is repaired or replaced at the mothership. **V3**: "It has defensive capabilities to withstand a nuclear explosion using its shield." The 2013 model's shield is hexagonal with a glowing cyan rim.
- **Left arm** (R31): bottom, grappling beam; top, CM gun and flashlight; inner side, a spike/blade combo; outer side, the shield and the bomb gun.
- **Pilebunker** (R30): a left-forearm spike that shoots forward, combined with a folding heat/vibroblade (double-sided; "note the end shape"). The arm also retrieves bombs.

## Fusion bomb, missiles and countermeasures

- **Fusion bomb** (R30, R32, R33; "megabomb" on R11, "FSB" in the demo): compact and safe unless armed, harmless if damaged early. Placed, launched or thrown. Sticks to targets three ways: magnet (metal), claw (organic), glue / expanding adhesive foam (other); the side attachers carry 3 spikes, 4 foam releasers and 2 magnets. Remote, timed or impact detonation. Stored in the shield, 2–6 at most (the demo shows 2/6). An indirect weapon. Anatomy: sensors and receiver (guidance, remote control, motion/proximity sensing) in the nose, the fusion warhead, and a tail with a small main thruster, 4 manoeuvring fins and RCS thrusters; it can be guided along a curving path to a target. Payload 1: a fusion nuke (heat, kinetic shockwave, radiation, EMP, maybe a gravitational anomaly). Payload 2: a particle bomb ("nuke-ish").
- **V1 / content lists**: "heavy explosives", a powerful sticky grenade with remote detonation and a large slow area-denial blast that also kills projectiles and shakes off pursuers; very short range, launched from the left hand; 2 at a time. **V3**: "fire a nuclear warhead"; megabombs launch as a homing missile/ICBM or attach by magnet, spike or glue, or are thrown or dropped. AAL Exterminator's smart bomb is modelled on it.
- **Missiles** (content lists): small homing missiles on the torso and shoulders, up to 100. The dev log calls them area-denial/bombardment micromissiles; the demo lists "EMIIM 37/90" (EM/IM missiles, *interpretation*). V3: concussive cryo homing missiles.
- **Countermeasure bomblets** (content lists): tiny bomblets from the lower legs that break lock-ons and hurt pursuers and projectiles. On planets they act as air-to-surface bombs from high up, and near the ground they fire backwards as a shotgun burst; in space they become clouds of floating proximity mines. The notebook puts CM guns in the knees, side pieces and left arm, and fires them up and down near the rifle (R23). V3: an incendiary frag bomblet flare dispenser.

## Targeting and camera (content lists, R23, R27)

Third person by default, with a **rectangle reticle**: an enemy under it is targeted, the one nearest the centre first. Once targeted and fired on, the arm leads the target and aims on its own, independent of the camera. **Manual aiming** switches to first person with a pinpoint crosshair inside a larger rectangle that is then reserved for missile lock-ons. R23 notes a "Star Fox lock-on laser" and sketches coverage arcs: the rifle a narrow forward cone, the head turret a wide arc, countermeasures the rear. V3 adds Freedom Gundam's multi-lock-on that wipes out a group at once. Gameplay camera and scale notes (S54) are in [interface-and-demo.md](interface-and-demo.md).

## V3: the full arsenal (2024 note)

The current list.

- **Mecha**: temgrav variable rifle/blade; super shield; fusion megabombs; concussive cryo homing missiles; incendiary frag bomblet flare dispenser; 2 automatic head lasers; a back automatic railgun multigun turret.
- **Mothership**: as in Armaments above.
- **Both**: after-images from the heat vents (evasion); a chaff generator (ECM, anti-lock-on, jamming); a lethal sensor pulse; a 360° self-recharging, sacrificial energy barrier; booster exhaust fry; hardened-frame collision attacks (kick, stomp, punch); an intentional reactor radiation leak; a super self-destruct blast; a **speed lance** (accelerate and plough through with a frontal energy lance, also used for FTL travel).
- **Coverage**: hot, cold, pierce, blunt, HE blast, frag, graviton disruption, nuclear shockwave, radiation, sonic, solid and energy; single and multiple targets, big and small, hard and soft, near and far.
- **Modes everywhere**: the rifle switches between any firearm type (sniper, machine gun, cannon, flamer, shotgun, blade); explosives detonate by timer, remote, proximity, sensor or impact; the railgun fires rapid pellets or big slugs; incendiary, frag, cryo and shockwave payloads switch on and off; lasers pulse, charge or fire continuously. Set at the mothership or in the field through loadouts.
- **Customisation**, originally: colours, unit name/callsign, loadout configs.

### Jager guns (2024 note)

An expansion idea: replace the single standard mech with modules (head, torso, arms, legs) and strap "Jager gun" models onto them where the standard systems were, each gun acting as the "nozzle" for that system (rifle, launcher, shield, blade). Every default element and weapon type stays in the arsenal, but they can be moved: give cryo to the megabomb and the missiles automatically become nuclear or incendiary. Sizes trade off: a small rifle aims faster and weighs less but has less range or damage; a big one hits harder but swings slowly and hurts mobility. A small shield still protects fully but has less knockback resistance, so a blast sends you flying "like a beach volleyball". Weapons can move to other slots: the shield's parts onto the guns for dual, quad or sextuple wielding, the temgrav onto the head or back as automatic missile defence. An alternative: fixed unique models with the same weapons in Zoids-like animal or Zeon mobile armour shapes, each with one special ability, all still shifting between fighting and jet forms.

### Supercores (2024 note)

Each campaign has supercores held by enemies, empowering them or their whole force. The player can destroy or steal one; a stolen one gives its power to the player, or serves as a consumable catalyst to charge an attack instantly or unlock one otherwise unavailable. Slots are limited (or cores expire in FTL travel), so they must be **retired** (sent home for study, earning achievement points for the character) or **reduced** (broken into resources, or spent on a temporary boost or overpowered attack; Reactorcore prefers the latter, with points for the capture alone). Benefits: stat boosts (mobility, refire, speed, health, shield, armour, ammo), auras, intel "cyber sight", or Divinoids-style weapon modifiers (triple shot, homing, extra elements, piercing, multi-detonation). See `reference/supercores.md`.

## Open questions

Collected in [index.md](index.md) and at the end of transcripts 03 and 04: which of the four biped-to-jet shifts, energy turrets vs railguns, the replacement scale, the head style, and what "GRS1", "FM" and L2–L5 mean.
