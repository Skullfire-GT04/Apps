import pygame as pg
from ..button import Button


class PixelButton(Button):

    def __init__(self, x : float, y : float, width : float, height : float, image_path : str, hover_img_path = None, command = lambda : print("A pixel button was pressed"), border_radius = 10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = "button"
        self.clr_settings = None
        self.load_color_settings("button")
        self.command = command
        self.bindings = {}
        self.hovering = False        
        self.parent = None
        self.id = None
        self.rect = None
        self.original_images = []
        self.images = []
        self.images.append(pg.image.load(image_path).convert_alpha())
        if hover_img_path: self.images.append(pg.image.load(hover_img_path))
        else: self.images.append(None)            
        self.original_images = self.images.copy()
        self.bd_radius = border_radius
        self.calc_new_rect()

    def draw(self, display : pg.display):
        pg.draw.rect(display, self.clr_settings["bg" if not self.hovering else "btn_hvr_clr"], self.rect, border_radius = self.bd_radius)

        img = self.images[0] if not self.hovering else self.images[1]
        if not img: img = self.images[0]

        img_rect = img.get_rect(topleft = (self.rect.x, self.rect.y))
        display.blit(img, img_rect)

    def calc_new_rect(self):
        pos_x, pos_y = self.get_absolute_pos()
        self.rect = pg.Rect(pos_x, pos_y, self.get_absolute_width(), self.get_absolute_height())

        for i in range(len(self.original_images)):
            if not self.original_images[i]: continue
            self.images[i] = pg.transform.scale(self.original_images[i], (self.rect.width, self.rect.height))

    def change_width(self, new_width):
        self.width = new_width
        self.calc_new_rect()

    def change_y(self, new_y):
        self.y = new_y
        self.calc_new_rect()
    
    def change_x(self, new_x):
        self.x = new_x
        self.calc_new_rect()
            
        