from game.config import Config
from game.enemy import Enemy, MysteryShip
import pygame as pg
from main import generate_enemies
from main import Game
from unittest.mock import patch
from game.sprites import Sprites


@patch('game.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
def test_generating_enemies():
    for spr in Sprites.all_sprites.sprites():
        spr.kill()
    shape = ["xxxxxx"]
    generate_enemies(shape[0])
    expected = len(shape[0])
    assert len(Sprites.aliens) == expected


@patch('game.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
def test_generating_enemies_with_spaced_shape():
    for spr in Sprites.all_sprites.sprites():
        spr.kill()
    shape = ["x x x x x x"]
    generate_enemies(shape)
    expected = len([i for i in shape[0] if i == 'x'])
    assert len(Sprites.aliens) == expected


@patch('game.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
@patch('main.Game.get_hits', lambda: {'hit1': [Enemy((10, 10))],
                                               'hit2': [Enemy((5, 5))],
                                               'hit3': [MysteryShip((5, 10), 1)]})
def test_score_with_spaceship():
    Config.SCORE = 0
    Game.update_score()
    expected = 700
    assert Config.SCORE == expected


@patch('game.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
@patch('main.Game.get_hits', lambda: {'hit1': [Enemy((10, 10))],
                                               'hit2': [Enemy((5, 5))]})
def test_score_only_aliens():
    Config.SCORE = 0
    Game.update_score()
    expected = 200
    assert Config.SCORE == expected
