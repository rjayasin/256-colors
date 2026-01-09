"""
- 16 x 16 grid of rectangles
- The image's aspect ratio is roughly 2 x 1
- Each rectangle is also roughtly 2 x 1

- Start with a 4000 x 2000 canvas
- Assume the padding around the rectangles is the same as the padding between the rectangles
- 15 gaps + 2 gaps surrounding = 17 total gaps for x and y
- 4000 = 17p (padding) + 16x (rect width)
- p = ~40
- 4000 = (17 * 40) + 16x
- 4000 = 680 + 16x
- 3320 = 16x
- x = 197.5308642
- p = 49.38271605


"""

from random import randrange
from PIL import Image, ImageDraw

XY_RATIO = 2.2
NUM_PADDING = 17
NUM_RECTS = 16
PADDING = 30

CANVAS_X = 4000

# dimensions of inner rectangles
RECT_X = (CANVAS_X - (PADDING * NUM_PADDING)) / NUM_RECTS
RECT_Y = RECT_X / XY_RATIO

CANVAS_Y = int(NUM_PADDING * PADDING + NUM_RECTS * RECT_Y)

def main():
    im = Image.new("RGB", (CANVAS_X, CANVAS_Y), color="WHITE")
    d = ImageDraw.Draw(im)
    for i in range(1, 17):
        for j in range(1, 17):
            d.rectangle(
                [
                    PADDING * j + RECT_X * (j - 1),
                    PADDING * i + RECT_Y * (i - 1),
                    PADDING * j + RECT_X * j,
                    PADDING * i + (RECT_Y * i),
                ],
                fill=rand_color(),
            )

    im.save("generated.jpg")

def rand_color():
    return (randrange(256), randrange(256), randrange(256))


if __name__ == "__main__":
    main()
