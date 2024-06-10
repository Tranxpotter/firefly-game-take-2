import pygame

import sprites
import sprites.player

class Game:
    def __init__(self) -> None:
        self.player = sprites.player.Player()
        
        
        self.sprites:list[pygame.sprite.Sprite] = []