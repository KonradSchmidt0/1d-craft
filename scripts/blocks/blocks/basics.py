import pygame

from scripts.CONSTANTS import BLOCK_SIZE_IN_PIXELS
from scripts.blocks.Block import Block
from scripts.blocks.interfaces.ICollidable import ICollidable
from scripts.rendering.super_sprite import GameSprite


class Air(Block):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Stone(Block, ICollidable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        a = pygame.image.load("assets/sprites/blocks/stone.png").convert_alpha()
        self.sprite = GameSprite(a, (.5, .5), forced_height=BLOCK_SIZE_IN_PIXELS)

    def get_game_sprite(self):
        return self.sprite


class Dirt(Block, ICollidable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        a = pygame.Surface((BLOCK_SIZE_IN_PIXELS, BLOCK_SIZE_IN_PIXELS))
        a.fill((130, 90, 70))
        self.sprite = GameSprite(a, (0.5, 0.5))

    def get_game_sprite(self):
        return self.sprite
