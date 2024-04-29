from gameObject import Vector2, GameObj
from pygame.sprite import Group, Sprite

class SpaceShip(Group):
    def __init__(
            self,
            position:Vector2 = Vector2(),
            velocity:Vector2 = Vector2(),
            acceleration:Vector2 = Vector2(),
            size:Vector2 = Vector2(10,10)
    ):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

        # costruzione segmenti
        # 1. top-left
        topLeft = GameObj()

