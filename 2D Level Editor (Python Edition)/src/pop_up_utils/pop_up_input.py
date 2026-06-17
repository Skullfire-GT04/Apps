import pygame as pg
from typing import List
from utils import BorderFrame, Label, InputBox, Button, ScrollableFrame, Animation


"""
This module defines a pop up window that appears on the screen
and asks the user for input

FEATURE: It can have multiple input fields for a single pop-up window
         and you can re-use the same object more than once for different input needs

RETURN TYPE: after each input submission it returns a dictionary with the input items
"""


class PopUpWindow:

    def __init__(self, font : str, anim_manager : Animation):
        self.container = BorderFrame(-1, -1, 0, 0)
        self.input_boxes = []
        self.return_fields = []
        self.font = font
        self.anim_manager = anim_manager
        self.active = False

        # size configurations (pixel sizes)
        self.max_label_width = 300
        self.max_input_width = 200
        self.label_height = 40
        self.input_height = 40
        self.label_text_size = int(self.label_height * 0.8)
        self.input_text_size = int(self.input_height * 0.8)
        self.padding = 10
        self.gap = 10

    def ask_input(self, fields : List[str]):
        if not fields: return
        self.active = True
        width = (max(self.max_label_width, self.max_input_width) + (2 * self.padding)) / pg.display.get_window_size()[0]
        height = ((max(self.label_height, self.input_height) * (2 * len(fields))) + (2 * self.padding) + (2 * len(fields) * self.gap)) / pg.display.get_window_size()[1]

        if height > 1:
            self.container = ScrollableFrame(-width, 0.1, width, height)
        else:
            self.container = BorderFrame(-width, (1 - height) / 2, width, height, border_width = 3)

        label_width = self.max_label_width / self.container.rect.width
        label_height = self.label_height / self.container.rect.height

        input_width = self.max_input_width / self.container.rect.width
        input_height = self.input_height / self.container.rect.height

        gap = self.gap / self.container.rect.height
        y_padding = self.padding / self.container.rect.height
        x_padding = self.padding / self.container.rect.width
        x = x_padding
        y = y_padding

        for field in fields:
            self.container.add_child(Label(x, y, label_width, label_height, self.font, padding = self.label_height - self.label_text_size, text_size = self.label_text_size, text = field))
            y += label_height + gap
            input_box = InputBox(x, y, input_width, input_height, self.font, text_size = self.input_text_size, placeholder = field, padding = self.input_height - self.input_text_size)
            y += input_height + gap
            self.container.add_child(input_box)
            self.input_boxes.append(input_box)
        self.return_fields = fields
        self.anim_manager.add_widget_animation(self.container, "translate_x", 200, (1 - width) / 2 ,0.1, 1)

    def draw(self, display : pg.display):
        self.container.draw(display)

    def update(self, event : pg.event.Event):
        self.container.update(event)
