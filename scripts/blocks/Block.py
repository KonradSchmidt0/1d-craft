from scripts.rendering.super_sprite import GameSprite


class Block:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_game_sprite(self) -> GameSprite | None:
        return None
