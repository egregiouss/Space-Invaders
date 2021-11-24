import pygame as pg
from config import Config as cfg

class Button():
    def __init__(self, text, on_click=lambda x: None):

        font = pg.font.Font('src/Pixeled.ttf', 20)
        self.on_click = on_click
        self.score_surf = font.render(text, False, 'white')
        self.b_rect = self.score_surf.get_rect(center=((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 2, cfg.GAME_HEIGHT / 2))

    def draw(self, screen):
        screen.blit(self.score_surf, self.b_rect)





