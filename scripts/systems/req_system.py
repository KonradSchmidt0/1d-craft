from scripts.Olympus import Olympus
from dataclasses import replace

from scripts.blocks.blocks.basics import Air


# Problem: We loop over all the blocks -> evil block at 0 decided to change block at 1 also into an evil block ->
#   we move onto block at position 1 -> it's a new evil block that also changes its neighbour on position 2 ->
#   we turn the entire map into all evil blocks in only one frame
# Solution:
def process_reqs(reqs: list, olympus: Olympus) -> Olympus:
    entities = olympus.entities.copy()
    block_world = olympus.block_world.copy()

    for req in reqs:
        command = req[0]

        if command == "destroy_self":
            entities.remove(req[1])
        elif command == "spawn_block":
            block_world[req[2]] = req[1]
        elif command == "destroy_block":
            block_world[req[1]] = Air()
        elif command == "place_block":
            x = req[1]
            if isinstance(block_world[x], Air):
                block_world[x] = req[2]



    return replace(olympus, entities=entities, block_world=block_world)
