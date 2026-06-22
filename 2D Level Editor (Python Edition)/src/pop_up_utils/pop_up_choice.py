import pygame as pg
from typing import List
from utils import BorderFrame, MultiLineLabel, Button, Animation
from .pop_up_template import PopUp


"""
Asks the user to choose between two or more choices, technically
you can invoke this widget with a single choice as well, but what's the point
of asking the user if there is only one choice broski
"""


class PopUpChoice(PopUp):

    def __init__(self, font : str, anim_manager : Animation):
        super().__init__(font, anim_manager)
    
        # size configurations (pixel sizes)
        self.box_width = 500
        self.box_height = 300
        self.padding = 10
        
        self.label_width = 500
        self.label_height = 200
        self.label_text_size = 15
        self.option_height = self.box_height - self.label_height

    def ask_choice(self, msg : str, choices : List[str], callback = lambda: print("Finished taking choice")):
        
        width = (self.box_width  + 2 * self.padding) / pg.display.get_window_size()[0]
        height = (self.box_height + 2 * self.padding) / pg.display.get_window_size()[1]

        self.container = BorderFrame(-width, (1 - height) / 2, width, height, border_width = 3, bd_radius = 5)

        label_width = self.label_width / self.box_width
        label_height = self.label_height / self.box_height

        self.container.add_child(MultiLineLabel(0.05, 0.05, label_width, label_height, self.font, text = msg, text_size = self.label_text_size, padding = 5))

        for choice in choices:
            pass