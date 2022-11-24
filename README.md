# DALLE2Textures
## What is this?
Uses OpenAI's API to interface with DALL-E 2. 
It loops through all files, and checks if they are in a directory we want to replace. 
It then asks DALL-E 2 to generate an image. Then it writes it back to a new pack.
Blocks are 1024x1024
Items are 512x512
Everything else is 256x256

## EXCEPTIONS:
Many things have not been retextured. These include
- Animated textures (Never)
- Complex/stitched textures (Never)
- Extended / Long textures (Never)
- Chiseled Deepslate, Crimson Stem (Top), Dark Prismarine, Dried Kelp Block

Wait, what? Yeah. It was, for some reason, flagged by the OpenAI safety system.

Couldn't you just generate it online? No. Craiyon / DALL-E Mini is a separate model trained on a smaller dataset that cannot create as high detail textures.

- GUI elements (Never
- Particles (Later)
- Fonts

I don't even know how that would work

- Paintings (Later)
- Sun (Maybe later)
- Moon (Never, it's animated)
- Map (Maybe later)
