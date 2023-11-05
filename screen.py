import json
import os
import pygame as pg
from math import sin, cos, pi
from player import Player

from event_handler import Event_Handler

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

class Screen:
    def __init__(self, name: str) -> None:
        with open(os.path.join("config", name+".ini"), 'r') as f:
            print(os.listdir())
            configs = dict(json.load(f))
            self.name = name
            self.background_file = str(configs["background_file"])
            self.background_image = pg.image.load(os.path.join("imgs", self.background_file+".png"))
            self.event_handler = Event_Handler()
            self.selector_file = str(configs["selector_file"])
            self.selector_image = pg.image.load(os.path.join("imgs", self.selector_file+".png"))

            self.planet_icons = [
                Planet_Icon("Sun", 0, 1, (600, 400)),
                Planet_Icon("Earth", 200, 1, 0)
            ]

            

    def draw(self, screen: pg.Surface, date = 0) -> None:
        screen.blit(self.background_image, (0,0))
        for icon in self.planet_icons:
            
            screen.blit(icon.image, icon.pos(date))

    def update(self, p: Player) -> Player:
        new_p = p.copy()
        new_p.star_date += 0.001
        return new_p