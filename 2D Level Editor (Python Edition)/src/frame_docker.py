import pygame as pg
from utils.button import Button
from .file_manager import FileManager
from .sprite_manager import SpriteManager


class DockerFrame:

    def __init__(self, app):
        self.frames = {}
        self.curr_frame = None
        self.max_label_width = 0.1
        self.label_height = 0.04
        self.curr_x = 0
        self.app = app
        self.frame_type_map = {
            "file_manager" : FileManager,
            "sprite_manager" : SpriteManager
        }

    def add_frame(self, name : str, type : str, *args, **kwargs):
        if self.frames.get(name, None): return
        if not self.frame_type_map.get(type, None): return
        
        temp = None
        if not args and not kwargs:
            temp = self.frame_type_map[type]()
        elif args and not kwargs:
            temp = self.frame_type_map[type](args)
        elif kwargs and not args:
            temp = self.frame_type_map[type](kwargs)
        else:
            temp = self.frame_type_map[type](args, kwargs)
        
        index = len(self.frames)
        btn = Button(self.curr_x, 1 - self.label_height, self.max_label_width, self.label_height, self.app.settings["MAIN_FONT"], text = name)
        btn.set_command(lambda: self.change_frame(name))

        self.frames[name] = {
            "frame" : temp,
            "btn" : btn,
            "index" : index
        }

        self.curr_x += self.max_label_width
        self.curr_frame = name

    # changes the current selected frame to the given index
    def change_frame(self, name : str):
        self.curr_frame = name
        self.frames[self.curr_frame]["frame"].update(pg.event.Event(pg.VIDEORESIZE))

    def delete_frame(self, name : str):
        if not self.frames.get(name, None): return
        
        index = self.frames[name]["index"]
        names = list(self.frames.keys())

        for i in range(index + 1, len(self.frames)):
            self.frames[names[i]]["btn"].change_x(self.frames[names[i]]["btn"].x - self.max_label_width)
            self.frames[names[i]]["index"] -= 1

        del self.frames[name]

    # updates the current selected frame and all the labels
    def update(self, event : pg.event):
        if not self.curr_frame: return

        self.frames[self.curr_frame]["frame"].update(event)

        for name in self.frames.keys():
            self.frames[name]["btn"].update(event)
    
    def draw(self, display : pg.Surface):
        if not self.curr_frame: return

        self.frames[self.curr_frame]["frame"].draw(display)

        for name in self.frames.keys():
            self.frames[name]["btn"].draw(display)
    