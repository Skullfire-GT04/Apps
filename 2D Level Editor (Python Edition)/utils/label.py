import pygame as pg
from utils.widget import Widget

"""
This is the parent class of all text-related widgets
it displays the text in the middle of the widget's display area
and leaves space for padding, and doesn't show overflowing text
"""


class Label(Widget):

    def __init__(self, x : float, y : float, width : float, height : float, font_path, bd_radius = 10, text = "A label", padding = 10, text_size = 20):

        self.text = text if text else "A label"
        self.font = pg.font.Font(font_path, size = text_size)
        self.padding = padding
        self.bd_radius = bd_radius
        self.text_starting_x = 0
        self.text_starting_y = 0

        super().__init__(x, y, width, height)
        self.load_color_settings("label")
        self.type = "label"
        self.calc_new_rect()

    # sets a new text for the label
    def set_text(self, new_text : str):
        self.text = new_text
        self.calc_display_text()
        self.calc_text_pos()

    def calc_display_text(self):
        index = 1
        while self.font.size(self.text[:index])[0] <= self.rect.width + 2 * self.padding and index < len(self.text):
            index += 1
        self.actual_display_text = self.text[:index]

    def calc_text_pos(self):
        text_width, text_height = self.font.size(self.actual_display_text)
        self.text_starting_y = (self.rect.height - text_height) / 2 + self.rect.y
        self.text_starting_x = (self.rect.width - text_width) / 2 + self.rect.x

    # draws the label onto the screen
    def draw(self, display : pg.Surface):
        # drawing the box around the text
        temp = self.rect.copy()
        temp.x -= self.padding
        temp.y -= self.padding
        temp.width += 2 * self.padding
        temp.height += 2 * self.padding
        pg.draw.rect(display, self.clr_settings["bg"], temp, border_radius = self.bd_radius)

        # drawing the text
        text_surf = self.font.render(self.actual_display_text, False, self.clr_settings["fg"])
        text_rect = text_surf.get_rect(topleft = (self.text_starting_x, self.text_starting_y))

        display.blit(text_surf, text_rect)

    def change_width(self, new_width):
        super().change_width(new_width)
        self.calc_display_text()
        self.calc_text_pos()
    
    def change_x(self, new_x):
        super().change_x(new_x)
        self.calc_text_pos()

    def change_y(self, new_y):
        super().change_y(new_y)
        self.calc_text_pos()

    def calc_new_rect(self):
        super().calc_new_rect()
        self.calc_display_text()
        self.calc_text_pos()

    # calculates the changes in self when parent changes
    # dimensions or coordinates
    def parent_changes(self):
        if not self.parent: return
        super().parent_changes()
        self.calc_display_text()
        self.calc_text_pos()