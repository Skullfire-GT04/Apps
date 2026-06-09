import pygame as pg
from utils.widget import Widget

"""
This module defines the animations a widget can have,
here is a list of all the animations defined and what they do:

(i) Translate horizontal : Moves a widget parallel to the horizontal axis
(ii) Translate Vertical : Moves a widget parallel to the vertical axis
(iii) Scale-Up : Increases the size of the widget
(iv) Scale-Down : Decreases the size of the widget

NOTE: The scaling animations maintains the center of the widget

FEATURE: You can activate multiple animations at once for the same widget
"""


class Animation:

    def __init__(self):
        self.anim_map = {
            "translate_x" : self.translate_x,
            "translate_y" : self.translate_y,
            "scale_up" : self.scale_up,
            "scale_down" : self.scale_down
        }
        self.animation_stack = {}

    def translate_x(self, widget : Widget) -> bool:
        if self.check_proximity(widget.x, self.animation_stack[widget][1], 0.01):
            widget.x = self.animation_stack[widget][1]
            widget.calc_new_rect()
            return True

        start_time = pg.time.get_ticks()
        change = self.animation_stack[widget][4] * (start_time - self.animation_stack[widget][5])
        widget.x += change
        self.animation_stack[widget][5] = pg.time.get_ticks()
        widget.calc_new_rect()
        return False

    def translate_y(self, widget : Widget) -> bool:
        if self.check_proximity(widget.y, self.animation_stack[widget][2], 0.01):
            widget.y = self.animation_stack[widget][2]
            widget.calc_new_rect()
            return True

        start_time = pg.time.get_ticks()
        change = self.animation_stack[widget][4] * (start_time - self.animation_stack[widget][5])
        widget.y += change
        self.animation_stack[widget][5] = pg.time.get_ticks()
        widget.calc_new_rect()
        return False

    def scale_up(self, widget : Widget) -> bool:
        pass
    
    def scale_down(self, widget : Widget) -> bool:
        pass

    def check_proximity(self, value1, value2, error) -> bool:
        return abs(value1 - value2) <= error
    
    # adds a new animation to the animation stack
    def add_widget_animation(self, widget : Widget, anim_type : str, time : int, x : float, y : float, scale : float):
        if not anim_type in self.anim_map.keys(): return

        # validating animation arguments
        temp = list(self.anim_map.keys())
        if anim_type == temp[0] and x == widget.x: return
        if anim_type == temp[1] and y == widget.y: return
        if anim_type == temp[2] and scale <= 1: return
        if anim_type == temp[3] and scale >= 1: return

        # calculating delta change (whatever that change might be, will depend on the animation type)
        delta = 0
        if anim_type == temp[0]:
            delta = (x - widget.x) / time
        elif anim_type == temp[1]:
            delta = (y - widget.y) / time
        else:
            delta = (scale - 1) / time

        self.animation_stack[widget] = [anim_type, x, y, scale, delta, pg.time.get_ticks()]

    # this function should be called in the main loop to properly animate the widgets
    def animate(self):
        del_items = []
        for widget in self.animation_stack.keys():
            if self.anim_map[self.animation_stack[widget][0]](widget): del_items.append(widget)

        # removing completed animations from the animation stack
        for item in del_items: del self.animation_stack[item]
            
            
