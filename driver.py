import pygame as pg
from utils.screen import Screen
from utils.player import Player
from utils.planet import Planet
from utils.globals import *

START_SCREEN = "navigation"


if __name__ == "__main__":
    pg.init()
    pg.display.set_caption("Star Trader")
    screen_display = pg.display.set_mode(SCREEN_SIZE)

    planets = {p : Planet(p) for p in ["Earth"]}
    screens = {s : Screen(s) for s in SCREEN_LIST}
    player = Player()
    player.cur_screen = screens[START_SCREEN]

    clock=pg.time.Clock()
    player.star_date = START_DATE
    while player.running:
        player.cur_screen = screens[player.cur_screen_name]
        player = player.cur_screen.update(player)
        player.cur_screen.draw(screen_display, date=player.star_date)
        pg.display.update()
            