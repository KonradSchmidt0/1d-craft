from scripts.Olympus import Olympus


class IEntityUpdatable:
    def __init__(self):
        pass

    def update(self, olympus: Olympus, dt: float):
        pass
