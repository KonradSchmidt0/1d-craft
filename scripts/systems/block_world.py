from scripts.CONSTANTS import WORLD_SIZE_IN_BLOCKS
from scripts.Olympus import Olympus
from scripts.blocks.interfaces.IUpdatable import IUpdatable
from scripts.blocks.blocks.basics import Block


def process_block_world(olympus: Olympus, dt):
    world = olympus.block_world
    change_request_queue = []

    for i, block in enumerate(world):
        if not isinstance(block, IUpdatable):
            continue
        req = block.update(get_block(i - 1, world), get_block(i + 1, world), dt, i)
        if req is not None:
            change_request_queue.append(req)

    return change_request_queue


def get_block(pos: int, block_world: list[Block]):
    if pos < 0 or pos >= WORLD_SIZE_IN_BLOCKS:
        return None
    else:
        return block_world[pos]
