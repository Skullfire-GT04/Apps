import pygame as pg
from utils.label import Label

"""
Conceptually this is just a label with a border
"""

class Console(Label):

    def __init__(self, x : float, y : float, width, height, font : str, bd_radius = 20, text_size = 15, padding = 10, border_width = 3):
        super().__init__(x, y, width, height, font, bd_radius, "Console Output", padding, text_size)
        self.load_color_settings("console")
        self.bd_width = border_width
        self.text = "Console Output"

    def draw(self, display):
        # adding the border around the text box
        temp = self.rect.copy()
        temp.x -= self.padding + self.bd_width
        temp.y -= self.padding + self.bd_width
        temp.width += 2 * self.bd_width + 2 * self.padding
        temp.height += 2 * self.bd_width + 2 * self.padding
        pg.draw.rect(display, self.clr_settings["bd_clr"], temp, border_radius = self.bd_radius)

        super().draw(display)