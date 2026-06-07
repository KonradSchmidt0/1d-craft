class IEntityRenderable:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_game_sprite(self):
        return None
