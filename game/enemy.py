from enum import Enum

import pygame as pg
from game.commonFuncs import CommonFuncs
from game.config import Config as cfg
from game.sprites import Sprites
from random import choice
from game.bullet import Bullet
class Enemy(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.cur_state = AlienState.Up
        self.image_down = self.setup_image()
        self.cur_state = AlienState.Down
        self.image_up = self.setup_image()
        self.speed = cfg.ENEMIES_SPEED
        self.points = 100
        self.image = self.image_down
        self.rect = self.image.get_rect(center=pos)


    def setup_image(self):
        if self.cur_state == AlienState.Down:
            return CommonFuncs.set_size(pg.image.load("game/images/alien.png").convert_alpha(), 50, 50)
        elif self.cur_state == AlienState.Mystery:
            return CommonFuncs.set_size(pg.image.load("game/images/ufo.png").convert_alpha(), 100, 50)
        return CommonFuncs.set_size(pg.image.load("game/images/alien3.png").convert_alpha(), 50, 50)

    def move(self) -> None:
        pg.rect.Rect.move_ip(self.rect, cfg.dir * cfg.ENEMIES_SPEED, 0)
        if self.cur_state == AlienState.Down:
            self.image = self.image_down
            self.cur_state = AlienState.Up
        else:
            self.image = self.image_up
            self.cur_state = AlienState.Down
        if cfg.isd:
            self.rect.y += cfg.DOWN_DIST



    @staticmethod
    def shoot():
        if Sprites.aliens.sprites():
            alien = choice(Sprites.aliens.sprites())
            bullet = Bullet(alien.rect.center[0], alien.rect.center[1])
            Sprites.all_sprites.add(bullet)
            Sprites.enemies_lasers.add(bullet)

    @staticmethod
    def check_dir():
        enemies = Sprites.aliens.sprites()
        for alien in enemies:
            if alien.rect.right >= cfg.GAME_WIDTH or alien.rect.left <= 0:
                cfg.dir *= -1
                cfg.isd = True
                cfg.MOVE_TIME -= 30
                pg.time.set_timer(cfg.ENEMY_MOVE, cfg.MOVE_TIME)
                cfg.ENEMY_SHOOT_TIME-=50
                pg.time.set_timer(cfg.ENEMY_SHOOT_TIME,cfg.ENEMY_SHOOT_TIME)
                break
            else:
                cfg.isd = False


class MysteryShip(Enemy):
    def __init__(self, pos, dir):
        super().__init__(pos)
        self.cur_state = AlienState.Mystery
        self.image = self.setup_image()
        self.rect = self.image.get_rect(center=pos)
        self.speed = cfg.ENEMIES_SPEED
        self.points = 500
        self.dir = dir


    def update(self) :
        pg.rect.Rect.move_ip(self.rect, self.dir * 7, 0)
        if self.rect.x >= cfg.GAME_WIDTH or self.rect.right <= 0:
            self.kill()

class AlienState(Enum):
    Up = 1,
    Down = 2,
    Mystery = 3










