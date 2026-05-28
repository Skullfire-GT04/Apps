import pygame as pg
from json import load

"""
This is a parent class of all widgets defined
in this folder
"""

class Widget:

    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y
        self.original_x = x
        self.original_y = y
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

    def set_new_position(self):
        # checking if the coordinates are in percentage
        if not isinstance(self.x, int) or not isinstance(self.y, int): return

        # checking if the widget is a stand_along widget or not
        if not self.parent: return

        # setting new coordinates otherwise
        self.x = self.parent.x + (self.original_x * self.parent.width)
        self.y = self.parent.y + (self.original_y * self.parent.height)

    # though I would advice against using this directly, but you do you ig bro
    def set_id(self, id_ : int):
        self.id = id_

    def draw(self):
        pass

    def update(self):
        pass