import pygame as pg
from utils.widget import Widget

"""
A simple check-button with only horizontal orientation (because that's what makes sense to me ig twin),

NOTE: Unlike the label widget which cuts off overflowing text
      this widget does no such thing
"""

class CheckButton(Widget):

    def __init__(self, x : float, y : float, radius : float, font_path : str, text = "Check Button", text_size = 20, text_justify = "right", border_width = 3, text_margin = 10):
        super().__init__(x, y, radius, radius)
        self.font = pg.font.Font(font_path, size = text_size)
        self.text = text
        self.type = "check_button"
        self.bd_width = border_width
        self.margin = text_margin
        self.load_color_settings("check_button")
        self.justification = text_justify
        self.checked = False
        self.calc_new_rect()

    def set_text_justification(self, new_justification : str):
        if not new_justification in ("left", "right"): return
        self.justification = new_justification
        self.calc_text_pos()

    def set_text(self, new_text : str):
        self.text = new_text
        self.calc_text_pos()

    def draw(self, display : pg.Surface):
        btn_pos = (self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2)
        # drawing the outer circle
        pg.draw.circle(display, self.clr_settings["bd_clr"], btn_pos, (self.rect.width // 2) + self.bd_width)

        # drawing the inner circle
        pg.draw.circle(display, self.clr_settings["unchecked_bg"], btn_pos, self.rect.width // 2)
        if self.checked:
            # drawing the checked inner circle
            pg.draw.circle(display, self.clr_settings["checked_bg"], btn_pos, self.rect.width // 3)

        # drawing the text
        text_surf = self.font.render(self.text, False, self.clr_settings["fg"])
        text_rect = text_surf.get_rect(topleft = (self.text_x, self.rect.y))
        display.blit(text_surf, text_rect)

    def calc_text_pos(self):
        if self.justification == "right":
            self.text_x = self.rect.x + self.rect.width + self.margin
        else:
            text_width = self.font.size(self.text)[0]
            self.text_x = self.rect.x - self.margin - text_width

    def update(self, event):
        super().update(event)
        if not self.enabled: return

        if hasattr(event, "pos"):
            x = self.rect.x
            y = self.rect.y
            if not (x <= event.pos[0] <= x + self.rect.width and y <= event.pos[1] <= y + self.rect.height): return

        if event.type == pg.MOUSEBUTTONDOWN:
            self.checked = not self.checked

    def calc_new_rect(self):
        super().calc_new_rect()
        self.calc_text_pos()
