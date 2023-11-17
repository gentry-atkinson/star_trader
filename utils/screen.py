import json
import os

import pygame as pg

from utils.player import Player
from utils.screen_status import ScreenStatus, Planet_Icon, Static_Icon, Icon

from utils.key_handler import *
from utils.globals import *

key_handlers = {
    "navigation" : NavKeyHandler,
    "cockpit" : CockpitKeyHandler,
    "local" : LocalKeyHandler
}

screen_status = ScreenStatus()


class Screen:
    def __init__(self, name: str) -> None:
        with open(os.path.join("config", name+".ini"), 'r') as f:
            print(os.listdir())
            configs = dict(json.load(f))
            self.name = name
            self.background_file = str(configs["background_file"])
            self.background_image = pg.image.load(os.path.join(IMG_DIR, self.background_file+".png"))
            self.event_handler = Key_Handler()
            self.selector_file = str(configs["selector_file"])
            self.selector_image = pg.image.load(os.path.join(IMG_DIR, self.selector_file+".png"))
            self.key_handler = key_handlers[str(configs["key_handler"])]()

            
            self.icons = {}
            if self.name == "navigation":
                self.icons["Sun"] = Planet_Icon("Sun", 0, 1, (600, 400))
                self.icons["Earth"] = Planet_Icon("Earth", 200, 1, 0)
                self.icons["Venus"] = Planet_Icon("Venus", 100, 0.615, 0.5)
                self.icons["Mars"] = Planet_Icon("Mars", 400, 1.88, 0.75)

            screen_status.focus = "Earth"

                
    def draw_on_center(a: Icon, b: pg.Surface, screen: pg.Surface, date):
        """
        Draw image b centered on image a on screen
        """
        a_x, a_y = a.pos(date)
        x_dif = b.get_width() - a.image.get_width()
        y_dif = b.get_height() - a.image.get_height()
        screen.blit(
            b,
            (a_x - (x_dif//2), a_y - (y_dif//2))
        )
            

    def draw(self, screen: pg.Surface, date = 0) -> None:
        screen.blit(self.background_image, (0,0))
        for name, icon in self.icons.items():
            screen.blit(icon.image, icon.pos(date))
        if screen_status.focus:
            Screen.draw_on_center(screen_status.focus_icon, self.selector_image, screen, date)

    def update(self, p: Player) -> Player:
        global screen_status
        new_p = p.copy()
        # new_p.star_date += 0.001
        new_p, screen_status = self.key_handler.process_keys(new_p, screen_status)
        if screen_status.focus:
            screen_status.focus_icon = self.icons[screen_status.focus]
        return new_p