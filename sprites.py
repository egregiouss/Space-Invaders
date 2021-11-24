from dataclasses import dataclass
import pygame as pg
import commonFuncs


@dataclass
class Sprites:
    all_sprites = pg.sprite.Group()
    enemies = pg.sprite.Group()
    aliens = pg.sprite.Group()
    bullets = pg.sprite.Group()
    bunkers = pg.sprite.Group()
    healths = pg.sprite.Group()
    player = pg.sprite.Group()
    enemies_lasers = pg.sprite.Group()
    mystery = pg.sprite.Group()