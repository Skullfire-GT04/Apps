from utils import BorderFrame, Label, InputBox, Button, PixelButton



class FileCard(BorderFrame):

    def __init__(self, x : float, y : float, width : float, height : float, font : str):
        super().__init__(x, y, width, height, bd_radius = 0, border_width = 2)

        label1 = Label(0.09, 0.14, 0.3, 0.1, font, text = "Name", text_size = 15)
        label2 = Label(0.09, 0.5, 0.3, 0.1, font, text = "Save Location", text_size = 15)

        # inputs
        self.name_input = InputBox(0.09, 0.3, 0.7, 0.1, font, placeholder = "File Name", text_size = 15, padding = 10, border_width = 2)
        self.path_input = InputBox(0.09, 0.66, 0.7, 0.1, font, placeholder = "File Path", padding = 10, border_width = 2)

        # buttons
        self.delete_btn = Button(0.93, 0.03, 0.05, 0.05, font)
        self.edit_btn = Button(0.1, 0.85, 0.15, 0.1, font, text = "Edit", text_size = 15)

        self.name = self.name_input.text
        # self.save_locations = save_location

        self.add_child(label1)
        self.add_child(label2)
        self.add_child(self.name_input)
        self.add_child(self.path_input)
        self.add_child(self.delete_btn)
        self.add_child(self.edit_btn)
