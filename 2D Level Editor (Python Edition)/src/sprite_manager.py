import pygame as pg
from utils import Label, ScrollableFrame, PixelButton

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
        heading = Label(0.4, 0.05, 0.2, 0.08, self.app.settings["INPUT_FONT"], text = "Sprite Groups")
        self.add_child(heading)

        # sprite card constants
        self.sprite_card_width = 0.2
        self.sprite_card_height = 0.2
        self.margin = 0.05

        # button coords
        self.btn_x = self.margin + (self.sprite_card_width / 2)
        self.btn_y = self.sprite_card_height / 2 + heading.y + self.margin + heading.height

        self.btn_size = 0.05

        self.add_btn = PixelButton(self.btn_x, self.btn_y, self.btn_size, self.btn_size, "res/OpenButton1/non_hovering.png",
                                   border_radius = 15)
        self.add_child(self.add_btn)
        self.add_btn.set_command(lambda: self.app.ask_choice("Are you making a new group or adding a new sprite/animation to an existing group?", ["Group", "Sprite/Animation"], self.delegate_choice_creation))

    def delegate_choice_creation(self):
        choice = self.app.get_choice()

        if choice == "Group":
            self.app.ask_input(["Group Name"], self.create_sprite_group)
        else:
            self.app.ask_input(["Which group?"], self.delegate_choice_group)

    def delegate_choice_group(self):
        pass

    def delegate_choice_loading(self):
        pass

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
        
        if self.sprite_mapping.get(output["Group Name"], None):
            self.app.show_message("Group name is already taken!", 2500)
            return
        self.sprite_mapping[output["Group Name"]] = dict()
        
    def add_sprite_animation(self, name : str, group_name : str, fp : str, frame_width : int, frame_height : int):
        pass

    def add_sprite(self, name : str, group_name : str, fp : str, width : int, height : int):
        pass

