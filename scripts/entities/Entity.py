class Entity:
    def __init__(self, x=0, **kwargs):
        super().__init__(**kwargs)
        self.x = x
