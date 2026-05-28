import pygame as pg
from utils.widget import Widget


class Label(Widget):

    def __init__(self, x : float, y : float, font, bd_radius = 10, text = "A label", padding = 10, text_size = 20):

        self.text = text
        self.font = pg.font.Font(font, size = text_size)
        self.text_width, self.text_height = self.font.size(self.text)
        self.padding = padding
        self.bd_radius = bd_radius
        
        width = self.text_width + 2 * self.padding
        height = self.text_height + 2 * self.padding

        super().__init__(x, y, width, height)
        self.calc_new_rect()
        self.are_dimensions_absolute = True
        self.type = "label"
        self.load_color_settings("label")

    # sets a new text for the label
    def set_text(self, new_text : str):
        self.text = new_text
        self.text_width, self.text_height = self.font.size(self.text)
        if self.parent:
            self.width = (self.text_width + 2 * self.padding) / self.parent.rect.width
            self.height = (self.text_height + 2 * self.padding) / self.parent.rect.height
            self.are_dimensions_absolute = False
        else:
            self.width = self.text_width + 2 * self.padding
            self.height = self.text_height + 2 * self.padding
            self.are_dimensions_absolute = True
        self.calc_new_rect()

    # draws the label onto the screen
    def draw(self, display : pg.Surface):
        # drawing the box around the text
        pg.draw.rect(display, self.clr_settings["bg"], self.rect, border_radius = self.bd_radius)

        # drawing the text
        text_surf = self.font.render(self.text, False, self.clr_settings["fg"])
        text_rect = text_surf.get_rect(topleft = (self.rect.left + self.padding, self.rect.top + self.padding))

        display.blit(text_surf, text_rect)

    def update(self, event : pg.event.Event):
        if event.type == pg.VIDEORESIZE:
            self.calc_new_rect()
            return

        