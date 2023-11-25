# TODO: plot market values on econ screen

import json
import os
from math import sqrt

import pygame as pg

from utils.player import Player
from utils.planet import Planet
from utils.screen_status import ScreenStatus, Planet_Icon, Static_Icon, Icon
from utils.helper_funcs import deep_compare_lists, euc_dis
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
            self.second_selector_file = str(configs["second_selector_file"])
            self.dot_file = str(configs["dot_file"])
            self.key_handler = None

            self.icons = {}
            screen_status.focus = ""

                
    def _draw_on_center(a: Icon, b: pg.Surface, screen: pg.Surface, date):
        """
        Draw image b centered on image a on screen
        """
        a_x, a_y = a.pos(date)
        x_dif = b.get_width() - a.image.get_width()
        y_dif = b.get_height() - a.image.get_height()
        screen.blit(
            b, (a_x - (x_dif//2), a_y - (y_dif//2))
        )

    def _draw_dotted_line(a: tuple, b: tuple, screen: pg.surface, dot: pg.surface):
        num_dots = euc_dis(a, b) // DIS_BETWEEN_LINE_DOTS
        a = a = (a[0] + PLANET_ICON_SIZE[0]//2 - DOT_SIZE//2, a[1] + PLANET_ICON_SIZE[1]//2 - DOT_SIZE//2)
        d_x = (a[0] - b[0]) // num_dots
        d_y = (a[1] - b[1]) // num_dots
        for _ in range(int(num_dots)):
            screen.blit(dot, a)
            a = (a[0] - d_x, a[1] - d_y)

            

    def draw(self, screen: pg.Surface, p: Player) -> None:
        screen.blit(self.background_image, (0,0))
        for _, icon in self.icons.items():
            screen.blit(icon.image, icon.pos())
        if screen_status.focus:
            Screen._draw_on_center(screen_status.focus_icon, self.selector_image, screen, p.star_date)

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
        self.dot_image = pg.image.load(os.path.join(IMG_DIR, self.dot_file+".png"))
        self.dot_image = pg.transform.scale(self.dot_image, (DOT_SIZE, DOT_SIZE))
        self.dot_image.fill(color=(0, 255, 0))
        self.key_handler = NavKeyHandler()
        assert deep_compare_lists(PLANET_LIST, self.planet_icons.keys()), "Incomplete planet list on Nav Screen"

    def get_travel_time(a: Planet_Icon, b: Planet_Icon):
        a_x, a_y = a.pos()
        b_x, b_y = b.pos()
        d_x = abs(a_x - b_x)
        d_y = abs(a_y - a_y)
        return TRAVEL_TIME_PER_PIXEL * sqrt(d_x**2 + d_y**2)
    
    def draw(self, screen: pg.Surface, p: Player) -> None:
        super().draw(screen, p)
        for _, icon in self.planet_icons.items():
            screen.blit(icon.image, icon.pos(p.star_date))
        if screen_status.focus and screen_status.focus != p.cur_planet:
            Screen._draw_dotted_line(
                self.planet_icons[p.cur_planet].pos(p.star_date), 
                screen_status.focus_icon.pos(p.star_date), 
                screen, self.dot_image
            )

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
        self.second_selector_image = pg.image.load(os.path.join(IMG_DIR, self.second_selector_file+".png"))
        self.dot_image = pg.image.load(os.path.join(IMG_DIR, self.dot_file+".png"))
        self.planet_icons = {
            "Venus" : Static_Icon("Venus", (200, 100), ECON_ICON_SIZE),
            "Mars" : Static_Icon("Mars", (400, 100), ECON_ICON_SIZE),
            "Earth" : Static_Icon("Earth", (600, 100), ECON_ICON_SIZE)
        }
        assert deep_compare_lists(PLANET_LIST, self.planet_icons.keys()), "Incomplete planet list on Econ Screen"
        self.product_icons = {
            "iron" : Static_Icon("Iron", (100, 200), ECON_PRODUCT_SIZE),
            "methane" : Static_Icon("Methane", (100, 300), ECON_PRODUCT_SIZE),
            "clothing" : Static_Icon("Clothing", (100, 400), ECON_PRODUCT_SIZE),
            "medicine" : Static_Icon("Medicine", (100, 500), ECON_PRODUCT_SIZE),
        }
        assert deep_compare_lists(PRODUCT_LIST, self.product_icons.keys()), "Incomplete planet list on Econ Screen"

    def draw(self, screen: pg.Surface, p: Player) -> None:
        super().draw(screen, p)
        for _, icon in self.planet_icons.items():
            screen.blit(icon.image, icon.pos(p.star_date))
        for _, icon in self.product_icons.items():
            screen.blit(icon.image, icon.pos(p.star_date))
        if screen_status.second_focus:
            Screen._draw_on_center(screen_status.second_focus_icon, self.second_selector_image, screen, p.star_date)
        for product in Screen._planet_list[screen_status.focus].products:
            pass

    def update(self, p: Player) -> Player:
        global screen_status
        p = super().update(p)
        if screen_status.focus:
            screen_status.focus_icon = self.planet_icons[screen_status.focus]
        else:
            screen_status.focus_icon = None

        if screen_status.second_focus:
            screen_status.second_focus_icon = self.product_icons[screen_status.second_focus]
        else:
            screen_status.second_focus_icon = None
        
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