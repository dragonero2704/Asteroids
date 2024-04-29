from pygame.sprite import Sprite, Group
from pygame.transform import scale
from pygame.surface import Surface
from pygame.color import THECOLORS
from pygame.mask import from_surface
from pygame.image import load
from math import hypot, atan2
class Vector2:
    def __init__(self, x:float = 0, y:float = 0):
        self.x = x
        self.y = y

    def module(self)->float:
        return hypot(self.x,self.y)
    def angle(self):
        return Vector2(
            atan2(self.y,self.x),
            0
        )
    # math operators
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __truediv__(self, scale:float):
        return Vector2(self.x / scale, self.y / scale)
    def __mul__(self, scale:float):
        return Vector2(self.x * scale, self.y * scale)
    
    # compare operators
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self == other
    
    def tuple(self):
        return (self.x, self.y)
    
    def isZero(self):
        return self.x == 0 and self.y == 0
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    def copy(self):
        return Vector2(self.x, self.y)

class GameObj(Sprite):
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
        super().__init__()
        if group is not None:
            self.add(group)   

        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.size = size

        if imagePath is None:
            if image is None:
                self.image = Surface(self.size.tuple(), masks=color)
            else:
                self.image = scale(image, self.size.tuple())
        else:
            try:
                self.image = scale(load(imagePath), self.size.tuple())
            except FileNotFoundError:
                raise FileNotFoundError(f"{imagePath} not found")
        
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.position.tuple()
        self.mask = from_surface(self.image)
    
    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration

        self.rect.x, self.rect.y = self.position.tuple()
    






