import pygame as pg
from screen import Screen
from player import Player

screen_list = ["navigation"]
START_SCREEN = "navigation"
START_DATE = 2276.0

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption("Star Trader")
    screen_display = pg.display.set_mode((1200, 800))

    running = True

    screens = {s : Screen(s) for s in screen_list}
    player = Player()
    player.cur_screen = screens[START_SCREEN]

    clock=pg.time.Clock()
    player.star_date = START_DATE
    while running:
        player = player.cur_screen.update(player)
        player.cur_screen.draw(screen_display, date=player.star_date)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False