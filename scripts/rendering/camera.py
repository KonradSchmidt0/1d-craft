# --- Camera ---
class Camera:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def world_to_screen(self, pos):
        wx, wy = pos
        return wx - self.x, wy - self.y
