#!usr/bin/python
#-*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_PINK, MENU_OPTION, COLOR_WHITE


class Menu:

    def __init__(self, window):
        self.window = window
        # carrega a imagem de fundo do menu
        self.surf = pygame.image.load('./asset/Menupg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        # toca a música do menu em loop
        pygame.mixer.music.load('asset/Inicial.wav')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            # titulo do jogo
            self.menu_text(90, "Lixchini", COLOR_WHITE, ((WIN_WIDTH / 2), 150))
            self.menu_text(70, "Shock", COLOR_WHITE, ((WIN_WIDTH / 2), 210))

            # controles
            self.menu_text(13, "P1: Setas - Mover | CTRL DIR - Atirar", COLOR_WHITE, ((WIN_WIDTH / 2), 260))
            self.menu_text(13, "P2: W A S D - Mover | CTRL ESQ - Atirar", COLOR_WHITE, ((WIN_WIDTH / 2), 278))

            # desenha as opções do menu, destacando a selecionada em rosa
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(19, MENU_OPTION[i], COLOR_PINK, ((WIN_WIDTH / 2), 300 + 30 * i))
                else:
                    self.menu_text(19, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 300 + 30 * i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        # vai para a proxima opção, volta ao inicio se chegar no fim
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        # vai para a opção anterior, vai para o fim se estiver no inicio
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        # confirma a opção selecionada
                        return MENU_OPTION[menu_option]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucidasanstypewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)