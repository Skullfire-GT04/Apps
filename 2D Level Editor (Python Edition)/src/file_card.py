from utils import BorderFrame, Label, InputBox, Button



class FileCard(BorderFrame):

    def __init__(self, x, y, width, height, font):
        super().__init__(x, y, width, height, bd_radius = 0, border_width = 2)

        label1 = Label(0.09, 0.14, 0.3, 0.1, font, text = "Name", text_size = 15)
        input1 = InputBox(0.09, 0.3, 0.7, 0.1, font, placeholder = "File Name", text_size = 15, padding = 10, border_width = 2)
        label2 = Label(0.09, 0.5, 0.3, 0.1, font, text = "Save Location", text_size = 15)
        input2 = InputBox(0.09, 0.66, 0.7, 0.1, font, placeholder = "File Path", padding = 10, border_width = 2)
        delete_btn = Button(0.8, 0.04, 0.15, 0.15, font)

        self.add_child(label1)
        self.add_child(input1)
        self.add_child(label2)
        self.add_child(input2)
        self.add_child(delete_btn)