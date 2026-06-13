import pygame

from scripts.CONSTANTS import BLOCK_SIZE_IN_PIXELS

# Unless specified otherwise, all positions are in pixels, not meters
class Camera:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def world_to_screen(self, pos):
        wx, wy = pos
        return wx - self.x, wy - self.y

    def get_mouse_x_in_world(self):
        return (self.x + pygame.mouse.get_pos()[0]) / BLOCK_SIZE_IN_PIXELS
