from typing import Iterable, Any
import pygame
from pygame.sprite import AbstractGroup, Sprite

from .properties import ImmovableProperty
from .collision import find_overlap, resolve_overlap
from .velocity import Velocity

class BaseBehaviorGroup(pygame.sprite.Group):
    def update(self, dt, *args: Any, **kwargs: Any) -> None:
        return
    
    def add(self, *sprites: Any | AbstractGroup | Iterable) -> None:
        raise NotImplementedError("add not implemented for Behavior Groups, use add_internal instead.")















class SolidBehavior(BaseBehaviorGroup):
    @staticmethod
    def handle_collision(sprite1:Sprite, sprite2:Sprite):
        if sprite1 == sprite2:
            return
        
        reset_velo = resolve_overlap(sprite1, sprite2)
        if reset_velo is None:
            return
        
        for sprite, axis in reset_velo:
            try:
                velocity:Velocity = sprite.__getattribute__("velocity")
            except AttributeError:
                continue
            velocity.__setattr__(axis, 0)
            
    
    def update(self, *args: Any, **kwargs: Any) -> None:
        pygame.sprite.groupcollide(self, self, False, False, self.handle_collision)


class GravityBehavior(BaseBehaviorGroup):
    def __init__(self, accel:float = -9.81, *sprites: Any | AbstractGroup | Iterable) -> None:
        """
        Initializes a GravityBehavior group with the specified acceleration value.
        
        Args:
            accel (float): The acceleration value to apply to sprites in the group. Defaults to -9.81 (Earth's gravity).
            *sprites (Any | AbstractGroup | Iterable): The sprites or sprite groups to add to the GravityBehavior group.
        """
        super().__init__(*sprites)
        self.accel = accel
        
    
    def update(self, dt, *args: Any, **kwargs: Any) -> None:
        
        for sprite in self.sprites():
            try:
                sprite.__getattribute__("velocity")
            except AttributeError:
                print(f"Immovable sprite with gravity behavior found! {sprite}")
                continue
            sprite.velocity.y += self.accel * dt






