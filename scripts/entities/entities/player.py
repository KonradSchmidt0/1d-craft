import pygame

from scripts.CONSTANTS import BLOCK_SIZE_IN_PIXELS
from scripts.Olympus import Olympus
from scripts.entities.Entity import Entity
from scripts.entities.functions.entity_movement import move_entity, dash_entity
from scripts.entities.interfaces.IStamina import IStamina
from scripts.entities.interfaces.IEntityRenderable import IEntityRenderable
from scripts.entities.interfaces.IEntityUpdatable import IEntityUpdatable
from scripts.rendering.super_sprite import GameSprite


class Player(Entity, IEntityUpdatable, IEntityRenderable, IStamina):
    def __init__(self, spd, x, radius=.2, dash_range=2.5, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.spd = spd
        self.radius = radius
        self.no_clip = False
        self.dir = 1
        self.dash_range = dash_range

        self.surface = pygame.image.load("assets/sprites/entities/Statue1.png").convert_alpha()

    def update(self, olympus: Olympus, dt: float):
        keys = pygame.key.get_pressed()
        horizontal_axis = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT])
        dashing_axis = (keys[pygame.K_w] or keys[pygame.K_UP]) - (keys[pygame.K_s] or keys[pygame.K_DOWN])

        self.dir = -1 if olympus.cam.get_mouse_x_in_world() < self.x else 1

        dash_command = False
        self.regen_stamina(dt, mult=(2 if self.no_clip else 1))
        if dashing_axis != 0:
            dash_command = self.try_consuming_stamina()

        if self.no_clip:
            self.no_clip_movement(horizontal_axis, dashing_axis * self.dir, dash_command, dt)
        else:
            self.player_movement(horizontal_axis, dashing_axis * self.dir, dash_command, olympus, dt)

        if olympus.input_state.no_clip_press:
            self.no_clip = not self.no_clip

    def get_game_sprite(self):
        return GameSprite(self.surface, (0.5, 0.5), forced_height=BLOCK_SIZE_IN_PIXELS * .9, flip=self.dir < 0)

    def player_movement(self, horizontal_axis, dashing_axis, dash_command, olympus, dt):
        if not dash_command:
            move_entity(
                spd_in_blocks=self.spd,
                x_input=horizontal_axis,
                radius=self.radius,
                entity=self,
                block_world=olympus.block_world,
                dt=dt
            )
            return

        dash_entity(
            length=self.dash_range,
            x_input=dashing_axis,
            radius=self.radius,
            entity=self,
            block_world=olympus.block_world,
        )

    def no_clip_movement(self, horizontal_axis, dashing_axis, dash_command, dt):
        if not dash_command:
            self.x += horizontal_axis * self.spd * dt
            return

        self.x += dashing_axis * self.dash_range