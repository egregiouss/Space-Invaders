from src.code.config import Config as cfg
from src.code.enemy import Enemy
import pygame as pg
from src.code.main import generate_enemies
from unittest.mock import patch
import pytest

from src.code.sprites import Sprites


@pytest.fixture()
@patch('src.code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
def enemy():
    return Enemy((10, 10))


def test_simple_movement_left(enemy):
    enemy.move()
    expected = (10 + cfg.dir * cfg.ENEMIES_SPEED, 10)
    assert expected == (enemy.rect.centerx, enemy.rect.centery)


def test_simple_movement_right(enemy):
    cfg.dir = -1
    enemy.move()
    expected = (10 + cfg.dir * cfg.ENEMIES_SPEED, 10)
    assert expected == (enemy.rect.centerx, enemy.rect.centery)


def test_multi_movement_left(enemy):
    for i in range(10):
        enemy.move()
    expected = (10 + (cfg.dir * cfg.ENEMIES_SPEED)*10, 10)
    assert expected == (enemy.rect.centerx, enemy.rect.centery)


def test_multi_movement_right(enemy):
    cfg.dir = -1
    for i in range(10):
        enemy.move()
    expected = (10 + (cfg.dir * cfg.ENEMIES_SPEED) * 10, 10)
    assert expected == (enemy.rect.centerx, enemy.rect.centery)

@patch('src.code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
def test_generating_enemies(enemy):
    shape = "xxxxxx"
    generate_enemies(shape)
    expected = len(shape)
    assert len(Sprites.aliens) == expected




