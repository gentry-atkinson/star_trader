import pygame as pg

from utils.player import Player
from utils.screen_status import ScreenStatus
from utils.globals import *

class Key_Handler:
    def __init__(self) -> None:
        pass

    def process_keys(self, p: Player, s: ScreenStatus) -> tuple:
        return (p, s)

class NavKeyHandler(Key_Handler):
    def __init__(self) -> None:
        super().__init__()
        pass

    def process_keys(self, p: Player, s: ScreenStatus) -> tuple:
        """
        tab: move to cockpit screen
        j: select a planet for a jump. Focus on current planet first
        up/down arrow: when in jump mode, change focus planet for a jump
        return: jump to a selected planet
        """
        events = pg.event.get()
        cur_idx = -1
        if s.focus in PLANET_LIST:
            cur_idx = PLANET_LIST.index(s.focus)
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    p.cur_screen_name = "cockpit"
                    s.focus = ""
                    s.focus_icon = None
                if event.key == pg.K_j:
                    s.focus = p.cur_planet
                if event.key == pg.K_UP and cur_idx > -1:
                    cur_idx = (cur_idx + 1) % len(PLANET_LIST)
                    s.focus = PLANET_LIST[cur_idx]
                if event.key == pg.K_DOWN and cur_idx > -1:
                    cur_idx = (cur_idx - 1) % len(PLANET_LIST)
                    s.focus = PLANET_LIST[cur_idx]
                if event.key == pg.K_RETURN and cur_idx > -1:
                    p.cur_planet = PLANET_LIST[cur_idx]
                    p.cur_screen_name = "jump"

            if event.type == pg.QUIT:
                p.running = False
        return (p, s)

class CockpitKeyHandler(Key_Handler):
    def __init__(self) -> None:
        super().__init__()
        pass

    def process_keys(self, p: Player, s: ScreenStatus) -> tuple:
        """
        n: move to navigation screen
        l: move to local screen
        e: move to economy screen
        """
        events = pg.event.get()
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_n:
                    p.cur_screen_name = "navigation"
                    s.focus = ""
                    s.focus_icon = None
                elif event.key == pg.K_l:
                    p.cur_screen_name = "local"
                    s.focus = ""
                    s.focus_icon = None
                elif event.key == pg.K_e:
                    p.cur_screen_name = "economy"
                    s.focus = ""
                    s.focus_icon = None
            if event.type == pg.QUIT:
                p.running = False
        return (p, s)
    
class LocalKeyHandler(Key_Handler):
    def __init__(self) -> None:
        super().__init__()
        pass

    def process_keys(self, p: Player, s: ScreenStatus) -> tuple:
        """
        tab: move to cockpit screen
        """
        events = pg.event.get()
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    p.cur_screen_name = "cockpit"
                    s.focus = ""
                    s.focus_icon = None
            if event.type == pg.QUIT:
                p.running = False
        return (p, s)
    
class EconomyKeyHandler(Key_Handler):
    def __init__(self) -> None:
        super().__init__()
        pass

    def process_keys(self, p: Player, s: ScreenStatus) -> tuple:
        """
        tab: move to cockpit sreen
        left/right arrow: scroll through planet selections
        up/down arrows: scroll through product selections
        """
        if s.focus_idx == -1:
            s.focus_idx = 0
            s.focus = PLANET_LIST[0]
        if s.second_focus_idx == -1:
            s.second_focus_idx = 0
            s.second_focus = PRODUCT_LIST[0]
        events = pg.event.get()
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    p.cur_screen_name = "cockpit"
                    s.focus = ""
                    s.focus_icon = None
                    s.second_focus = ""
                    s.second_focus_icon = None
                if event.key == pg.K_LEFT:
                    s.focus_idx = (s.focus_idx+1) % len(PLANET_LIST)
                    s.focus = PLANET_LIST[s.focus_idx]
                if event.key == pg.K_RIGHT:
                    s.focus_idx = (s.focus_idx-1) % len(PLANET_LIST)
                    s.focus = PLANET_LIST[s.focus_idx]
                if event.key == pg.K_UP:
                    s.second_focus_idx = (s.second_focus_idx-1) % len(PRODUCT_LIST)
                    s.second_focus = PRODUCT_LIST[s.second_focus_idx]
                if event.key == pg.K_DOWN:
                    s.second_focus_idx = (s.second_focus_idx+1) % len(PRODUCT_LIST)
                    s.second_focus = PRODUCT_LIST[s.second_focus_idx]
                if event.key == pg.K_RETURN:
                    s.toggle = True
            if event.type == pg.QUIT:
                p.running = False
        return (p, s)
    
class EmptyKeyHandler(Key_Handler):
    def __init__(self) -> None:
        super().__init__()
        pass

    def process_keys(self, p: Player, s: ScreenStatus) -> tuple:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                p.running = False
        return (p, s)