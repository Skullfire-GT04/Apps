# This is the main file to run to start the app, you can check inside
# the src/settings folder to tinker with the settings of the app to your liking

# Contributor - V Cube (github username) (https://github.com/Skullfire-GT04)

import pygame as pg
from json import load
from utils.widget import *
from utils.frame import *
from utils.border_frame import BorderFrame
from utils.button import Button
from utils.label import Label

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
        self.temp = Frame(0.1, 0.1, 0.5, 0.8, 10)
        self.btn = Button(0.1, 0.1, self.settings["MAIN_FONT"], size = 25, padding = 14, bd_radius = 20)
        self.btn.toggle_key_binding(pg.K_a)
        self.label = Label(0.1, 0.3, self.settings["MAIN_FONT"], text_size = 25)
        self.temp.add_child(self.btn)
        self.temp.add_child(self.label)
        self.temp.set_bg("#01100a")

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

    # the main loop for the app
    def run(self):
        while self.running:
            for event in pg.event.get():
                # checking if the main_window was resized
                if event.type == pg.VIDEORESIZE:
                    pass
                if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or event.type == pg.QUIT:
                    self.running = False                    
                if event.type == pg.KEYDOWN and event.key == pg.K_k:
                    self.label.set_text("Hello there matey!")
                self.temp.update(event)

            self.screen.fill("black")

            self.temp.draw(self.screen)

            pg.display.update()
            self.clock.tick(self.settings["FPS"])
        pg.quit()


if __name__ == "__main__":
    a = App()
    a.run()