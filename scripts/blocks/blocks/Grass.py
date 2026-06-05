import random

import pygame

from scripts.CONSTANTS import BLOCK_SIZE_IN_PIXELS
from scripts.blocks.Block import Block
from scripts.blocks.blocks.basics import Dirt
from scripts.blocks.interfaces.ICollidable import ICollidable
from scripts.blocks.interfaces.IFertile import IFertile
from scripts.blocks.interfaces.IUpdatable import IUpdatable
from scripts.rendering.super_sprite import GameSprite


class Grass(Block, IUpdatable, IFertile, ICollidable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timer = 0
        self.bias = random.uniform(1, 2)

    def get_game_sprite(self):
        a = pygame.Surface((BLOCK_SIZE_IN_PIXELS, BLOCK_SIZE_IN_PIXELS))
        a.fill((100, 200, 70))
        return GameSprite(a, (0.5, 0.5))

    def update(self, left_neigh, right_neigh, dt, pos):
        if not self.is_fertile_right_now():
            return

        neighs = random.choice([[left_neigh, right_neigh], [right_neigh, left_neigh]])
        at_least_one_dirt = False
        for nei in neighs:
            if not isinstance(nei, Dirt):
                continue

            at_least_one_dirt = True

        if at_least_one_dirt:
            self.timer += dt
        else:
            self.timer = 0
            return

        if self.timer <= 10 * self.bias:
            return

        self.timer = 0
        neighs_and_offsets = [(left_neigh, -1), (right_neigh, 1)]

        for nei in neighs_and_offsets:
            if not isinstance(nei[0], Dirt):
                continue

            return ["spawn_block", Grass(), pos + nei[1]]
