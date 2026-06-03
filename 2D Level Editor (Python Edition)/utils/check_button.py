import pygame as pg
from utils.widget import Widget

"""
A simple check-button with only horizontal orientation (because that's what makes sense to me ig twin),
it should be noted that the width and height passed into the constructor is for the button size,
and not the whole widget size, i.e. button + text
"""

class CheckButton(Widget):

    def __init__(self, x : float, y : float, width : float, height : float, font_path : str, text = "Check Button", text_size = 20, text_justify = "right"):
        super().__init__(x, y, width, height)
        self.font = pg.font.Font(font_path, size = text_size)
        self.text = text
        self.type = "check_button"
        self.load_color_settings("check_button")
        self.justification = text_justify
        self.btn_rect = pg.Rect()
        self.calc_new_rect()
        self.btn_rect.width = self.rect.width
        self.btn_rect.height = self.rect.height
        self.calc_btn_pos()

    def set_text_justification(self, new_justification : str):
        if not new_justification in ("left", "right"): return
        self.justification = new_justification
        self.calc_text_pos()

    def draw(self, display : pg.Surface):
        pass

    def calc_text_pos(self):
        pass

    def update(self, event):
        super().update(event)

    def calc_new_rect(self):
        super().calc_new_rect()
