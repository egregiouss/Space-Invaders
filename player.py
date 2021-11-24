import pygame as pg

from bullet import Bullet
from config import Config as cfg
from sprites import Sprites
from commonFuncs import CommonFuncs


class Ship(pg.sprite.Sprite):
    def __init__(self, pos=(cfg.GAME_WIDTH / 2, cfg.GAME_HEIGHT)):
        super().__init__()
        self.image = CommonFuncs.change_size(pg.image.load('src/ship.png').convert_alpha(), 0.1)

        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = cfg.PLAYER_SPEED
        self.size_x = self.rect.size[0]
        self.size_y = self.image.get_size()[1]
        self.reload = False
        self.shot_time = 0


class Player(Ship):
    def __init__(self):
        super().__init__()

    def get_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            if self.rect.x <= (cfg.GAME_WIDTH - self.speed - self.size_x):
                self.rect.x += self.speed
        elif keys[pg.K_LEFT]:
            if self.rect.x >= 0:
                self.rect.x -= self.speed
        if keys[pg.K_SPACE]:
            self.shoot()

    def update(self) -> None:
        self.get_input()

    def shoot(self):
        if pg.time.get_ticks() - self.shot_time > cfg.RELOAD_TIME:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            Sprites.all_sprites.add(bullet)
            Sprites.bullets.add(bullet)
            self.shot_time = pg.time.get_ticks()
