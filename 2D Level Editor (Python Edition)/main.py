# This is the main file to run to start the app, you can check inside
# the settings folder to tinker with the settings of the app to your liking

# Contributor - V Cube (github username) (https://github.com/Skullfire-GT04)

import pygame as pg
from json import load
from utils.border_frame import BorderFrame
from utils.console import Console
from utils.button import Button
from utils.label import Label
from utils.input_box import InputBox
from utils.slider import Slider

class App:
    def __init__(self):
        # trying to load the main settings
        self.settings = dict()
        self.running = True
        self.load_main_settings()

        if not self.settings: return

        pg.init();
        self.screen = pg.display.set_mode(self.settings["SCREEN_SIZE"])
        pg.display.set_caption(self.settings["APP_NAME"])
        self.clock = pg.time.Clock()
        self.frames = []
        self.independent_widgets = []
        self.temp = BorderFrame(0.01, 0, 0.3, 1, 10)
        self.btn = Button(0.1, 0.1, 0.7, 0.14, self.settings["MAIN_FONT"], text_size = 25, padding = 10, bd_radius = 20, text = "Click me !")
        self.label = Label(0.1, 0.3, 0.7, 0.23, self.settings["MAIN_FONT"], text_size = 20)
        self.console = Console(0.4, 0.9, 0.2, 0.03, self.settings["MAIN_FONT"])
        self.btn.set_command(self.change_text)
        self.independent_widgets.append(Label(0.7, 0.5, 0.3, 0.23, self.settings["MAIN_FONT"], text = "Label2", text_size = 30))
        self.in_box = InputBox(0.1, 0.7, 0.5, 0.02, self.settings["MAIN_FONT"], text_size = 15)
        self.slider = Slider(0.5, 0.75, 0.03, 0.2)
        self.slider.set_value(50)
        self.independent_widgets.append(self.console)
        self.temp.add_child(self.btn)
        self.temp.add_child(self.label)
        self.temp.add_child(self.in_box)
        self.temp.add_child(self.slider)
        self.counter = 0

    def load_main_settings(self):
        try:
            with open("settings/main_settings.json", "r") as f:
                self.settings = load(f)
        except FileNotFoundError as e:
            print("Main settings not found exiting app....")
            self.running = False

    # updated the current frame
    def update(self):
        pass

    def change_text(self):
        self.counter += 1
        self.label.set_text(f"Counter: {self.counter}")

    # the main loop for the app
    def run(self):
        while self.running:
            for event in pg.event.get():
                # checking if the main_window was resized if so then changing the stand-alone widgets accordingly
                if event.type == pg.VIDEORESIZE:
                    for widget in self.independent_widgets:
                        widget.calc_new_rect()
                if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or event.type == pg.QUIT:
                    self.running = False                    
                if event.type == pg.KEYDOWN and event.key == pg.K_k:
                    self.label.set_text("Hello there matey! Come aboard !")
                    self.slider.set_orient("horizontal")
                self.temp.update(event)

            self.screen.fill("black")

            self.temp.draw(self.screen)
            
            # drawing the independent widgets on top of the frames
            for i in range(len(self.independent_widgets)):
                self.independent_widgets[i].draw(self.screen)

            pg.display.update()
            self.clock.tick(self.settings["FPS"])
        pg.quit()


if __name__ == "__main__":
    a = App()
    a.run()