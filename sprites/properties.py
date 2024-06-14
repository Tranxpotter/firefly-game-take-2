from typing import Iterable, Any, Type
import pygame
from pygame.sprite import AbstractGroup, Sprite

from .velocity import Velocity

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
        sprite.__setattr__("velocity", Velocity())



all_groups:list[Type[BasePropertyGroup]] = [ImmovableProperty, MovableProperty]

class PropertyManager:
    def __init__(self) -> None:
        self.properties = {group:group() for group in all_groups}
    
    def add_sprite(self, sprite, properties:Iterable[Type[BasePropertyGroup]]) -> None:
        for property in properties:
            assert property in self.properties, f"property {property} not found in PropertyManager"
            self.properties[property].add_internal(sprite)
    
    
    def get_behavior(self, property:Type[BasePropertyGroup]) -> BasePropertyGroup:
        assert property in self.properties, f"property {property} not found in PropertyManager"
        return self.properties[property]