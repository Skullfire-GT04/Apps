from utils.child_widget import ChildWidget
from utils.widget import Widget
import pygame as pg


class Button(ChildWidget):

    def __init__(self, x, y, font_path, size = 16, text = "A button", bd_radius = 10, padding = 10):
        self.text = text
        self.bg = "#4c5ac6"
        self.fg = "#E7E7E7"
        self.type = "button"
        self.font = pg.font.Font(font_path, size)
        self.text_width, self.text_height = self.font.size(self.text)
        self.bd_radius = bd_radius
        self.padding = padding

        width = self.text_width + 2 * padding
        height = self.text_height + 2 * padding

        super().__init__(x, y, width, height)

    def set_text(self, new_text : str):
        self.text = new_text
        self.text_width, self.text_height = self.font.size(self.text)

    def draw(self, display : pg.Surface):
        pg.draw.rect(display, self.bg, pg.Rect(self.x, self.y, self.width, self.height), border_radius = self.bd_radius)

        # drawing the text
        text_surf = self.font.render(self.text, False, self.fg)
        text_rect = text_surf.get_rect(topleft = (self.x + self.padding, self.y + self.padding))
        display.blit(text_surf, text_rect)

    def update(self, frame : Widget):
        pass        