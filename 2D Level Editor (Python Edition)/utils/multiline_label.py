import pygame as pg
from .label import Label
from math import ceil


"""
This module defines a multi-line label, the text field of this widget
should contain proper text formatting with '\n' characters, because it 
internally divides the text with '\n' as the delimiter

NOTE: This widget doesn't position the text in the center, since it doesn't make sense in this context
"""


class MultiLineLabel(Label):

    def __init__(self, x : float, y : float, width : float, height : float, font_path : str, text = "This is a label", bd_radius = 10, padding = 10, text_size = 20, text_gap = 5):
        self.text_gap = text_gap
        self.display_chunks = []
        super().__init__(x, y, width, height, font_path, text = text, padding = padding, text_size = text_size, bd_radius = bd_radius)

    def set_text(self, new_text):
        self.text = new_text
        self.calc_display_text()

    # clamps text according to the widget width
    def calc_display_text(self):  
        self.display_chunks = []
        temp = ""
        for ch in self.text:
            if ch == '\n': 
                self.display_chunks.append(temp) 
                temp = ""
            elif self.font.size(temp)[0] > self.rect.width:
                self.display_chunks.append(temp[:-1])
                temp = temp[-1]
            else: temp += ch
        self.clamp_height()

    # clamps text according to widget height
    def clamp_height(self):
        unit = self.font.size("a")[1] + self.text_gap
        total_units = ceil(self.rect.height / unit)
        self.display_chunks = self.display_chunks[:total_units]
            
    def calc_text_pos(self):
        self.text_starting_x = self.rect.x
        self.text_starting_y = self.rect.y

    def draw(self, display : pg.Surface):
        temp = self.rect.copy()
        temp.x -= self.padding
        temp.y -= self.padding
        temp.width += 2 * self.padding
        temp.height += 2 * self.padding + self.text_gap

        pg.draw.rect(display, self.clr_settings["bg"], temp, border_radius = self.bd_radius)

        y = self.text_starting_y
        for chunk in self.display_chunks:
            text_surf = self.font.render(chunk, True, self.clr_settings["fg"])
            text_rect = text_surf.get_rect(topleft = (self.text_starting_x, y))
            display.blit(text_surf, text_rect)
            y += self.font.size("a")[1] + self.text_gap

    def change_height(self, new_height):
        super().change_height(new_height)
        self.calc_display_text()
        
    

    