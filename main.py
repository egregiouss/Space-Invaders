import random
import pathlib
import sys
import pygame as pg
import pygame.sprite
from game.player import Player, Ship

from game.config import Config as cfg
from game.sprites import Sprites
from game.enemy import Enemy, MysteryShip
from game.bunker import BunkerElement
from game.states import States
from game.highscore import Highscore


CWD = pathlib.Path.cwd()
scenes = {
    'menu':[States.PLAY, States.HIGHSCORE],
    'high':[States.MENU],
    'typing':[States.MENU, States.PLAY],
    'play':[States.LOSE]
}
def generate_hud():
    for i in range(50, 50*(cfg.hps+1), 50):
        ship = Ship((cfg.GAME_WIDTH + i, cfg.GAME_HEIGHT))
        Sprites.healths.add(ship)


def generate_bunker(shape, offset_x, offset_y):
    for line in range(0, len(shape)):
        for el in range(0, len(shape[line])):
            if shape[line][el] == "x":
                wall = BunkerElement(el * 5 + offset_x, line * 5 + offset_y)
                Sprites.bunkers.add(wall)
                Sprites.all_sprites.add(wall)


def generate_bunkers(lvl):
    generate_bunker(cfg.BUNKERS_SHAPES[lvl][0], 50, cfg.GAME_HEIGHT - 120)
    generate_bunker(cfg.BUNKERS_SHAPES[lvl][1], 250, cfg.GAME_HEIGHT - 120)
    generate_bunker(cfg.BUNKERS_SHAPES[lvl][2], 450, cfg.GAME_HEIGHT - 120)
    generate_bunker(cfg.BUNKERS_SHAPES[lvl][3], 650, cfg.GAME_HEIGHT - 120)


def generate_enemies(shape):
    enemies = []
    offset = (cfg.GAME_WIDTH - len(shape[0]) * cfg.ENEMIES_SIZE - (len(shape[0]) - 1) * cfg.offset) / 2
    for line in range(0, len(shape)):
        for el in range(0, len(shape[line])):
            if shape[line][el] == "x":
                enemie = Enemy((offset + el * (cfg.ENEMIES_SIZE + cfg.offset),
                                (cfg.ENEMIES_SIZE + cfg.offset) * line + offset))
                Sprites.aliens.add(enemie)
                Sprites.enemies.add(enemie)
                Sprites.all_sprites.add(enemie)
                enemies.append(enemie)

