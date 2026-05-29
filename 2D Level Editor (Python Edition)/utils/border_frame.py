from utils.frame import Frame
import pygame as pg


"""
This module defines the same frame class as frame.py
but adds a border around the frame
"""

class BorderFrame(Frame):

    def __init__(self, x : int, y : int, width : int, height : int, bd_radius = 10, border_width = 10):
        super().__init__(x, y, width, height, bd_radius)
        self.bd_width = border_width

    def draw(self, display : pg.Surface):
        temp = self.rect.copy()
        temp.x -= self.bd_width
        temp.y -= self.bd_width
        temp.width += 2 * self.bd_width
        temp.height += 2 * self.bd_width
        pg.draw.rect(display, self.clr_settings["bd_clr"], temp, border_radius = self.bd_radius)
        super().draw(display)