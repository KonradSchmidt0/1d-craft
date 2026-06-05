class ICollidable:
    def __init__(self, radius=0.5, offset=0):
        self.radius = radius
        self.offset = offset

    def is_colliding_with_point(self, my_pos, point):
        return my_pos - self.radius + self.offset < point < my_pos + self.radius + self.offset
