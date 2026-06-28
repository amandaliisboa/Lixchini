#!usr/bin/python
#-*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # move o fundo para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]
        # quando sair da tela, volta para a direita para criar o efeito de scroll infinito
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH