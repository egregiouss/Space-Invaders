from src.code.config import Config as cfg
from src.code.enemy import Enemy, MysteryShip
import pygame as pg
from src.code.main import generate_enemies
from src.code.main import Game
from unittest.mock import patch
import pytest
from src.code.sprites import Sprites


@patch('src.code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
def test_generating_enemies():
    shape = ["xxxxxx"]
    generate_enemies(shape[0])
    expected = len(shape[0])
    assert len(Sprites.aliens) == expected


@patch('src.code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
def test_generating_enemies_with_spaced_shape():
    shape = ["x x x x x x"]
    generate_enemies(shape)
    expected = len([i for i in shape[0] if i == 'x'])
    assert len(Sprites.aliens) == expected


@patch('src.code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
@patch('src.code.main.Game.get_hits', lambda: {'hit1': [Enemy((10, 10))],
                                               'hit2': [Enemy((5, 5))],
                                               'hit3': [MysteryShip((5, 10), 1)]})
def test_score_with_spaceship():
    Game.update_score()
    expected = 700
    assert cfg.SCORE == expected


@patch('src.code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
@patch('src.code.main.Game.get_hits', lambda: {'hit1': [Enemy((10, 10))],
                                               'hit2': [Enemy((5, 5))]})
def test_score_only_aliens():
    Game.update_score()
    expected = 200
    assert cfg.SCORE == expected