class Game:
    def __init__(self, lvl=0):
        self.font = pg.font.Font('game/images/Pixeled.ttf', 20)
        self.setup_game()
        if lvl != 0:
            shape = cfg.ENEMY_SHAPES[lvl]
            generate_enemies(shape)
            generate_bunkers(lvl)
        self.alien_direction = 1
        self.move_time = 0
        self.enemies = []
        self.state = States.MENU
        self.menu_btns = {}
        self.need_input = True
        self.input_text = ""



    def setup_game(self):
        player = Player()
        Sprites.player.add(player)
        Sprites.all_sprites.add(player)
    def update(self, events):
        if self.state == States.LOSE:
            self.game_over()
        elif self.state == States.PLAY and len(Sprites.aliens.sprites()) == 0:
            if cfg.LVL < len(cfg.ENEMY_SHAPES.keys()):
                cfg.LVL += 1
                load_lvl(cfg.LVL)
            else:
                self.game_win()
        elif self.state == States.HIGHSCORE:
            self.draw_highscores()
        else:
            if self.state == States.MENU:
                self.show_menu()
                self.update_menu()
            elif self.state == States.TYPING:
                if self.need_input:
                    self.draw_input(events)

            elif self.state == States.PLAY:
                for e in events:
                    if e.type == cfg.ENEMY_SHOOT:
                        Enemy.shoot()
                    if e.type == cfg.ENEMY_MOVE:
                        Enemy.check_dir()
                        for i in Sprites.aliens.sprites():
                            i.move()


                    if e.type == mystery:
                        dir = random.choice(("left", "right"))
                        if dir == "left":
                            myst = MysteryShip((100, 100), 1)
                        else:
                            myst = MysteryShip((cfg.GAME_WIDTH - 100, 100), -1)
                        pg.time.set_timer(mystery, random.randint(7000, 10000))
                        Sprites.mystery.add(myst)
                        Sprites.enemies.add(myst)
                        Sprites.all_sprites.add(myst)

                Sprites.enemies.update()
                Sprites.player.update()
                Sprites.bullets.update(cfg.BULLET_SPEED)
                Sprites.bunkers.update()
                Sprites.enemies_lasers.update(-cfg.BULLET_SPEED)
                pg.draw.line(screen, (255, 255, 255), (cfg.GAME_WIDTH, 0), (cfg.GAME_WIDTH, cfg.GAME_HEIGHT), 4)
                self.update_score()
                self.draw_score()
                self.check_collisions()
                Sprites.all_sprites.draw(screen)
                Sprites.healths.draw(screen)

    def draw_input(self, events):
        screen.fill((30, 30, 30))
        self.draw_text(self.font, "Enter your name", "white",
                       ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 2, cfg.GAME_HEIGHT / 8))
        self.draw_text(self.font, self.input_text, "white",
                       ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 2, cfg.GAME_HEIGHT / 2))
        self.draw_btn("back", ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 6, cfg.GAME_HEIGHT-100))
        for e in events:
            self.get_input(e)
            if e.type == pg.MOUSEBUTTONDOWN and self.menu_btns["back"].collidepoint(pg.mouse.get_pos()):
                self.state = States.MENU

    def draw_text(self,font, text, color, pos):
        surf = font.render(text, False, color)
        rect = surf.get_rect(center = pos)
        screen.blit(surf, rect)

    def check_collisions(self):
        pg.sprite.groupcollide(Sprites.bullets, Sprites.bunkers, True, True)
        pg.sprite.groupcollide(Sprites.enemies_lasers, Sprites.bunkers, True, True)
        hits_in_player = pg.sprite.groupcollide(Sprites.enemies_lasers, Sprites.player, True, False)
        crash_in_player = pg.sprite.groupcollide(Sprites.aliens, Sprites.player, False, False)
        if hits_in_player:
            if cfg.hps > 0:
                cfg.hps -= 1
                Sprites.healths.sprites()[-1].kill()
                print(cfg.hps)
            else:
                Sprites.player.sprites()[0].kill()
                self.state = States.LOSE
        if crash_in_player:
            cfg.hps = -1
            Sprites.player.sprites()[0].kill()
            self.state = States.LOSE

    @staticmethod
    def update_score():
        hits = Game.get_hits()
        if hits:
            for hit in hits.values():
                for enemy in hit:
                    cfg.SCORE += enemy.points

    @staticmethod
    def get_hits():
        return pygame.sprite.groupcollide(Sprites.bullets, Sprites.enemies, True, True)

    def draw_score(self):
        score_surf = self.font.render(f'score: {cfg.SCORE}', False, 'white')
        score_rect = score_surf.get_rect(topright=(cfg.GAME_WIDTH + cfg.HUD_WIDTH - 10, -10))
        screen.blit(score_surf, score_rect)

    def show_menu(self):
        screen.fill((30, 30, 30))
        self.draw_btn("Play", ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 2, cfg.GAME_HEIGHT / 2))
        self.draw_btn("Highscore", ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 2, cfg.GAME_HEIGHT / 2 + 100))



    def draw_btn(self, text, pos):
        btn_text = self.font.render(text, False, 'white')
        btn = btn_text.get_rect(center=pos)
        self.menu_btns[text] = btn
        screen.blit(btn_text, btn)

    def update_menu(self):
        for e in events:
            if e.type == pg.MOUSEBUTTONDOWN and self.menu_btns["Play"].collidepoint(pg.mouse.get_pos()):
                self.state = States.TYPING
                print(len(Sprites.aliens.sprites()))
            if e.type == pg.MOUSEBUTTONDOWN and self.menu_btns["Highscore"].collidepoint(pg.mouse.get_pos()):
                self.state = States.HIGHSCORE

    def get_input(self, e):
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_RETURN:
                self.need_input = False
                self.state = States.PLAY
                print(self.input_text)
            elif e.key == pg.K_BACKSPACE:
                pass
            else:
                self.input_text += e.unicode

    def game_over(self):
        self.draw_text(self.font, "GAME OVER", "red", ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 2, cfg.GAME_HEIGHT / 10))
        if not save.isSave:
            save.add(self.input_text, cfg.SCORE)
            save.isSave = True
        self.draw_table()

        self.restart()

    def restart(self):
        self.draw_btn("try again", ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 6, cfg.GAME_HEIGHT - 100))
        self.draw_btn("menu", ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) - 100, cfg.GAME_HEIGHT - 100))
        for spr in Sprites.all_sprites.sprites():
            spr.kill()
        self.input_text =''
        for e in events:
            if e.type == pg.MOUSEBUTTONDOWN and self.menu_btns["try again"].collidepoint(pg.mouse.get_pos()):
                self.state = States.PLAY
                cfg.hps = 3
                cfg.LVL = 1
                cfg.SCORE = 0
                load_lvl(1)
            elif e.type == pg.MOUSEBUTTONDOWN and self.menu_btns["menu"].collidepoint(pg.mouse.get_pos()):
                self.state = States.MENU
                cfg.hps = 3
                cfg.LVL = 0
                cfg.SCORE = 0
                self.need_input = True


    def draw_highscores(self):
        screen.fill((30, 30, 30))
        self.draw_text(self.font, "HIGHSCORES", "white", ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 2, cfg.GAME_HEIGHT / 8))
        self.draw_table()
        self.draw_btn("back", ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 6, cfg.GAME_HEIGHT - 100))
        for e in events:
            if e.type == pg.MOUSEBUTTONDOWN and self.menu_btns["back"].collidepoint(pg.mouse.get_pos()):
                self.state = States.MENU

    def draw_table(self):
        offset = 50
        for player in save.get_all().keys():
            self.draw_text(self.font, str(player), "white",
                           ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 2 - 100, cfg.GAME_HEIGHT / 8 + offset))
            self.draw_text(self.font, str(save.get(player)), "white",
                           ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 2 + 50, cfg.GAME_HEIGHT / 8 + offset))
            offset += 50

    def game_win(self):
        self.draw_text(self.font, f"{self.input_text}, YOU WON!", "green", ((cfg.GAME_WIDTH + cfg.HUD_WIDTH) / 2, cfg.GAME_HEIGHT / 10))
        if not save.isSave:
            save.add(self.input_text, cfg.SCORE)
            save.isSave = True
        self.draw_table()
        self.restart()


