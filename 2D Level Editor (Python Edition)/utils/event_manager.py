import pygame as pg

# This module defines which type of widgets are eligible for which type of events

WIDGET_TYPES_ALL = ("frame", "button", "label", "slider", "console", "input", "check_button")


EVENT_MAP = {
    pg.MOUSEMOTION : ("button", "label", "slider", "check_button"),
    pg.MOUSEBUTTONDOWN : ("button", "input", "slider", "check_button"),
    pg.MOUSEBUTTONUP : ("button", "input", "slider"),
    pg.KEYDOWN : ("button", "input"),
    pg.KEYUP : ("button", "input")
}