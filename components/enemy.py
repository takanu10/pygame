import random
import pygame
from .sprite import Sprite

class Enemy(Sprite):
    """Class that defines logic for the main enemies the player has to avoid"""

    def __init__(self):
        super().__init__()
        image = pygame.image.load("./static/enemy.png")
        self.image = pygame.transform.scale(image, (80,60))
        self.rect = self.image.get_rect(
            center=(
            random.randint(600 + 20, 600 + 100), 
            random.randint(0, 600)))

        self.speed = random.randint(4,14)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
    