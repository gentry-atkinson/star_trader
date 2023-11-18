import pygame as pg

from utils.player import Player
from utils.screen_status import ScreenStatus
from utils.globals import *

class Key_Handler:
    def __init__(self) -> None:
        pass

    def process_keys(p: Player, s: ScreenStatus) -> tuple:
        return (p, s)

class NavKeyHandler(Key_Handler):
    def __init__(self) -> None:
        super().__init__()
        pass

    def process_keys(self, p: Player, s: ScreenStatus) -> tuple:
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

            if event.type == pg.QUIT:
                p.running = False
        return (p, s)

class CockpitKeyHandler(Key_Handler):
    def __init__(self) -> None:
        super().__init__()
        pass

    def process_keys(self, p: Player, s: ScreenStatus) -> tuple:
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
            if event.type == pg.QUIT:
                p.running = False
        return (p, s)
    
class LocalKeyHandler(Key_Handler):
    def __init__(self) -> None:
        super().__init__()
        pass

    def process_keys(self, p: Player, s: ScreenStatus) -> tuple:
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