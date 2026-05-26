import pygame as pg

"""
This is a parent class of all widgets defined
in this folder
"""

class Widget:

    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pass

    def update(self):
        pass