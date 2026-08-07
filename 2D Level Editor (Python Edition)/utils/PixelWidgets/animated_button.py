import pygame as pg
from ..button import Button



class AnimatedButton(Button):

    def __init__(self, x : float, y : float, width : float, height : float, command = lambda : print("A pixel button was pressed"), border_radius = 10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = "button"
        self.clr_settings = None
        self.command = command
        self.bindings = {}
        self.enabled = True
        self.hovering = False        
        self.parent = None
        self.id = None
        self.bd_radius = border_radius
        self.rect = None
        self.original_images = []
        self.images = []
        self.fps = 12 # this is what I thought looked best
        self.frame_change_time = 1000 / self.fps
        self.current_frame = 0
        self.next_change_time = -1
        self.load_color_settings("button")
        self.calc_new_rect()

    def load_images(self, img_path : str, frame_width : int, frame_height : int):
        img = pg.image.load(img_path).convert_alpha()
        self.original_images.clear()
        for i in range(img.get_height() // frame_width):
            for j in  range(img.get_width() // frame_height):
                temp = pg.Surface((frame_width, frame_height)).convert_alpha()
                temp.set_colorkey((0, 0, 0))
                temp.blit(img, (0, 0), (j * frame_width, i * frame_height, frame_width, frame_height))
                self.original_images.append(temp.copy())
        self.calc_new_rect()
        self.next_change_time = -1
        self.current_frame = 0

    def set_frame_rate(self, new_rate : int):
        self.fps = new_rate if new_rate > 0 else self.fps
        self.frame_change_time = 1000 / self.fps
            
    def calc_new_rect(self):
        pos_x, pos_y = self.get_absolute_pos()
        self.rect = pg.Rect(pos_x, pos_y, self.get_absolute_width(), self.get_absolute_height())
        self.images.clear()
        for i in range(len(self.original_images)):
            self.images.append(pg.transform.scale(self.original_images[i], (self.rect.width, self.rect.height)))

    def draw(self, screen : pg.display):
        pg.draw.rect(screen, self.clr_settings["bg"] if not self.hovering else self.clr_settings["btn_hvr_clr"], self.rect, border_radius = self.bd_radius)
        if not self.images: return

        # updating the current frame
        if self.next_change_time < 0: self.next_change_time = pg.time.get_ticks() + self.frame_change_time
        if pg.time.get_ticks() >= self.next_change_time:
            self.current_frame += 1
            self.current_frame %= len(self.images)
            self.next_change_time = pg.time.get_ticks() + self.frame_change_time

        # drawing the current frame
        screen.blit(self.images[self.current_frame], self.rect)    

    def change_width(self, new_width):
        self.width = new_width
        self.calc_new_rect()

    def change_y(self, new_y):
        self.y = new_y
        self.calc_new_rect()
    
    def change_x(self, new_x):
        self.x = new_x
        self.calc_new_rect()
    
    def parent_changes(self):
        self.calc_new_rect()
