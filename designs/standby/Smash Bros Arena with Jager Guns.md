# Smash Bros Arena with Jager Guns

## WIP name:
AAL Smash Droids: Vibranium Knockout Arena

## Summary
Imagine super smash bros gameplay, but have a humanoid single character (customizable) 32x32px style, like Jager and attacks are done with guns/melee weapons instead of innate abilities. They can have loadouts for jump type (double big jump, triple medium jump, quad small jump, kirby style fly) and a basic mouse direction based smash attack (also loadout based). Maybe some body loadout pack too for 'more weight less speed', and similar class types. sort of a build-your-own-character combined with a vast arsenal of guns that players can discard and swap during combat. Players can only carry two weapons at any given time and only use one of them at any given time (requiring a swap that may have a "equip" time, based on the weapon being pulled out), so its about clever positioning, aiming, resource use (what you have and what you can get around the level) and trying to hit the opponent without getting hit yourself by using terrain, mobility, abilities or waiting for the opponent to be caught in a delay, like reloading a weapon or having a cooldown period.

Game would use Jager Guns and Jager Melee as the main attack method to increase vibranium charge in the bodies of android fighters; more hits = more vibranium instability = knockback sends further.

Damage splits into two types:
light-hits = increases vibranium charge in character, but doesn't launch with a knockback, if barely.
smash-hits = increases vibranium charge greatly and also launches character with knockback.
also theres:
kill-hits = can break the character if integrity/hp threshold is surpassed with a strong enough hit/impact. Or crushed.

If knocked out, the vibration will finally dissipate due to combat mode turned off to resist damage (armor works sort of like Phase Shift in Gundam Seed - its only active when powered and provides maximum protection, but if turned off, its basically just regular titanium/aluminum in strenght, easily dispatched. You could say any "damage" taken while Phase Shift is on will increase a kind of "heat buildup" that makes the armor more critical the more it takes damage. Although instead of heat, its more about stored momentum/vibration/tension that gets released into the armor. If safe and out of combat, this dissipation of force can happen safely without character being kicked off into orbit or the non-powered armor shattering/tearing from the "release".)

There are some difference compared to Super Smash Bros's mechanics and system to allow for ranged weapon combat to be feasible and not become annoying, such as reworking hitstun mechanics, dodging/shield, mobility to use mouse aim + hotkey for "jumping/dashing" towards a location instead of the usual press W to jump upward - possibly to support micro-gravity arenas or reversed gravity arenas etc.

## Plot
While testing an experimental armor frame android, the developers/engineers/scientists notice that while extremely durable, even comically so, it has the unfortunate side effect of becoming easier to blast off into the far horizon unintentionally if hit too hard after accumulating enough "vibration" from most impacts, damage and hits. Deemed unusable for conventional combat due to how easily it accumulates the damage from almost everything mildly hazardous, it was nevertheless repurposed for a fun android battle arena activity where remote operated humanoid bots duke it out in makeshift arenas with hazards just to see the androids blast off and fly away at comical speeds. Someone on the team remembered the game "super smash bros" or "brawlhalla" and everyone rejoiced at the idea to make it a real thing for sake of entertainment and lulz.

## Gameplay
Sort of like Duck Game with various random guns on a smash-bros esque arena. Players spawn at spawn points ala Unreal Tournament/Smash Bros and proceed to use their pre-selected favorite loadout of primary wep, secondary wep, aux reusable/passive ability, aux consumable item, jump type, smash punch, block type. Goal is to defeat other opponents by raising their damage and finally knocking them away with a smash hit or somehow making them go off screen otherwise. Primary/secondary weps can be dropped/thrown/swapped with other free guns or melee weapons on the level. Dedicated melee weapons (swords, hammers, etc) are often way better than default smash punch in some way.

Controls and combat feel mildly like soldat or Halo:CE; WASD to move/jump/crouch, mouse to aim/shoot/punch(or block if holding melee), QEFRZXC for weapon handlings(switch, drop, throw, swap, interact/use) or item/ability use and block/dash/sprint.

There may also be different android variants that have different designs for different playstyles with pros and cons, like the typical light/medium/heavy stuff, but with the caveat that more armor/health/damage requires adding bigger or more weakpoints to exploit compared to lighter/frailer classes, mainly because playing as a faster class requires more effort on the player's part to defeat a tougher opponent, so having exposed weakpoints or some other mechanic that inconveniences a heavier class for the price of being durable is necessary to attain balanced gameplay.

## Resources
This one is tricky. Having ammo will help with balancing some weapons, allowing them to be more devastating and unrestricted. Not having ammo will force arbitrary balancing, but the characters needing only to focus on combat without worrying about resources is a good thing.

One solution is to have regenerating ammo and ammo replenishment boosters. Ammo regen can be per round per X milliseconds while not firing with a delay before ammo regen kicks in. Deadlier, faster, more forceful, bigger and easier-to-use weapons would have bigger "penalties" compared to weaker, slower and hard-to-use weapons.

