import json
import os
from math import sqrt

import pygame as pg

from utils.player import Player
from utils.planet import Planet
from utils.screen_status import ScreenStatus, Planet_Icon, Static_Icon, Icon
from utils.helper_funcs import deep_compare_lists
from utils.key_handler import *
from utils.globals import *


screen_status = ScreenStatus()

class Screen:
    _planet_list = None
    def __init__(self, name: str) -> None:
        with open(os.path.join("config", name+".ini"), 'r') as f:
            #print(os.listdir())
            configs = dict(json.load(f))
            self.name = name
            self.background_file = str(configs["background_file"])
            self.background_image = pg.image.load(os.path.join(IMG_DIR, self.background_file+".png"))
            self.selector_file = str(configs["selector_file"])
            self.selector_image = pg.image.load(os.path.join(IMG_DIR, self.selector_file+".png"))
            self.key_handler = None

            self.icons = {}
            screen_status.focus = "Earth"

                
    def _draw_on_center(a: Icon, b: pg.Surface, screen: pg.Surface, date):
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
        for _, icon in self.icons.items():
            screen.blit(icon.image, icon.pos())
        if screen_status.focus:
            Screen._draw_on_center(screen_status.focus_icon, self.selector_image, screen, date)

    def update(self, p: Player) -> Player:
        # new_p.star_date += 0.001
        global screen_status
        p, screen_status = self.key_handler.process_keys(p, screen_status)
        return p
    
    def set_planet_dict(p: list[Planet]) -> None:
        Screen._planet_list = p
    
class NavScreen(Screen):
    def __init__(self) -> None:
        super().__init__("navigation")
        self.planet_icons = {}
        self.planet_icons["Sun"] = Planet_Icon("Sun", 0, 1, (600, 400))
        self.planet_icons["Earth"] = Planet_Icon("Earth", 200, 1, 0)
        self.planet_icons["Venus"] = Planet_Icon("Venus", 100, 0.615, 0.5)
        self.planet_icons["Mars"] = Planet_Icon("Mars", 400, 1.88, 0.75)
        self.key_handler = NavKeyHandler()
        assert deep_compare_lists(PLANET_LIST, self.planet_icons.keys()), "Incomplete planet list on Nav Screen"

    def get_travel_time(a: Planet_Icon, b: Planet_Icon):
        a_x, a_y = a.pos()
        b_x, b_y = b.pos()
        d_x = abs(a_x - b_x)
        d_y = abs(a_y - a_y)
        return TRAVEL_TIME_PER_PIXEL * sqrt(d_x**2 + d_y**2)
    
    def draw(self, screen: pg.Surface, date = 0) -> None:
        super().draw(screen, date)
        for _, icon in self.planet_icons.items():
            screen.blit(icon.image, icon.pos(date))

    def update(self, p: Player) -> Player:
        global screen_status
        p = super().update(p)
        if screen_status.focus:
            screen_status.focus_icon = self.planet_icons[screen_status.focus]
        else:
            screen_status.focus_icon = None
        return p


class CockpitScreen(Screen):
    def __init__(self) -> None:
        super().__init__("cockpit")
        self.key_handler = CockpitKeyHandler()

class LocalScreen(Screen):
    def __init__(self) -> None:
        super().__init__("local")
        self.key_handler = LocalKeyHandler()

class EconomyScreen(Screen):
    def __init__(self) -> None:
        super().__init__("economy")
        self.key_handler = EconomyKeyHandler()
        self.planet_icons = {
            "Venus" : Static_Icon("Venus", (200, 100), ECON_ICON_SIZE),
            "Mars" : Static_Icon("Mars", (400, 100), ECON_ICON_SIZE),
            "Earth" : Static_Icon("Earth", (600, 100), ECON_ICON_SIZE)
        }
        assert deep_compare_lists(PLANET_LIST, self.planet_icons.keys()), "Incomplete planet list on Econ Screen"
        
        self.product_icons = {
            "Iron" : Static_Icon("Iron", (100, 200), ECON_PRODUCT_SIZE),
            "Methane" : Static_Icon("Methane", (100, 300), ECON_PRODUCT_SIZE),
            "Clothing" : Static_Icon("Clothing", (100, 400), ECON_PRODUCT_SIZE),
            "Medicine" : Static_Icon("Medicine", (100, 500), ECON_PRODUCT_SIZE),
        }

    def draw(self, screen: pg.Surface, date = 0) -> None:
        super().draw(screen, date)
        for _, icon in self.planet_icons.items():
            screen.blit(icon.image, icon.pos(date))
        for _, icon in self.product_icons.items():
            screen.blit(icon.image, icon.pos(date))

    def update(self, p: Player) -> Player:
        global screen_status
        p = super().update(p)
        if screen_status.focus:
            screen_status.focus_icon = self.planet_icons[screen_status.focus]
        else:
            screen_status.focus_icon = None
        return p

def ScreenFactory(name: str) -> Screen:
    if name == "navigation":
        s = NavScreen()
        return s
    elif name == "cockpit":
        s = CockpitScreen()
        return s
    elif name == "local":
        s = LocalScreen()
        return s
    elif name == "economy":
        s = EconomyScreen()
        return s
    else:
        s = Screen(name)
        return s