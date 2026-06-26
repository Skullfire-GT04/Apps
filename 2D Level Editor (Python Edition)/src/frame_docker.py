import pygame as pg
from utils.button import Button
from .file_manager import FileManager
from .sprite_manager import SpriteManager
from .canavs import Canvas


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
            "sprite_manager" : SpriteManager,
            "canvas" : Canvas
        }

    def add_frame(self, name : str, type_ : str, *args, **kwargs):
        if self.frames.get(name, None): return
        if not self.frame_type_map.get(type_, None): return
        
        temp = None
        if not args and not kwargs:
            temp = self.frame_type_map[type_]()
        elif args and not kwargs:
            temp = self.frame_type_map[type_](*args)
        elif kwargs and not args:
            temp = self.frame_type_map[type_](**kwargs)
        else:
            temp = self.frame_type_map[type_](*args, **kwargs)
        
        index = len(self.frames)
        btn = Button(self.curr_x, 1 - self.label_height, self.max_label_width, self.label_height, self.app.settings["MAIN_FONT"], text = name)
        btn.set_command(lambda: self.change_frame(name))

        self.frames[name] = {
            "frame" : temp,
            "btn" : btn,
            "index" : index
        }

        self.curr_x += self.max_label_width
        if not self.curr_frame: self.curr_frame = name

    # changes the current selected frame to the given index
    def change_frame(self, name : str):
        self.curr_frame = name
        self.frames[self.curr_frame]["frame"].update(pg.event.Event(pg.VIDEORESIZE))

    def change_frame_name(self, name : str, new_name : str):
        if not self.frames.get(name, None): return
        if self.frames.get(new_name, None): return

        data = self.frames[name]
        del self.frames[name]
        self.frames[new_name] = data
        data["btn"].set_text(new_name)
        data["btn"].set_command(lambda: self.change_frame(new_name))

        if self.curr_frame == name: self.curr_frame = new_name

    def delete_frame(self, name : str):
        if not self.frames.get(name, None): return
        
        index = self.frames[name]["index"]
        names = list(self.frames.keys())

        for i in range(index + 1, len(self.frames)):
            self.frames[names[i]]["btn"].change_x(self.frames[names[i]]["btn"].x - self.max_label_width)
            self.frames[names[i]]["index"] -= 1
        self.curr_x -= self.max_label_width
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
    