import pygame as pg
from config import Config as cfg


def change_size(image, multiplier):
    img_size = image.get_size()
    return pg.transform.scale(image, (img_size[0] * multiplier, img_size[1] * multiplier))


class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = change_size(pg.image.load('src/ship.png').convert_alpha(), 0.1)

        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 3

    def get_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            if self.rect.x <= (cfg.SCREEN_WIDTH - self.speed - self.image.get_size()[0]):
                self.rect.x += self.speed
        elif keys[pg.K_LEFT]:
            if self.rect.x >= 0:
                self.rect.x -= self.speed

    def update(self) -> None:
        self.get_input()
