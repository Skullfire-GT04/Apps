# This is the main file to run to start the app, you can check inside
# the settings folder to tinker with the settings of the app to your liking

# Contributor - V Cube (github username) (https://github.com/Skullfire-GT04)

import pygame as pg
from json import load

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
                # checking if the main_window was resized if so then changing the stand-alone widgets accordingly
                if event.type == pg.VIDEORESIZE:
                    for widget in self.independent_widgets:
                        widget.calc_new_rect()
                if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or event.type == pg.QUIT:
                    self.running = False                    
                

            self.screen.fill("black")

            pg.display.update()
            self.clock.tick(self.settings["FPS"])
        pg.quit()


if __name__ == "__main__":
    a = App()
    a.run()