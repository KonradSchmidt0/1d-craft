import pygame.transform


class GameSprite:
    def __init__(self, surface, anchor=(0, 0), scale=1, forced_height=None, forced_width=None):
        """
        image: pygame.Surface
        anchor: (ax, ay) where 0..1 represent relative anchor
            (0,0) = top-left
            (0.5,0.5) = center
            (1,1) = bottom-right
        scale: scale is utilized only if all the forced fields are set to None
        forced_...: if only one forced axis is given, the second axis will confirm by keeping correct aspect ratio
        """
        (w, h) = surface.get_width(), surface.get_height()
        ratio_how_bigger_is_width = w / h

        self.w = forced_width
        self.h = forced_height

        if self.w is not None and self.h is not None:
            pass
        elif self.w is not None:
            self.h = self.w / ratio_how_bigger_is_width
        elif self.h is not None:
            self.w = self.h * ratio_how_bigger_is_width
        else:
            self.w = w * scale
            self.h = h * scale

        self.surface = pygame.transform.scale(surface, (self.w, self.h))
        self.anchor = anchor

    def get_offset(self):
        """
        Returns how many pixels you have to offset this image while rendering
        """

        # Apply anchor
        x = -self.w * self.anchor[0]
        y = -self.h * self.anchor[1]

        return x, y
