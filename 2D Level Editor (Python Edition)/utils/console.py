import pygame as pg
from utils.widget import Widget


class Console(Widget):

    def __init__(self, x : float, y : float, font, width, height, bd_radius = 20, text_size = 15):
        super().__init__(x, y, width, height)