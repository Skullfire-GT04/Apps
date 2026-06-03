import pygame as pg
from utils.widget import Widget

"""
A basic slider widget with two orientations,
the bottom value for vertical orientation is at the top
and for horizontal it is at left
"""


class Slider(Widget):

    def __init__(self, x : float, y : float, width : float, height : float, from_ = 0, to = 100, orient = "vertical", border_radius = 10):
        super().__init__(x, y, width, height)
        self.type = "slider"
        self.load_color_settings("slider")
        self.from_ = from_
        self.to = to
        self.value = from_
        self.orient = orient
        self.bd_radius = border_radius
        self.hovering = False
        self.selected = False
        self.calc_new_rect()
        self.btn_rect = pg.Rect()

    # sets a new value 
    def set_value(self, new_val : int):
        if not self.from_ <= new_val <= self.to: return
        self.value = new_val

    def set_orient(self, new_orient : str):
        if not new_orient in ("horizontal", "vertical"): return
        self.orient = new_orient
        self.calc_step_val()
        self.calc_btn_radius()
    
    def calc_step_val(self):
        self.step_value = (self.get_absolute_width() if self.orient == "horizontal" else self.get_absolute_height()) / abs(self.to - self.from_)

    def calc_btn_radius(self):
        if self.orient == "horizontal":
            self.btn_radius = self.get_absolute_height()
        else:
            self.btn_radius = self.get_absolute_width()

    def draw(self, display : pg.Surface):
        pg.draw.rect(display, self.clr_settings["bg"], self.rect, border_radius = self.bd_radius) 

        temp = self.rect.copy()
        filled_len = self.value * self.step_value
        if self.orient == "horizontal":
            temp.width = filled_len
        else:
            temp.height = filled_len

        pg.draw.rect(display, self.clr_settings["fill_clr"], temp, border_radius = self.bd_radius)

        btn_pos = [0, 0]

        if self.orient == "horizontal":
            btn_pos[1] = self.rect.top + self.rect.height / 2
            btn_pos[0] = self.rect.x + filled_len
        else:
            btn_pos[0] = self.rect.left + self.rect.width / 2
            btn_pos[1] = self.rect.y + filled_len

        self.btn_rect = pg.draw.circle(display, self.clr_settings["btn_bg"] if not (self.hovering or self.selected) else self.clr_settings["btn_hvr_clr"], btn_pos, self.btn_radius)

    def calc_new_rect(self):
        super().calc_new_rect()
        self.calc_step_val()
        self.calc_btn_radius()

    def update(self, event : pg.event):
        super().update(event)

        if event.type == pg.MOUSEBUTTONUP:
            self.selected = False

        if hasattr(event, "pos"):
            x = self.btn_rect.x
            y = self.btn_rect.y
            if not (x <= event.pos[0] <= x + self.btn_rect.width and y <= event.pos[1] <= y + self.btn_rect.height):
                if not self.selected: 
                    self.hovering = False
                    return

        if event.type == pg.MOUSEMOTION: 
            self.hovering = True
        
        if event.type == pg.MOUSEBUTTONDOWN:
            self.selected = True

        if self.selected:
            if self.orient == "horizontal":
                if event.pos[0] < self.rect.x: self.value = self.from_
                elif event.pos[0] > self.rect.x + self.rect.width: self.value = self.to
                else:
                    cord_x = event.pos[0] - self.rect.x
                    self.value = cord_x // self.step_value
            else:
                if event.pos[1] < self.rect.y: self.value = self.from_
                elif event.pos[1] > self.rect.y + self.rect.height: self.value = self.to
                else:
                    cord_y = event.pos[1] - self.rect.y
                    self.value = cord_y // self.step_value
