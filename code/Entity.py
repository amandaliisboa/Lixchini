#-*- coding: utf-8 -*-

from abc import ABC
import pygame.image
from code.Const import ENTITY_SCALE

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load("./asset/" + name + ".png").convert_alpha()
        scale = ENTITY_SCALE.get(self.name, 1)
        self.surf = pygame.transform.scale(self.surf, (self.surf.get_width() * scale, self.surf.get_height() * scale))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    def move(self, ):
        pass
