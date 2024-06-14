from typing import Iterable, Any, Type, Sequence
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
    """
    Implements a `SolidBehavior` group that handles collisions between sprites in the group. When two sprites in the group collide, the `handle_collision` method is called to resolve the overlap and reset the velocity of the colliding sprites along the axis of collision.
    
    The `update` method of the `SolidBehavior` group uses `pygame.sprite.groupcollide` to detect collisions between all sprites in the group, and then calls the `handle_collision` method for each pair of colliding sprites.
    """
    @staticmethod
    def handle_collision(sprite1:Sprite, sprite2:Sprite):
        """
        Resolves the overlap between two sprites in the `SolidBehavior` group and resets the velocity of the colliding sprites along the axis of collision.
        
        Args:
            sprite1 (pygame.sprite.Sprite): The first sprite involved in the collision.
            sprite2 (pygame.sprite.Sprite): The second sprite involved in the collision.
        """
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
    """
    Implements a `GravityBehavior` group that applies a constant acceleration force to all sprites in the group, simulating the effect of gravity.
    
    The `update` method of the `GravityBehavior` group iterates through all sprites in the group and updates their `velocity.y` attribute by adding the acceleration value multiplied by the time delta. If a sprite does not have a `velocity` attribute, a warning message is printed.
    
    Args:
        accel (float): The acceleration value to apply to sprites in the group. Defaults to -9.81 (Earth's gravity).
        *sprites (Any | AbstractGroup | Iterable): The sprites or sprite groups to add to the GravityBehavior group.
    """
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




all_groups:list[Type[BaseBehaviorGroup]] = [SolidBehavior, GravityBehavior]

class BehaviorManager:
    def __init__(self) -> None:
        self.behaviors = {group:group() for group in all_groups}
    
    def add_sprite(self, sprite, behaviors:Iterable[Type[BaseBehaviorGroup]]) -> None:
        for behavior in behaviors:
            assert behavior in self.behaviors, f"behavior {behavior} not found in BehaviorManager"
            self.behaviors[behavior].add_internal(sprite)
    
    
    def get_behavior(self, behavior:Type[BaseBehaviorGroup]) -> BaseBehaviorGroup:
        assert behavior in self.behaviors, f"behavior {behavior} not found in BehaviorManager"
        return self.behaviors[behavior]