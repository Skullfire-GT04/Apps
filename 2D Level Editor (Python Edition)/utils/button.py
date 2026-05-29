from utils.label import Label
import pygame as pg

"""
This class defines the button widget,
it will be a child widget and will need to belong to a frame at all times
though technically you can have a standalone button as well.
"""

class Button(Label):

    def __init__(self, x : float, y : float, width : float, height : float, font_path, text_size = 16, text = "A button", bd_radius = 10, padding = 10, command = lambda: print("A button was pressed")):
        self.hovering = False
        self.command = command
        self.bindings = {}

        super().__init__(x, y, width, height, font_path, bd_radius = bd_radius, text = text, padding = padding, text_size= text_size)
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
        temp = self.rect.copy()
        temp.width += 2 * self.padding
        temp.height += 2 * self.padding
        pg.draw.rect(display, self.clr_settings["bg"] if not self.hovering else self.clr_settings["btn_hvr_clr"], temp, border_radius = self.bd_radius)

        # drawing the text
        text_surf = self.font.render(self.actual_display_text, False, self.clr_settings["fg"])
        text_rect = text_surf.get_rect(topleft = (self.text_starting_x, self.text_starting_y))

        display.blit(text_surf, text_rect)

    # adds/removes a key binding to the button
    def toggle_key_binding(self, key_code : int):
        if not self.bindings.get(key_code, None):
            self.bindings[key_code] = 1
        else:
            del self.bindings[key_code]

    # updates the button based on the event passed
    def update(self, event : pg.event.Event):
        super().update(event)

        x = self.rect.x 
        y = self.rect.y

        # checking if the event is mouse related and the mouse pointer collides with the button area
        if hasattr(event, "pos"):
            if not (x <= event.pos[0] <= x + self.rect.width and y <= event.pos[1] <= y + self.rect.height):
                self.hovering = False
                return
        
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
        
    def set_command(self, new_command):
        if not callable(new_command): return
        self.command = new_command