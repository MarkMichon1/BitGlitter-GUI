from PIL import Image, ImageDraw

from datetime import datetime
from random import choice


class IconPaletteManager: #todo all to db eventually
    '''A fun easter egg that generates a random application icon at each startup.  Days of significance will have their
    own custom color themes as well.  For any contributors reading this who would like to add some of their own, you're
    more than welcome!  Be sure the foreground letters can be read easily from the background pixels beforehand.  This
    object is what essentially manages the IconPalette objects.'''

    def __init__(self):
        self.date_dict = {}

    def create_icon(self):
        try:
            active_palette = self.date_dict[datetime.now().timetuple().tm_yday]
            letter_colors = active_palette.letter_colors
            background_colors = active_palette.background_colors
        except: # make this entire thing a DB call?  since certain events can have a range, the optimum approach to
            letter_colors = ((254, 124, 6),)
            background_colors = ((167, 62, 217), (124, 33, 170))

        image = Image.new('RGB', (110, 110), 'white')
        draw = ImageDraw.Draw(image)

        # background render
        for y_range in range(11):
            for x_range in range(11):
                draw.rectangle((
                   (10 * x_range),
                   (10 * y_range),
                   (10 * (x_range + 1) - 1),
                   (10 * (y_range + 1) - 1)), fill=f'rgb{str(choice(background_colors))}')

        # letter render
        letter_pixel_coordinates = ((2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 3), (3, 5), (3, 7), (4, 4), (4, 6),
                                    (6, 4), (6, 5), (6, 6), (7, 3), (7, 7), (8, 3), (8, 5), (8, 6))
        for coordinate in letter_pixel_coordinates:
            draw.rectangle((
                (10 * coordinate[0]),
                (10 * coordinate[1]),
                (10 * (coordinate[0] + 1) - 1),
                (10 * (coordinate[1] + 1) - 1)), fill=f'rgb{str(choice(letter_colors))}')

        image.save('icon.png')


class IconPalette:
    def __init__(self, day_of_year_range, letter_colors, background_colors):
        self.day_of_year = day_of_year_range
        self.letter_colors = letter_colors
        self.background_colors = background_colors

'''todo:

- database integration
- datetime day objects as dictionary key?  will need a bit of time to think about this

'''