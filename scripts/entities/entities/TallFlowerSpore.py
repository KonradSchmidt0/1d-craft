import random
import pygame

from scripts.CONSTANTS import BLOCK_SIZE_IN_PIXELS
from scripts.Olympus import Olympus
from scripts.blocks.blocks.LongFlower import LongFlower
from scripts.blocks.blocks.basics import Air, Dirt
from scripts.entities.Entity import Entity
from scripts.entities.interfaces.IEntityRenderable import IEntityRenderable
from scripts.entities.interfaces.IEntityUpdatable import IEntityUpdatable
from scripts.rendering.super_sprite import GameSprite
from scripts.systems.block_world import get_block


class RedFlowerSpore(Entity, IEntityUpdatable, IEntityRenderable):
    def __init__(self, x):
        super().__init__(self)
        self.x = x
        self.vel = random.choice([3.2, -3.2]) * random.uniform(0.9, 1.1)
        self.timer = 0
        self.maxTimer = random.uniform(4, 20)

        a = pygame.Surface((BLOCK_SIZE_IN_PIXELS * 0.15, BLOCK_SIZE_IN_PIXELS * 0.15))
        a.fill((50, 128, 50))
        a.set_alpha(125)
        self.game_sprite = GameSprite(a, (0.5, 0.5))

    def update(self, olympus: Olympus, dt: float):
        self.x += self.vel * dt
        self.timer += dt

        if self.timer < self.maxTimer:
            return []

        o = [["destroy_self", self]]

        int_x = round(self.x)
        block_at_my_pos = get_block(int_x, olympus.block_world)
        if not isinstance(block_at_my_pos, Air):
            return o

        offsets = [int_x - 1, int_x + 1]
        for offset in offsets:
            if not isinstance(get_block(offset, olympus.block_world), Dirt):
                continue
            o.append(["place_block", int_x, LongFlower()])
            print("Plant seeded at", int_x)
            break

        return o

    def get_game_sprite(self):
        return self.game_sprite
