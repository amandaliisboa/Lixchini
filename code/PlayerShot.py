from code.Entity import Entity
from code.Const import ENTITY_SPEED


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # tiro do player se move da esquerda para a direita
        self.rect.centerx += ENTITY_SPEED[self.name]