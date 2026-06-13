import pygame as pg
from utils import BorderFrame, Button, InputBox, Label, ScrollableFrame

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

        # constants

        # file cards
        self.file_card_width = 0.33
        self.file_card_height = 0.35
        self.margin = 0.05

        # add btn
        self.btn_size = 0.07

        # coordinate variables
        self.file_card_x = self.margin
        self.file_card_y = self.margin + 0.1

        # adding a heading label
        heading = Label(0.4, 0.03, 0.2, 0.05, self.app.settings["MAIN_FONT"], text = "File Cards")

        # adding the button which adds a new file cards
        self.add_btn = Button(self.file_card_x + self.file_card_width / 2, self.file_card_y + self.file_card_height / 2, self.btn_size, self.btn_size,
                              self.app.settings["MAIN_FONT"], text = "Add/Load")
        
        self.add_btn.set_command(self.add_file_card)
        self.add_child(self.add_btn)
        self.add_child(heading)
        

    # adds a file card UI
    def add_file_card(self):
        frame = BorderFrame(self.file_card_x, self.file_card_y, self.file_card_width, self.file_card_height, border_width = 3, bd_radius =  0)
        label1 = Label(0.03, 0.03, 0.3, 0.15, self.app.settings["MAIN_FONT"], text = "Name")
        input1 = InputBox(0.03, 0.21, 0.8, 0.2, self.app.settings["MAIN_FONT"], placeholder = "File Name")
        label2 = Label(0.03, 0.44, 0.3, 0.15, self.app.settings["MAIN_FONT"], text = "Save Location")
        input2 = InputBox(0.03, 0.62, 0.8, 0.2, self.app.settings["MAIN_FONT"], placeholder = "File Path")

        delete_btn = Button(0.8, 0, 0.15, 0.15, self.app.settings["MAIN_FONT"])

        # frame.add_child(label1)
        # frame.add_child(input1)
        # frame.add_child(label2)
        # frame.add_child(input2)
        # frame.add_child(delete_btn)

        self.add_child(frame)
        self.change_coords()

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
        self.add_btn.change_y(self.file_card_y + self.file_card_height / 2)

    # creates a new file 
    def add_file(self, name : str):
        pass
    
    # tries to load a file from given file path
    def load_file(self, fp : str):
        pass