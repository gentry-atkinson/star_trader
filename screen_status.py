import pygame as pg
import os
from math import sin, pi, cos

class ScreenStatus:
    def __init__(self) -> None:
        self.focus = None


class Planet_Icon:
    def __init__(self, name, radius, orbit, starting_position) -> None:
        self.name = name
        self.radius = radius
        self.orbital_period = orbit
        self.starting_position = starting_position
        self.image = pg.image.load(os.path.join("imgs", name+"_nav_icon.png"))
    
    def pos(self, date: float) -> tuple:
        pos_x = 600 + self.radius * sin(2*pi*(date % self.orbital_period)/self.orbital_period)
        pos_y = 400 - self.radius * cos(2*pi*(date % self.orbital_period)/self.orbital_period)
        return(pos_x - self.image.get_width(), pos_y  - self.image.get_height())

class Static_Icon:
    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position
        self.image = pg.image.load(os.path.join("imgs", name+"_nav_icon.png"))