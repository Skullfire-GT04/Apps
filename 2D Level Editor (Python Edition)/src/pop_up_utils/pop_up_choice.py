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
        self.output = None
    
        # size configurations (pixel sizes)
        self.box_width = 500
        self.box_height = 200
        self.padding = 0
        
        self.button_height = self.box_height * 0.3
        self.label_width = self.box_width - (2 * self.padding)
        self.label_height = self.box_height - self.button_height - (2 * self.padding)
        self.label_text_size = 15
        self.button_text_size = 15

    def ask_choice(self, msg : str, choices : List[str], callback = lambda: print("Finished taking choice")):
        if not choices: return
        
        width = (self.box_width  + 2 * self.padding) / pg.display.get_window_size()[0]
        height = (self.box_height + 2 * self.padding) / pg.display.get_window_size()[1]

        self.container = BorderFrame(-width, (1 - height) / 2, width, height, border_width = 2, bd_radius = 5)

        label_width = self.label_width / self.container.rect.width
        label_height = self.label_height / self.box_height

        rel_padding_x = self.padding / self.container.rect.width 
        rel_padding_y = self.padding / self.container.rect.height

        self.container.add_child(MultiLineLabel(rel_padding_x, rel_padding_y, label_width, label_height, self.font, text = msg, text_size = self.label_text_size, padding = 5))

        choice_width = (self.container.rect.width / len(choices))
        rel_choice_width = choice_width / self.container.rect.width
        rel_choice_height = self.button_height / self.container.rect.height

        x = 0
        y = 1 - rel_choice_height

        for choice in choices:
            self.container.add_child(Button(x, y, rel_choice_width, rel_choice_height, self.font, self.button_text_size, text = choice, padding = 0, command = lambda choice=choice: self.submit(choice, callback)))
            x += rel_choice_width
        self.active = True
        self.anim_manager.add_widget_animation(self.container, "translate_x", 150, (1 - width) / 2, 0, 1)

    def submit(self, choice : str, callback):
        self.output = choice
        self.active = False
        self.anim_manager.add_widget_animation(self.container, "translate_y", 150, 0, 1.1, 1, callback = self.cleanup)
        callback()