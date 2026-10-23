# Trash Miner Web Game

## WIP Name
AAL Trash Miner: Landfill Recycling Bonanza

## Premise
Old landfills decades/centuries ago need to be reopened and the materials/riches recycled out of it - both to gain valuable resources and to heal/restore the land for future wellbeing. Gameplay involves a hazmat dude on a bulldozer pushing around piles of junk/compost/material with satisfying physics interaction, like plowing the bulldozer into a sea of trash and push as much of the stuff into whatever disposal spot (for the material to be sent for reprocessing) it needs to be delivered to.

By doing this, the player progressively earns upgrades to increase the size and power of their bulldozer, while encountering bigger piles, heavier stuff, more numerous stuff, longer distances, special conditions or hazards.

Game sort of promotes positive values of recycling, taking care of environment and reducing waste. It both shows that landfills are nasty and makes it satisfying to decompile them to eventually change a ruined location into a good healed one.

## Original inspiration
I saw ads on reddit for a game called Zombie Miner, which had a bulldozer push ores and gems into a grinder for coins. Coins were then used to upgrade the bulldozer into a bigger one, or buy larger/wider bridges so that it could handle more weight and have more space for more ores to be pushed over it at once, or unlock a new set of resources to mine, buy shortcuts, conveyor belts, bonus structures and such. The appeal of the game was mainly with the satisfying act of pushing physics enabled chunks/spheres that represented resources, the ability to upgrade the dozer and be able to push more stuff faster and bigger, while unlocking even bigger hoards of resources to collect.

The problem with that game is:
- premise is stupid; zombie miner collecting gold, makes no sense, no sense of meaning why I should play it.
- game is about endless greed; player is tasked with continually getting more gold for the sake of more gold, thats not a sustainable nor healthy goal.
- a lot of the game is built around pre-built handmade maps; those are expensive to make and not that fun to replay. A procedurally generated map solution is needed.
- theres no infinite metagame here, just a gauntlet of prebuilt maps. Needs an infinite metagame to provide meaning and be a generator for campaigns that are gauntlets of proc gen maps. Standard Reactorcore's design mentality stuff should be applied here.
- the ads were clearly prerendered, so they were likely cheating in showing what the actual gameplay or performance looks like. Either way I need a solution that have the "push thousands (or more) physics objects around a level into a collider/area" work reliably with 60fps, even if it gets crazy. If thats unfeasible, then I need a different setup that achieves the gameplay of moving stuff with physics in some satisfying manner.

## Art style/visual setup
a top-down or isometric view, probably using lowpoly 3d assets, built with Asset Forge program or using pre-existing 3d lowpoly assets. Alternatively a 2D top-down solution could work too, but I'm leaning towards lowpoly 3d with simple/basic arcade physics; bulldozer/plow is just cube/box, while chunks are just spheres or points with a radius.

## Low & High Metagame
Low metagame is about a campaign of tackling a single landfill where each sector is a separate level. Player clears it, gets close to the core where more dense and more uhh... juicy/valuable/horrid stuff is? Each successfully cleaned landfill earns a satisfying "completed" mark on the player log in the high metagame.

High metagame is about clearing multiple landfill over a vast region in different towns, cities, etc. City names are randomized and maybe even occasionally comically funny and local-sounding (based on where the game is localized). Like in low metagame, each successfully cleaned town/city/area earns a satisfying "completed" mark on the global player log.

Part of me thinks about adding ranks to the high metagame, but I really don't want player chasing nonsense titles and medals to their name. Maybe instead just show an overworld of regions that start off all sickly, poisoned and ruined by landfills turned into clean beginning-to-heal nature zones with organized looking recycling centers creating new sources of raw materials for those areas, even if its just a visual thing.

I'd like each campaign to have a supercore inspired system where each campaign has a unique quirk to it that a player can loot for some kind of ingame benefit which they can then bring over and stack with another such bonus artifact in another campaign. These artifacts degraged after some campaigns, so player always cycles between different sets of artifacts per campaign that changes things up. Maybe I should even take inspiration from corruption cards so that they're actually detrimental temporary curses inflicted from the past that the player unleashes upon themselves as they open up new landfills and the icky horrors they contain. These curses could either affect the trash chunks, the level as a whole, specific level hazards, chaotic weather events or other ambient events or affect the player directly somehow.

Player gets really down and dirty during the job so it takes a while for these "curses" to wear off. Kinda also drives home the point of how bad of an idea landfills are in this way.

## WIP todo:
- content (player, upgrades, trash types, hazards, goals, levels, campaigns, etc.)
- ask AI to see feasiblity stuff, improve design, suggest ideas