from utils import Button, Label, ScrollableFrame, PixelButton
from .file_card import FileCard
from os import path


"""
This module handles the creation, loading,
unloading, and saving of files that the app is
currently working on
"""

class FileManager(ScrollableFrame):

    def __init__(self, app, docker):
        super().__init__(0, 0, 1, 1)
        self.app = app
        self.docker = docker

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
        
        self.add_btn.set_command(lambda: self.app.ask_input(["Name", "Save Location"], self.get_file_info))
        self.add_child(self.add_btn)
        self.add_child(heading)
        
    # adds a file card to the UI
    def get_file_info(self):
        output = self.app.get_input()
        # validating the input
        if not output["Name"]:
            self.app.show_message("Invalid Name!", 2000)
            return
        
        # making sure the file name is something ok with the OS
        if output["Name"].isdigit():
            self.app.show_message("Name cannot be a number!", 2000)
            return
        
        # making sure the save location exists
        if not path.exists(output["Save Location"]):
            self.app.show_message("Invalid Save Location!", 2000)
            return

        # checking if the file name already exists as one of the active files
        if self.docker.frames.get(output["Name"], None):
            self.app.show_message("File with this name exists already!", 3000)
            return
        
        # asking the user for further clarification as to the status of the file
        self.app.ask_choice("Are you making a new file, or loading an old file?", ["Make New", "Load"], lambda: self.add_file_card(output["Name"], output["Save Location"]))

    def add_file_card(self, name : str, save_location : str):
        choice = self.app.get_choice()

        file_card = None
        if choice == "Make New":
            file_card = FileCard(self.file_card_x, self.file_card_y + self.delta, self.file_card_width, self.file_card_height, self.app.settings["MAIN_FONT"], name, save_location, self.app, self)
        else:
            file_card = self.load_file(path.join(save_location, name))
        self.add_child(file_card)
        self.change_coords()

    # removes and unloads a file card and a file
    # repositions all the other file cards accordingly
    def remove_file_card(self, name : str):
        pass

    # repositions the add_btn and changed the coordinate for the next
    # file card
    def change_coords(self, added = True):
        if added:
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