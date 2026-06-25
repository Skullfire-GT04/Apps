from utils import BorderFrame, Label, InputBox, Button, PixelButton

"""
This module represents a singular file that the app is working on,
it stores the data the file has generated and the save location
"""

class FileCard(BorderFrame):

    def __init__(self, x : float, y : float, width : float, height : float, font : str, name  : str, save_location : str, app, file_manager):
        super().__init__(x, y, width, height, bd_radius = 0, border_width = 2)
        self.app = app
        self.manager = file_manager
        self.name = name
        self.save_location = save_location

        label1 = Label(0.09, 0.14, 0.3, 0.1, font, text = "Name", text_size = 15)
        label2 = Label(0.09, 0.5, 0.3, 0.1, font, text = "Save Location", text_size = 15)

        # inputs
        self.name_input = InputBox(0.09, 0.3, 0.7, 0.1, font, placeholder = "File Name", text_size = 15, padding = 10, border_width = 2)
        self.name_input.disable()
        self.name_input.set_text(name)
        self.path_input = InputBox(0.09, 0.66, 0.7, 0.1, font, placeholder = "File Path", padding = 10, border_width = 2)
        self.path_input.disable()
        self.path_input.set_text(save_location)
        
        # buttons
        self.delete_btn = PixelButton(0.93, 0, 0.07, 0.07, "res/CloseButton1/non_hovering.png", border_radius = 5)
        self.edit_btn = PixelButton(0.1, 0.82, 0.15, 0.15, "res/EditButton1/non_hovering.png")
        self.save_btn = Button(0.3, 0.83, 0.3, 0.14, font, text_size = 15, text = "Save Changes", padding = 5)
        self.save_file = Button(0.66, 0.83, 0.3, 0.14, font, text = "Save File", text_size = 15, padding = 5)
        

        # custom coloring
        self.delete_btn.clr_settings["bg"] = "#b01925"
        self.delete_btn.clr_settings["btn_hvr_clr"] = "#660f16"


        self.name = self.name_input.text
        # self.save_locations = save_location

        self.add_child(label1)
        self.add_child(label2)
        self.add_child(self.name_input)
        self.add_child(self.path_input)
        self.add_child(self.delete_btn)
        self.add_child(self.edit_btn)
        self.add_child(self.save_btn)
        self.add_child(self.save_file)

        # flags 
        self.editing = False

        self.edit_btn.set_command(self.toggle_edit_mode)
        self.save_btn.set_command(self.save_changes)
        self.delete_btn.set_command(self.manager.remove_file_card(self.name))

    def toggle_edit_mode(self):
        self.editing = not self.editing

        if self.editing:
            self.name_input.enable()
            self.path_input.enable()
        else:
            self.name_input.disable()
            self.path_input.disable()
            self.save_changes()

    def save_changes(self):
        pass

    
    