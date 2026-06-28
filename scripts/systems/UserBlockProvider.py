from scripts.blocks.blocks.Grass import Grass
from scripts.blocks.blocks.LongFlower import LongFlower
from scripts.blocks.blocks.basics import Stone, Dirt, Wall

PLACEABLE_BLOCKS = [
    Stone, Dirt, Grass, LongFlower, Wall
]


class UserBlockProvider:
    def __init__(self):
        self.chosen = 0

    def get_current_chosen_block(self):
        return PLACEABLE_BLOCKS[self.chosen]

    def handle_key_press(self, key: int):
        """Switch block by pressing 1–9 (or however many blocks exist)."""
        index = key - 1  # key 1 → index 0, key 2 → index 1, etc.
        if 0 <= index < len(PLACEABLE_BLOCKS):
            self.chosen = index
            print("Chosen new block:", self.get_current_chosen_block().__name__)

    def handle_scroll(self, direction: int):
        self.chosen = (self.chosen + direction) % len(PLACEABLE_BLOCKS)
        print("Chosen new block:", self.get_current_chosen_block().__name__)