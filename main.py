import sys

import pygame.sprite

from player import Player, Ship
import pygame as pg
from config import Config as cfg
from sprites import Sprites
from enemy import Enemy, EnemyGroup
from bunker import BunkerElement


class Game:
    def __init__(self):
        self.player = pg.sprite.GroupSingle(Player())
        Sprites.all_sprites.add(self.player)
        shape = ["xxxxxxxxxxx",
                 "xxxxxxxxxxx",
                 "xxxxxxxxxxx",
                 "xxxxxxxxxxx"]
        self.generate_enemies(shape)
        self.generate_bunkers()
        self.generate_hud()
        self.alien_direction = 1
        self.move_time =0
        self.enemies = []


    def generate_enemies(self, shape):
        enemies = []
        offset = (cfg.GAME_WIDTH - len(shape[0]) * cfg.ENEMIES_SIZE - (len(shape[0]) - 1) * cfg.offset) / 2
        for line in range(0, len(shape)):
            for el in range(0, len(shape[line])):
                if shape[line][el] == "x":
                    enemie = Enemy((offset + el * (cfg.ENEMIES_SIZE + cfg.offset), (cfg.ENEMIES_SIZE + cfg.offset) * line + offset))
                    Sprites.enemies.add(enemie)
                    Sprites.all_sprites.add(enemie)
                    enemies.append(enemie)
        self.enemiesGroup = EnemyGroup(enemies)

    def generate_hud(self):
        ship = Ship((cfg.GAME_WIDTH + 50, cfg.GAME_HEIGHT))
        hp = Sprites.healths.add(ship)
        Sprites.all_sprites.add(ship)

    def generate_bunkers(self):
        shape = ["    xxxxxxxxxxxxxxxx",
                 "   xxxxxxxxxxxxxxxxxx",
                 "  xxxxxxxxxxxxxxxxxxxx",
                 " xxxxxxxxxxxxxxxxxxxxxx",
                 "xxxxxxxxxxxxxxxxxxxxxxxx",
                 "xxxxxxxxxxxxxxxxxxxxxxxx",
                 "xxxxxxxxxxxxxxxxxxxxxxxx",
                 "xxxxxxxxxxxxxxxxxxxxxxxx",
                 "xxxxxxxx        xxxxxxxx",
                 "xxxxxxx          xxxxxxx",
                 "xxxxxx            xxxxxx",
                 "xxxxx              xxxxx"]

        self.generate_bunker(shape, 50, 680)
        self.generate_bunker(shape, 250, 680)
        self.generate_bunker(shape, 450, 680)
        self.generate_bunker(shape, 650, 680)

    def generate_bunker(self, shape, offset_x, offset_y):
        for line in range(0, len(shape)):
            for el in range(0, len(shape[line])):
                if shape[line][el] == "x":
                    wall = BunkerElement(el * 5 + offset_x, line * 5 + offset_y)
                    Sprites.bunkers.add(wall)
                    Sprites.all_sprites.add(wall)

    def update(self):
        self.player.update()
        Sprites.bullets.update(cfg.BULLET_SPEED)
        self.enemiesGroup.update()
        Sprites.bunkers.update()
        Sprites.enemies_lasers.update(-cfg.BULLET_SPEED)
        pg.draw.line(screen, (255, 255, 255), (cfg.GAME_WIDTH, 0), (cfg.GAME_WIDTH, cfg.GAME_HEIGHT), 4)

        pygame.sprite.groupcollide(Sprites.bullets, Sprites.enemies, True, True)
        pg.sprite.groupcollide(Sprites.bullets, Sprites.bunkers, True, True )
        pg.sprite.groupcollide(Sprites.enemies_lasers, Sprites.bunkers, True, True)
        Sprites.all_sprites.draw(screen)


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((cfg.GAME_WIDTH + cfg.HUD_WIDTH, cfg.GAME_HEIGHT))
    clock = pg.time.Clock()
    game = Game()
    ENEMY_SHOOT = pg.USEREVENT + 1
    pg.time.set_timer(ENEMY_SHOOT, 1000)
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if e.type == ENEMY_SHOOT:
                Enemy.shoot()



        screen.fill((30, 30, 30))
        game.update()

        pg.display.flip()
        clock.tick(60)
