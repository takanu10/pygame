import pygame
from .sprite import Sprite

class Player(Sprite):
    """Class that defines logic for the player sprite"""

    def __init__(self, pos, **kwargs):
        super().__init__(**kwargs)
        self.image = pygame.image.load("./images/human.png")
        #self.image = pygame.Surface((100, 100))
        # self.surf.set_colorkey((255, 255, 255), RLEACCEL)        
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # if self.limits:
        #     self.move_to(300,300)
        # if self.limits:
        #     self.move_to(
        #         self.limits.center[0] - self.rect.width / 2,
        #         self.limits.bottom - self.rect.height,
        #     )
