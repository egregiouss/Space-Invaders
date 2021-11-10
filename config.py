from dataclasses import dataclass


@dataclass()
class Config:
    GAME_WIDTH = 800
    GAME_HEIGHT = 800
    HUD_WIDTH = 300
    HUD_HEIGHT = GAME_HEIGHT

    PLAYER_SPEED = 3
    BULLET_SPEED = -8
    RELOAD_TIME = 500
    MOVE_TIME = 200
    ENEMIES_LINES = 3
    ENEMIES_SPEED = 10
    ENEMIES_SIZE = 50
    offset = 5
    DOWN_DIST = 10
    BLOCK_SIZE = 5


