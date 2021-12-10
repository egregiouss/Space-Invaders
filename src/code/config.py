import pathlib
from dataclasses import dataclass
import pygame as pg
from pathlib import Path


pg.init()
@dataclass()
class Config:
    CWD = pathlib.Path.cwd()

    GAME_WIDTH = 800
    GAME_HEIGHT = 600
    HUD_WIDTH = 300
    HUD_HEIGHT = GAME_HEIGHT

    PLAYER_SPEED = 7
    BULLET_SPEED = -8
    RELOAD_TIME = 500
    MOVE_TIME = 500
    ENEMIES_LINES = 3
    ENEMIES_SPEED = 10
    ENEMIES_SIZE = 50
    offset = 5
    DOWN_DIST = 20
    BLOCK_SIZE = 5
    isd = False
    dir = 1
    ENEMY_MOVE = 0
    SCORE = 0
    hps = 1
    LVL = 0
    FONT = pg.font.Font('../images/Pixeled.ttf', 20)
    ENEMY_SHAPES = {1: ["x"],
                    2: ["xx"],
                    3: ["xxx"]}
    ENEMY_PATH = "../images/alien.png"
    UFO_PATH = "../images/ufo.png"
    PLAYER_PATH = "../images/ship.png"

