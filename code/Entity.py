#-*- coding: utf-8 -*-

from abc import ABC
import pygame.image
from code.Const import ENTITY_SCALE, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        # carrega a imagem da entidade
        self.surf = pygame.image.load("./asset/" + name + ".png").convert_alpha()
        # aplica o fator de escala definido no Const (padrao 1 se nao tiver)
        scale = ENTITY_SCALE.get(self.name, 1)
        self.surf = pygame.transform.scale(self.surf, (self.surf.get_width() * scale, self.surf.get_height() * scale))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_dmg = 'None'  # guarda o nome de quem causou o ultimo dano
        self.score = ENTITY_SCORE[self.name]

    def move(self):
        pass