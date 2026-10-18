# Game Design Presentation HTML Generator (Prompt)

I want us to create cool visual showcases of my game design skills as impressively well-thoughtout, highly detailed, professional HTML presentations. They're something I can show to people, properly and fully showcasing a particular game design project, be it a gamer, an employer, an investor, a fellow game developer, a govt official, or anyone curious about games or game design.

Basically I'll feed you these main materials:
- This prompt (Your main task)
- One or more particular project-specific documents, which may or may not include variants/alternatives of said project within. (Usually titled something akin to '[game_project_name].txt/md')
- 'Reactorcore's game design mentality bible'[1] (A big detailed reference guidebook on the topic of game design that helps steer how to fill in the blanks and how to make design decisions. Its essentially how to help you think like I would think as a game designer.) Its a big document so I split it into 2 parts: "2a BIBLE Reactorcores Game Design Mentality Bible.md" and "2b BIBLE Reactorcores Game Design Mentality Bible.md" (both are located in the root folder).

Based on the provided components, you would build a complete, well-formatted, highly detailed HTML file that works both on PC and Mobile that showcases the game project with a responsive website design that works on any device.
It would be accompanied with lavish CSS styling, as well as mermaid.js diagrams where approapriate, tasteful use of emojis and color-coding, and some strategic AI generated images at key locations in the document.

If you encounter multiple variants and alternatives in the provided '[game_project_name].txt/md' of a game project, your first reply should be to list the variants found in that txt/md file and ask which one we should start with. This way we'll focus on building each individual game showcase page one by one with the best quality and care given to it without being overwhelmed trying to do multiple pages at once.

Admittedly often the '[game_project_name].txt/md' documents may not have everything fleshed out and some are more a loose collection of ideas than a completed design. They may also refer to things you may not be familiar with or have missing details that I never got around to filling out. Nevertheless, each project idea, design or premise still warrants its own individual project page. You are to be inspired by what information there is available, then using the provided wealth of knowledge in the 'Reactorcore's game design mentality bible' to become a highly creative game designer yourself, armed with my mentality to craft an excellent new game design that fits the idea provided in the '[game_project_name].txt/md'.

## Approximate HTML structure:

Generally I'm aiming for a more technical overview of the project. I want to balance the presentation to be layperson friendly and somewhat visual and organized, but offering a compelling amount of depth and detail that'll captivate the interest of the reader to understand that this is very much a well-thoughout project. It should be professional yet blunt, well structured and formatted, colorful yet theme adherent, neither too vague nor too difficult to digest.

Regarding sections in the HTML, heres what I might need and don't need. Of course, everything depends on a per-project case so the below is only a suggestion, not a rigid set of requirements.

### Do need:
- Before the title, in the upper left corner, have a small humble unobtrusive label saying: "Reactorcore's Personal Game Design Project" that links to 'https://www.patreon.com/ReactorcoreGames' if clicked on. Use 'position: absolute;' for this one. Give a container background to make it stand out against the stuff behind it.

- **Title**: Centered, impactful title following this format: `[Thematic Name]: [3-Word Game Type]`
  - Example: "Metal Gear Solid: Tactical Espionage Action". Ensure the latter part is styled as a subtitle with a smaller font and a different color. If the original provided title is not in that format, then create a new title to take its place.
  - Behind the title is a hero image (see below '### Visual elements' for info on this).

- Game Overview (1-3 short paragraphs, like a TL;DR for what this game is and what it offers.)

- Target Audience (based on interests, UX/UI complexity and fundamental human needs fulfillment), Game's Purpose (what fundamental human need(s) does it fulfill for the player), Core Concept (bluntly state how it fulfills said human need(s)). These are presented as 3 cards arranged horizontally in a single row if on PC, while on mobile they're vertically stacked.

- Controls & Interface Info (either as a list of default player controls (whether its menu navigation and/or gameplay) or an explaining text if a list here seems out of place. Additionally talk/write about how the game actually plays/is controlled by the player, as in, what or who player is controlling and how. 

- 'Vignette image' goes here (see below '### Visual elements' for info on this). Has a subtitle text element that says what the gameplay feels like, framed as a quote, overlaid in the bottom left corner of that image, with everything done to ensure it doesn't accidently blend with the image (outline, shadow, overlay card between text and image at 70% opacity, but don't dim the image itself).

