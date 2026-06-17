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
        self.count = 0
        self.animation_stack = {}

    def translate_x(self, index : int) -> bool:
        reached = False
        widget = self.animation_stack[index]["widget"]
        
        if self.animation_stack[index]["delta"] < 0:
            if widget.x <= self.animation_stack[index]["x"]:
                widget.x = self.animation_stack[index]["x"]
                reached = True
        
        if self.animation_stack[index]["delta"] > 0:
            if widget.x >= self.animation_stack[index]["x"]:
                widget.x = self.animation_stack[index]["x"]
                reached = True

        if not reached:
            start_time = pg.time.get_ticks()
            widget.x += self.animation_stack[index]["delta"] * (start_time - self.animation_stack[index]["last_time"])
            self.animation_stack[index]["last_time"] = start_time

        widget.calc_new_rect()
        if hasattr(widget, "children"): widget.change_children()

        return reached

    def translate_y(self, index : int) -> bool:
        reached = False
        widget = self.animation_stack[index]["widget"]
        
        if self.animation_stack[index]["delta"] < 0:
            if widget.y <= self.animation_stack[index]["y"]:
                widget.y = self.animation_stack[index]["y"]
                reached = True
        
        if self.animation_stack[index]["delta"] > 0:
            if widget.y >= self.animation_stack[index]["y"]:
                widget.y = self.animation_stack[index]["y"]
                reached = True

        if not reached:
            start_time = pg.time.get_ticks()
            widget.y += self.animation_stack[index]["delta"] * (start_time - self.animation_stack[index]["last_time"])
            self.animation_stack[index]["last_time"] = start_time

        widget.calc_new_rect()
        if hasattr(widget, "children"): widget.change_children()
        
        return reached

    def scale(self, index : int) -> bool:
        reached_width = reached_height = False
        start_time = pg.time.get_ticks()
        widget = self.animation_stack[index]["widget"]

        if self.animation_stack[index]["scale"] > 1:
            if widget.width >= self.animation_stack[index]["end_w"]: reached_width = True
            if widget.height >= self.animation_stack[index]["end_h"]: reached_height = True
        
        if self.animation_stack[index]["scale"] < 1:
            if widget.width <= self.animation_stack[index]["end_w"]: reached_width = True
            if widget.height <= self.animation_stack[index]["end_h"]: reached_height = True
        
        if not reached_width:
            widget.width += self.animation_stack[index]["delta_w"] * (start_time - self.animation_stack[index]["last_time"])
        else:
            widget.width = self.animation_stack[index]["end_w"]
        
        if not reached_height:
            widget.height += self.animation_stack[index]["delta_h"] * (start_time - self.animation_stack[index]["last_time"])
        else:
            widget.height = self.animation_stack[index]["end_h"]

        self.animation_stack[index]["last_time"] = start_time
        widget.calc_new_rect()
        if hasattr(widget, "children"): widget.change_children()

        return reached_width and reached_height
    
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
        if anim_type == temp[0] or anim_type == temp[1]: 
            self.animation_stack[self.count] = {
                "widget" : widget,
                "anim_type" : anim_type,
                "x" : x,
                "y" : y,
                "delta" : delta,
                "last_time" : pg.time.get_ticks()
            }
        else: 
            self.animation_stack[self.count] = {
                "widget" : widget,
                "anim_type" : anim_type,
                "delta_w" : delta_w,
                "delta_h" : delta_h,
                "end_w" : end_w,
                "end_h" : end_h,
                "scale" : scale,
                "last_time" : pg.time.get_ticks()
            }
        self.count += 1

    # this function should be called in the main loop to properly animate the widgets
    def animate(self):
        del_items = []
        for key in self.animation_stack.keys():
            if self.anim_map[self.animation_stack[key]["anim_type"]](key):
                del_items.append(key)

        if not del_items: return

        for item in del_items: del self.animation_stack[item]            
            
