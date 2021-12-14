
import pygame as pg
import pytest
import unittest


from src.code.enemy import Enemy

from unittest.mock import patch


@pytest.fixture()
@patch('code.enemy.Enemy.setup_image', lambda x: pg.Surface((50, 50)))
def enemy():
    return Enemy((10, 10))

class TestOne(unittest.TestCase):
    def test_simple_movement_left(enemy):
        enemy.move()
        expected = (10 + 10, 10)
        assert expected == (enemy.rect.centerx, enemy.rect.centery)

