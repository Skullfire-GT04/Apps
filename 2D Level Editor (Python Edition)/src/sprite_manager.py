import pygame as pg
from utils import BorderFrame, Button, Label, ScrollableFrame

"""
This module manages the loading of spritesheets or individual
sprites, the user can change the animation speed of any sprite group's
particular animation, you can also move the individual frame's positions.
You can also add frames or delete frames from an animation
"""

class SpriteManager(ScrollableFrame):

    def __init__(self, **kwargs):
        super().__init__(0, 0, 1, 1)
        self.sprite_mapping = dict()

    def create_sprite_group(self, name : str):
        pass

    def add_sprite_animation(self, name : str, group_name : str):
        pass

