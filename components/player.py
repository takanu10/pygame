import pygame
from .sprite import Sprite

class Player(Sprite):
    """Class that defines logic for the player sprite"""

    def __init__(self, pos, **kwargs):
        super().__init__(**kwargs)
        image = pygame.image.load("./static/human.png")
        self.image = pygame.transform.scale(image, (50,80))     
        self.rect = self.image.get_rect()
        self.rect.center = pos


