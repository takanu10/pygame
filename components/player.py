import pygame
from .sprite import Sprite

class Player(Sprite):
    """Class that defines logic for the player"""

    def __init__(self, pos, **kwargs):
        super().__init__(**kwargs)
        self.image = pygame.image.load("./images/human.png").convert()
        # self.surf.set_colorkey((255, 255, 255), RLEACCEL)        
        self.rect = self.image.get_rect()
        self.rect.center = pos

        if self.limits:
            self.move_to(
                self.limits.center[0] - self.rect.width / 2,
                self.limits.bottom - self.rect.height,
            )

    def draw():
        pass