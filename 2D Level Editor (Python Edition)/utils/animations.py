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

FEATURE: You can active multiple animations at once
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
        pass

    def translate_y(self, widget : Widget) -> bool:
        pass

    def scale_up(self, widget : Widget) -> bool:
        pass
    
    def scale_down(self, widget : Widget) -> bool:
        pass
    
    def add_widget_animation(self, widget : Widget, anim_type : str, time : int, x : float, y : float, scale : float):
        if not anim_type in self.anim_map.keys(): return

        # validating animation arguments
        temp = self.anim_map.keys()
        if anim_type == temp[0] and x == widget.x: return
        if anim_type == temp[1] and y == widget.y: return
        if anim_type == temp[2] and scale <= 1: return
        if anim_type == temp[3] and scale >= 1: return

        # calculating delta change (whatever that change might be, will depend on the animation type)

        self.animation_stack[widget] = [anim_type, x, y, scale]

    # this function should be called in the main loop to properly animate the widgets
    def animate(self):
        del_items = []
        for widget in self.animation_stack.keys():
            if not self.anim_map[self.animation_stack[widget][0]](widget): del_items.append(widget)

        # removing completed animations from the animation stack
        for item in del_items: del self.animation_stack[item]
            
            
