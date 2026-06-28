import pygame as pg
from utils import Label, ScrollableFrame, PixelButton

"""
This module manages the loading of spritesheets or individual
sprites, the user can change the animation speed of any sprite group's
particular animation, you can also move the individual frame's positions.
You can also add frames or delete frames from an animation
"""

class SpriteManager(ScrollableFrame):

    def __init__(self, app, docker):
        super().__init__(0, 0, 1, 1)
        self.app = app
        self.docker = docker
        self.sprite_mapping = dict() # stores the actual groups and sprites
        self.widget_mapping = dict() # stores widget mapping of all animations and sprites belonging to a group
        

        # adding a heading (lol that rhymes)
        heading = Label(0.4, 0.05, 0.2, 0.08, self.app.settings["INPUT_FONT"], text = "Sprite/Animations")
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
                                   border_radius = 0)
        self.add_child(self.add_btn)
        self.add_btn.set_command(lambda: self.app.ask_choice("Are you adding a new sprite or an animation?", ["Sprite", "Animation"], self.delegate_choice_creation))

    def delegate_choice_creation(self):
        choice = self.app.get_choice()

        if choice == "Sprite":
            self.app.ask_input(["Which group?", "File Path", "Name", "Width", "Height"], lambda: self.validate_input(animation = False), persist = True)
        else:
            self.app.ask_input(["Which group?", "File Path", "Name", "Frame Width", "Frame Height"], self.validate_input, persist = True)

    def validate_input(self, animation = True):
        output = self.app.get_input()
        
    def add_sprite_animation(self):
        pass

    def add_sprite(self):
        pass

