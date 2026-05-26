# This is the main file to run to start the app, you can check inside
# the src/settings folder to tinker with the settings of the app to your liking

# Contributor - SV Cube (github username) (https://github.com/Skullfire-GT04)

import pygame as pg


class App:
    def __init__(self):
        pg.init();
        self.screen = pg.display.set_mode()
        self.frames = []

    # updated the current frame
    def update(self):
        pass

    # the main loop for the app
    def run(self):
        pass