import pygame as pg

# This module defines which type of widgets are eligible for which type of events

EVENT_MAP = {
    pg.MOUSEMOTION : ("button", "label", "slider"),
    pg.MOUSEBUTTONDOWN : ("button", "input", "slider"),
    pg.MOUSEBUTTONUP : ("button", "input", "slider"),
    pg.KEYDOWN : ("button", "input"),
    pg.KEYUP : ("button", "input")
}