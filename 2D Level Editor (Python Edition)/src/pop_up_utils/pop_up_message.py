import pygame as pg
from .pop_up_template import PopUp
from typing import List
from utils import Console, Animation, MultiLineLabel

"""
This module provides a way to send messages to the user, the message
disappears after the specified amount of time
"""

class PopUpMessage(PopUp):

    def __init__(self, font_path : str, animation_manager : Animation):
        super().__init__(font_path, animation_manager)
        self.hide_time = None

        # size configurations (pixel sizes)
        self.text_size = 20
        self.padding = 10
        self.text_gap = 5
        self.max_text_width = 400
        self.max_text_height = 500

        # font for measuring
        self.font_copy = pg.font.Font(font_path, self.text_size)

    def show_message(self, msg : str, time : int):
        formatted_msg = self.format_msg(msg)
        
        text_width = self.font_copy.size(formatted_msg[0])[0] + (2 * self.padding)
        text_height = self.font_copy.size(formatted_msg[0])[1] * len(formatted_msg) + (2 * self.padding)

        msg = "\n".join(formatted_msg) if len(formatted_msg) > 1 else formatted_msg[0]

        label_width = text_width / pg.display.get_window_size()[0]
        if text_height > self.max_text_height: text_height = self.max_text_height
        label_height = text_height / pg.display.get_window_size()[1]

        label_x = (1 - label_width) / 2

        if len(formatted_msg) > 1:
            self.container = MultiLineLabel(label_x, 1.1, label_width, label_height, self.font, msg, bd_radius = 5, 
                                   padding = self.padding, text_size = self.text_size)
        else:
            self.container = Console(label_x, 1.1, label_width, label_height, self.font, bd_radius = 5, text_size = self.text_size, padding = self.padding)
            self.container.set_text(msg)
        
        self.active = True
        self.anim_manager.add_widget_animation(self.container, "translate_y", 150, 0, (1 - label_height) - 0.05, 1, lambda time=time: self.set_hide_time(time))

    def format_msg(self, msg : str) -> List[str]:
        out = []
        chunk = ""
        words = msg.split(" ")
        for word in words:
            if self.font_copy.size(chunk)[0] > self.max_text_width:
                out.append(chunk[:-1])
                chunk = chunk[-1]
            chunk += word + " "
        out.append(chunk)
        return out
    
    def draw(self, display):
        super().draw(display)    
        if self.hide_time and pg.time.get_ticks() >= self.hide_time:
            self.anim_manager.add_widget_animation(self.container, "translate_y", 150, 0, 1.1, 1, callback = self.cleanup)
            self.active = False
    
    def cleanup(self):
        super().cleanup()
        self.hide_time = None

    def set_hide_time(self, time : int):
        self.hide_time = pg.time.get_ticks() + time