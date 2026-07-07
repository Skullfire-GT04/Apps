from utils import Button, Label, ScrollableFrame, PixelButton
from .file_card import FileCard
from .card_utility import move_cards
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
        self.files = dict()

        # adding a heading label
        heading = Label(0.4, 0.03, 0.2, 0.05, self.app.settings["MAIN_FONT"], text = "File Cards")

        # constants

        # file cards configurations
        self.file_card_width = 0.3
        self.file_card_height = 0.4
        self.margin = 0.02

        # add btn configurations
        self.btn_size = 0.04

        # coordinate variables (don't touch these pls)
        self.file_card_x = self.margin
        self.original_y = self.margin + heading.y + heading.height
        self.file_card_y = self.original_y
        self.file_card_x_positions = [round(self.margin * i + self.file_card_width * (i - 1), 2) for i in range(1, int(1 // (self.file_card_width + self.margin)) + 1)]

        # adding the button which adds a new file cards
        self.add_btn = PixelButton(self.file_card_x + self.file_card_width / 2, self.file_card_y + self.file_card_height / 2, self.btn_size, self.btn_size + 0.01,
                                   "res/AddButton1/non_hovering.png", hover_img_path = "res/AddButton1/hovering.png")
        
        self.add_btn.set_command(lambda: self.app.ask_input(["Name", "Save Location"], self.get_file_info, persist = True))
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
        if self.files.get(output["Name"], None):
            self.app.show_message("File with this name exists already!", 3000)
            return
        
        self.app.close_input()
        
        # asking the user for further clarification as to the status of the file
        self.app.ask_choice("Are you making a new file, or loading an old file?", ["Make New", "Load"], lambda: self.add_file_card(output["Name"], output["Save Location"]))

    def add_file_card(self, name : str, save_location : str):
        choice = self.app.get_choice()

        file_card = None
        if choice == "Make New":
            file_card = FileCard(self.file_card_x, self.file_card_y + self.delta, self.file_card_width, self.file_card_height, self.app.settings["INPUT_FONT"], name, save_location, self.app, self)
        else:
            file_card = self.load_file(path.join(save_location, name))

        if file_card:
            self.add_file(name, file_card = file_card)
            self.add_child(file_card)
            self.change_coords()
        else:
            if choice == "Load":
                self.app.show_message("Failed to load file, please make sure it is in the correct directory!", 3500)
            else:
                self.app.show_message("Failed to create new file, please try again!", 3000)

    # removes and unloads a file card and a file
    # repositions all the other file cards accordingly
    def ask_remove_file_card(self, name : str):
        self.app.ask_choice("Are you sure? (Invincible meme lol)", ["Yes", "Nah"], lambda name=name: self.remove_file_card(name))

    def remove_file_card(self, name : str):
        choice = self.app.get_choice()
        if choice == "Nah": return
        self.delete_child(self.files[name])
        index = list(self.files.keys()).index(name)
        del self.files[name]
        self.docker.delete_frame(name)
        self.change_coords(added = False, after_index = index)

    # repositions the add_btn and changed the coordinate for the next
    # file card
    def change_coords(self, added = True, after_index = None):
        if added:
            self.file_card_x += self.file_card_width + self.margin

            if(self.file_card_x > 1 - (self.file_card_width + self.margin)):
                self.file_card_x = self.margin
                self.file_card_y += self.file_card_height + self.margin

            self.add_btn.change_x(self.file_card_x + self.file_card_width / 2)
            self.add_btn.change_y((self.file_card_y + self.delta) + self.file_card_height / 2)

        else:
            cards = list(self.files.values())
            move_cards(after_index, cards, self.add_btn, self.file_card_width, self.file_card_height, self.margin)

            self.file_card_x -= round(self.file_card_width + self.margin, 2)
            if self.file_card_x < self.margin:
                max_cards = 1 // (self.file_card_width + self.margin)
                self.file_card_x = round(self.margin * max_cards + (self.file_card_width * (max_cards - 1)), 2)
                self.file_card_y -= round(self.file_card_height + self.margin, 2)


    # creates a new file 
    def add_file(self, name : str, file_card : FileCard):
        self.files[name] = file_card
        self.docker.add_frame(name, "canvas", app = self.app, docker = self.docker, file_manager = self)
    
    # tries to load a file from given file path
    def load_file(self, fp : str):
        print(fp)
    
    # changes the name of the file_card internally, it does not check whether
    # the new name is valid or not, so checks should be made before invoking this function
    def change_file_card_name(self, name : str, new_name : str):
        data = self.files[name]
        del self.files[name]
        self.files[new_name] = data
        self.docker.change_frame_name(name, new_name)
        
        