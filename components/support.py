import random
import pygame
from .sprite import Sprite


class Support(Sprite):
    """Class that defines logic for support sprites that decrease timer when hit by player"""
    def __init__(self, w=40, h=40, color=(255,255,255), bgcolor=(0,0,255), **kwargs):
        super().__init__(**kwargs)

        self.image = pygame.Surface((w,h))
        self.rect = self.image.get_rect()
        self.image.fill(bgcolor)

    def draw():
        pass