from scripts.CONSTANTS import BLOCK_SIZE_IN_PIXELS
from scripts.rendering.super_sprite import GameSprite


def render(screen, camera, gamesprites_and_pos: [GameSprite, int, int]):
    for g_sprite, x, y in gamesprites_and_pos:
        w_x, w_y = camera.world_to_screen((x, y))
        o_x, o_y = g_sprite.get_offset()
        screen.blit(g_sprite.surface, (w_x + o_x, w_y + o_y))


class RendererQueue:
    def __init__(self):
        self.queue = []

    def add_sprite_1d_pos(self, spr, x):
        self.queue.append((spr, x, 0))

    def add_sprite_with_2d_pos(self, spr, x, y):
        self.queue.append((spr, x, y))

    def add_world(self, world):
        for i, block in enumerate(world):
            spr = block.get_game_sprite()
            if spr is None:
                continue
            self.queue.append([spr, i * BLOCK_SIZE_IN_PIXELS, 0])

    def add_entities(self, entities):
        for e in entities:
            spr = e.get_game_sprite()
            if spr is None:
                continue
            x = e.x
            self.queue.append((spr, x * BLOCK_SIZE_IN_PIXELS, 0))

    def pop_queue(self):
        a = self.queue
        self.queue = []
        return a