- Game Layers; This section talks about how the game is structured as a whole, with the below sub-sections filling in the details. CSS wise, its a container with vertically stacked wide cards.
	1. Moment-to-Moment active gameplay; Equivalent to actually controlling a character on a stage or issuing direct commands on a grid map in a specific scenario.
	2. Low Metagame; Equivalent to a local campaign/gauntlet of X amount of challenges/levels/areas/places, all tied together with a story arc and/or a regional world map. This card talks about how does the progression work from end-to-end.
	3. High Metagame; Equivalent to a bigger overworld map where 'Low_Metagame' campaigns take place as key events that both shape the high metagame's overworld and also influences what type of future low metagame campaigns it will generate, like an evolving persistent universe. For some game projects, the high metagame is a fully realized layer, but in some other games it may take a much simpler form, like a persistent log of completed low metagame campaigns that the user can simply view as a collection of memories they created together with this game and/or a way to get the randomization seed from the previously completed run to replay it again for fun, for experimentation, for faster speedruns, or any other reason. If the '[game_project_name].txt/md' doesn't provide any info on this, create something to fill this in creatively. This card talks about what is the on-going persistent experience of playing this game like, in the long-term from the player's point of view.
	4. Practical Game Flow (how does an average play session experience play out, from starting the app/exe on the users device to playing the game for some time and either pausing and quitting due to irl reasons or by reaching a convenient ingame exit point and closing the app, hopefully satisfying the human needs that this game was designed to provide for.)
	
- Game Modes (Assuming if there are more than one, then do a title and short description for each one and what purpose they serve (short quick session, long epic campaigns, high intensity, low intensity, that kind of stuff etc.). If theres just one game mode, then do just that one but give it a longer description. Game modes can be primary/secondary or alternative ways to play the same game and they're included with the game itself. These are not the same as standalone sequels, spin offs or alternative remixes of the game that might be mentioned in the '[game_project_name].txt/md' that would be different games that'd need their own separate pages.)

