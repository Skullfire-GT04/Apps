import pygame as pg
from utils import ScrollableFrame, PixelButton, Label

class SpriteGroup(ScrollableFrame):

    def __init__(self, x : float, y : float, width : float, height : float, name : str, font : str, sprite_manager, app):
        super().__init__(x, y, width, height, bd_radius = 0)
        self.name = name
        self.manager = sprite_manager
        self.app = app

        # constants
        self.anim_width = 0.14
        self.anim_height = 0.14
        self.margin = 0.01
        self.bd_width = 3

        self.heading = Label(0.25, 0.03, 0.5, 0.13, font, text = self.name, padding = 5, bd_radius = 5, text_size = 15)
        self.add_child(self.heading)

    def draw(self, display : pg.Surface):
        super().draw(display)
        # drawing a border around the widget
        pg.draw.rect(display, self.clr_settings["bd_clr"], self.rect, self.bd_width, border_radius = self.bd_radius)