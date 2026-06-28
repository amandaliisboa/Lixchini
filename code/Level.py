#!usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font
import random
from code.Const import WIN_HEIGHT, COLOR_RED, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COLOR_BLUE, COLOR_GREEN, \
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.Enemy import Enemy


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        # cria o fundo do level
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))

        # cria o player 1 e mantém o score da fase anterior
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)

        self.timeout = TIMEOUT_LEVEL

        # cria o player 2 se for modo multiplayer
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)

        # timers para spawn de inimigos e contagem regressiva
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        # carrega a musica do level correspondente
        if self.name == 'Level1':
            pygame.mixer.music.load('./asset/level1.mp3')
        elif self.name == 'Level2':
            pygame.mixer.music.load('./asset/level2.wav')
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == EVENT_ENEMY:
                    # spawna um inimigo aleatorio
                    choice = random.choice(('enemy1', 'enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        # tempo esgotado, salva o score e passa pro proximo level
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                # verifica se ainda existe algum player vivo
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    # todos os players morreram, fim de jogo
                    return False

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                # players e inimigos podem atirar
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                # exibe o health e score de cada player na tela
                if ent.name == 'Player1':
                    self.level_text(text_size=14, text=f'Player1 - Health: {ent.health} | Score: {ent.score}',
                                    text_color=COLOR_BLUE, text_pos=(10, 25))
                elif ent.name == 'Player2':
                    self.level_text(text_size=14, text=f'Player2 - Health: {ent.health} | Score: {ent.score}',
                                    text_color=COLOR_GREEN, text_pos=(10, 45))

            # informações de debug no canto da tela
            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',
                            text_color=COLOR_RED, text_pos=(10, 5))
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=COLOR_RED,
                            text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=COLOR_RED,
                            text_pos=(10, WIN_HEIGHT - 20))

            pygame.display.flip()

            # verifica colisões e remove entidades sem vida
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            clock.tick(60)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

