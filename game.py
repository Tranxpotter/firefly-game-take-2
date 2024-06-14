import pygame

import sprites
import sprites.player
from sprites.properties import PropertyManager
from sprites.behaviors import BehaviorManager

class Game:
    def __init__(self) -> None:
        self.property_manager = PropertyManager()
        self.behavior_manager = BehaviorManager()
        
        
        
        self.sprites:list[pygame.sprite.Sprite] = []
    
    
    