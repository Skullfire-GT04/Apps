import pygame as pg
from utils.widget import Widget


class Slider(Widget):

    def __init__(self, x : float, y : float, width : float, height : float, from_ = 0, to = 100, orient = "vertical", border_radius = 10):
        super().__init__(x, y, width, height)
        self.type = "slider"
        self.load_color_settings("slider")
        self.from_ = from_
        self.to = to
        self.value = from_
        self.orient = orient
        self.bd_radius = border_radius

    def draw(self, display : pg.Surface):
        pass
