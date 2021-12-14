
import pygame as pg
import pytest

from code.config import Config
from code.enemy import Enemy, MysteryShip

from code.main import generate_enemies
from code.main import Game
from unittest.mock import patch
from code.sprites import Sprites


@pytest.fixture()
@patch('code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
def enemy():
    return Enemy((10, 10))


def test_simple_movement_left(enemy):
    enemy.move()
    expected = (10 + Config.dir * Config.ENEMIES_SPEED, 10)
    assert expected == (enemy.rect.centerx, enemy.rect.centery)


def test_simple_movement_right(enemy):
    Config.dir = -1
    enemy.move()
    expected = (10 + Config.dir * Config.ENEMIES_SPEED, 10)
    assert expected == (enemy.rect.centerx, enemy.rect.centery)


def test_multi_movement_left(enemy):
    for i in range(10):
        enemy.move()
    expected = (10 + (Config.dir * Config.ENEMIES_SPEED)*10, 10)
    assert expected == (enemy.rect.centerx, enemy.rect.centery)


def test_multi_movement_right(enemy):
    Config.dir = -1
    for i in range(10):
        enemy.move()
    expected = (10 + (Config.dir * Config.ENEMIES_SPEED) * 10, 10)
    assert expected == (enemy.rect.centerx, enemy.rect.centery)



@patch('code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
def test_generating_enemies():
    for spr in Sprites.all_sprites.sprites():
        spr.kill()
    shape = ["xxxxxx"]
    generate_enemies(shape[0])
    expected = len(shape[0])
    assert len(Sprites.aliens) == expected


@patch('code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
def test_generating_enemies_with_spaced_shape():
    for spr in Sprites.all_sprites.sprites():
        spr.kill()
    shape = ["x x x x x x"]
    generate_enemies(shape)
    expected = len([i for i in shape[0] if i == 'x'])
    assert len(Sprites.aliens) == expected


@patch('code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
@patch('code.main.Game.get_hits', lambda: {'hit1': [Enemy((10, 10))],
                                               'hit2': [Enemy((5, 5))],
                                               'hit3': [MysteryShip((5, 10), 1)]})
def test_score_with_spaceship():
    Config.SCORE = 0
    Game.update_score()
    expected = 700
    assert Config.SCORE == expected


@patch('code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
@patch('code.main.Game.get_hits', lambda: {'hit1': [Enemy((10, 10))],
                                               'hit2': [Enemy((5, 5))]})
def test_score_only_aliens():
    Config.SCORE = 0
    Game.update_score()
    expected = 200
    assert Config.SCORE == expected





