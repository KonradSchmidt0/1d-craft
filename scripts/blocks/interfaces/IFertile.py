class IFertile:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def is_fertile_right_now(self):
        return True
