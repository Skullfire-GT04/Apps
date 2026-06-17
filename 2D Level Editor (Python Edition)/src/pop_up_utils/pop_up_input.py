import pygame as pg
from utils import Frame, Label, InputBox, Button


"""
This module defines a pop up window that appears on the screen
and asks the user for input

FEATURE: It can have multiple input fields for a single pop-up window
         and you can re-use the same object more than once for different input needs

RETURN TYPE: after each input submission it returns a dictionary with the input items
"""


class PopUpWindow:

    def __init__(self, display : pg.display):
        self.container = Frame(-1, -1, 0, 0)
        self.labels = []
        self.input_boxed = []
        self.display = display

    # preps the container for the new input
    def init(self):
        children = self.container.children.values()
        for child in children: self.container.delete_child(child)
        