Halo style:
Start with a loadout of fully loaded primary and secondary, but no ammo regen but you can still find small or big ammo packs to replenish occasional ammo if its the right type. Player is forced more often to ditch their spent weapons and keep adapting to whatever they pick up to keep fighting. Spent weapons stay on the level until they get pushed away, or thrown hard at something enough times, causing them to break, or looted and kept safe until new ammo is found for them.

Hotline Miami style:
No ammo reloads for weapons, but there are more guns thrown in to the level to offer replacements when ammo runs out of current guns. Weapons can still be thrown/dropped even if they have ammo in them, but weapon have different durabilities that will cause them to shatter/explode/break after they endure enough hits.

Smash Bros style:
No ammo management at all, but weapons are now strongly balanced out/nerfed to compensate for infinite attacks. Weapons have soldat style refire and reload and prefire delays that determine their usage. Unlike soldat, weapons will continue to complete their reload process if they're stashed/swapped away into inventory. Weapons will pause their reload process if dropped or thrown away.

Like in soldat, if both primary/secondary weapons are discarded, then player can use primary fire click to try to slap the opponents weapon from their hands (with a 1sec per try "rate of fire").

Either way I'll have to revisit which one I should choose out of those 3 styles. I'm also wondering if I want weapons to have secondary firing modes or not. All this will ofcourse determine what the final player controls would be.

## Arena Design
Might take some design hints from how Soldat2D did map design; have corners, curves, hills, obstacles, and projectile-only colliders to break up line of sight. Weapon ranges are also greatly stylized to emphasize distance classes more arbitrarily, like making a big arena be like 100 meters accross and a sniper rifle's range would be 150 meters (ultra long range), a long range projectile weapon would be 60 meters, medium would be 30 meters, short would be 10 meters, melee would be 3-1 meters - or something akin to that kind of forced design to compensate for the smaller sizes of arenas vs what the true ranges of such weapons would realistically be.

Could also have breakable cover objects like reinforced crates, barrels, boxes, tables and glass that could be used as temporary cover during a firefight to avoid being hit, until those things break.

Player movement vs weapon usage speed vs projectile speeds would also be more attuned to the realities of this arbitrary arena combat space. I'd make players move relatively slowly and floaty-like so they're not annoying to hit, but projectiles would be mildly slower than they realistically are to allow some semblance of dodging, meanwhile weapons themselves would be nerfed by having them turn at their own rate to face the mouse aim crosshair, so slower weapons would be slow and deliberate to face the direction the player is aiming at. The point of all this is to avoid the game being too fast/twitch-reflex based in favor of a more comfy pace of gameplay that values more tactical thinking and strategy than just pure skill and reaction speeds.

## Game Modes
- Arena Tournament Gauntlet - basically floppy heroes or traditional smash game campaign. Gauntlet of random stages until a souped up final challenger.

- Boss Hunter - linear levels gauntlet with a randomized house-boss opponent awaiting - inspired by Robot Wars with stuff like Sir Killalot, Matilda, Sgt. Bash, Shunt, etc. Except they have modules and randomized equipment. 

- Weapon gallery - just a fun lab to test various guns against destructible things like that street fighter 2 car wrecking stage, where once the car is broken layer by layer, the engine block is exposed and it can be whacked around with knockback to send it off stage like a player knockout event. Dunno about having a timelimit for it, maybe calculate performance/score somehow else, maybe DPS, but it doesn't fully capture all aspects of how difficult it is to use the weapon or what drawbacks it has that in the absence of taking those into account would give a skewed performance rating for that weapon. Dunno, I gotta brainstorm this more.

Both arena and boss hunter could be made a multiplayer coop thing too. I kinda want to avoid pvp, but maybe I could genuinely frame it as a sparring to prepare against tougher opponents type of thing and thus have a fourth game mode for it. I'd explicitly make it called "Spar Training" and encourage helping the other person grow without making it being about degrading each other - maybe making it all be framed as a "dance" where both sides need to become better and attain equal score instead of the other hoarding the K:D ratio. Not sure, I need to think on this idea more.

## Content
Typical gun and melee stuff with using the chests as drops, ammo containers for refuel, all the stats of damage, rate of fire, reload, range, etc. All based on the Jager spritesheets for all those.
Player sprites could be any 32x32 pixel image of any kind of character, plus having 2 rayman style hands to place upon the weapons when they're holding one. Weapons are a separate sprite btw. Player can choose to hue-shift the character sprite and apply a color tint to their hand sprites. Player can also choose HUD color, as it works similar to Fallout 3's recolorable monocolor hud.
Stages... I could make hand crafted arenas, but they would have zones where random extra things would spawn, so while stages are always the same, they differ in each playthrough.
Powerups could be a thing too; medkits, ammo/item supply packs, temporary stat boosters (speed, damage, rof, jump height, -multipliers etc.)