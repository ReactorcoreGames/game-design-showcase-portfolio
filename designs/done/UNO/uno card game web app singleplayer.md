# Project Super UNO
(Note: UNO is probably a trademark and mau-mau sounds like some sort of silly cat sounds and thus feels lame for this game, so I'd need a completely new name for this game. If theres different variants with different context/theme, then maybe those could influence the name.)

I'm thinking about making a UNO card game clone on PC as a singleplayer game with all the mechanics and content from the original game, but with perhaps new ideas, new mechanics, new cards and a lore context that would make sense with Uno's gameplay of 2-6 players taking turns to eliminate each other by getting rid of their cards while avoiding to accumulate them.

I'm essentially aiming for something that feels like an mega expansion pack in terms of card types in the deck but still streamlined; easy to learn and effortless to play as the original UNO.

It should have an infinite persistent "high metagame" that ties all matches together to a sort of "worldmap" thing that works as sort of a "local area campaign/gauntlet" generator as the "low metagame" and they somehow of feed into each other with outcomes from low metagame influencing the high metagame, while the high metagame influences the low metagame in what it offers next to the player.

Player would boot up the game, enter the worldmap and then be given a choice of what kind of session they want to play and whatever they choose will still count towards the persistent high metagame that shapes something on the world map.

Additionally there could also be a trophy log with replayable seeds + exaggerated memories effect to make everything feel 3x bombastic and crazier in some regards.

## Tech (not relevant for the game design showcase page)
I know the document says "web app" in its filename, but I'm open to this being a portable-install standalone singleplayer PC game with local folder for savefiles to make the persistent stuff work - though since this game will not contain modding and technically it *is* possible to have persistent savefiles even with a offline downloaded copy of a html5 webgame, I'm not writing the web app thing off either. Dunno, up to you. 

The graphics/visuals could be handled with pure code-driven art + particle effects + screen effects, so technically the project could even survive/thrive without a needing a single png/jpg image if need be (not necessarily, but its an option).

I'd bring sound effects into the project as needed with a "reuse, reuse, reuse" mentality to do more with less, yet still achieving good levels of "game juice feel". 


## My ideas
- Check Pokemon TCG trainer cards for ideas
- Shields/dodges/deflects/redirect/parry ala nanaca crash usables/consumables
- Spy/reveal
- Abilities vs consumables?
- Abilities have requirements to use.
- Abilities/passives = super cores? (For metagame purposes)
- Abilities inspired by advance wars CO powers?
- Like the old mobile game uno knockoff I had where I try to shed all cards while trying my best to ensure opponents have more cards when I shed the last one, the point system counts the card values and if some reaches a score they are eliminated from the game.
- Reactive characters with facial expressions of: idle + idle side glances, card lift neutral/disgust/excitement with % to show their true feelings, anger/dissatisfaction on hit by opponent, happiness on win, smug when laying an attack card, knockout on elimination, out cold when out of game.
- Player can choose their character ala street fighter or mortal kombat.
- Randomized encounters, with 2-6 players, team or free for all, extra cards, extra rules, starting cards amount, start with special curse/nuke card, etc. 
- World map with nodes, continues, ala SMB3 (Super Mario Bros 3).
- Final bosses with extra consumables or other passives.
- Up to 8 color suites (rainbow+brown)
- Dual/triple/quad color cards
- Pokemon inspired Elemental cards - fire, water, plant + electric, ground, psychic, metal. (See addon doc)
- Atomic card ("jack" card from mau mau that doubles damage to opponent players if played/used as last card)
- Knockout rule: if player accumulates 25-50 or more cards, they are eliminated from the session.


## Loose list of context/title ideas
(This is the "rename UNO to something else" section + give it meaning/framing for the high/low metagames. That said, my ideas here are unrefined/vague.)

+ Bonfire: Cozy Card Battles
(Bunch of friends sit near a magical bonfire and throw "cards" into it to have something cool happen. Cards are sort of (elemental) firewood/fuel and they change the nature and color of the flame, blessing or slapping the player as per typical UNO gameplay - but its more of a friendly cozy game of being together and having fun (common activity, the bonfire results in some procedural lightshow, so this game isn't exactly about winning/losing, but playing, building up something neat and having it play out with longer matches creating a longer and more impressive firework show of some sort. Maybe the common draw pile/deck is some orb that hovers above the bonfire as a component/complement to it.)

+ Ultimate Card: Wizard Singularity Supremacy
(Bunch of competing wizards are in a quest for ultimate power and they're battling against each other by casting a singularity together (as the discard card pile) which is fed elemental attacks and everyone is trying to line up their final card to trigger something that lets them claim the amassed power. Each wizard has their own random deck that is contributing to the total set of cards - maybe has deck-building elements similar to Pokemon TCGs rules but for UNO card decks? Maybe this works sort of like Street Fighter 2's inspired singleplayer campaign thing?)

+ Power Pile: Who Takes it All?
(A bunch of hopelessly greedy gamblers get together to throw cards into a pile to try to win it all to themselves as per typical UNO gameplay. Longer games encouraged for bigger pile accumulation for bigger bang/reward. Maybe has a bank vault and trophy room element that is about celebrating gained prestige, power and wealth?)

(I think all three games might be worth making, each gathering all the available pieces and nuggets from this document and picking the ones that they will benefit from the best, then tailoring a suitable high metagame (overarching, infinite) & low metagame (local, finite) setup per game. Under the hood they'd use the same foundations, but would be 3 different games with their own art-styles/mood/feel/menus.)

(Regardless, all would still try to make it as content rich as possible and greatly expanded compared to regular UNO/mau-mau. Obviously some systems like opponent HP makes more sense in the more competitive variants and the others.)


## Regular ruleset:
- Based on what is on the pile, play that color/symbol/element/number or a wild card.
- Player can play multiple cards of the same number as a bunch/set/cluster, arranging their order to be whichever they want the top most card to be. Applies to action cards too. (Rummy rules)
- If no cards, pick up to 3 cards from deck and end turn if none. If one did then play it (optionally).
- If card has an attack (block, draw +2, etc) then next player in turn can shove it to the next player in order by playing a similar card type with same symbol (draw +2, block), passing the accumulate draw + amount upon the last player that can't keep passing on the stack chain. (Reverse doesn't apply, it isn't an attack card).
- Otherwise just play one card per turn and try to strategize that you shed your last card with opponents having more cards and/or for pile to be as big as possible upon your victory.
- At start player can also just draw up to 3 cards from the deck instead of playing one even if they already have one.
- Cards in deck have rarities.
- Common - numbers 0 to 9
- Uncommon - block and reverse, draw +1, etc.
- Rare - draw +2-3
- Legendary - wild cards, super cards, etc.

(In this my game, deck is infinite and pile starts from nothing and grows with more cards, virtually forever. Deck thus does not run out and pile does not get reshuffled into a deck at any point. Performance wise it's lightweight, no cards are tracked except for elemental pileups as a separate markup, otherwise it's just "248 cards in pile" variable, with an upper limit that will stop the game at 999 cards, should it ever get that high. Whoever had lowest cards/points wins in such scenarios.)

Note: yelling UNO is not necessary in this game. Auto warning appears when a player has one card left. That said, a player can win by offloading more cards during their turn to win too. Maybe have a benefit for reserving one card to finish with it as a risk-reward choice, like 50% more damage bonus to opponent.


## Modes
- Free for all - typical uno
- Teams - uno where atleast one side has 2 players. Typically 2v2, 1v2, 3v3, or 2v2v2, 2v3, 3v4, etc. Fair-ish teams, so 3v1 is not ok unless handicaps are introduced in a David vs Goliath style. Friendly fire is on.
- Conspiracy - random alliances, but backstabbing aplenty, friendly fire on, or teams, but turns are not team1a>team1b>team2a>team2b, but instead team1a>team2a>team1b>team2b.
- (Ehh, Maybe teams is friendly fire off so action cards only affect enemy, while conspiracy is ff on.)
- Player count 2-8 players, maybe 2-6.


## Card types
- Numbers 0-9
- Reverse
- Targeted reverse (lingering effect system needed to support this functionality)
- Skip/double turn 
- Targeted skip
- Draw+N
- Targeted draw
- Wild color (user choses color)
- Wild color draw until color gotten or up to 10 cards
- Shield - blocks/absorbs action card, nullifying it's effects (skip, draw).
- Deflect - the NO U card, sends effect of action card back to who put it.
- Redirect - like deflect, but you can choose who gets hit by it.
- Parry - like deflect but doubles the counter attack effect. No u on steroids, basically 
- Dodge - let the next player get hit by the effects of the action card.
- MAD card - curse card, force everyone to draw +N cards, user is spared if it's their last card.
- Dark/Light switch (UNO flip) card.
- Ability use card (use an ability card in secondary inventory load out, not part of regular play cards, they're sort of like artifact cards, but player gets to customize their player character like AW:DS let's me equip skill bonuses).
- Apoc Card - Flip coin 3x to maybe draw 25 cards (7/8 chance to be dud)
- Burden card - curse card, using it forces user to draw 10 cards, even if it's their last one.
- Swap hands with next player
- Swap with targeted player
- Swap all hands in the direction of turns
- Reveal n trade+N - next player has to show you their hand and you get to give them random card and they give you the specific card you want from them.
- Trade targeted.
- Reveal and steal - unlike trade, you grab their card without giving one to them. Technically a net loss but you can disarm them of a super card that way.
- Give+N - directly give cards to next player.
- Give Targeted - same as above but choose who gets it.
- Show hand. - reveal next players hand and keep it visible until their next turn when they can resume their privacy.
- Show hand targeted.
- Show all hands. Everyone including you will reveal their hands until your next turn.

(All above may have a combo that combines two, three or even four effects into one card, either 1 type of effect x times or x types of effects per 1 time.)

**Variants:**
- One color
- Black color (any/joker/choose color)
- Dual color flex
- Tri color flex
- Quad color flex
- Hidden power flex (can't use it unless condition is met)
- Draw 1-10+
- Skip 1-3 or all (double turn)

**Other:**
- Artifact cards/supercore cards (see: Supercore concept, its recorded somewhere).
- (+1 to all draws)
- (-1 to all draws)
- (All X cards have Y ability/action)
- (Reveal a hand)
- (Reveal all hands except own)
- (Never reveal your hand)
- (Limit no suitable cards draw to 2 or 1 before turn end)
- (On your turn always or optionally start by placing a card directly from draw pile to discard pile)

**Color modes:**
- Classic 4 rgby (red green blue yellow)
- Extended 6 rgbyop (orange purple)
- Maximum 8 + 2 (teal brown + black and white as wild cards)
- (Flipped versions use inverted colors/layout)
- Elementally charged (water, plant, fire, electric, ground, psychic, metal, fairy + dark and light)

## A List Of UNO Variations
(I saw this list online - could work as a bunch of "mutators" that the low metagame could occasionally have if the "give me a chaos game" option is chosen on the high metagame screen.)

```
UNO Buffet
Instead of starting with the normal seven-card hand, players start out with a buffet-friendly 10 or 20 cards. While this can be a heavier start, it also leads to some more dramatic runs of playing like numbers, especially If you are allowing stacking (which the company has stated over and over again is not allowed).

UNO Extra
For the people who like to add extra hot sauce onto their chips, this version of UNO is spicy. Set new extreme action cards, like +3 or +6, have skips that go over two players, and add freezes that knock a player out for two or three rounds of play. 

UNO Flip
In this variation, players flip the draw pile instead of drawing from it. This means that the top card of the draw pile is revealed and then placed on the bottom of the draw pile, creating a new top card. Players must then play a card that matches the new top card by color, number, or symbol.

UNO M.A.D.
With this UNO variation of Wild Draw Four, we bring back the fun of the Cold War with Mutually Assured Destruction. By playing the designated Wild Draw Four card, every player draws four. The only exception is that this card can be played as the final card of the hand, letting the winner claim triumphant victory as everyone else draws four.

UNO Matchmaker
In this chaotic version of UNO, players who see that their exact card has been played (a green 4, a red 2, etc.) can play theirs on top of it – no matter where they are in the flow of the game. If you successfully play your card, play resumes within the flow of the game.

UNO ONU
In this Bizarro world-variation of UNO, players try to accumulate as many cards as possible. Play goes on until there are no more cards in the deck, and the player with the most cards wins. 

UNO Points
Similar to hearts, this UNO variation has players earning point values for the cards in their hands after each game. This is a great way to play if you’ve got people who can’t always seem to win, but get close – this will reward them for keeping their card count low. Each number card is worth its face value in points, and each Skip, Reverse, and Draw Two card is worth 20 points. The player with the lowest score after the chosen number of rounds wins the game.

UNO Race
This variation of UNO is played in teams, with each team trying to get rid of all their cards first. A minimum of four players are required. Teams work together to play cards and strategize to get rid of their cards as quickly as possible. Team stacking is allowed, so if one player plays a 2 and the teammate also has 2s, they can stack immediately before the opposing team plays.

UNO Red Zero
UNO can’t always be about making other people draw cards. Sometimes, bad luck falls on the cardplayer. With UNO Red Zero, the red zero is the doomsday card. In order to play it, you must first draw ten cards.

UNO Rummy
This variation involves forming sets and runs with the cards in your hand, similar to the game of Rummy. Players must try to form sets of cards with the same number (e.g., three "4" cards) or runs of cards in the same color (e.g., a red "3," a red "4," and a red "5"). When a player has formed a set or run, they can lay it down on the table and draw new cards to replace them. The first player to get rid of all their cards wins the game. In this instance, UNO must be declared when a player is working on their last set of cards, e.g. all one type of number, or a run of the same color.

UNO Silent Sevens
Once someone plays a seven, the game becomes silent until another seven is played. Anyone who speaks has to draw a card. If it’s time for UNO, you raise one finger.

UNO Stack
Ah, the infamous stacking rule for UNO. Though not an official rule, it’s included in most home versions of UNO. Essentially, it involves stacking cards that match – either in color or value – on top of each other. This includes action cards! So if someone plays a +2, you can stack a matching +2 on top of it, and so on until it isn’t matched. If a player cannot play a card, they must draw one from the draw pile or comply with the action cards.

UNO Swap Hands
You start this UNO variation by designating a number. Once that number is played, its player can choose to swap hands with another player. The players then continue the game with their new hands. If you choose to swap with a player who has just one card, “UNO!” must be declared at the time of the swap, or you’ll have to face the typical four-card penalty.

## Uno wiki
Uno includes 108 cards: 25 in each of four color suits (red, yellow, green, blue), each suit consisting of one zero, two each of 1 through 9, and two each of the action cards "Skip", "Draw Two", and "Reverse". The deck also contains four "Wild" cards and four "Wild Draw Four".[5] Sets manufactured since 2018 include 112 cards, adding one "Wild Shuffle Hands" and three customizable Wild cards.[1]

Seven-O: Every time a "7" is played, whoever played it must swap hands with another player of their choice before ending their turn. Every time a "0" is played, all players pass their hands to the next player in the current direction of play, after which play continues normally.[5]

Jump-In: If a player has exactly the same card (both number and color) as the top card of the discard pile, they may play it immediately, even if it is not their turn. Play then continues as if that player had just taken their turn.
```


## Chats with AI for research
I chatted with ChatGPT/Deepseek/Perplexity about UNO/mau-mau to map out what exists in existing uno and what new ideas could exist.

### ChatGPT
```
UNO (mau-mau)

==

Here are some ideas for new cards and mechanics you could introduce in your Uno-inspired game:

- **Swap Hands**: A card that forces you to swap hands with another player (or an AI opponent) when played.
- **Peek**: Allows you to look at the top three cards of your deck and choose one to keep in your hand.
- **Shield**: Prevents the effects of any power cards played by other players for a single round.
- **Copycat**: Copies the effect of the last power card played by another player.
- **Shuffle**: Forces all players to shuffle their hands and draw a new hand of seven cards.
- **Pass On**: Allows you to pass on the effects of a power card to another player instead of taking the effects yourself.
- **Double Down**: Lets you play two cards on your turn instead of one.

Feel free to mix and match these ideas, or come up with your own to create a unique and engaging gaming experience!

== (me: give me even more ideas)

Of course! Here are some additional ideas for new cards and mechanics:

- **Wild Choice**: A wild card that lets you choose which color will be played next, similar to a regular Wild card, but also allows you to look at the top three cards of your deck and choose one to keep in your hand.
- **Reverse All**: Reverses the direction of play for every player, not just the next player.
- **Skip Chain**: Skips the next player's turn and continues skipping players until a player can play a Skip card of their own to break the chain.
- **Copy Color**: Allows you to copy the color of the last card played and play any card of that color from your hand.
- **Hand Limit**: Forces all players to discard cards until they have a set number of cards in their hand (e.g., three cards).
- **Super Draw Four**: Similar to a regular Draw Four card, but forces the next player to draw eight cards instead of four.

Hopefully these suggestions give you even more ideas for creating an exciting and dynamic game!
```

### Deepseek's ideas
```
Creating a UNO-inspired card game with fresh mechanics, lore, and streamlined gameplay while retaining the original's accessibility is an exciting challenge! Here's a structured approach to bring your vision to life:

---

### **Core Gameplay Enhancements**  
**1. New Card Mechanics (Balanced & Streamlined):**  
   - **Double Down Wild Card:** Play two cards in one turn (if they match color/number), but the next player draws two if they can’t match.  
   - **Chain Draw:** A wild card that forces the next player to draw cards equal to the number of Chain Draws played consecutively (e.g., three Chain Draws = draw six cards).  
   - **Shield Card:** Blocks a Draw Two/Draw Four for one turn. Limited to one use per player per round.  
   - **Swap Hands:** A wild card that lets you trade hands with any player, adding chaos and strategy.  
   - **Jester Wild Card:** Randomly applies a classic effect (Reverse, Skip, Draw Two) to the game.  

   **Balance:** Phase in new cards gradually (e.g., unlock via progression) and keep classic cards as the core. Add tooltips and tutorials to explain new mechanics.

**2. Strategic Depth:**  
   - **Energy System:** Earn "energy" by playing action/wild cards. Spend it to activate character abilities (tied to lore) or reroll a bad hand once per game.  
   - **Persistent Effects:** Introduce "Artifact" cards that stay in play (e.g., "All Draw penalties +1 this round"). Players vote to ban one artifact each game for balance.  

---

### **Lore & Worldbuilding**  
**1. Thematic Context:**  
   - **Dystopian Game Show:** Frame matches as a televised battle in a fictional world where contestants duel to avoid "elimination" (losing all points). Winners gain fame; losers face humorous, lore-friendly punishments.  
   - **Faction-Based Characters:** Create 6-8 unique characters (e.g., a trickster mage, a robotic dealer) with passive abilities tied to their lore. Examples:  
     - **The Gambler:** Once per game, peek at an opponent’s hand.  
     - **The Engineer:** Redraw one card after playing a Wild.  

**2. Story Mode:**  
   - **Campaign Structure:** A singleplayer journey through themed "arenas" (e.g., a casino, a magic academy) with AI opponents. Each arena boss introduces a new mechanic (e.g., a boss who shuffles artifacts into the deck).  
   - **Lore-Driven Challenges:** Complete objectives like "Win using only Shield cards" to unlock character backstories and cosmetic upgrades.  

---

### **Singleplayer Modes & Progression**  
**1. AI Personalities:**  
   - **Difficulty Levels:**  
     - **Chaotic (Easy):** AI prioritizes fun over strategy (plays wild cards immediately).  
     - **Tactician (Hard):** AI counts cards and saves Shields for critical moments.  
   - **Adaptive AI:** Opponents learn from the player’s habits (e.g., if you hoard Wild cards, they’ll play more aggressively).  

**2. Progression System:**  
   - **Unlockables:** Earn currency to buy card skins, character outfits, and themed decks (e.g., "Cyberpunk" cards with neon effects).  
   - **Daily Challenges:** Short, randomized scenarios (e.g., "Survive 10 turns with a 20-card hand").  

---

### **Visual & Audio Design**  
   - **Dynamic Card Animations:** Make new cards feel impactful (e.g., a Shield card creates a force field around the player’s hand).  
   - **Thematic Arenas:** Each arena changes visuals and music (e.g., a pirate ship with sea shanties, a futuristic lab with synth beats).  
   - **Character Banter:** Unique voice lines for interactions (e.g., "You’ve activated my trap card!" when a Chain Draw is played).  

---

### **Technical Considerations**  
   - **Accessibility:** Include colorblind modes, scalable UI, and customizable controls.  
   - **Cross-Platform Play:** Optional online/local multiplayer to expand reach.  
   - **Mod Support:** Allow players to create custom cards/characters (if feasible).  

---

### **Example Play Session**  
A player in story mode faces "The Collector," a boss who starts with a 10-card hand but gains energy for every card opponents draw. The player uses Swap Hands to cripple The Collector’s strategy, then finishes with a Double Down + Chain Draw combo, unlocking a new Jester card for future matches.

---

By blending UNO’s simplicity with light strategic layers and a playful narrative, your game can appeal to both casual players and those seeking deeper challenges. Focus on iterative testing to ensure new mechanics feel intuitive, and let the lore enhance—not overshadow—the cardplay.
```


## Elemental aspects to cards
(UNO elemental styled spinoff or addon to my superuno. The idea is that colors means something more than just color and has stacking, reactive or synergistic effects.)

### Elements that a card may have:
(basic)
- water (blue): defeats fire . washes away ground
- fire (red): defeats plant . blows up with electric
- plant (green): defeats water . invades ground.
- electric (yellow): explodes fire . electrocutes water and plants
(expansion1)
- ground (brown): blocks fire . nourishes plant, blocks move unless player has counter
- psychic (purple): bypasses all but plant and electric, reverses direction
- metal (metal grey): blocks water, plant, ground, but fire and electric melt through.
(expansion2)
- radiation/nuclear/fairy/magic (teal/pink): distorts, catalyses or crashes/nullifies (?)
- (uses 'UNO Flip' inspired function, changes the next card into a worse/better version of it (weaker or more powerful))
- neutral (light grey) - buffer card that can clear/reset ongoing stacks, can be placed on anything.

### Concepts when playing a card:
- Regular/neutral (no special effect or buildup, when a color/element has no reaction to other element).
- Same element (fire on fire card)
- Strong against (water on fire card)
- Resisted (cant play fire/electric cards against ground card)
- Blocked (skip opponent turn unless they can counter it)
- Special effect (cause draw 2 when electric on fire card, per each fire card in stack (elemental energy buildup feature))

Extra Active. (crap, I forgot what I meant by this.)
Elemental infused Draw 2+, etc.

Elemental buildup release effects:
- water to ground . mudslide
- water to fire . smokescreen
- fire to electric . explosion
- fire to plant . firestorm
- electric to fire . plasma
- electric to metal . stun storm
- plant to psychic . mutation
- plant to ground . overgrowth

Any combination not seen here means it doesn't have an effect - regular/neutral.

Ground, metal, psychic don't have detonations, but they buildup an oppressive wall/blocking/aura effect by themselves the more they stack. They also defuse buildup stacks of other elements.

Elemental buildup levels:
- 2 cards, small
- 3 cards, medium
- 4 cards, heavy
- 5+ cards or more, nuke (doesn't scale past 5 cards in terms of power)

### Dark/Light variants of all cards:
- Dark - harms others or sows chaos
- Light - helps self or creates harmony
- Alternatively Dark Wild Cards forces the cards into DARK MODE ala UNO Flip and Light Wild Cards forces into LIGHT MODE (Normal).

### Other cards:
Draw 4, 6, 8, 10
Catalyze current element to nuke status and detonate it (or pass it on, depends on what they do)
Roulette/Kenny draw (say color, keep drawing from deck until you get that color/element)

### Ideas/inspiration:
- UNO No Mercy
- UNO Elite NFL
- UNO Flip! 
- UNO All Wild
- UNO Flex
- Pokemon TCG Trainer Cards
- Advance Wars: Dual Strike (CO Powers and SCO Powers)


## Misc Loose Ideas

### ONU (extended ideas)
> "In this Bizarro world-variation of UNO, players try to accumulate as many cards as possible. Play goes on until there are no more cards in the deck, and the player with the most cards wins."

--

(Note: This is an experimental idea, I was exploring different UNO alternatives - both official and community made and picked out the ones that were interesting and tried to fix them, but I didn't put that much effort into this one - they're both unbaked. I'm still on the fence - it could be refined and included as another mode with edited rules and different cards - still using the main game's UNO/card game framework - but maybe it would just dilute the overall game.)

#### Variant 1
Players show their hands revealed at all times, no privacy with cards. (To prevent taking card from deck when they do have a valid card to discard)
Rely on swap hands cards to win by playing draw +N cards to buff your opponents then yoink away their hand for yourself at the last moment. Otherwise play normally.

#### Variant 2
Keep privacy but at start of each turn draw one card. Only use cards if you see a benefit for it.
Draw cards always aim at self, but next player can steal the benefit through stacking. Hands can be swapped to steal bountiful collections from others.

---

### Lofi Idea Text Based Graphics
*(discarded - I only came up with this to create the cheapest possible way to visually show a game of UNO without needing card graphics by simply utilizing text. Now that Claude Opus can effectively draw cards using code and even animate their motion, it will be far superior to this idea entirely.)*

Broader idea is about using primarily text based only visual representations and text only layouts for game projects, maybe using particle or shader effects too.

Brainstorm a layout for UNO using text. Do one as a vertical column, then a 4 corners + center discard pile.