from scripts.Olympus import Olympus


class IEntityUpdatable:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self, olympus: Olympus, dt: float):
        pass
