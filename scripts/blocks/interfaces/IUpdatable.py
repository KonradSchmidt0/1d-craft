from scripts.blocks.blocks.basics import Block


class IUpdatable:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self,
               left_neigh: Block | None,
               right_neigh: Block | None,
               dt: float,
               pos: int
               ) -> list[list] | None:
        pass
