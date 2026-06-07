class IStamina:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stamina_regen = kwargs.get("stamina_regen", 1)
        self.stamina = 1

    def regen_stamina(self, dt, mult=1):
        self.stamina = min(self.stamina + self.stamina_regen * mult * dt, 1)

    def try_consuming_stamina(self):
        if self.stamina < 1:
            return False

        self.stamina = 0
        return True
