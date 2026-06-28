import pygame as pg
from utils import Frame, Slider, CheckButton, Button

class Canvas:

    def __init__(self, app, docker, file_manager):
        self.app = app
        self.docker = docker
        self.file_manager = file_manager