import pygame as pg
from utils import BorderFrame, Button, InputBox, Label


class FileManager(BorderFrame):

    def __init__(self, kwargs):
        super().__init__(0, 0, 1, 1, border_width = 3, bd_radius = 15)
        self.widgets = []
        self.app = kwargs["app"]

        # constants

        # file cards
        self.file_card_width = 0.33
        self.file_card_height = 0.35
        self.margin = 0.05

        # add btn
        self.btn_size = 0.07

        # coordinate variables
        self.x = self.margin
        self.y = self.margin

        # adding the button which adds a new file cards
        self.add_btn = Button(self.x + self.file_card_width / 2, self.y + self.file_card_height / 2, self.btn_size, self.btn_size,
                              self.app.settings["MAIN_FONT"], text = "Add/Load")
        
        self.widgets.append(self.add_btn)
        self.add_btn.set_command(self.add_file_card)
        

    # adds a file card UI
    def add_file_card(self):
        frame = BorderFrame(self.x, self.y, self.file_card_width, self.file_card_height)
        label1 = Label(0.03, 0.03, 0.3, 0.15, self.app.settings["MAIN_FONT"], text = "Name")
        input1 = InputBox(0.03, 0.21, 0.8, 0.2, self.app.settings["MAIN_FONT"], placeholder = "File Name")
        label2 = Label(0.03, 0.44, 0.3, 0.15, self.app.settings["MAIN_FONT"], text = "Save Location")
        input2 = InputBox(0.03, 0.62, 0.8, 0.2, self.app.settings["MAIN_FONT"], placeholder = "File Path")

        delete_btn = Button(0.8, 0, 0.15, 0.15, self.app.settings["MAIN_FONT"])

        frame.add_child(label1)
        frame.add_child(input1)
        frame.add_child(label2)
        frame.add_child(input2)
        frame.add_child(delete_btn)

        self.widgets.append(frame)
        self.change_coords()

    # repositions the add_btn and changed the coordinate for the next
    # file card
    def change_coords(self):
        self.x += self.file_card_width + self.margin

        if(self.x > 1 - (self.file_card_width + self.margin)):
            self.x = self.margin
            self.y += self.file_card_height + self.margin

        self.add_btn.change_x(self.x + self.file_card_width / 2)
        self.add_btn.change_y(self.y + self.file_card_height / 2)

    # creates a new file 
    def add_file(self, name : str):
        pass
    
    # tries to load a file from given file path
    def load_file(self, fp : str):
        pass

    def draw(self, display : pg.display):
        for widget in self.widgets: widget.draw(display)
    
    def update(self, event : pg.event):
        for widget in self.widgets: widget.update(event)