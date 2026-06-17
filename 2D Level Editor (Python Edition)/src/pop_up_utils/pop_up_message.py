import pygame as pg
from utils import Console, Animation

"""
This module provides a way to send messages to the user
"""


class PopUpMessage:

    def __init__(self, display : pg.display, font_path : str, animation_manager : Animation):
        self.container = Console(-1, -1, 0, 0, font_path)
        self.font = self.container.font
        self.display = display
        self.anim_manager = animation_manager