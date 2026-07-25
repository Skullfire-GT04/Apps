import pygame as pg
from .scrollable_frame import ScrollableFrame

"""
This is essentially 
aa scrollable frame which prevents overflowing widgets
but only works if the frame contains only a single kind of widgets
"""

class SingleWidgetScrollableFrame(ScrollableFrame):

    def __init__(self, x : float,y : float, width : float, height : float, bd_radius = 10):
        super().__init__(x, y, width, height, bd_radius = bd_radius)
        self.scroll_speed = 0

    def set_scroll_speed(self, new_scroll_speed : float):
        self.scroll_speed = new_scroll_speed

    def draw(self, display):
        pg.draw.rect(display, self.clr_settings["bg"], self.rect, border_radius = self.bd_radius)
        
        for child in self.children.values():
            if child.y >= 0 and child.y <= 1:
                child.draw(display)