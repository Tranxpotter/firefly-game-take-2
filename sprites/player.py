from typing import Any
import pygame
from pygame.sprite import _Group, Group, Sprite
from .behaviors import SolidBehavior
from .properties import MovableProperty

PlayerGroup = Group()

class Player(Sprite):
    def __init__(self, *, rect:pygame.Rect, hp:float, attack:float, defence:float) -> None:
        properties = [
            SolidBehavior,
            MovableProperty
        ]
        PlayerGroup.add(self)
        for property in properties:
            
        super().__init__()
        
    
    def update(self, *args: Any, **kwargs: Any) -> None:
        return super().update(*args, **kwargs)