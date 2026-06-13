import pygame as pg
from .frame import Frame


"""
This module implements a scrollable frame,
the scroll only work for the vertical axis
"""

class ScrollableFrame(Frame):

    def __init__(self, x, y, width, height, bd_radius = 10):
        super().__init__(x, y, width, height, bd_radius = bd_radius)
        self.scroll_speed = 0.1
    

    def update(self, event : pg.Event):
        super().update(event)

        if event.type == pg.MOUSEWHEEL:
            for child in self.children:
                self.children[child].change_y(self.children[child].y + (self.scroll_speed if event.y > 0 else - self.scroll_speed))
                

