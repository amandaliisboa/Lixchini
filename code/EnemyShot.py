from code.Entity import Entity
from code.Const import ENTITY_SPEED

class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # tiro do inimigo se move da direita para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]