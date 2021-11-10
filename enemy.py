import pygame as pg
from commonFuncs import CommonFuncs
from config import Config as cfg
from sprites import Sprites
from random import choice
from bullet import Bullet
class Enemy(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = CommonFuncs.set_size(pg.image.load("src/alien.png").convert_alpha(), 50, 50)
        self.rect = self.image.get_rect(center=pos)
        self.speed = cfg.ENEMIES_SPEED
        self.move_time = 0
    alien_direction = 1


    def update(self, dir, isd) -> None:
        if pg.time.get_ticks() - self.move_time > cfg.MOVE_TIME:
            self.rect.x += dir * cfg.ENEMIES_SPEED
            if isd:
                self.rect.y += cfg.DOWN_DIST



            self.move_time = pg.time.get_ticks()

    @staticmethod
    def shoot():
        if Sprites.enemies.sprites():
            alien = choice(Sprites.enemies.sprites())
            bullet = Bullet(alien.rect.center[0], alien.rect.center[1])
            Sprites.all_sprites.add(bullet)
            Sprites.enemies_lasers.add(bullet)


class EnemyGroup:
    def __init__(self, enemies):
        self.enemies = enemies
        self.dir = 1
        self.isDown = False
    def check_dir(self):
        enemies = Sprites.enemies.sprites()
        for alien in enemies:
            if alien.rect.right >= cfg.GAME_WIDTH or alien.rect.left <= 0:
                self.dir *= -1
                self.isDown = True
                break
            else:
                self.isDown = False

    def update(self):
        self.check_dir()
        for en in self.enemies:
            en.update(self.dir, self.isDown)










