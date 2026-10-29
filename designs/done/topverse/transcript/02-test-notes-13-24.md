# TopVerse notebook transcript: Test Notes 13–24

This chunk mostly works out how buildings and vehicles (DRCs/MDRCs) are built and fought. It covers the interior cell rules and how they map to entrance cells (Vehicle Setup 2 and its continuation), interior walls, doors and armour as sacrificial protection, the vehicle-level "facade" box entity with an optional freeform overlay, vehicle combat (universal HP, penetrative hits that hit random interior cells and pass through), separated-cell MDRCs joined by phantom girders or bio-struts on mobility coasters, and a kit list for vehicle personnel. It then turns to the vertical layers, with altitude thresholds for moving between sky, surface, soil/sea and deep in combat. On foot, it covers standard room exits (wall exits, underpassages, holes), the universal cross-character item inventory with its room-network escape items, the on-foot DRC/MDRC exploration room network (entry/corridor/location/transit rooms), and emergency escape mechanics (wall buster, drill, Fulton blimp). It ends with a regional Pokemon fear/loyalty behaviour index.

## Scan Topverse Test Notes (13).jpg

Single notebook page (grid paper), titled "Vehicle Setup 2".

**Vehicle Setup 2**

*Diagram:* Three sketches across the top.
- **"1."**: a square floor plan with a grid of inner walls. Letters mark rooms by size: "L" (twice, one marked "×L"), "M", and a small "S" box at top right. A label above reads "subsystem sizes" with a line pointing into the plan. On the left edge there is an exit marker (a diamond/arrow shape pointing left), and an arrow leads down-left from it to a tiny sketch of a little vehicle or object with small dots.
- **"2."**: an adjacent square of the same size with a central dot and short dash marks radiating outward in all directions (like a blast or a spread of 3x3 cell divisions around the centre).
- A third, narrower box on the right: a vertical bay with ladder/rung marks along both sides and a vehicle silhouette (a tank-like or mecha-like shape with a long barrel or antenna pointing up) parked inside. It is labelled: "max minor vehicle size that can fit inside a DRC entrance."
- A line from the drawings to the text below reads "(external on vehicle facade.)".

*(interpretation)* Sketch 1 seems to be the interior layout divided into subsystem slots of different sizes (S/M/L), and sketch 2 the same footprint seen as raw cells (possibly showing a penetrative hit spreading). The third sketch shows the largest minor vehicle that fits in one entrance cell's bay. "(external on vehicle facade.)" probably means the subsystems drawn inside also show externally on the vehicle facade.

Interior areas:
- subsystems, weapons, interfaces, controls, furniture
- internal defences (traps, troops, turrets etc.)
- propulsion, drive, tanks, reserves, storage
- each entrance cell correspond to 3x3 interior cell. Building/Vehicle cannot be larger than entrance cells allow. 2ent = 2^(3x3) int cells
- exit between entrance & exterior correspond to their cells respectively, though interior wise exit(s) can be placed anywhere in 3x3 int cell.
- minor vehicles are allowed on board.
- boundary walls can be broken and exiting through them is possible, leading outside the respective entrance cell, dropping from above. This is a one-way exit only.
- busting a hole/new entrance between int/ext can be done, but each int/ext pair may only have 1-1 amount of active entrances.

*(interpretation)* "2ent = 2^(3x3) int cells" is written with "(3x3)" as a superscript. It most likely means "2 entrance cells = 2 × (3x3) interior cells", i.e. 18 interior cells, not an exponent.

## Scan Topverse Test Notes (14).jpg

Single notebook page, titled "Cont. Veh Set 2" (continuation of Vehicle Setup 2).

**Cont. Veh Set 2**

*Diagram:* A floor plan of two adjoining interior cells side by side, with labelled parts:
- Left cell: thick hatched border walls on all sides. Inside are a "+" mark, a filled dot, a short vertical bar, and a small square with a cross in the top-right area. A triangle marker on the top wall is labelled "(EXIT A)".
- Right cell: a hatched top wall with a dot at the corner labelled "(shift door (common))". Inside are a large hatched square "(solid block (armor))", a short wall stub, and a small hatched rectangle in the bottom-right corner "(individual border segment) (nah.)". A gap with a diagonal swing line on the bottom wall is labelled "(swing door)", and the bottom-right corner is labelled "(EXIT B)".
- Between the cells: a vertical dividing wall with a small segmented rectangle across it, labelled "(armor wall segment)".
- Bottom-left labels: "full border segment (yeah.)" pointing at the thick hatched outer wall, "(half table)", and "(support armor pillars)" pointing at the short bars/dot inside the left cell.

