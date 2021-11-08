from dataclasses import dataclass
import pygame as pg


@dataclass
class Sprites:
    all_sprites = pg.sprite.Group()
    mobs = pg.sprite.Group()
    bullets = pg.sprite.Group()