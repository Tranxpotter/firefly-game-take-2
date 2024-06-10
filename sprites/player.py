import pygame
from pygame.sprite import _Group
from .behaviors import SolidBehavior

class Player(pygame.sprite.Sprite):
    def __init__(self, *, rect:pygame.Rect, hp:float, attack:float, defence:float) -> None:
        groups = [
            SolidBehavior
        ]
        super().__init__()
    
    