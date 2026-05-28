import pygame as pg
from json import load

"""
This is a parent class of all widgets defined
in this folder
"""

class Widget:

    def __init__(self, x : float, y : float, width : float, height : float):
        self.x = x 
        self.y = y
        self.rect = None
        self.are_dimensions_absolute = False
        self.type = "widget"
        self.clr_settings = None
        self.id = None
        self.parent = None
        self.width = width
        self.height = height

    # loads the color settings of a particular widget type defined in the color_settings.json file
    def load_color_settings(self, type : str):
        try:
            with open("settings/color_settings.json", "r") as f:
                self.clr_settings = load(f).get(type, {})
        except FileNotFoundError as e:
            # if color setting are not found, then a generic color schema is applied
            self.clr_settings = {
                "bg" : "blue",
                "fg" : "white",
                "fill_clr" : "black",
                "btn_hvr_clr" : "cyan",
                "bd_clr" : "grey"
            }

    # though I would advice against using this directly, but you do you ig bro
    def set_id(self, id_ : int):
        self.id = id_

    def get_absolute_width(self):
        if not self.are_dimensions_absolute:
            if not self.parent:
                return self.width * pg.display.get_window_size()[0]
            else:
                return self.width * self.parent.get_absolute_width()
        else: return self.width
        
    def get_absolute_height(self):
        if not self.are_dimensions_absolute:
            if not self.parent:
                return self.height * pg.display.get_window_size()[1]
            else:
                return self.height * self.parent.get_absolute_height()
        else: return self.height
        
    def get_absolute_pos(self):
        if not self.parent:
            return (pg.display.get_window_size()[0] * self.x, pg.display.get_window_size()[1] * self.y)
        else:
            temp = self.parent.get_absolute_pos()
            x = temp[0] + (self.parent.get_absolute_width() * self.x)
            y = temp[1] + (self.parent.get_absolute_height() * self.y)
            return (x, y)
    
    def calc_new_rect(self) -> pg.Rect:
        pos = self.get_absolute_pos()
        self.rect = pg.Rect(pos[0], pos[1], self.get_absolute_width(), self.get_absolute_height())

    def draw(self):
        pass

    def update(self, event : pg.event.Event):
        pass