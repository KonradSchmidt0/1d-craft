from pygame import math

from scripts.systems.block_world import get_block
from scripts.blocks.interfaces.ICollidable import ICollidable

SUBSTEP_SIZE = .1

def move_entity(spd_in_blocks, x_input, radius, entity, block_world, dt):
    dash_entity(spd_in_blocks * dt, x_input, radius, entity, block_world)

def dash_entity(length, x_input, radius, entity, block_world):
    df = length * math.clamp(x_input, -1, 1)

    is_future_pos_solid = lambda _df: (
        is_point_in_world_solid(entity.x + _df + radius, block_world) or
        is_point_in_world_solid(entity.x + _df - radius, block_world)
    )

    if not is_future_pos_solid(df):
        entity.x += df
        return

    # substeps
    while 0 + SUBSTEP_SIZE < df * x_input:
        df -= SUBSTEP_SIZE * x_input
        print(df)
        if not is_future_pos_solid(df):
            entity.x += df
            return
        pass

    return


def is_point_in_world_solid(point, block_world):
    block_pos = round(point)
    block = get_block(block_pos, block_world)

    if not isinstance(block, ICollidable):
        return False

    return block.is_colliding_with_point(block_pos, point)
