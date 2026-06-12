import pygame as pg
from utils.button import Button
from .file_manager import FileManager
from .sprite_manager import SpriteManager


class DockerFrame:

    def __init__(self, app):
        self.frames = []
        self.labels = []
        self.names = []
        self.curr_frame = -1
        self.max_label_width = 0.1
        self.label_height = 0.04
        self.curr_x = 0
        self.app = app
        self.frame_type_map = {
            "file_manager" : FileManager,
            "sprite_manager" : SpriteManager
        }

    def add_frame(self, name : str, type : str, *args, **kwargs):
        if name in self.names: return
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
        
        self.frames.append(temp)
        self.names.append(name)
        index = len(self.frames) - 1
        temp = Button(self.curr_x, 1 - self.label_height, self.max_label_width, self.label_height, self.app.settings["MAIN_FONT"], text = name)
        temp.set_command(lambda: self.change_frame(index))
        self.labels.append(temp)
        self.curr_x += self.max_label_width
        self.curr_frame = index

    # changes the current selected frame to the given index
    def change_frame(self, index : int):
        if index < 0 or index >= len(self.frames): return
        self.curr_frame = index
        self.frames[self.curr_frame].update(pg.event.Event(pg.VIDEORESIZE))

    def delete_frame(self, name : str):
        if name not in self.names: return
        index = self.names.index(name)

        for i in range(index + 1, len(self.names)):
            self.labels[i].change_x(self.labels[i].x - self.max_label_width)

        self.names.pop(index)
        self.labels.pop(index)
        self.frames.pop(index)
        self.curr_frame += 1
        if self.curr_frame > len(self.frames): self.curr_frame = 0 if len(self.frames) else -1

    # updates the current selected frame and all the labels
    def update(self, event : pg.event):
        if self.curr_frame < 0: return

        self.frames[self.curr_frame].update(event)
        for label in self.labels:
            label.update(event)
    
    def draw(self, display : pg.Surface):
        if self.curr_frame < 0: return

        self.frames[self.curr_frame].draw(display)

        for i in range(len(self.frames)):
            self.labels[i].draw(display)
    