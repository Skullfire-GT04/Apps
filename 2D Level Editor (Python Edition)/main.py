# This is the main file to run to start the app, you can check inside
# the settings folder to tinker with the settings of the app to your liking

# Contributor - V Cube (github username) (https://github.com/Skullfire-GT04)

"""
TODO: 

(i) Implement Frame Docker Widget : Semi-Done
(ii) Make file manager frame
(iii) Make animation manager frame
(iv) Make animation customization frame
(v) Make canvas frame

"""

import pygame as pg
from typing import List
from json import load
from utils import Animation, MultiLineLabel
from src import DockerFrame, PopUpWindow, PopUpMessage, PopUpChoice


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
        self.anim_manager = Animation()

        # flags
        self.input_pop_up = False
        
        
        # adding default widgets and frames to the app
        self.docker = DockerFrame(self)
        self.pop_up_window = PopUpWindow(self.settings["INPUT_FONT"], self.anim_manager)
        self.pop_up_message = PopUpMessage(self.settings["INPUT_FONT"], self.anim_manager)
        self.pop_up_choice = PopUpChoice(self.settings["INPUT_FONT"], self.anim_manager)

        self.docker.add_frame(self.settings["FILE_MANAGER_NAME"], "file_manager", app = self, docker = self.docker)
        self.docker.add_frame(self.settings["SPRITE_MANAGER_NAME"], "sprite_manager", app = self)

        self.independent_widgets = []

    def load_main_settings(self):
        try:
            with open("settings/main_settings.json", "r") as f:
                self.settings = load(f)
        except FileNotFoundError as e:
            print("Main settings not found exiting app....")
            self.running = False

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

                self.pop_up_window.update(event)
                self.pop_up_message.update(event)
                self.pop_up_choice.update(event)

                # updating the current frame if no pop-up input field is active
                if (not self.pop_up_window.active and not self.pop_up_choice.active) or event.type == pg.VIDEORESIZE:
                    self.docker.update(event)

            # clearing the screen
            self.screen.fill("black")

            # animating widgets
            self.anim_manager.animate()

            # drawing frames
            self.docker.draw(self.screen)
            self.pop_up_window.draw(self.screen)
            self.pop_up_choice.draw(self.screen)
            self.pop_up_message.draw(self.screen)

            pg.display.update()
            self.clock.tick(self.settings["FPS"])
        pg.quit()

    def show_message(self, msg : str, time : int):
        self.pop_up_message.show_message(msg, time)

    def ask_input(self, params : List[str], callback):
        self.pop_up_window.ask_input(params, callback)

    def get_input(self):
        return self.pop_up_window.output
    
    def get_choice(self):
        return self.pop_up_choice.output

    def ask_choice(self, msg : str, choices : List[str], callback):
        self.pop_up_choice.ask_choice(msg, choices, callback = callback)


if __name__ == "__main__":
    a = App()
    a.run()