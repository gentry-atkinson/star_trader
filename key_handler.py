import pygame as pg
from player import Player

class Key_Handler:
    def __init__(self) -> None:
        pass

    def process_keys(p: Player):
        pass

class Nav_Key_Handler(Key_Handler):
    def __init__(self) -> None:
        super().__init__()
        pass

    def process_keys(p: Player):
        events = pg.event.get()
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    pass
                if event.key == pg.K_RIGHT:
                    pass