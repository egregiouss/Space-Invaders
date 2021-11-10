from config import Config as cfg
import pygame as pg


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((4, 10))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x


    def update(self, speed):
        self.rect.y += speed
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()
