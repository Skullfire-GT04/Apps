import pygame as pg
from utils import ScrollableFrame, Label, PixelButton
from .sprite_group import SpriteGroup


class SpriteGroupManager(ScrollableFrame):

    def __init__(self, app, docker):
        super().__init__(0, 0, 1, 1, bd_radius = 0)
        self.app = app
        self.docker = docker
        self.groups = dict()

        # adding a heading 
        heading = Label(0.35, 0.04, 0.3, 0.08, self.app.settings["INPUT_FONT"], text = "Sprite Groups")
        self.add_child(heading)

        # constants
        self.group_width = 0.8
        self.group_height = 0.1
        self.margin = 0.1
        self.btn_size = 0.05

        # variables
        self.group_card_x = self.margin
        self.group_card_y = heading.y + heading.height + self.margin

        # add btn
        self.add_btn = PixelButton((1 - self.btn_size) / 2, self.group_card_y + (self.group_height / 2), self.btn_size, self.btn_size, 
                                   "res/AddButton1/non_hovering.png", hover_img_path = "res/AddButton1/hovering.png", border_radius = 4)
        self.add_child(self.add_btn)
        self.add_btn.set_command(lambda: self.app.ask_input(["Group Name"], self.add_group, persist = True))

    def add_group(self):
        name = self.app.get_input().get("Group Name", None)

        if not name:
            self.app.show_message("Invalid Name!", 2000)
            return
        
        if name.isdigit():
            self.app.show_message("Name cannot be a number!", 2000)
            return
        
        if self.groups.get(name, None):
            self.app.show_message("Group with this name already exists!", 2000)
            return
        
        index = len(self.groups) + 1
        self.groups[name] = SpriteGroup(self.margin, self.group_card_y, self.group_height, name, index, self.app, self)
        self.add_child(self.groups[name])
        self.app.close_input()
        self.change_coords()

    def change_coords(self, added = True, after_index = None):
        if added:
            self.group_card_y += self.group_height + self.margin
            self.add_btn.change_y(self.add_btn.y + self.margin + self.group_height)

    def remove_group(self, name : str):
        pass


