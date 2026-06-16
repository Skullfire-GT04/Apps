import pygame as pg
from ..button import Button


class PixelButton(Button):

    def __init__(self, x : float, y : float, width : float, height : float, image_path : str, hover_img_path = None, command = lambda : print("A pixel button was pressed")):
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
        self.images = []
        self.images.append(pg.image.load(image_path).convert_alpha())
        if hover_img_path: self.images.append(pg.image.load(hover_img_path))
        else: self.images.append(None)            
        self.calc_new_rect()

    def draw(self, display : pg.display):
        pg.draw.rect(display, self.clr_settings["bg" if not self.hovering else "btn_hvr_clr"], self.rect)

        img = self.images[0] if not self.hovering else self.images[1]
        if not img: img = self.images[0]

        img_rect = img.get_rect(topleft = (self.rect.x, self.rect.y))
        display.blit(img, img_rect)

    def calc_new_rect(self):
        super().calc_new_rect()

        for i in range(len(self.images)):
            if not self.images[i]: continue
            self.images[i] = pg.transform.scale(self.images[i], (self.rect.width, self.rect.height))
            
        