import pygame as pg
from utils import BorderFrame, Label, Button, PixelButton, InputBox


class SpriteGroup(BorderFrame):

    def __init__(self, margin : float, y : float, height : float, name : str, index : int, app, manager):
        super().__init__(margin, y, 1 - 2 * margin, height, bd_radius = 3, border_width = 1)
        self.name = name
        self.app = app
        self.manager = manager

        # adding a label for the index
        self.index_label = Label(0, 0, 0.1, 1, self.app.settings["INPUT_FONT"], text = str(index), padding = 0)
        self.add_child(self.index_label)

        # adding a label for the group name
        self.name_input = InputBox(self.index_label.x + self.index_label.width + 0.05, 0, 0.3, 1, self.app.settings["INPUT_FONT"], bd_radius = 3, padding = 0,
                                   border_width = 1)
        self.name_input.set_text(self.name)
        self.name_input.disable()
        self.add_child(self.name_input)

        # adding a removing button
        self.remove_button = PixelButton(1 - (0.05), 0.1, 0.04, 0.4, "res/CloseButton1/non_hovering.png", border_radius = 3)
        self.remove_button.clr_settings["bg"] = "#EA3737"
        self.remove_button.clr_settings["btn_hvr_clr"] = "#6F1414"
        self.remove_button.set_command(lambda: self.manager.remove_group(self.name))
        self.add_child(self.remove_button)

        # edit name button
        self.edit_btn = PixelButton(self.name_input.x + self.name_input.width, 0.35, 0.05, 0.3, "res/EditButton1/non_hovering.png", border_radius = 3)
        self.add_child(self.edit_btn)

        # flags
        self.editing = False

    def toggle_edit(self):
        self.editing = not self.editing
        if not self.editing:
            self.name_input.disable()
            self.save_changes()
        else:
            self.name_input.enable()

    def save_changes(self):
        pass


    