from typing import Iterable, Any
import pygame
from pygame.sprite import AbstractGroup, Sprite

class BasePropertyGroup(pygame.sprite.Group):
    def update(self, *args: Any, **kwargs: Any) -> None:
        return
    
    def add(self, *sprites: Any | AbstractGroup | Iterable) -> None:
        raise NotImplementedError("add not implemented for Property Groups, use add_internal instead.")

class ImmovableProperty(BasePropertyGroup):
    ...

class MovableProperty(BasePropertyGroup):
    def add_internal(self, sprite: Any | Sprite, layer: None = None) -> None:
        super().add_internal(sprite, layer)
        sprite.velocity = 
        