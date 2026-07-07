import pygame as pg
from utils import BorderFrame, Label, Button, PixelButton, InputBox


class SpriteGroup(BorderFrame):

    def __init__(self, x : float, y : float, width : float, height : float, name : str, index : int, app, manager):
        super().__init__(x, y, width, height, bd_radius = 3, border_width = 3)
        self.name = name
        self.app = app
        self.manager = manager

        # adding a label for the index
        self.index_label = Label(0, 0, 0.1, 1, self.app.settings["INPUT_FONT"], text = str(index), padding = 0)
        self.add_child(self.index_label)

        # adding a label for the group name
        self.name_input = InputBox(self.index_label.x + self.index_label.width, 0, 0.3, 1, self.app.settings["INPUT_FONT"], bd_radius = 3, padding = 0,
                                   border_width = 1, placeholder = "")
        self.name_input.set_text(self.name)
        self.name_input.disable()
        self.add_child(self.name_input)

        # adding a removing button
        self.remove_button = PixelButton(1 - 0.1, 0.1, 0.1, 0.8, "res/CloseButton1/non_hovering.png", border_radius = 10)
        self.remove_button.clr_settings["bg"] = "#EA3737"
        self.remove_button.clr_settings["btn_hvr_clr"] = "#6F1414"
        self.remove_button.set_command(lambda: self.manager.ask_remove_group_card(self.name))
        self.add_child(self.remove_button)

        # edit name button
        self.edit_btn = PixelButton(self.name_input.x + self.name_input.width, 0, 0.15, 1, "res/EditButton1/non_hovering.png", border_radius = 3)
        self.edit_btn.set_command(self.toggle_edit)
        self.add_child(self.edit_btn)

        # save changes button
        self.save_btn = Button(self.edit_btn.x + self.edit_btn.width, 0, 0.3, 1, self.app.settings["INPUT_FONT"], text = "Save changes", padding = 0, bd_radius = 3)
        self.add_child(self.save_btn)
        self.save_btn.set_command(self.save_changes)

        # flags
        self.editing = False

    def toggle_edit(self):
        self.editing = not self.editing
        self.app.show_message(f"Edit Status: {self.editing}", 1000)
        if not self.editing:
            self.name_input.set_text(self.name)
            self.name_input.disable()
        else:
            self.name_input.enable()

    def save_changes(self):
        if self.name_input.text != self.name:
            if not self.name_input.text:
                self.app.show_message("Invalid Name!", 2000)
                return
            if self.name_input.text.isdigit():
                self.app.show_message("Name cannot be a number!", 2000)
                return
            if self.manager.groups.get(self.name_input.text, None):
                self.app.show_message("A group with this name already exists!", 2000)
                return

        self.manager.change_group_name(self.name, self.name_input.text)
        self.name = self.name_input.text

    def set_index(self, new_index : int):
        self.index_label.set_text(str(new_index))
    