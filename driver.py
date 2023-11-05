import pygame as pg
from screen import Screen

screen_list = ["navigation"]
START_SCREEN = "navigation"

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption("Star Trader")
    screen_display = pg.display.set_mode((1200, 800))

    running = True

    screens = {s : Screen(s) for s in screen_list}
    cur_screen = screens[START_SCREEN]

    clock=pg.time.Clock()
    
    while running:
        cur_screen.draw(screen_display, date=0.66)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False