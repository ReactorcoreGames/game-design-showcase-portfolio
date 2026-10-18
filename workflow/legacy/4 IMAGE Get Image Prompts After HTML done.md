# Generate text for image prompts using the context of the HTML file

## Goal
I wanna generate some images for the HTML file in the 'Ready HTML Pages' folder, so based on the presentation we've made and the 5 images it will have, provide 5 detailed image generation prompts for each one. I'll use them to manually go cook up some images.

## Method
Describe them in detail yet concisely, use no more than 600 characters per prompt including consistent character details, keep each result as a single paragraph, plus an additional extra 150 characters that defines a unified art style among them using keywords as an attachment tacked to the end of each of them, written as keywords. And also another extra 110 characters on top of that are available to describe a color scheme, inspired by the game showcase html's css theme.

## Rules for how to word the prompt
- The prompts for the images you are creating should not have explicit written text elements in it like labels, signage, titles, etc. In other words avoid stuff like 'the sign says "Billy"'. If the context has references of established names or things, then opt to describe them without referencing them directly (Example : Dont = Super Mario, Do = Cartoony plumber in a red blue overall outfit).

- Generally try to have a main focal point in each image and begin with describing the image with camera framing, angle, lens and cinematography terms, then do a main subject with their most important details, then do secondary details and surroundings. Then lastly the added tacked on art style snippet.

- An important point to consider is that an AI will be interpreting the prompt, so try to word them in a way that would lead to a visual result that would adhere to the context and nuance of the game project. Essentially avoid situations where objects or characters that would be predictable to appear as something else than what the project intended if they were told to about to an AI that had no prior knowledge of said character. This means even if in the project something is referred to as "drone" in the sense of a particular "automated submarine unmanned droid/machine/robot", theres a risk the image generator AI will mistakenly take the word "drone" and just add in a typical quad copter flying drone.

- If theres a central character or other central specific repeating thing (location, vehicle, machines, object, etc.) in the game project, then ensure that they are mentioned consistently in the prompts where they are included, so if theres a "teal abyssal frogman guardian in glowing armor" character, make sure its mentioned in full instead of just referring to them as "the guardian in armor" in a later prompt. Doing this mistake can cause said abyssal frogman creature to be shown as a regular human knight, so we need to be consistent and aware about this.

## Example output

<output>

Here are the five detailed image generation prompts for [Game Name]:
Title Image: (16:9)
(prompt here). Long exposure photography, soft lighting, vibrant colors, highly detailed, dynamic action, painterly particle effects, ethereal speed lines. Sharp red-black color theme with white accents and markings.

Vignette Image: (16:9)
(prompt here). Long exposure photography, soft lighting, vibrant colors, highly detailed, dynamic action, painterly particle effects, ethereal speed lines. Sharp red-black color theme with white accents and markings.

Feature Image: (16:9)
(prompt here). Long exposure photography, soft lighting, vibrant colors, highly detailed, dynamic action, painterly particle effects, ethereal speed lines. Sharp red-black color theme with white accents and markings.

Box Art Cover: (2:3)
(prompt here). Long exposure photography, soft lighting, vibrant colors, highly detailed, dynamic action, painterly particle effects, ethereal speed lines. Sharp red-black color theme with white accents and markings.

Story Overworld Image: (16:9)
(prompt here). Long exposure photography, soft lighting, vibrant colors, highly detailed, dynamic action, painterly particle effects, ethereal speed lines. Sharp red-black color theme with white accents and markings.

Unified Art Style (for all five, already included in prompts): 
Long exposure photography, soft lighting, vibrant colors, highly detailed, dynamic action, painterly particle effects, ethereal speed lines. Sharp red-black color theme with white accents and markings.

</output>

## Note about style
(Artstyle and the way the prompt should be written always depend on the game project's own context/identity/essence. You can do long exposure photography, cinematic, silhouette art, oil painting in the style of frank frazetta, anime, cartoon, watercolor, lowpoly, sketch lineart, cyberpunk, glitch art, photography, and many many others, whichever you think best suits the style of the game in question.)