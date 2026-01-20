"""
- 16 x 16 grid of rectangles
- Each rectangle is roughly 2.2

- Start with a 4000 pixel width canvas
- Assume the padding around the rectangles is the same as the padding between the rectangles
- 15 gaps + 2 gaps surrounding = 17 total gaps for x and y
- 4000 = 17p (padding) + 16x (rect width)
- p = ~30

"""

from random import randrange, choice
from itertools import combinations
from PIL import Image, ImageDraw

NUM_RECTS = 16
NUM_PADDING = NUM_RECTS + 1

# some magic numbers from which other numbers can be derived
PADDING = 30
CANVAS_X = 4000
XY_RATIO = 2.2

# dimensions of inner rectangles
RECT_X = (CANVAS_X - (PADDING * NUM_PADDING)) / NUM_RECTS
RECT_Y = RECT_X / XY_RATIO

CANVAS_Y = int(NUM_PADDING * PADDING + NUM_RECTS * RECT_Y)

color_pool = []


def main():
    populate_color_pool()

    im = Image.new("RGB", (CANVAS_X, CANVAS_Y), color="WHITE")
    d = ImageDraw.Draw(im)
    for i in range(1, NUM_RECTS + 1):
        for j in range(1, NUM_RECTS + 1):
            d.rectangle(
                [
                    PADDING * j + RECT_X * (j - 1),
                    PADDING * i + RECT_Y * (i - 1),
                    PADDING * j + RECT_X * j,
                    PADDING * i + (RECT_Y * i),
                ],
                fill=get_random_color(),
            )

    im.save("generated.jpg")


# generate random colors by approximating Richter's technique
def populate_color_pool():
    # start by mixing the 3 primary colors to make a dozen new hues
    # we'll mix RGB colors since we're dealing with screens rather than paint
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    primary_colors = [red, green, blue]

    # generate every possible combination of the primary colors
    primary_color_combos = []
    for amount in range(1, len(primary_colors) + 1):
        combos = combinations(primary_colors, amount)
        for combo in combos:
            primary_color_combos.append(combo)

    # average those combinations to simulate mixing them together
    for combo in primary_color_combos:
        averaged = average_colors(combo)
        color_pool.append(averaged)

    # the color pool now contains 7 colors
    # add white and black to those colors to create a variety
    # of shades and tones, 180 different colors in all

    # pick a random color from color_pool
    # generate a random n, n, n color and average it with the first
    # add the resulting color to the color pool

    primaries_with_white_and_black = []
    for _ in range(7, 181):
        pool_primary = choice(color_pool)
        grey_scale = randrange(255)
        grey = (grey_scale, grey_scale, grey_scale)
        mixed = average_colors((pool_primary, grey))
        primaries_with_white_and_black.append(mixed)

    color_pool.extend(primaries_with_white_and_black)

    return color_pool


def get_random_color():
    return choice(color_pool)


# Return the average color of n many RGB color tuples
def average_colors(colors):
    average_color = []
    for component in zip(*colors):
        avg = sum(component) / len(component)
        average_color.append(int(avg))
    return tuple(average_color)


if __name__ == "__main__":
    main()
