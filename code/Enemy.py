#!usr/bin/python
#-*- coding: utf-8 -*-

from code.Entity import Entity
from code.EnemyShot import EnemyShot
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # define o delay inicial antes do inimigo poder atirar
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        # inimigo se move da direita para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        # quando o delay chega a zero, atira e reinicia o contador
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))