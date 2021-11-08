from dataclasses import dataclass


@dataclass()
class Config:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    PLAYER_SPEED = 3
    BULLET_SPEED = -8
    RELOAD_TIME = 500
