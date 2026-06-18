import pygame as pg
from .pop_up_template import PopUp
from utils import Console, Animation

"""
This module provides a way to send messages to the user, the message
disappears after the specified amount of time
"""


class PopUpMessage(PopUp):

    def __init__(self, font_path : str, animation_manager : Animation):
        super().__init__(font_path, self.anim_manager)

        # size configurations (pixel sizes)
        self.text_size = 20

        self.font_copy = pg.font.Font(font_path, self.text_size)

    def show_message(self, msg : str, time : int):

        # calculating appropriate size for container
        pass