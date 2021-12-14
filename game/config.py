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
    ENEMY_SHOOT_TIME = 800
    offset = 5
    DOWN_DIST = 20
    BLOCK_SIZE = 5
    isd = False
    dir = 1
    ENEMY_MOVE = 0
    ENEMY_SHOOT = 0
    SCORE = 0
    hps = 3
    LVL = 0
    ENEMY_SHAPES = {2: ["xxxxxxxxx",
                        "xxxxxxxxx"],
                    3: ["xxxxxxxxx",
                        "xxxxxxxxx",
                        "xxxxxxxxx"],
                    1: ["xxxxxxxx",
                        "xx    xx",
                        "xx    xx",
                        "xx    xx",
                        "xxxxxxxx"],

                    }
    BUNKERS_SHAPES = {2: [["    xxxxxxxxxxxxxxx",
                           "   xxxxxxxxxxxxxxxxxx",
                           "  xxxxxxxxxxxxxxxxxxxx",
                           " xxxxxxxxxxxxxxxxxxxxxx",
                           "xxxxxxxxxxxxxxxxxxxxxxxx",
                           "xxxxxxxxxxxxxxxxxxxxxxxx",
                           "xxxxxxxxxxxxxxxxxxxxxxxx",
                           "xxxxxxxxxxxxxxxxxxxxxxxx",
                           "xxxxxxxx        xxxxxxxx",
                           "xxxxxxx          xxxxxxx",
                           "xxxxxx            xxxxxx",
                           "xxxxx              xxxxx"]]*4,
                      1: [["    xxxxxxxxxxxxxxx     ",
                           "   xxxxxxxxxxxxxxxxxx   ",
                           " xxxx    xxxxxx    xxxx ",
                           "xxxxx    xxxxxx    xxxx",
                           " xxxx    xxxxxx    xxxx ",
                           "  xxx    xxxxxx    xxx  ",
                           "   xxxxxxxxxxxxxxxxxx   ",
                           "         xxxxxx         ",
                           "         xxxxxx         ",
                           "         xxxxxx         ",
                           "         xxxxxx         "],
                          ["xxxxxx            xxxxxx",
                           "xxxxxx            xxxxxx",
                           "xxxxxx           xxxxxxx",
                           "xxxxxx        xxxxxxxxxx",
                           "xxxxxx     xxxxxxxxxxxxx",
                           "xxxxxx   xxxxxx   xxxxxx",
                           "xxxxxx  xxxxxx    xxxxxx",
                           "xxxxxxxxxxxxx     xxxxxx",
                           "xxxxxxxxxx        xxxxxx",
                           "xxxxxxx           xxxxxx",
                           "xxxxxx            xxxxxx",
                           "xxxxxx            xxxxxx"],
                          ["xxxxxx            xxxxxx",
                           "xxxxxx            xxxxxx",
                           "xxxxxx           xxxxxxx",
                           "xxxxxx        xxxxxxxxxx",
                           "xxxxxx     xxxxxxxxxxxxx",
                           "xxxxxx   xxxxxx   xxxxxx",
                           "xxxxxx  xxxxxx    xxxxxx",
                           "xxxxxxxxxxxxx     xxxxxx",
                           "xxxxxxxxxx        xxxxxx",
                           "xxxxxxx           xxxxxx",
                           "xxxxxx            xxxxxx",
                           "xxxxxx            xxxxxx"],

                          ["xxxxxxxxxxxxxxxxxxxxxxxx",
                           "xxxxxxxxxxxxxxxxxxxxxxxx",
                           "xxxxxxxxxxxxxxxxxxxxxxxx",
                           "xxxxxxxxxxxxxxxxxxxxxxxx",
                           "         xxxxxx         ",
                           "         xxxxxx         ",
                           "         xxxxxx         ",
                           "         xxxxxx         ",
                           "         xxxxxx         ",
                           "         xxxxxx         ",
                           "         xxxxxx         "]
                          ],
                      3:[["xxxxxxxxxxxxxxxxxxxxxxxx",
                          "xxxxxxxxxxxxxxxxxxxxxxxx"],
                         ["xxxxxxxxxxxxxxxxxxxxxxxx",
                          "xxxxxxxxxxxxxxxxxxxxxxxx"],
                         ["xxxxxxxxxxxxxxxxxxxxxxxx",
                          "xxxxxxxxxxxxxxxxxxxxxxxx"],
                         ["xxxxxxxxxxxxxxxxxxxxxxxx",
                          "xxxxxxxxxxxxxxxxxxxxxxxx"]
                         ]}
