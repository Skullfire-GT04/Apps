import pygame as pg

# This module defines which type of widgets are eligible for which type of events

WIDGET_TYPES_ALL = ("frame", "button", "label", "slider", "console", "input", "check_button")

# custom events
INPUT_BOX_TICK_EVENT = pg.USEREVENT + 1

# special events widgets customizations
TICK_EVENT_WIDGETS = tuple(["input"])

# event mapping for widget types
EVENT_MAP = {
    pg.MOUSEMOTION : ("button", "label", "slider", "check_button"),
    pg.MOUSEBUTTONDOWN : ("button", "input", "slider", "check_button"),
    pg.MOUSEBUTTONUP : ("button", "input", "slider"),
    pg.KEYDOWN : ("button", "input"),
    pg.KEYUP : ("button", "input"),
    INPUT_BOX_TICK_EVENT : TICK_EVENT_WIDGETS
}


# should only be called after pg.init() has been called
def init_tick_event():
    pg.time.set_timer(INPUT_BOX_TICK_EVENT, 250)