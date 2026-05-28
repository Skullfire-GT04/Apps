import pygame as pg
from utils.widget import Widget
from utils.event_manager import EVENT_MAP

"""
This module defines the frame class which will the container
class for all widgets defined in this folder
"""

class Frame(Widget):

    def __init__(self, x : int, y : int, width : int, height : int, full_screen_mode = False, bd_radius = 10):
        super().__init__(x, y, width, height)
        self.type = "frame"
        self.full_screen_mode = full_screen_mode
        self.bd_radius = bd_radius
        self.bg = "#01011a" # a bluish black color
        self.id_count = 0
        self.children = {} # this list will contain all the child widgets contained inside this frame
        
        # this dictionary is what defines which type of 
        # children are eligible to be nested inside a frame
        # and their event mappings
        self.child_event_map = {
            "button" : 0,
            "label" : 1,
            "input" : 2,
            "slider" : 3,
            "frame" : 4
        }

        self.child_grouping = [{} for _ in range(len(self.child_event_map))]

    # sets the background color of the frame to given color
    def set_bg(self, color : str):
        self.bg = color

    # draws the frame on a given surface
    def draw(self, display : pg.Surface):
        pg.draw.rect(display, self.bg, pg.Rect(self.x, self.y, self.width, self.height), border_radius = self.bd_radius)

        for child in self.children.values():
            child.draw(display)

    # updates the frame and all its children
    def update(self, event : pg.event.Event):
        
        # checking if is is a mouse event, then does the event lie within the bounds of the frame
        if hasattr(event, "pos"):
            x = self.x if isinstance(self.x, int) else self.parent.x + (self.x * self.parent.width)
            y = self.y if isinstance(self.y, int) else self.parent.y + (self.y + self.parent.height)
            if not (x <= event.pos[0] <= x + self.width and y <= event.pos[1] <= y + self.height): return    

        for child_type in EVENT_MAP.get(event.type, tuple()):
            for child in self.child_grouping[self.child_event_map[child_type]].values():
                child.update(event)
    
    # deletes a child widget from the frame 
    def delete_child(self, child : Widget):
        if not self.children.get(child.id, None): return False
        del self.child_grouping[self.child_event_map[self.children[child.id].type]][child.id]
        del self.children[child.id]
        return True
    
    # adds a child widget 
    def add_child(self, child : Widget):
        if not isinstance(self.child_event_map.get(child.type, None), int): return
        self.children[self.id_count] = child
        child.parent = self
        self.child_grouping[self.child_event_map[child.type]][self.id_count] = child
        child.id = self.id_count
        self.id_count += 1