import pygame as pg
from typing import List
from utils import BorderFrame, Label, InputBox, Button, ScrollableFrame, Animation
from .pop_up_template import PopUp


"""
This module defines a pop up window that appears on the screen
and asks the user for input

FEATURE: It can have multiple input fields for a single pop-up window
         and you can re-use the same object more than once for different input needs

RETURN TYPE: after each input submission it returns a dictionary with the input items
             (I say return but the process invoking the input as to access the output)
"""


class PopUpWindow(PopUp):

    def __init__(self, font : str, anim_manager : Animation):
        super().__init__(font, anim_manager)

        self.input_boxes = []
        self.return_fields = []
        self.output = dict()
        self.persist = False

        # size configurations (pixel sizes)
        self.max_label_width = 300
        self.max_input_width = 300
        self.label_height = 30
        self.input_height = 30
        self.label_text_size = int(self.label_height * 0.9)
        self.input_text_size = int(self.input_height * 0.8)
        self.padding = 20
        self.gap = 30
        self.submit_btn_width = 120
        self.submit_btn_height = 30
        self.submit_btn_text_size = int(self.submit_btn_height * 0.5)
        self.cancel_btn_width = self.submit_btn_width
        self.cancel_btn_height = self.submit_btn_height
        self.cancel_btn_text_size = int(self.cancel_btn_height * 0.5)

    def ask_input(self, fields : List[str], callback, persist = False):
        if not fields: return
        self.active = True
        self.persist = persist
        width = (max(self.max_label_width, self.max_input_width, self.submit_btn_width) + (2 * self.padding)) / pg.display.get_window_size()[0]
        height = ((max(self.label_height, self.input_height) * (2 * len(fields))) + (2 * self.padding) + (2 * len(fields) * self.gap) + self.submit_btn_height) / pg.display.get_window_size()[1]

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
        submit_btn_width = self.submit_btn_width / self.container.rect.width
        submit_btn_height = self.submit_btn_height / self.container.rect.height
        cancel_btn_width = self.cancel_btn_width / self.container.rect.width
        cancel_btn_height = self.cancel_btn_height / self.container.rect.height

        for field in fields:
            self.container.add_child(Label(x, y, label_width, label_height, self.font, padding = (self.label_height - self.label_text_size) / 2, text_size = self.label_text_size, text = field))
            y += label_height + gap
            input_box = InputBox(x, y, input_width, input_height, self.font, text_size = self.input_text_size, placeholder = field, padding = (self.input_height - self.input_text_size) / 2, border_width = 2)
            y += input_height + gap
            self.container.add_child(input_box)
            self.input_boxes.append(input_box)

        submit_btn = Button(x_padding, y, submit_btn_width, submit_btn_height, self.font, text = "Submit", text_size = self.submit_btn_text_size, padding = (self.submit_btn_height - self.submit_btn_text_size) / 2)
        submit_btn.set_command(lambda: self.submit(callback))
        submit_btn.toggle_key_binding(pg.K_KP_ENTER)

        cancel_btn = Button(1 - (x_padding + cancel_btn_width), y, cancel_btn_width, cancel_btn_height, self.font, text = "Cancel", text_size = self.cancel_btn_text_size, padding = (self.cancel_btn_height - self.cancel_btn_text_size) / 2)
        cancel_btn.set_command(self.close)

        self.container.add_child(submit_btn)
        self.container.add_child(cancel_btn)

        self.return_fields = fields
        self.anim_manager.add_widget_animation(self.container, "translate_x", 200, (1 - width) / 2 ,0.1, 1)

    def submit(self, callback):
        self.output = dict()
        for i in range(len(self.return_fields)):
            self.output[self.return_fields[i]] = self.input_boxes[i].text if self.input_boxes[i].typed_in else ""
        callback()
        if not self.persist: self.close()

    def close(self):
        self.anim_manager.add_widget_animation(self.container, "translate_x", 200, -1, 1, 1, callback = self.cleanup)
        self.input_boxes = []
        self.active = False
        self.persist = False
