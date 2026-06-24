import pygame as pg
from utils import Animation, BorderFrame

"""
This module defines the basis of all pop up widgets defined
in this folder

NOTE: All pop-up-widgets defined with this template have the parent
      set to the main window
"""

class PopUp:

    def __init__(self, font : str, anim_manager : Animation):
        self.font = font
        self.anim_manager = anim_manager
        self.container = None
        self.active = False

    def draw(self, display : pg.Surface):
        if not self.container: return
        self.container.draw(display)

    def update(self, event : pg.event):
        if not self.container: return
        self.container.update(event)

    def cleanup(self):
        self.container = None
        