import pygame

from scripts.CONSTANTS import BLOCK_SIZE_IN_PIXELS
from scripts.blocks.blocks.basics import Block
from scripts.rendering.super_sprite import GameSprite


class LongFlower(Block):
    def __init__(self):
        super().__init__()
        a = pygame.Surface((BLOCK_SIZE_IN_PIXELS, BLOCK_SIZE_IN_PIXELS * 0.5))
        a.fill((50, 128, 50))
        self.game_sprite = GameSprite(a, (0.5, 0.5))

    def get_game_sprite(self):
        return self.game_sprite
