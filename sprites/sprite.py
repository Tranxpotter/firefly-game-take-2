from typing import Protocol, TypeAlias, Union
from pygame.sprite import Sprite
from .velocity import Velocity

class _MovableSprite(Protocol):
    @property
    def velocity(self) -> Velocity:...

MovableSprite:TypeAlias = Union[Sprite, _MovableSprite]