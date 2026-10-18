## returning to project

Ok, I'm returning to this project after a hiatus and I want to complete it. The new things today is that Opus 5.5 is now here and better than ever when it comes intelligence, the second thing is that I now have AI Batch Image Generator that if I recall correctly, does have CLI that you would be able to tap into. The latter means I don't have to paste prompts into my AI image service manually, but instead you Claude can just do them with the desired aspect ratio set.

The project actually exists in two places:
1. This project folder itself is the place where we "cook/build" things.
2. The repo that is hosted to github of the final product is here: "C:\14 Repos\game-design-showcase-portfolio"

And the Batch AI Image Generator is here: "C:\ClaudeWorkspace\AI image gen batch program"
(It already has my credentials loaded it, it can handle the different aspect ratios needed for the game design showcase pages and we'd be using Flux 2 Klein 4B model that I have a daily free limit of ~70 images before I have to wait for a reset. Generally I'd want to do all images per project in a single attempt so the prompts better be good and locked in style and content wise before we fire 'em away. Always use the "Standard" resolution size the program offers.)

## whats done and needs doing

This folder is where my todo projects are awaiting processing into html pages with illustrations:

C:\ClaudeWorkspace\HTML Game Design Showcase Maker\!GameDesignPortfolio\designs STANDBY

Back in the day I'd run older and much more limited Claude Sonnet 3 through these as 3 steps:
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\!GameDesignPortfolio\auxiliary html making prompts\task 1 initial page.txt"
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\!GameDesignPortfolio\auxiliary html making prompts\task 2 adjustments to initial page plan.txt"
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\!GameDesignPortfolio\auxiliary html making prompts\task 3 lore story add.txt"

Or these: (can't remember which, but the ones below are the definitive task documents.)
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\1 MAIN Game Design Presentation HTML Generator.md"
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\2a BIBLE Reactorcores Game Design Mentality Bible.md"
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\2b BIBLE Reactorcores Game Design Mentality Bible.md"
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\3 STORY add a section for story context.md"
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\4 IMAGE Get Image Prompts After HTML done.md"
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\5 FIX IMAGES for previous wording mistakes.md"
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\6 typography upgrade.txt"
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\7 Add SEO to RCG design html project pages.txt"
"C:\ClaudeWorkspace\HTML Game Design Showcase Maker\ADDON Game design article links page.md"

Nowadays, I think you'd be perfectly able to do each page per session and with much better quality.

Since this place is so dusty and disorganized, plus my whole workflow of "make stuff in here, then transfer it over there and hook it up to the nexus page" is a bit of a mess that if you advice moving everything to "C:\14 Repos\game-design-showcase-portfolio", cleanup/organize the workspace for a more streamlined setup for now and future additions, then lets do it.

Regardless, I'd run through the standby designs one-by-one, giving them like 4-5 AI generated images, then retiring the completed design text files into this folder:

C:\ClaudeWorkspace\HTML Game Design Showcase Maker\!GameDesignPortfolio\TXT done designs

After I had done a batch of designs as much as I could, I'd then publish to github pages via the github repo, but also to cloudflare pages via this thing:
"C:\14 Repos\CLOUDFLARE PAGES DEPLOYER\deploy-to-cloudflare RC GD Portfolio.bat"
(its an alternative backup if github pages explodes)

And I managed to do about half of the catalog, but got swept into other tasks so the rest weren't completed.

Now comes today and I want for you to continue and finish the work, but also revisit the old pages since they were done by Sonnet 3, not Opus 5.5. Same with the nexus page too. I think the existing AI images for the existing published projects are great and the page themes/colors generally are ok-ish (can be enhanced somewhat with your touch), but the concepts from my game design philosophy and nuances from my designs may have skipped a beat on many occasion and left the old entries a bit half-cooked.

While the purpose of the pages isn't a perfect GDD nor does it go into the details of the various games, the showcase pages are supposed to give fairly competent overview of each project. Since Sonnet was simple and the prompts I was using tried their best, I think the information and structure of the pages could be overhauled/improved greatly and suit each project better. I still think the 5 AI images per project is a good amount, so every new project will still get those - with the style preset used to be what would match the best per that project - and my Batch AI Image Generator has a lot of style preset suffixes to choose from, so give them wide usage across the different projects.

In regards to the workflow, I'd want to do this mostly via the Claude Code cloud since I have credits to spend there, but obviously that'd be only possible for the writing/design and AI image *prompt* portions, where as the actual batch generated images would need to be done afterwards on a local session and you'd only be able to sus out what the Batch AI Image Generator (BAIG) provides in terms of styles, aspect ratios and usage limits, then process the designs/write their pages, then based on that figure out what style would fit and what images the page would need in terms of prompts (taking into account the Batch AI Image Generator's Flux 2 Klein 4B's 1000 character limit that also needs to consider the style suffix you'd attach to the end of each prompt) and only then after the cloud sessions are over, I'd go back to local session, do a github pull to my local machine, we do the AI images by you using the CLI for BAIG and once we get all the images created, JPEG optimized, thumbnailed if I recall correctly that I needed to do that too, and renamed to filenames/path that are already set and pre-built into the pages you've made, then we can finally push all the data back to github and publish the updates to github pages and cloudflare too.