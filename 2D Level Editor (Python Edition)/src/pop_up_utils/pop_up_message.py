import pygame as pg
from .pop_up_template import PopUp
from utils import Console, Animation, BorderFrame, MultiLineLabel

"""
This module provides a way to send messages to the user, the message
disappears after the specified amount of time
"""


class PopUpMessage(PopUp):

    def __init__(self, font_path : str, animation_manager : Animation):
        super().__init__(font_path, animation_manager)

        # size configurations (pixel sizes)
        self.text_size = 15
        self.padding = 10
        self.max_text_width = 300
        self.max_text_height = 400

        # font for measuring
        self.font_copy = pg.font.Font(font_path, self.text_size)

    def show_message(self, msg : str, time : int):
        # calculating appropriate size for container
        text_width, text_height = self.font_copy.size(msg)


        container_width = text_width + (2 * self.padding) if text_width + (2 * self.padding) <= self.max_text_width else self.max_text_width
        container_height = text_height + (2 * self.padding) if text_height + (2 * self.padding) <= self.max_text_height else self.max_text_height

        