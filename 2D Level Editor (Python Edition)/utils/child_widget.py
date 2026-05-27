import pygame as pg
from utils.widget import Widget



class ChildWidget(Widget):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.original_x = x
        self.original_y = y

    def set_new_position(self, parent : Widget):
        self.x = parent.x + self.original_x
        self.y = parent.y + self.original_y