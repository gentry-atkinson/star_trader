import pygame as pg
from player import Player
from screen_status import ScreenStatus

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
        planet_list = ["Venus", "Earth", "Mars"]
        cur_idx = -1
        if s.focus in planet_list:
            cur_idx = planet_list.index(s.focus)
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    p.cur_screen_name = "cockpit"
                    s.focus = ""
                    s.focus_icon = None
                if event.key == pg.K_j:
                    s.focus = p.cur_planet
                if event.key == pg.K_UP and cur_idx > -1:
                    cur_idx = (cur_idx + 1) % len(planet_list)
                    s.focus = planet_list[cur_idx]
                if event.key == pg.K_DOWN and cur_idx > -1:
                    cur_idx = (cur_idx - 1) % len(planet_list)
                    s.focus = planet_list[cur_idx]

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