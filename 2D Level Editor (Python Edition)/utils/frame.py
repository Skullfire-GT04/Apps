import pygame as pg
from utils.widget import Widget
from utils.child_widget import ChildWidget

"""
This module defines the frame class which will the container
class for all widgets defined in this folder
"""

class Frame(Widget):

    def __init__(self, x : int, y : int, width : int, height : int, full_screen_mode = False, bd_radius = 10):
        super().__init__(x, y, width, height)
        self.full_screen_mode = full_screen_mode
        self.bd_radius = bd_radius
        self.bg = "#01011a" # a bluish black color
        self.children = [] # this list will contain all the child widgets contained inside this frame
        
        # this dict is really important since it classifies which child
        # elements will receive which type of event inputs

        self.event_map = {
            pg.MOUSEMOTION : ("button"),
            pg.MOUSEBUTTONDOWN : ("button")
        }

        self.child_event_map = {
            "button" : 0
        }

        self.child_grouping = [[] for _ in range(len(self.child_event_map))]

    def set_bg(self, color : str):
        self.bg = color

    def draw(self, display : pg.Surface):
        pg.draw.rect(display, self.bg, pg.Rect(self.x, self.y, self.width, self.height), border_radius = self.bd_radius)

        for child in self.children:
            child.draw(display)

    def update(self, event : pg.event.Event):
        for child in self.children:
            child.update(self)

    def delete_child(self, id_ : int):
        if id_ < 0 or id_ >= len(self.children): return False
        self.children.pop(id_)
        return True
    
    def add_child(self, child : ChildWidget) -> int:
        self.children.append(child)
        child.set_new_position(self)
        return len(self.children) - 1