import pygame as pg
from config import Config as cfg
from bullet import Bullet
from sprites import Sprites


def change_size(image, multiplier):
    img_size = image.get_size()
    return pg.transform.scale(image, (img_size[0] * multiplier, img_size[1] * multiplier))


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = change_size(pg.image.load('src/ship.png').convert_alpha(), 0.1)

        self.rect = self.image.get_rect(midbottom=(cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT))
        self.speed = 3
        self.size_x = self.rect.size[0]
        self.size_y = self.image.get_size()[1]
        self.reload = False
        self.shot_time = 0

    def get_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            if self.rect.x <= (cfg.SCREEN_WIDTH - self.speed - self.size_x):
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