def load_lvl(lvl):
    generate_hud()
    for spr in Sprites.all_sprites.sprites():
        spr.kill()
    font = pg.font.Font('game/images/Pixeled.ttf', 20)
    screen.fill((30, 30, 30))
    score_surf = font.render(f"LEVEL {lvl}:", False, 'white')
    score_rect = score_surf.get_rect(center=((cfg.GAME_WIDTH + cfg.HUD_WIDTH)/2, cfg.GAME_HEIGHT/2))
    screen.blit(score_surf, score_rect)
    pg.display.flip()
    pg.time.delay(1000)
    return Game(lvl)


def main():
    global ENEMY_SHOOT, mystery, screen, save, events
    cfg.ENEMY_SHOOT = pg.USEREVENT + 1
    cfg.ENEMY_MOVE = pg.USEREVENT + 2
    mystery = pg.USEREVENT + 3
    pg.init()
    game_is_started = False
    screen = pg.display.set_mode((cfg.GAME_WIDTH + cfg.HUD_WIDTH, cfg.GAME_HEIGHT))
    clock = pg.time.Clock()
    game = Game()
    pg.time.set_timer(cfg.ENEMY_SHOOT, cfg.ENEMY_SHOOT_TIME)
    pg.time.set_timer(cfg.ENEMY_MOVE, cfg.MOVE_TIME)
    pg.time.set_timer(mystery, random.randint(7000, 10000))
    generate_hud()
    save = Highscore()
    while True:
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()
        screen.fill((30, 30, 30))
        game.update(events)
        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()


