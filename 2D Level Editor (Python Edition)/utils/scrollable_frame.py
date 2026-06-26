import pygame as pg
from .frame import Frame

"""
This module implements a scrollable frame,
the scroll only work for the vertical axis

NOTE: Any widget made from this class should take into account the delta
      or scroll value when adding children, the reason I have not added it in the add_child
      method explicitly is because I want to provide the user with full freedom

"""


class ScrollableFrame(Frame):

    def __init__(self, x, y, width, height, bd_radius = 10):
        super().__init__(x, y, width, height, bd_radius = bd_radius)
        self.scroll_speed = 0.05
        self.type = "scrollable_frame"
        self.delta = 0        
    
    def scroll_children(self, value : float):
        for child in self.children.values():
            child.change_y(child.y + value)

    def update(self, event : pg.Event):
        super().update(event)
        if not self.enabled: return

        if event.type == pg.MOUSEWHEEL:
            self.delta += - self.scroll_speed if event.y < 1 else self.scroll_speed
            
            # adding scroll limits
            if self.delta > 0: self.delta = 0

            # scrolling the children
            if self.delta: 
                self.scroll_children(-self.scroll_speed if event.y < 1 else self.scroll_speed)
