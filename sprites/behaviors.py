from typing import Iterable, Any
import pygame
from pygame.sprite import AbstractGroup, Sprite

from .properties import ImmovableProperty
from .collision import find_overlap, resolve_overlap

class BaseBehaviorGroup(pygame.sprite.Group):
    def update(self, *args: Any, **kwargs: Any) -> None:
        return
    
    def add(self, *sprites: Any | AbstractGroup | Iterable) -> None:
        raise NotImplementedError("add not implemented for Behavior Groups, use add_internal instead.")

















class SolidBehavior(BaseBehaviorGroup):
    @staticmethod
    def handle_collision(sprite1:Sprite, sprite2:Sprite):
        if sprite1 == sprite2:
            return
        
        resolve_overlap(sprite1, sprite2)
    
    def update(self, *args: Any, **kwargs: Any) -> None:
        pygame.sprite.groupcollide(self, self, False, False, self.handle_collision)


class GravityBehavior(BaseBehaviorGroup):
    def update(self, *args: Any, **kwargs: Any) -> None:
        for sprite in self.sprites():
    