- Game Features & Mechanics (Pick between 3, 6, or 9 things (depends on how complex/big game is) as big vertically stacked wide cards, to talk about in the format of a technical document but made easy for a layperson to follow. You can go fairly in-depth per each thing, opening up major key features or mechanics that this particular game has that are unique to it. If it helps explain it better, use mermaid.js Diagrams to visualize the feature or mechanic. Ensure any text used in those mermaid.js diagrams are large enough to be legible and still works even if scaled to mobile vs pc.

- 'Feature image' goes here (see below '### Visual elements' for info on this). Pick the feature you thought was most important to this particular game and have the image be about that specifically. Has a subtitle text element that says what highlight why that feature is so interesting, framed as a quote, overlaid in the bottom left corner of that image, with everything done to ensure it doesn't accidently blend with the image (outline, shadow, overlay card between text and image at 70% opacity, etc.).

- Short section of fun bits of trivia, if relevant to the game. (optional)

- A 2 column equally split section with a 3:2 'box art cover' image on the left side (see below '### Visual elements' for info on this), and on the right side theres a card with the game's title and back-of-the-book-cover style description on right side. The box art cover image is scaled automatically for PC and mobile, enforcing the 2 column split layout at all times for this section.

- **Footer:**
```
All my links: https://linktr.ee/reactorcore
All my releases: https://reactorcore.itch.io/
Reactorcore Games - 2025
```

### Don't need:
- Development Timeline
- Technical Specifications
- Useless stats or ego/boasting stuff

(Note: Again, all the above 'do need' sections heavily depend on the context document I'll provide to you, so the provided information may override those sections to better suit that particular project's presentation. Generally, focus the entire page more on describing the user experience, for the player's point of view or benefit, like a promise of something great.)

## Visual elements:

Additionally I'll want to populate the HTML with strategic visual elements, with fairly wide creative liberty.

- **CSS-based visuals** - Use CSS for reliable visual elements such as card layouts with gradients and shadows, progress bars, stat meters, badges/labels, timeline visualizations, comparison tables, and visual hierarchy through typography and color. Hover responsiveness to change border color or section/card color is ok, but avoid translate/position or size change animations on mouse hover. Avoid cliche blue-orange color themes.

- **Mermaid.js diagrams**: You can create diagrams using mermaid.js; flow charts, mind maps, venn diagrams, hierarchy charts, any type of data visualization charts, comparison charts, and so on. Can be used to illustrate game flow, system architecture, player progression, feature differences or similarities, nuances about the game, etc. Either placed somewhere in between the 'Game Features & Mechanics' section (as an intermission illustration) or placed after that section as its own extra section with suitable descriptions and info related to the thing its talking about. Alternatively, you can use HTML tables styled with CSS instead of mermaid.js.

- **AI generated images** You don't get to generate these, I'll make them manually but what I do need from you is to already insert the images into the code. All images are coming from a local folder '../projects/images/[project_name_shortened]_[image_name].jpg'. All images should correctly auto-scale with page size for pc and mobile. I need these specific images:
	- **title image** ([project_name_shortened]_1_title.jpg) as a mood setter and hero for the game's context, with a big title text placed over it with a strong black shadow to make it stand out against it. The image is 16:9 aspect ratio.
	- **vignette image** ([project_name_shortened]_2_vignette.jpg) that conveys what the general gameplay feels like. The image is 16:9 aspect ratio.
	- **feature image** ([project_name_shortened]_3_feature.jpg) that highlights one prominent aspect/feature/mechanic of this game. Its prompt can be either a vignette or a visual metaphor. This image is usually embedded among the 'Game Features & Mechanics' section. The image is 16:9 aspect ratio.
	- **box art cover** ([project_name_shortened]_4_boxart.jpg) as a final send off at the end of the page to leave the reader compelled/excited/intrigued. Unlike all other images, this one is a 2:3 aspect ratio image.
	
The pages will be hosted on github pages so the filepaths to images have to be correct, like so:
<img src="../projects/images/aalsw_3_feature.jpg" alt="Physics-Based Combat Feature">

Note: Write the final 4 image names to the top of the HTML file in a commented-out area so it will be easier for me to get their names them instead of having to scroll through the whole document to find each one. Also right below them in that same commented-out area, also have a single sentence line describing what that image should depict, given the context of the game and the specific image in question. The 'project_name_shortened' part of the filename should be below 20 characters in lenght.

### General rules for using CSS styling:
- Title should be big, bold and impactful, using colors, font and style that fits best given a particular game project's context. Use an animated 2 color gradient for the title and any subsequent H2 headings (see '#### CSS Animation Effects for Titles' for more info). 
- Sections or cards should have colored borders and/or dropshadows. Apply professional principles of visual design, typography, layouts and color. The layout, design, colors and typography should be brave, expressive and reflect the game-in-question's identity.
- Use emojis and gradient colors tastefully to add more visual flair to the different sections on the page where suitable.
- Avoid awkward card layouts (e.g., 3 cards on first row, 1 lone card on second row, etc).
- If you make regular text bold, then give it a color too.
- Always add a "br" html tag between regular text paragraphs and break up huge paragraphs into smaller ones too, so that the reading experience isn't an awful uniform wall of text, but a pleasant spaced out organized one. This rule is especially important for large blocks of technical text.
- Use reliable text-shadow glow effects instead of CSS gradient text (background-clip: text) for all titles and headings to ensure cross-browser compatibility. Avoid and never use -webkit-background-clip: text or -webkit-text-fill-color: transparent as these cause rendering issues (blurry, unreadable) on certain browser/OS combinations.
- If using external fonts, avoid font loading issue that causes image security errors in Firefox. (The problem is Google Fonts imports are placed inside <style> blocks as @import statements instead of proper <link> tags in the <head>.)

To make it easier to swap the CSS colors later have a block like this one at the top of the CSS section:
```css
:root {
  --background-color: #112131;
  --container-bg: #223355;
  --border-color: #e4e9f0;
  --text-color: #2d3436;
  (and so on.)
}
```

Generally never have the background be pure white or pure black but somewhere between in the 10-90% range of brightness with a hint of color/hue, while all colors in general for most elements should have saturation between 20-90%, depending on project context.

#### CSS Animation Effects for Titles

Use **CSS-only animated text-shadow effects** for maximum compatibility and performance. All effects use `text-shadow`, `color`, and `@keyframes`:

Choose one of below animated text-shadow effects for the main title's first part (H1) and any H2 headers too:

- **Glow Pulse**: `text-shadow` intensity pulses rhythmically using multiple shadow layers
- **Color Shift Glow**: `text-shadow` colors transition through preset palettes while maintaining glow
- **Breathing Glow**: Slow, rhythmic glow expansion/contraction via shadow blur radius
- **Neon Flicker**: Rapid, subtle glow fluctuations with occasional intensity spikes
- **Multi-Color Glow**: Multiple colored shadows layer and animate independently
- **Directional Glow**: Shadow positions shift to create moving light source effects
- **Intensity Wave**: Glow strength waves across the text using staggered animations
- **Halo Effect**: Outer glow ring expands/contracts around text
- **Electric Buzz**: Quick shadow flickers with varying colors and intensities
- **Ember Glow**: Warm, flickering glow like burning embers
- **Underline Glow**: Animated glowing borders using `::before`/`::after` with `box-shadow`
- **Multi-Layer**: Combine glow pulse + color shift, or breathing + flicker effects

Whichever you chose, ensure legibility and match game identity.

Again, the color scheme, title animation effects, layout, typography, overall style and sections all depends on the game-project-in-question.