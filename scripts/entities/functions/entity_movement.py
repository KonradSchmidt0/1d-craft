from scripts.systems.block_world import get_block
from scripts.blocks.interfaces.ICollidable import ICollidable


def move_entity(spd_in_blocks, x_input, radius, entity, block_world, dt):
    df = x_input * spd_in_blocks * dt
    movement_dir = 1 if df > 0 else -1

    if is_point_in_world_solid(entity.x + df + radius * movement_dir, block_world) and not entity.no_clip is True:
        return

    entity.x += df


def is_point_in_world_solid(point, block_world):
    block_pos = round(point)
    block = get_block(block_pos, block_world)

    if not isinstance(block, ICollidable):
        return False

    return block.is_colliding_with_point(block_pos, point)
