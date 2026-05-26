import pygame as pg
from widget import Widget

"""
This module defines the frame class which will the container
class for all widgets defined in this folder
"""

class Frame(Widget):

    def __init__(self, x : int, y : int, width : int, height : int, full_screen_mode = False):
        super().__init__(x, y, width, height)
        self.full_screen_mode = full_screen_mode
        self.bg = "#01011a" # a bluish black color
        self.children = [] # this list will contain all the child widgets contained inside this frame

    def set_bg(self, color : str):
        self.bg = color

    def draw(self):
        pass

    def update(self):
        pass

    def delete_child(self, id_ : int):
        if id_ < 0 or id_ >= len(self.children): return False
        self.children.pop(id_)
        return True
    
    def add_child(self, child : Widget):
        pass