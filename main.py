import random
import sys

import pygame

from scripts.CONSTANTS import WORLD_SIZE_IN_BLOCKS, BLOCK_SIZE_IN_PIXELS
from scripts.Olympus import Olympus
from scripts.blocks.blocks.Grass import Grass
from scripts.blocks.blocks.basics import Stone, Air, Dirt
from scripts.entities.entities.player_cursor import PlayerCursor
from scripts.entities.entities.TallFlowerSpore import RedFlowerSpore
from scripts.entities.entities.player import Player
from scripts.rendering.camera import Camera
from scripts.rendering.renderer import render, RendererQueue
from scripts.systems.InputState import InputState
from scripts.systems.block_world import process_block_world
from scripts.systems.entity_world import process_entities
from scripts.systems.req_system import process_reqs


def main():
    pygame.init()

    # --- Pygame ---
    WIDTH, HEIGHT = 800, 450
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # --- Rendering ---
    cam = Camera(WORLD_SIZE_IN_BLOCKS * BLOCK_SIZE_IN_PIXELS / 2 - WIDTH / 2, -HEIGHT * (3 / 5))
    renderer_queue = RendererQueue()

    # --- World ---
    player = Player(3.5, WORLD_SIZE_IN_BLOCKS / 2, radius=0.2)
    player_cursor = PlayerCursor(WORLD_SIZE_IN_BLOCKS / 2, 2.5, player)
    olympus = Olympus(
        block_world=[random.choice([Stone(), Dirt(), Grass(), Air()]) for _ in range(WORLD_SIZE_IN_BLOCKS)],
        entities=[player, player_cursor],
        input_state=InputState(),
        cam=cam
    )

    olympus.block_world[round(WORLD_SIZE_IN_BLOCKS / 2) - 3] = Air()
    olympus.block_world[round(WORLD_SIZE_IN_BLOCKS / 2) - 2] = Dirt()
    olympus.block_world[round(WORLD_SIZE_IN_BLOCKS / 2) - 1] = Air()
    olympus.block_world[round(WORLD_SIZE_IN_BLOCKS / 2)] = Air()
    olympus.block_world[round(WORLD_SIZE_IN_BLOCKS / 2) + 1] = Air()
    olympus.block_world[round(WORLD_SIZE_IN_BLOCKS / 2) + 2] = Dirt()

    for i in range(20):
        olympus.entities.append(RedFlowerSpore(WORLD_SIZE_IN_BLOCKS / 2))

    while True:
        dt = clock.tick(120) / 1000.0

        # EVENT LOOP
        olympus.input_state = InputState()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    olympus.input_state.no_clip_press = True

        # LOGIC
        requests = process_block_world(olympus, dt)
        entities_req = process_entities(olympus, dt)
        requests.extend(entities_req)
        olympus = process_reqs(requests, olympus)

        cam.x += (player.x * BLOCK_SIZE_IN_PIXELS - WIDTH / 2 - cam.x) * dt * 4

        # DRAW
        renderer_queue.add_world(olympus.block_world)
        renderer_queue.add_entities(olympus.entities)

        screen.fill((25, 25, 25))

        render(screen, cam, renderer_queue.pop_queue())
        pygame.display.flip()


if __name__ == "__main__":
    main()
