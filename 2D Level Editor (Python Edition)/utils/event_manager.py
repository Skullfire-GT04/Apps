import pygame as pg

# This module defines which type of widgets are eligible for which type of events

WIDGET_TYPES_ALL = ("frame", "button", "label", "slider", "console", "input", "check_button", "scrollable_frame")


# event mapping for widget types
EVENT_MAP = {
    pg.MOUSEMOTION : ("button", "label", "slider", "input"),
    pg.MOUSEBUTTONDOWN : ("button", "input", "slider", "check_button"),
    pg.MOUSEBUTTONUP : ("button", "input", "slider"),
    pg.KEYDOWN : ("button", "input"),
    pg.KEYUP : ("button", "input"),
    pg.MOUSEWHEEL : ("scrollable_frame", "slider")
}

# timed events
INPUT_BOX_TICK_SPEED = 2 # per second