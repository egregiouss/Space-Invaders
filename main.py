import sys
from player import Player
import pygame as pg
from config import Config as cfg


class Game:
    def __init__(self):
        self.player = pg.sprite.GroupSingle(Player((cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT)))

    def update(self):
        self.player.update()
        self.player.draw(screen)


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
    clock = pg.time.Clock()
    game = Game()

    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill((30, 30, 30))
        game.update()

        pg.display.flip()
        clock.tick(60)
