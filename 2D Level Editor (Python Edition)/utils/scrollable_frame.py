import pygame as pg
from .frame import Frame


"""
This module implements a scrollable frame,
the scroll only work for the vertical axis
"""

class ScrollableFrame(Frame):

    def __init__(self, x, y, width, height, bd_radius = 10):
        super().__init__(x, y, width, height, bd_radius = bd_radius)
        self.scroll_speed = 0.05
        self.type = "scrollable_frame"
        self.delta = 0        
    
    def draw(self, display):
        pg.draw.rect(display, self.clr_settings["bg"], self.rect, border_radius = self.bd_radius)

        for child in self.children.values():
            child.change_y(child.y + self.delta)
            child.draw(display)
            child.change_y(child.y - self.delta)

    def update(self, event : pg.Event):
        super().update(event)

        if event.type == pg.MOUSEWHEEL:
            self.delta += - self.scroll_speed if event.y < 1 else self.scroll_speed
            if self.delta >= 0: self.delta = 0

                