*(interpretation)* "(yeah.)" vs "(nah.)" records a decision: border walls come as full-length segments per cell side, not as individually placed small segments.

**Interior Cell supports, walls, door, armor.**

- Intended as a) sacrificial armor to protect occupants of int cell in event of penetrative hit upon (m)DRC and b) as walls, cover, pillars etc to organize/control/guide traffic/access inside the interior of a (m)DRC.
- Can use materials/thickness/density for less/more hp for said supports/walls/armor.
- Border wall segments prevent exposure to outside elements (vacuum(space), flood(UW), dust (desert storm), etc. They also block the one-way exit out of the DRC's interior.
- Exposed border walls (lack of) only affect its own cell; there is no chain/adjacent spillover.

## Scan Topverse Test Notes (15).jpg

Single notebook page, titled "Vehicle Level Setup (the Facade)".

**Vehicle Level Setup (the Facade)**

*Diagram (top):* A small box labelled "ext" with two zig-zag (spring-like) fills, arrow pointing down into a larger grid. The grid is 3 rows by 5 columns of interior cells, labelled:
- Left column: top and bottom are long rectangles with stripes, labelled "thruster (air/space travel)". The middle is a 3x3 grid of small circles labelled "missile battery module".
- Second column: top and bottom are heavily scribbled circles, labelled "wheel (ground travel)".
- Third column, top: a seat-like shape labelled "cockpit".
- Fourth column: circles with an X at top and bottom labelled "turret", and a small filled circle in the middle with "exit" written next to it.
- "int" is written under the grid.
- "NOTE: Can define where weapon firing offset is on vehicle", with a dashed line across to the next drawing.

An arrow "=>" leads to a hatched rectangle on the right containing a small grid square (the missile battery) on the left and two circles with barrels (turrets) on the right. It is labelled "Vehicle ~~[scribbled-out word]~~ Entity (true shape) (collider)". Next to it is a list "FRONT / MIDDLE / BACK / L/C/R" between dashed lines (the firing offset options).

*Diagram (bottom):* A large freeform vehicle drawing laid over the same rectangle: angular hexagonal armour plates around the edges, a comb/tread pattern along the top and bottom left, a striped block and the missile grid on the left, two turret circles with barrels on the right, a pointed nose cone extending right, and small diamonds at corners. Lines from the "Vehicle Entity" label point to it.

Overlay Facade (optional freeform facade to make building/vehicle look anything you want. Goes on top of box entity, so ideally choose a facade that fully covers it. Weapons/Systems/Etc. can optionally render below or above the facade

*(interpretation)* The pipeline is: exterior (entrance) cells → interior cells holding modules → a simple rectangular "Vehicle Entity" that is the true collider → an optional freeform art overlay. Weapon firing points are set as front/middle/back × left/centre/right.

## Scan Topverse Test Notes (16).jpg

Single notebook page, titled "Vehicle Level Mechanics".

**Vehicle Level Mechanics**

*Diagram (top left):* A small hatched rectangle with a grid square on the left and two turret circles with barrels on the right (the same Vehicle Entity box as scan 15).

- Vehicle is like a character. Plays like one.
- Gets controls, mobility, abilities, weapons, traits, etc. via modules installed in the interior.
- Weapons are pregrouped and firing location offsets are user-defined (or just use the usual weapon/attack sys)
- Recieve damage => subtract universal HP, no locational damage or advanced targetting. Additional "Armor HP" possible. (via modules)
- Damage recieved will affect int/ext, randomly causing damage to support structures of ext, while if hit was penetrative/overpowering enough, then select random int cell and deal damage to occupants in a random order. If hit still has power, exit out the opposite side and continue flight (to another target).

*Diagram (bottom left):* A perspective sketch of two planes meeting at an edge: an upright grid labelled "(vertical plane) int" and a flat grid labelled "ext = (horizontal plane)". A projectile (drawn as a bullet with a trail) flies in from the lower right, labelled "(hit)" where it strikes the horizontal "ext" plane. It continues up to "(int hit)" on the vertical plane, and a big arrow exits out the other side at upper left, labelled "(exit)". A dome shape sits where the two planes meet.

*(interpretation)* The interior is pictured as a separate plane "above" the exterior, matching the glossary's "interior hit from above": a strong shot passes through the hull, hits one interior cell, and carries on.

## Scan Topverse Test Notes (17).jpg

Single notebook page, titled "Seperated Cell DRCs" (sic).

**Seperated Cell DRCs**

*Diagram (top):* A dashed box labelled "DRC" (annotated "– total DRC area") containing two separate small squares that don't touch. Lines from both lead to the note "Only these two ext cells are built." A big double arrow points down to the second drawing.

*Diagram (middle):* A dashed box labelled "MDRC" with the same two squares, now marked "1." and "2.", each with hatched borders. They are joined by long rectangular lattice girders (zig-zag truss pattern) forming an L/Z-shaped frame, with corner dots and a bracket outline showing the overall rectangle. A pointer from below marks the girder.

- If DRC, do nothing
- If MDRC, put appropriate mobility coasters under every cell and draw a rect support frame above, connecting all cells together. using phantom girders / bio struts.

Should support
- Mechanical
  - various materials
  - various techs.
- Biological
  - various materials (bone, growth, strand)

- Mobility coaster, drawn under cell floor, but above surface terrain. Coaster appearance, size, texture depends on propulsion type e.g. wheels, hovercraft, wings, thrusters, seahull, UW hull/propeller, UG crawler, tank treads etc.
- Support framework connecting all cells, rendered above 1F, 2F casting a shadow on everything below it.

*Diagram (bottom right):* A larger rectangular frame with dots at the corners and a lattice of thin lines (girders) running horizontally and vertically, with small squares and × marks at their junctions. Several scattered cell squares sit inside it, some marked with ×, others blank, arranged irregularly (top right, centre, lower left as two adjacent cells, bottom middle). The frame ties all of them together.

*(interpretation)* "Phantom girders" and "bio struts" are the mechanical and biological versions of the connecting frame for an MDRC whose cells aren't adjacent. "1F, 2F" likely means first and second floor.

## Scan Topverse Test Notes (18).jpg

Single notebook page, titled "Vehicle/MDRC personnel class/role". No diagrams.

**Vehicle/MDRC personnel class/role**

- survival kit + signal/flare/comms/phone
- Hev suit (protection)
- Emergency Gun + Blade + Bazooka
- Thruster/jetpack/g-hook/skates/fins/ballast
- Life support system –
  - oxygen –temp –pressure –sustain –health
  - burden compared to dedicated combateer.
- Shield/Barrier/Bubble (extreme hazards)
- Temporary housing, water, rations, supplies, first aid
- Flashlight/speaker/Binocs/shovel/Pick/Hammer
- Scanner/survey equipment/analyser/3D printer
- Climb spikes/magnets/adhesive, forge
- Fulton balloon
- Wallet, ID, keys, cards etc.

inspiration: Knights of Sidonia personnel outfit
- Different tiers/techs/styles
- cost; cheap & weak, expensive & good.

*(interpretation)* "Hev suit" is likely the HEV suit from Half-Life. "g-hook" is likely a grapple hook. "Knights of Sidonia" is written "Sidonta" but clearly means the anime/manga. "burden compared to dedicated combateer" probably means the life support kit weighs on the wearer compared to a pure combat role.

## Scan Topverse Test Notes (19).jpg

Single notebook page, titled "Altitude Ranges (Fair/Balanced layer transitions in combat)".

**Altitude Ranges (Fair/Balanced layer transitions in combat)**

*Diagram:* A vertical altitude chart with a long double-headed arrow on the far left spanning the whole page (up and down). Three overlapping vertical bars show the range of each layer, stepping right as they go deeper. Each layer has its "home" point (marked with a small circle) and threshold ticks:

- Top: "(escape up)" with three small up-arrows above "10km" and a bar continuing up with "etc."
- "5km (drop from high atmo)"
- "o — sky" (sky layer home point)
- "(go high) +500m"
- "+250m (return surface)"
- "o — surface" (surface home point; drawn as a double horizontal line across)
- "(rise) –50m"
- "–100m ↓ (Dive)"
- "o — soil/sea" (soil/sea home point)
- "–500m (leave deep)"
- "–1km (GO DEEPER)"
- "o — DEEP" (deep layer home point)
- "–10km etc. (CRUST ↓↓↓)" at the bottom

*(interpretation)* Each layer has a band, and the bands overlap, giving hysteresis. From the surface you climb to +500 m to "go high" into the sky layer, and from the sky you must descend to +250 m to return to the surface. From the surface you dive to –100 m to reach soil/sea, and from soil/sea you rise to –50 m to return. From soil/sea you go to –1 km to enter deep, and from deep you rise to –500 m to leave. From the sky, 5 km means you've dropped from high atmo, and 10 km is the "escape up" threshold. This stops units flickering between layers in combat.

Boxed note: Altimeter + vertical speed

*Diagram (inside the box):* A small vehicle icon with sketchy motion lines above and below. Next to it: "^ 3502m" (current altitude with an up caret), "(50m/s)!" (vertical speed), and a row of "v v v v" chevrons below. An arrow from the motion lines is labelled "falling/rising visual effect".

## Scan Topverse Test Notes (20).jpg

Single notebook page, titled "Room exits onfoot (standard)".

**Room exits onfoot (standard)**

*Diagram (top left):* A square room with 3x3 small squares inside it: the 8 outer positions plus the walls. Arrows radiate out from every side and corner (8 directions). Two labels point at it: "Wall/Bound exit (full or partial)" (squares sitting on the walls) and "Underpassage" (squares inside the room).

*Diagram (middle):* A side/top cross-section of a boundary wall running across the page.
- Left part: a hatched wall with a gap where a thick bar sits lower. A big arrow points up through the gap, labelled "partial wall exit". Below is a small character (circle with head) and the label "projectiles & character collide" pointing at the hatched section.
- Middle: a long hatched section labelled "thick boundary wall" with two small circles (pillars or studs) on it. Lines from these go to the note "Can have material properties and be destroyable."
- A bracket symbol "] E" between sections (possibly a door frame).
- Right part: a thin line wall with diagonal hatching, and four big up-arrows passing through it. Labelled "full wall exit (more thinner boundary wall." A small character is below it. A note with a projectile icon reads "projectiles pass through." with "(but characters will collide.)" above it.

*(interpretation)* The two exits differ like this: on a partial wall exit, projectiles and characters both collide with the wall except at the opening. A full wall exit is a thinner boundary that projectiles pass through but characters can't, except via the exit.

*Diagram (lower):* A wall line with a small grid/striped block (a staircase or door) at the bottom with an up-arrow through it. Beside it are two round icons: one a cracked/rocky circle with an arrow, one a tent/arch shape with an up-arrow. Labelled "Bound wall reflects target cell locale enviro." with a bracket.

- Can have material properties and be destroyable. (doors optional.) locks too!

*Diagram (bottom left):* A small square with a scribbled dark blob (a hole) in it and an arrow pointing to the note below.

Under passage differentiate from holes by having a clear slope/stairs with respective direction of travel. In contrast, holes are just black pits with no bottom readily visible or very faint.

*(interpretation)* "Bound wall reflects target cell locale enviro." means the boundary wall's look matches the environment of the cell it leads to (e.g. a rocky look for a cave, a tent look for a camp).

## Scan Topverse Test Notes (21).jpg

Single notebook page, titled "Universal cross-char item inventory (on foot)".

**Universal cross-char item inventory (on foot)**

Sort of like backpack in pokemon/dungeon games with items that do meta-level functions, regardless of current role – though environment depended.

- Room network escape items (Return to tile travel mode)
  - Wall buster (surface) → *[tiny drawing: a charge on a wall with "3 2 1" countdown, an explosion, then an arched doorway]*
  - Drill digger machine (UG) ↑→ *[tiny drawing: a drill pointing right]*
  - Ballast dinghie (UW) ↑ *[tiny drawing: an inflatable boat/raft]*
  - Fulton blimp (surface) ↑ *[tiny drawing: a balloon with a basket]* (or jetpack)
  - Excavator bore (surface) ↓ *[tiny drawing: a boring machine with a drill head pointing down]*
  - LEO↑ shuttle / Deep sea↑ riser bell / Bedrock↑→ gnawer / Deep core penetrator
  - Orbital escape pod ↓ / Evacuation Rocket ↑ (space related)
- Health/status fix/boost related items
- Role 'resupply packs' / 'switch kits' (portable)
- Special artifacts, weapons, devices, tools, etc

Side notes (bracketed on the right):
- Next to wall buster / drill / dinghie: "Creates new Exit door at location, allowing immediate exit."
- Next to the LEO shuttle line: "(orbit to bedrock)" with a down-arrow to "Deep core penetrator".

= Not usable by =
- Pokemon/kaiju
- Minor vehicles
- Major vehicles/MDRCs

*(interpretation)* The arrows after each item show the direction of escape (up/down/sideways through layers). The LEO shuttle / riser bell / bedrock gnawer / deep core penetrator line gives escape items for orbit, deep sea, bedrock and core respectively. The bracket "(orbit to bedrock)" says that series covers the layers from orbit down to bedrock, and the deep core penetrator covers what lies below.

## Scan Topverse Test Notes (22).jpg

Single notebook page, titled "DRC/MDRC fleet exploration room network (ON FOOT)".

**DRC/MDRC fleet exploration room network (ON FOOT)**

*Diagram:* Room types connected by dashes in a chain:
- "E" a square with a circle: "entry (multiple)"
- "C" a long rectangle with tick marks: "corridor"
- "L" a square with an × and dashed edges: "location (multiple)"
- "T" a small square with ↑↓ arrows: "(Layer transit room)"
- Next to them: "(E & L&T have 8 door outlets)" with a drawing of a square divided 3x3 with dots at the 8 outer positions (centre empty).

- Random connectivity
- Multiple paths possible & likely
- Empty spots may be present too (minimal)
- Air & UG (soil) & UW (sea) are present too, usually there is an empty surface plot/room and user can enter another layer through it or via a "stairs"-like transit room. Air is only accessible via flight or scaffold dock (city only) or cliff.
- Room/corridor/hub theming depends on tile. City, forest, plains, mountain etc. + planned/unplanned (official/unofficial) (catwalks or wild trails?)

*(interpretation)* Entry, location and transit rooms are 3x3-cell rooms with doors possible at each of their 8 edge positions. Corridors link them.

## Scan Topverse Test Notes (23).jpg

Single notebook page, titled "Emergency escape (room network on foot)". The "y" of "Emergency" is overwritten by a slash.

**Emergency escape (room network on foot)**

*Diagram:* A square room with a stick figure in it.

- Any room, any time – if user has special item they can get out back into the tilemap region to travel elsewhere.

**Wall Buster**

*Diagram:* Three-step strip: (1) a stick figure places a charge (arrow/cone shape) on a hatched wall, (2) "Boom" with an explosion burst on the wall, (3) the figure stands next to the wall, which now has a darker hole section with a dashed outline (the new area).

- New area created (collider zone to exit)
- Hole sprite overlay on top of wall.

**Drill**

*Diagram:* Four-step strip: (1) a figure holding a drill faces a hatched wall, (2) the figure moves toward the wall with a dashed line, (3) the figure drills into the wall with a burst, (4) the wall is left with a hole and dashed outline.

- leaves a hole behind (Multiplayer)

Aim at wall, shoot, go through.

**Fulton Blimp/Balloon (Not instant)**

*Diagram:* Three room squares: (1) a figure with a balloon attached above, (2) the figure lifting up with motion lines, an attacker shooting arrows near it, labelled "Rise in Altitude until threshold (still shootable) (balance delay)", (3) the room empty except for faint marks, labelled "Gone."

- Altitude rise goes through all layers – (UG, surface, sky) full exit once top of sky reached

*(interpretation)* "Leaves a hole behind (Multiplayer)" likely means the drilled hole persists so other players can use it or see it.

## Scan Topverse Test Notes (24).jpg

Single notebook page, titled "Regional Pokemon Fear/Loyalty Behaviour Index". No diagrams.

**Regional Pokemon Fear/Loyalty Behaviour Index**

\* General human attitude
\* Faction specific attitude (override)

- Initially an area may be wild and untame, so PKMN may approach and attack humans like predators.
- If retaliated, fear will grow and they will avoid humans unless one is obviously weak and alone.
- If tamed (feed (or give something nice) while set boundaries to/by blocking/dodging their attacks, and not counter attacking.) then PKMN will become friendly and allied to humans or faction.
- If faction tamed PKMN sees/hears/feels its people hurt/attacked by others, it will come to aid to heal, defend, attack or harass.
- The fear/loyalty values are region-specific.

*(interpretation)* "dodging" is written beneath "blocking" as an alternative, and "attacked" is written above "defend" as an insertion after "hurt" in the previous line ("hurt/attacked by others"), though it could also be read as "defend/attacked".

## New terms

- **Entrance cell → 3x3 interior cell rule**: already in the glossary, but stated here as a hard cap: "Building/Vehicle cannot be larger than entrance cells allow".
- **Shift door / swing door**: interior door types. The shift (sliding) door is the common one.
- **Full border segment vs individual border segment**: border walls are placed as whole-side segments ("yeah"), not piecemeal ("nah").
- **Solid block (armor), armor wall segment, support armor pillars**: interior armour pieces that protect occupants from penetrative hits (the "fuses" in the glossary).
- **Vehicle Entity**: the simple rectangular true-shape collider of a vehicle. It has universal HP plus optional module "Armor HP".
- **Overlay Facade**: an optional freeform art layer drawn over the Vehicle Entity box. Weapons/systems can render above or below it.
- **Firing offset (FRONT/MIDDLE/BACK × L/C/R)**: user-defined weapon firing positions on the vehicle box.
- **Separated Cell DRC**: a DRC/MDRC whose entrance cells aren't adjacent. Only the occupied cells are built.
- **Mobility coaster**: the propulsion visual drawn under each MDRC cell floor (wheels, hover, wings, thrusters, seahull, UW propeller, UG crawler, treads).
- **Phantom girders / bio struts**: the support frame joining separated MDRC cells (mechanical / biological). It is rendered above floors and casts a shadow.
- **Combateer**: a dedicated combat role (in contrast to vehicle/MDRC personnel).
- **Altitude thresholds (layer transitions)**: sky / surface / soil-sea / deep home points with overlapping enter/leave thresholds (+500 / +250 m, –100 / –50 m, –1 km / –500 m, 5 km, 10 km).
- **Wall/Bound exit (full or partial), Underpassage, Hole**: the standard on-foot room exit types.
- **Universal cross-char item inventory**: a backpack shared across characters for meta-level items (escape items, health, role resupply/switch kits, artifacts).
- **Escape items**: Wall buster, Drill digger machine, Ballast dinghie, Fulton blimp, Excavator bore, LEO shuttle, Deep sea riser bell, Bedrock gnawer, Deep core penetrator, Orbital escape pod, Evacuation Rocket.
- **Room types E / C / L / T**: entry, corridor, location, layer transit room. E, L and T have 8 door outlets.
- **Scaffold dock**: city-only access point to the Air layer of a room network.
- **Fear/Loyalty Behaviour Index**: region-specific PKMN attitude toward humans, with faction-specific overrides.
- **LEO**: low Earth orbit (escape shuttle).
- **Hev suit**: likely the HEV suit (Half-Life reference).

## Open questions

- Scan 13: the meaning of the radiating-dash sketch "2." is unclear (blast spread, or the cell grid?). The small object at the bottom-left end of the arrow is too small to identify.
- Scan 13: "2ent = 2^(3x3) int cells" is read as 2 × (3x3), but it is written as a superscript.
- Scan 15: one word after "Vehicle" is scribbled out and unreadable.
- Scan 20: the "] E" bracket symbol between the wall sections is unclear (door frame?).
- Scan 21: it's unclear whether "(orbit to bedrock)" annotates the whole LEO/riser/gnawer series.
- Scan 24: placement of "attacked" (after "hurt" or after "defend").

## Cross-references

- Scans 13–14 add detail to the glossary's DRC/MDRC model: entrance cell = 3x3 interior cells, one-way drop-out exits through broken boundary walls, interior armour/struts as sacrificial "fuses".
- Scan 16 is the source of the "Interior hit / hull hit" glossary entry. It adds that the hit picks a random interior cell, damages occupants in random order, then can exit the opposite side and hit another target.
- Scan 15's "Vehicle Entity + Overlay Facade" refines the glossary's "Facade (the zoomed-out vehicle-combat look)".
- Scan 17 extends DRC entrance layout to non-contiguous cells, with mobility coasters for MDRCs.
- Scan 19 gives concrete transition numbers for the glossary's vertical layers (sky, surface, soil/sea, deep, crust). The layer names here differ slightly ("soil/sea", "DEEP", "CRUST") from the glossary list (shallow/soil, UW, UG, bedrock, depths).
- Scans 21 and 23 detail the glossary's "Fulton balloon / blimp" escape item and add a whole family of escape items. Scan 18 also lists the Fulton balloon in personnel kit.
- Scan 22 refines the Syndemic-derived room network (glossary) into E/C/L/T room types for DRC/MDRC exploration, with layer transit rooms linking Air/UG/UW.
- Scan 24 ties into the Pokemon TCG subgame and the factions system. It fits the "equilibrium universe" idea (wild PKMN only become fearful or allied through player action).
