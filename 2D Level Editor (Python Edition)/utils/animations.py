import pygame as pg
from utils.widget import Widget

"""
This module defines the animations a widget can have,
here is a list of all the animations defined and what they do:

(i) Translate horizontal : Moves a widget parallel to the horizontal axis
(ii) Translate Vertical : Moves a widget parallel to the vertical axis
(iii) Scale-Up : Increases the size of the widget
(iv) Scale-Down : Decreases the size of the widget

NOTE: The scaling animations does not maintain the center of the widget

FEATURE: You can activate multiple animations at once for the same widget
"""


class Animation:

    def __init__(self):
        self.anim_map = {
            "translate_x" : self.translate_x,
            "translate_y" : self.translate_y,
            "scale_up" : self.scale,
            "scale_down" : self.scale
        }
        self.animation_stack = []

    def translate_x(self, index : int) -> bool:
        widget = self.animation_stack[index][0]
        if self.check_proximity(widget.x, self.animation_stack[index][2], 0.01):
            widget.x = self.animation_stack[index][2]
            return True
        start_time = pg.time.get_ticks()
        widget.x += self.animation_stack[index][4] * (start_time - self.animation_stack[index][5])
        self.animation_stack[index][5] = start_time
        widget.calc_new_rect()
        return False

    def translate_y(self, index : int) -> bool:
        widget = self.animation_stack[index][0]
        if self.check_proximity(widget.y, self.animation_stack[index][3], 0.01):
            widget.y = self.animation_stack[index][3]
            return True
        start_time = pg.time.get_ticks()
        widget.y += self.animation_stack[index][4] * (start_time - self.animation_stack[index][5])
        self.animation_stack[index][5] = start_time
        widget.calc_new_rect()
        return False

    def scale(self, index : int) -> bool:
        reached_width = reached_height = False
        start_time = pg.time.get_ticks()
        widget = self.animation_stack[index][0]

        if self.check_proximity(widget.width, self.animation_stack[index][4], 0.01):
            widget.width = self.animation_stack[index][4]
            reached_width = True
        else:
            widget.width += self.animation_stack[index][2] * (start_time - self.animation_stack[index][6])

        if self.check_proximity(widget.height, self.animation_stack[index][5], 0.01):
            widget.height = self.animation_stack[index][5]
            reached_height = True
        else:
            widget.height += self.animation_stack[index][3] * (start_time - self.animation_stack[index][6])

        self.animation_stack[index][6] = start_time
        widget.calc_new_rect()

        return reached_width and reached_height

    def check_proximity(self, value1, value2, error) -> bool:
        return abs(value1 - value2) <= error
    
    # adds a new animation to the animation stack
    def add_widget_animation(self, widget : Widget, anim_type : str, time : int, x : float, y : float, scale : float):
        if not self.anim_map.get(anim_type, None): return

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

        # calculating the center position of the widget for scaling animations
        end_w = widget.width * scale
        end_h = widget.height * scale
        delta_w = (end_w - widget.width) / time
        delta_h = (end_h - widget.height) / time

        # adding the animation to the stack
        if anim_type == temp[0] or anim_type == temp[1]: self.animation_stack.append([widget, anim_type, x, y, delta, pg.time.get_ticks()])
        else: self.animation_stack.append([widget, anim_type, delta_w, delta_h, end_w, end_h, pg.time.get_ticks()])


    # this function should be called in the main loop to properly animate the widgets
    def animate(self):
        del_items = []
        for i in range(len(self.animation_stack)):
            if self.anim_map[self.animation_stack[i][1]](i): del_items.append(i)

        count = 0
        index = 0
        while index < len(self.animation_stack):
            if index in del_items:
                self.animation_stack.pop(index - count)
                count += 1
            else: index += 1
            
            
