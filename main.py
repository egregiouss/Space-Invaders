import sys
from player import Player
import pygame as pg



class Game:
    def __init__(self):
        self.player = pg.sprite.GroupSingle(Player((SCREEN_WIDTH /2, SCREEN_HEIGHT)))

    def update(self):
        self.player.update()
        self.player.draw(screen)







if __name__ == "__main__":
    pg.init()
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
