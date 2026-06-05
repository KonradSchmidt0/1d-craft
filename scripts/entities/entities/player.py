import pygame

from scripts.CONSTANTS import BLOCK_SIZE_IN_PIXELS
from scripts.Olympus import Olympus
from scripts.entities.Entity import Entity
from scripts.entities.functions.entity_movement import move_entity
from scripts.entities.interfaces.IEntityRenderable import IEntityRenderable
from scripts.entities.interfaces.IEntityUpdatable import IEntityUpdatable
from scripts.rendering.super_sprite import GameSprite


class Player(Entity, IEntityUpdatable, IEntityRenderable):
    def __init__(self, spd, x, radius=.2, **kwargs):
        super().__init__(self, **kwargs)
        self.x = x
        self.spd = spd
        self.radius = radius
        self.no_clip = False
        self.dir = 1

        a = pygame.image.load("assets/Statue1.png").convert_alpha()
        self.game_sprite = GameSprite(a, (0.5, 0.5), forced_height=BLOCK_SIZE_IN_PIXELS * .9)

    def update(self, olympus: Olympus, dt: float):
        keys = pygame.key.get_pressed()
        horizontal_axis = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT])
        vertical_axis = (keys[pygame.K_s] or keys[pygame.K_DOWN]) - (keys[pygame.K_w] or keys[pygame.K_UP])

        self.dir = 1 if horizontal_axis > 0 else self.dir
        self.dir = -1 if horizontal_axis < 0 else self.dir

        move_entity(
            spd_in_blocks=self.spd,
            x_input=horizontal_axis,
            radius=self.radius,
            entity=self,
            block_world=olympus.block_world,
            dt=dt
        )

        if olympus.input_state.no_clip_press:
            self.no_clip = not self.no_clip

    def get_game_sprite(self):
        return self.game_sprite
