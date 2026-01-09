"""
- 16 x 16 grid of rectangles
- The image's aspect ratio is roughly 2 x 1
- Each rectangle is also roughtly 2 x 1

- Start with a 4000 x 2000 canvas
- Assume the padding around the rectangles is the same as the padding between the rectangles
- 15 gaps + 2 gaps surrounding = 17 total gaps for x and y
- 2000 = 17p (padding) + 16x (rect height)
- p = ~1/4x
- 2000 = 17 * (.25x) + 16x
- 2000 = 20.25x
- x = 98.7654321
- p = 24.69135802


"""

from random import randrange
from PIL import Image, ImageDraw

CANVAS_X = 4000
CANVAS_Y = 2000
PADDING = 24.69135802
RECT_X = 98.7654321
RECT_Y = RECT_X / 2

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
