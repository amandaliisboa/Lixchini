#!usr/bin/python
#-*- coding: utf-8 -*-

import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        # cria a janela do jogo
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        score = Score(self.window)
        while True:
            # mostra o menu e espera o jogador escolher uma opcao
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # Player1, Player2
                # roda o level 1
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    # se passou do level 1, roda o level 2
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        # se passou dos dois levels, salva e mostra o score
                        score.save_score(menu_return, player_score)
                        score.show_score()

            elif menu_return == MENU_OPTION[3]:
                # jogador escolheu ver o ranking
                score.show_score()

            elif menu_return == MENU_OPTION[4]:
                # jogador escolheu sair
                pygame.quit()
                raise SystemExit