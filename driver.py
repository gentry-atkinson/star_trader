import pygame as pg

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Star Trader")

    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False