from scripts.blocks.Block import Block
from scripts.entities.Entity import Entity
from dataclasses import dataclass

from scripts.systems.InputState import InputState


@dataclass
class Olympus:
    block_world: list[Block]
    entities: list[Entity]
    input_state: InputState
