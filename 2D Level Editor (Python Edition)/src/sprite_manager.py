import pygame as pg
from utils import Label, ScrollableFrame, PixelButton
from .sprite_group import SpriteGroup

"""
This module manages the loading of spritesheets or individual
sprites, the user can change the animation speed of any sprite group's
particular animation, you can also move the individual frame's positions.
You can also add frames or delete frames from an animation
"""

class SpriteManager(ScrollableFrame):

    def __init__(self, app):
        super().__init__(0, 0, 1, 1)
        self.app = app
        self.sprite_mapping = dict() # stores the actual groups and sprites
        self.widget_mapping = dict() # stores references to sprite groups and animations

        # adding a heading (lol that rhymes)
        heading = Label(0.4, 0.05, 0.2, 0.15, self.app.settings["INPUT_FONT"], text = "Sprite Groups")
        self.add_child(heading)

        # constants
        self.margin = 0.03
        self.group_width = 0.44
        self.group_height = 0.4

        # group coords
        self.group_card_x = self.margin
        self.group_card_y = heading.y + heading.height + self.margin

        # button coords
        self.btn_x = self.margin + (self.group_width / 2)
        self.btn_y = self.group_height / 2 + heading.y + self.margin + heading.height

        self.btn_size = 0.05

        self.add_btn = PixelButton(self.btn_x, self.btn_y, self.btn_size, self.btn_size, "res/AddButton1/hovering.png", hover_img_path = "res/AddButton1/non_hovering.png",
                                   border_radius = 15)
        self.add_child(self.add_btn)
        self.add_btn.set_command(lambda: self.app.ask_input(["Group Name"], self.create_sprite_group))

    def create_sprite_group(self):
        output = self.app.get_input()

        if not output.get("Group Name", None):
            self.app.show_message("Internal Error, try again!", 2500)
            return

        if not output["Group Name"]:
            self.app.show_message("Invalid group name!", 2500)
            return 
        
        if output["Group Name"].isdigit():
            self.app.show_message("Group name cannot be a number!", 2500)
            return        
        
        if self.widget_mapping.get(output["Group Name"], None):
            self.app.show_message("Group with this name already exists!", 2500)
            return

        self.widget_mapping[output["Group Name"]] = SpriteGroup(self.group_card_x, self.group_card_y, self.group_width, self.group_height, output["Group Name"], self.app.settings["INPUT_FONT"], self, self.app)
        self.add_child(self.widget_mapping[output["Group Name"]])

    def add_sprite_animation(self, name : str, group_name : str, fp : str, frame_width : int, frame_height : int):
        pass

