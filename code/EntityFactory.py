#!usr/bin/python
#-*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
import random
from code.Enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:

            case 'Level1Bg':
                list_bg = []
                # cria duas copias de cada camada do fundo para o efeito de scroll
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                # mesmo esquema do level 1, mas com 5 camadas
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                # player 1 começa no lado esquerdo, parte de cima
                return Player('Player1', (10, WIN_HEIGHT / 2 - 100))

            case 'Player2':
                # player 2 começa no lado esquerdo, um pouco abaixo do player 1
                return Player('Player2', (10, WIN_HEIGHT / 2))

            case 'enemy1':
                # inimigo aparece fora da tela pela direita em altura aleatoria
                return Enemy('enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

            case 'enemy2':
                return Enemy('enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))