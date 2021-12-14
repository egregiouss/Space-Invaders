import pygame as pg
from code.config import Config as cfg
class BunkerElement(pg.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.image = pg.Surface((cfg.BLOCK_SIZE, cfg.BLOCK_SIZE))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.bottom = y
        self.rect.centerx = x
