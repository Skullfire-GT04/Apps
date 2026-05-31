import pygame as pg
from utils.console import Console
from utils.event_manager import INPUT_BOX_TICK_EVENT


class InputBox(Console):

    def __init__(self, x : float, y : float, width : float, height : float, font : str, bd_radius = 10, text_size = 20, padding = 20, border_width = 4, placeholder = "You can type here..."):
        super().__init__(x, y, width, height, font, bd_radius, text_size, padding, border_width)
        self.load_color_settings("input")
        self.text = placeholder
        self.show_tick = True        
        self.selected = False
        self.tick_width = 2

    def draw(self, display : pg.Surface):
        temp = self.rect.copy()
        temp.x -= self.padding + self.bd_width
        temp.y -= self.padding + self.bd_width
        temp.width += 2 * self.bd_width + 2 * self.padding
        temp.height += 2 * self.bd_width + 2 * self.padding
        pg.draw.rect(display, self.clr_settings["bd_clr"] if not self.selected else self.clr_settings["active_bd_clr"], temp, border_radius = self.bd_radius)

        super().draw(display)
        if self.show_tick:
            text_width, text_height = self.font.size(self.text)
            pg.draw.rect(display, self.clr_settings["tick_clr"], pg.Rect(self.text_starting_x + text_width, self.text_starting_y, self.tick_width, text_height))

    def update(self, event : pg.event):
        super().update(event)

        if event.type == INPUT_BOX_TICK_EVENT:
            print("yeah")
            self.show_tick = not self.show_tick
        