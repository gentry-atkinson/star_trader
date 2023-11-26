import os
from math import sin, pi, cos

import pygame as pg

from utils.globals import *

class ScreenStatus:
    def __init__(self) -> None:
        self.focus = None
        self.focus_idx = -1
        self.focus_icon = None
        self.second_focus = None
        self.second_focus_idx = -1
        self.second_focus_icon = None
        self.toggle = False

class Icon:
    def __init__(self, name) -> None:
        self.name = name
        self.highlight = False
        pass

class Planet_Icon(Icon):
    def __init__(self, name, radius, orbit, starting_position) -> None:
        super().__init__(name)
        self.radius = radius
        self.orbital_period = orbit
        self.starting_position = starting_position
        self.image = pg.image.load(os.path.join(IMG_DIR, name+"_nav_icon.png"))
        self.image = pg.transform.scale(self.image, PLANET_ICON_SIZE)
    
    def pos(self, date: float) -> tuple:
        pos_x = 600 + self.radius * sin(2*pi*(date % self.orbital_period)/self.orbital_period)
        pos_y = 400 - self.radius * cos(2*pi*(date % self.orbital_period)/self.orbital_period)
        return(pos_x - self.image.get_width()//2, pos_y  - self.image.get_height()//2)

class Static_Icon(Icon):
    def __init__(self, name: str, position: tuple, size: tuple) -> None:
        super().__init__(name)
        self.position = position
        self.image = pg.image.load(os.path.join(IMG_DIR, name+"_nav_icon.png"))
        self.image = pg.transform.scale(self.image, size)
        self.highlight = True


    def pos(self, date=None) -> tuple:
        return self.position