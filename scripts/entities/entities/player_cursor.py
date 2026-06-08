import pygame
from pygame import math

from scripts.CONSTANTS import BLOCK_SIZE_IN_PIXELS, WORLD_SIZE_IN_BLOCKS
from scripts.Olympus import Olympus
from scripts.blocks.blocks.basics import Stone
from scripts.entities.Entity import Entity
from scripts.entities.entities.player import Player
from scripts.entities.interfaces.IEntityRenderable import IEntityRenderable
from scripts.entities.interfaces.IEntityUpdatable import IEntityUpdatable
from scripts.rendering.super_sprite import GameSprite


class PlayerCursor(Entity, IEntityUpdatable, IEntityRenderable):
    def __init__(self, x, cursor_range, player: Player, **kwargs):
        super().__init__(**kwargs)
        self.player = player
        self.cursor_range = cursor_range

        self.mouse_x_in_world = x
        self.x = round(x)

        a = pygame.Surface((BLOCK_SIZE_IN_PIXELS * 1.1, BLOCK_SIZE_IN_PIXELS * 1.1))
        a.fill((0, 0, 0))
        a.set_alpha(51)
        self.game_sprite = GameSprite(a, (0.5, 0.5))

    def update(self, olympus: Olympus, dt: float):
        mouse_pos = olympus.cam.get_mouse_x_in_world()
        player_x = self.player.x
        offset_from_player = mouse_pos - player_x

        self.mouse_x_in_world = player_x + math.clamp(offset_from_player, -self.cursor_range, self.cursor_range)
        self.mouse_x_in_world = math.clamp(self.mouse_x_in_world, 0, WORLD_SIZE_IN_BLOCKS - 1)
        self.x = round(self.mouse_x_in_world)

        if pygame.mouse.get_pressed()[0]:
            return [["destroy_block", self.x]]
        elif pygame.mouse.get_pressed()[2]:
            return [["place_block", self.x, Stone()]]

        return None

    def get_game_sprite(self):
        return self.game_sprite
