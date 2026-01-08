# What is this?

This will be the last coding project I ever write without using AI in any form.

I saw the painting [*256 Colors* by Gerhard Richter at SFMOMA](https://www.sfmoma.org/artwork/FC.643/) in January of 2026.

![painting](painting.jpg)

I was intrigued by the painting and the title and wanted to know more. From the SFMOMA website: 

> To do it, he developed a mathematical system. See if you can follow me here. First, he mixed the three primary colors to make a dozen new hues. He added white and black to those colors, to create a variety of shades and tones – 180 different colors in all. Then he assigned a number to each of the colors. Finally, he drew those numbers randomly from a box, and applied those colors to the grid in front of you. There are 256 rectangles in the grid, so some of the colors repeat. 
> 
>He’s working through ideas of chance, of finding ways to produce images generated from a source outside of oneself.  

I remarked to a friend that I found it interesting that Richter chose the number of colors he did, and also found his random color generation technique to be interesting. I said to my friend that it'd probably take 15 minutes to write the code to generate this image, but then I realized that in 2026 an AI could likely one-shot this. 

The idea that I can write code to recreate the image of a painting does not devalue the painting. The idea that AI can easily write code to do this does devalue code. 

I'm not convinced that this is entirely a bad thing. It's a sign of changing times.

As a sendoff to those old times, I will write a python script that can generate images like Richter's painting without using AI.

# Create an image
```
uv run 256_colors.py
```