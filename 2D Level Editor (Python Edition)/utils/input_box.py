import pygame as pg
from utils.console import Console
from utils.event_manager import INPUT_BOX_TICK_SPEED

"""
This is the parent class for all text input based widgets,
conceptually is a label, but it draws the text not in the middle 
but right justified
"""

class InputBox(Console):

    def __init__(self, x : float, y : float, width : float, height : float, font : str, bd_radius = 10, text_size = 20, padding = 20, border_width = 4, placeholder = "You can type here..."):
        super().__init__(x, y, width, height, font, bd_radius, text_size, padding, border_width)
        self.load_color_settings("input")
        self.type = "input"
        self.hovering = False
        self.set_text(placeholder)
        self.placeholder = placeholder
        self.not_allowed_chars = {}
        self.typed_in = False
        self.show_tick = False
        self.last_tick_show = pg.time.get_ticks()
        self.selected = False
        self.tick_width = 2

    def set_text(self, new_text):
        super().set_text(new_text)
        self.typed_in = True

    def draw(self, display : pg.Surface):
        if self.selected:
            temp = pg.time.get_ticks()
            if temp >= self.last_tick_show + 1000 // INPUT_BOX_TICK_SPEED:
                self.show_tick = not self.show_tick
                self.last_tick_show = temp

        temp = self.rect.copy()
        temp.x -= self.padding + self.bd_width
        temp.y -= self.padding + self.bd_width
        temp.width += 2 * self.bd_width + 2 * self.padding
        temp.height += 2 * self.bd_width + 2 * self.padding
        pg.draw.rect(display, self.clr_settings["bd_clr"] if not self.selected and not self.hovering else self.clr_settings["active_bd_clr"], temp, border_radius = self.bd_radius)

        temp.x += self.bd_width
        temp.y += self.bd_width
        temp.width -= 2 * self.bd_width
        temp.height -= 2 * self.bd_width
        pg.draw.rect(display, self.clr_settings["bg"], temp, border_radius = self.bd_radius)

        text_surf = self.font.render(self.actual_display_text, False, self.clr_settings["fg" if self.typed_in else "placeholder_fg"])
        text_rect = text_surf.get_rect(topleft = (self.text_starting_x, self.text_starting_y))
        display.blit(text_surf, text_rect)

        if self.show_tick:
            text_width, text_height = self.font.size(self.actual_display_text)
            pg.draw.rect(display, self.clr_settings["tick_clr"], pg.Rect(self.text_starting_x + text_width, self.text_starting_y, self.tick_width, text_height))
    
    def calc_text_pos(self):
        text_height = self.font.size(self.actual_display_text)[1]
        self.text_starting_y = (self.rect.height - text_height) / 2 + self.rect.y
        self.text_starting_x = self.rect.x

    def calc_display_text(self):
        count = 1
        while self.font.size(self.text[len(self.text) - count - 1:len(self.text)])[0] <= self.rect.width and count < len(self.text):
            count += 1
        self.actual_display_text = self.text[len(self.text) - count:len(self.text)]

    # adds or removes not allowed characters
    def toggle_not_allowed_char(self, char : str):
        if not isinstance(char, str): return
        if self.not_allowed_chars.get(char, None): del self.not_allowed_chars[char]
        else: self.not_allowed_chars[char] = 1

    def update(self, event : pg.event):
        super().update(event)
        if not self.enabled: return

        if hasattr(event, "pos"):
            x = self.rect.x
            y = self.rect.y
            if not (x <= event.pos[0] <= x + self.rect.width and y <= event.pos[1] <= y + self.rect.height): 
                self.hovering = False
                if event.type == pg.MOUSEBUTTONDOWN: self.selected = False
                return

        if event.type == pg.MOUSEMOTION:
            self.hovering = True

        # selecting the text_box
        if event.type == pg.MOUSEBUTTONDOWN:
            self.selected = not self.selected
            if self.selected and not self.typed_in:
                self.set_text("")
            if not self.selected: 
                self.show_tick = False
            if not self.selected and not len(self.text): 
                self.typed_in = False
            if not self.selected and not self.typed_in:
                self.set_text(self.placeholder)
            
        # writing into the input box
        if event.type == pg.KEYDOWN and self.selected:
            if self.not_allowed_chars.get(event.unicode, None): return
            if event.key != pg.K_BACKSPACE:
                self.set_text(self.text + event.unicode)
            else:
                self.set_text(self.text[:-1] if len(self.text) > 1 else "")
            self.typed_in = True if len(self.text) else False

