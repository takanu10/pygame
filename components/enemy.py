import random
import pygame
from .sprite import Sprite

class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface(20,10)
        self.surface.fill((255, 165, 0))
        self.rect = self.surface.get_rect(
            center=(
            random.randint(600 + 20, 600 + 100), 
            random.randint(0, 600)))

        self.speed = random.randint(4,14)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
