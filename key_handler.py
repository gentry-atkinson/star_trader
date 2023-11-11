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
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    pass
                if event.key == pg.K_RIGHT:
                    pass
        return (p, s)

class CockpitKeyHandler(Key_Handler):
    def __init__(self) -> None:
        super().__init__()
        pass

    def process_keys(self, p: Player, s: ScreenStatus) -> tuple:
        events = pg.event.get()
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    pass
                if event.key == pg.K_RIGHT:
                    pass
        return (p, s)