import pygame as pg
from utils.widget import Widget
from utils.event_manager import EVENT_MAP, WIDGET_TYPES_ALL

"""
This module defines the frame class which will the container
class for all widgets defined in this folder
"""

class Frame(Widget):

    def __init__(self, x : float, y : float, width : float, height : float, bd_radius = 10):
        super().__init__(x, y, width, height)
        self.type = "frame"
        self.bd_radius = bd_radius
        self.id_count = 0
        self.children = {} # this list will contain all the child widgets contained inside this frame
        self.load_color_settings("frame")
        self.calc_new_rect()
        
        # this dictionary is what defines which type of 
        # children are eligible to be nested inside a frame
        # and their event mappings
        self.child_event_map = {widget : i for i, widget in zip(range(len(WIDGET_TYPES_ALL)), WIDGET_TYPES_ALL)}
        self.child_grouping = [{} for _ in range(len(self.child_event_map))]

    # draws the frame on a given surface
    def draw(self, display : pg.Surface):
        pg.draw.rect(display, self.clr_settings["bg"], self.rect, border_radius = self.bd_radius)

        for child in self.children.values():
            child.draw(display)

    # updates the frame and all its children
    def update(self, event : pg.event.Event):
        
        # checking if is is a mouse event, then does the event lie within the bounds of the frame
        if hasattr(event, "pos"):
            x = self.rect.left
            y = self.rect.top 
            if not (x <= event.pos[0] <= x + self.rect.width and y <= event.pos[1] <= y + self.rect.height): return    

        if event.type == pg.VIDEORESIZE:
            super().update(event)
            for child in self.children.keys():
                self.children[child].update(event)
            return

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
        child.set_parent(self)
        self.child_grouping[self.child_event_map[child.type]][self.id_count] = child
        child.id = self.id_count
        self.id_count += 1

    def change_children(self):
        for child in self.children:
            self.children[child].parent_changes()
    
    def change_x(self, new_x):
        super().change_x(new_x)
        self.change_children()
    
    def change_y(self, new_y):
        super().change_y(new_y)
        self.change_children()

    def change_height(self, new_height):
        super().change_height(new_height)
        self.change_children()
    
    def change_width(self, new_width):
        super().change_width(new_width)
        self.change_children()
    
    def parent_changes(self):
        super().parent_changes()
        for child in self.children:
            self.children[child].parent_changes()
