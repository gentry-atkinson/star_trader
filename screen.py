import json
import os

import pygame as pg

from player import Player
from screen_status import ScreenStatus, Planet_Icon, Static_Icon

from key_handler import Key_Handler, NavKeyHandler, CockpitKeyHandler

key_handlers = {
    "navigation" : NavKeyHandler,
    "cockpit" : CockpitKeyHandler
}

screen_status = ScreenStatus()


class Screen:
    def __init__(self, name: str) -> None:
        with open(os.path.join("config", name+".ini"), 'r') as f:
            print(os.listdir())
            configs = dict(json.load(f))
            self.name = name
            self.background_file = str(configs["background_file"])
            self.background_image = pg.image.load(os.path.join("imgs", self.background_file+".png"))
            self.event_handler = Key_Handler()
            self.selector_file = str(configs["selector_file"])
            self.selector_image = pg.image.load(os.path.join("imgs", self.selector_file+".png"))
            self.key_handler = key_handlers[str(configs["key_handler"])]()

            
            self.planet_icons = []
            if self.name == "navigation":
                self.planet_icons.append(Planet_Icon("Sun", 0, 1, (600, 400)))
                self.planet_icons.append(Planet_Icon("Earth", 200, 1, 0))

                

            

    def draw(self, screen: pg.Surface, date = 0) -> None:
        screen.blit(self.background_image, (0,0))
        for icon in self.planet_icons:
            
            screen.blit(icon.image, icon.pos(date))

    def update(self, p: Player) -> Player:
        global screen_status

        new_p = p.copy()
        new_p.star_date += 0.001
        new_p, screen_status = self.key_handler.process_keys(new_p, screen_status)
        return new_p