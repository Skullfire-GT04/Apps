from utils import Button, Label, ScrollableFrame, PixelButton
from .file_card import FileCard

"""
This module handles the creation, loading,
unloading, and saving of files that the app is
currently working on
"""

class FileManager(ScrollableFrame):

    def __init__(self, kwargs):
        super().__init__(0, 0, 1, 1)
        self.app = kwargs["app"]
        self.docker = kwargs["docker"]
        self.pop_up_window = kwargs["pop_up_window"]

        # constants

        # file cards configurations
        self.file_card_width = 0.3
        self.file_card_height = 0.4
        self.margin = 0.02

        # add btn configurations
        self.btn_size = 0.04

        # coordinate variables (don't touch these pls)
        self.file_card_x = self.margin
        self.file_card_y = self.margin + 0.1

        # adding a heading label
        heading = Label(0.4, 0.03, 0.2, 0.05, self.app.settings["MAIN_FONT"], text = "File Cards")

        # adding the button which adds a new file cards
        self.add_btn = PixelButton(self.file_card_x + self.file_card_width / 2, self.file_card_y + self.file_card_height / 2, self.btn_size, self.btn_size + 0.01,
                                   "res/AddButton1/non_hovering.png", hover_img_path = "res/AddButton1/hovering.png")
        
        self.add_btn.set_command(self.add_file_card)
        self.add_child(self.add_btn)
        self.add_child(heading)
        
    # adds a file card to the UI
    def add_file_card(self):
        file_card = FileCard(self.file_card_x, self.file_card_y + self.delta, self.file_card_width, self.file_card_height, self.app.settings["MAIN_FONT"])
        self.add_child(file_card)
        self.change_coords()

    def add_default_inputs(self, name : str):
        pass

    # removes and unloads a file card and a file
    # repositions all the other file cards accordingly
    def remove_file_card(self, name : str):
        pass

    # repositions the add_btn and changed the coordinate for the next
    # file card
    def change_coords(self):
        self.file_card_x += self.file_card_width + self.margin

        if(self.file_card_x > 1 - (self.file_card_width + self.margin)):
            self.file_card_x = self.margin
            self.file_card_y += self.file_card_height + self.margin

        self.add_btn.change_x(self.file_card_x + self.file_card_width / 2)
        self.add_btn.change_y((self.file_card_y + self.delta) + self.file_card_height / 2)

    # creates a new file 
    def add_file(self, name : str):
        pass
    
    # tries to load a file from given file path
    def load_file(self, fp : str):
        pass