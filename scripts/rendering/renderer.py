from scripts.CONSTANTS import BLOCK_SIZE_IN_PIXELS
from scripts.blocks.Block import Block
from scripts.entities.Entity import Entity
from scripts.entities.interfaces.IEntityRenderable import IEntityRenderable
from scripts.rendering.camera import Camera

# The renderer optimization doesn't if each edge of a sprite is outside bounds, only looks if origin is
# As such, it is necessary to give it some wiggle room
# TLDR: set this width of biggest sprite
RENDER_WIGGLE_ROOM_IN_PIXELS = BLOCK_SIZE_IN_PIXELS

def render(screen, camera, gamesprites_and_pos):
    for g_sprite, x, y in gamesprites_and_pos:
        w_x, w_y = camera.world_to_screen((x, y))
        o_x, o_y = g_sprite.get_offset()
        screen.blit(g_sprite.surface, (w_x + o_x, w_y + o_y))


def is_in_render_distance(x_in_pixels, screen_x, screen_width):
    wiggle = RENDER_WIGGLE_ROOM_IN_PIXELS
    return screen_x - wiggle < x_in_pixels < screen_x + screen_width + wiggle


class RendererQueue:
    def __init__(self):
        self.queue = []

    def add_sprite_1d_pos(self, spr, x):
        self.queue.append((spr, x, 0))

    def add_sprite_with_2d_pos(self, spr, x, y):
        self.queue.append((spr, x, y))

    def add_world(self, world: list[Block], cam: Camera, screen_width):
        for i, block in enumerate(world):
            x = i * BLOCK_SIZE_IN_PIXELS
            if not is_in_render_distance(x, cam.x, screen_width):
                continue
            spr = block.get_game_sprite()
            if spr is None:
                continue
            self.queue.append([spr, x, 0])

    def add_entities(self, entities: list[Entity], cam: Camera, screen_width):
        for e in entities:
            x = e.x * BLOCK_SIZE_IN_PIXELS
            if not is_in_render_distance(x, cam.x, screen_width):
                continue
            if not isinstance(e, IEntityRenderable):
                continue
            spr = e.get_game_sprite()
            if spr is None:
                continue
            self.queue.append((spr, x, 0))

    def pop_queue(self):
        a = self.queue
        self.queue = []
        return a
