from utils.frame import Frame
import pygame as pg


"""
This module defines the same frame class as frame.py
but adds a border around the frame
"""

class BorderFrame(Frame):

    def __init__(self, x : int, y : int, width : int, height : int, bd_radius = 10, border_width = 10):
        super().__init__(x + border_width, y + border_width, width - border_width, height - border_width, bd_radius)
        self.bd_width = border_width

    def draw(self, display : pg.Surface):
        pg.draw.rect(display, self.clr_settings["bd_clr"], pg.Rect(self.x - self.bd_width, self.y - self.bd_width, self.width + 2 * self.bd_width, self.height + 2 * self.bd_width), border_radius = self.bd_radius)
        super().draw(display)