from utils.widget import Widget
import pygame as pg

"""
This class defines the button widget,
it will be a child widget and will need to belong to a frame at all times
though technically you can have a standalone button as well,
but I suggest using the stand_alone_button.py module for that.

Because this one's width and height scales relative to the parent
"""

class Button(Widget):

    def __init__(self, x : float, y : float, font_path, size = 16, text = "A button", bd_radius = 10, padding = 10, command = lambda: print("A button was pressed")):
        self.text = text
        self.font = pg.font.Font(font_path, size)
        self.text_width, self.text_height = self.font.size(self.text)
        self.bd_radius = bd_radius
        self.padding = padding
        self.hovering = False
        self.command = command
        self.bindings = {}

        # calculating the width and height
        width = self.text_width + 2 * self.padding
        height = self.text_height + 2 * self.padding

        super().__init__(x, y, width, height)
        self.calc_new_rect()
        self.are_dimensions_absolute = True
        self.load_color_settings("button")
        self.type = "button"

    # settings a new text to the button and also changing 
    # the size of the button accordingly
    def set_text(self, new_text : str):
        self.text = new_text
        self.text_width, self.text_height = self.font.size(self.text)
        if self.parent:
            self.width = (self.text_width + 2 * self.padding) / self.parent.rect.width
            self.height = (self.text_height + 2 * self.padding) / self.parent.rect.height
            self.are_dimensions_absolute = False
        else:
            self.width = self.text_width + 2 * self.padding
            self.height = self.text_height + 2 * self.padding
            self.are_dimensions_absolute = True
        self.calc_new_rect()

    # draws the button onto the screen
    def draw(self, display : pg.Surface):
        # drawing the box around the text
        pg.draw.rect(display, self.clr_settings["bg"] if not self.hovering else self.clr_settings["btn_hvr_clr"], self.rect, border_radius = self.bd_radius)

        # drawing the text
        text_surf = self.font.render(self.text, True, self.clr_settings["fg"])
        text_rect = text_surf.get_rect(topleft = (self.rect.left + self.padding, self.rect.top + self.padding))
        display.blit(text_surf, text_rect)

    # adds/removes a key binding to the button
    def toggle_key_binding(self, key_code : int):
        if not self.bindings.get(key_code, None):
            self.bindings[key_code] = 1
        else:
            del self.bindings[key_code]

    # updates the button based on the event passed
    def update(self, event : pg.event.Event):
        x = self.parent.rect.x 
        y = self.parent.rect.y

        # checking if the event is mouse related and the mouse pointer collides with the button area
        if hasattr(event, "pos"):
            if not (x <= event.pos[0] <= x + self.rect.width and y <= event.pos[1] <= y + self.rect.height):
                self.hovering = False
                return
            else: print("hovering", event.pos)
        
        # checking for key bindings
        if hasattr(event, "key"):
            if self.bindings.get(event.key, None):
                self.command()
                return

        # checking if the mouse is hovering over the button
        if event.type == pg.MOUSEMOTION:
            self.hovering = True

        # checking if the mouse has clicked the button
        if event.type == pg.MOUSEBUTTONDOWN:
            self.command()
        
