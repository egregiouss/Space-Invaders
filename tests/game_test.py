
import pygame as pg
import pytest


from code.enemy import Enemy, MysteryShip

from code.main import generate_enemies
from code.main import Game
from unittest.mock import patch
from code.sprites import Sprites
from code.config import Config


@pytest.fixture()
@patch('code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
def enemy():
    return Enemy((10, 10))


def test_simple_movement_left(enemy):
    enemy.move()
    expected = (10 + 10, 10)
    assert expected == (enemy.rect.centerx, enemy.rect.centery)

