from gameObject import Vector2, GameObj
from pygame.sprite import Sprite, Group
from pygame.transform import scale, rotate
from pygame.surface import Surface
from pygame.color import THECOLORS
from pygame.mask import from_surface
from pygame.image import load
from math import hypot, atan2

class SpaceShip(GameObj):
    def __init__(
            self,
            position:Vector2 = Vector2(),
            velocity:Vector2 = Vector2(),
            acceleration:Vector2 = Vector2(),

            imagePath:str = None,
            image:Surface = None,
            color:tuple[4] = THECOLORS["red"],
            size:Vector2 = Vector2(10,10),
            group:Group = None
    ):
        super().__init__(position, velocity, acceleration, imagePath, image, color, size, group)
        self.angle = 0


