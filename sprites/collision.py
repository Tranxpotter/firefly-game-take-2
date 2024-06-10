from typing import Literal

import pygame
from pygame.sprite import Sprite

from .properties import ImmovableProperty


def find_overlap(sprite1: Sprite, sprite2: Sprite):
    """
    Finds the overlap between two sprites along the x and y axes.
    Returns a tuple (overlap_x, overlap_y) where overlap_x and overlap_y are the overlap distances.
    """
    # Get the bounding rectangles of the sprites
    rect1 = sprite1.rect
    rect2 = sprite2.rect
    if rect1 is None or rect2 is None:
        print(f"find_overlap missing rect from {sprite1 if rect1 is None else sprite2 if rect2 is None else (sprite1, sprite2)}")
        return (0, 0)
    
    # Calculate the overlap along the x-axis
    if rect1.right < rect2.left or rect1.left > rect2.right:
        overlap_x = 0
    else:
        overlap_x = min(rect1.right, rect2.right) - max(rect1.left, rect2.left)

    # Calculate the overlap along the y-axis
    if rect1.bottom < rect2.top or rect1.top > rect2.bottom:
        overlap_y = 0
    else:
        overlap_y = min(rect1.bottom, rect2.bottom) - max(rect1.top, rect2.top)

    return overlap_x, overlap_y

def resolve_overlap(sprite1: Sprite, sprite2: Sprite) -> list[tuple[Sprite, Literal["x", "y"]]] | None:
    """
    Resolves the overlap between two sprites by moving the movable sprite(s)
    along the axis with the least overlap. If both sprites are movable, it
    moves them simultaneously by half the overlapped distance.
    Returns a tuple (sprite, Literal["x", "y"])
    """
    if sprite1.rect is None or sprite2.rect is None:
        print(f"find_overlap missing rect from {sprite1 if sprite1.rect is None else sprite2 if sprite2.rect is None else (sprite1, sprite2)}")
        return
    
    sprite1_movable = ImmovableProperty not in [type(group) for group in sprite1.groups()]
    sprite2_movable = ImmovableProperty not in [type(group) for group in sprite2.groups()]

    if not sprite1_movable and not sprite2_movable:
        return

    overlap_x, overlap_y = find_overlap(sprite1, sprite2)

    if overlap_x == 0 and overlap_y == 0:
        return

    if overlap_x < overlap_y:
        # Resolve along the x-axis
        if sprite1_movable and sprite2_movable:
            # Move both sprites by half the overlap distance
            sprite1.rect.x -= overlap_x // 2
            sprite2.rect.x += overlap_x // 2
            return [(sprite1, "x"), (sprite2, "x")]
        elif sprite1_movable:
            # Move sprite1 by the full overlap distance
            sprite1.rect.x -= overlap_x
            return [(sprite1, "x")]
        else:
            # Move sprite2 by the full overlap distance
            sprite2.rect.x += overlap_x
            return [(sprite2, "x")]
    else:
        # Resolve along the y-axis
        if sprite1_movable and sprite2_movable:
            # Move both sprites by half the overlap distance
            sprite1.rect.y -= overlap_y // 2
            sprite2.rect.y += overlap_y // 2
            return [(sprite1, "y"), (sprite2, "y")]
        elif sprite1_movable:
            # Move sprite1 by the full overlap distance
            sprite1.rect.y -= overlap_y
            return [(sprite1, "y")]
        else:
            # Move sprite2 by the full overlap distance
            sprite2.rect.y += overlap_y
            return [(sprite2, "y")]