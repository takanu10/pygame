import pygame


class Sprite(pygame.sprite.Sprite):
    """base class for the types of objects in this game"""
    def __init__(self, limits=None):
        super().__init__()
        # self.image = pygame.Surface(30,30)
        self.rect = self.image.get_rect()
        self.limits = limits

    def boundaries(self):
        """Method that ensures boundaries are maintained"""
        if not self.limits:
            return

        # if self.rect.x < self.limits.left:
        #     self.rect.x = self.limits.left

        # if self.rect.x + self.rect.width > self.limits.right:
        #     self.rect.x = self.limits.right - self.rect.width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.x < self.limits.left:
            self.rect.x = self.limits.left
        if self.rect.x + self.rect.width > self.limits.right:
            self.rect.x = self.limits.right - self.rect.width
        if self.rect.top <= self.limits.top:
            self.rect.top = self.limits.top
        if self.rect.bottom >= self.limits.bottom:
            self.rect.bottom = self.limits.bottom

    def move(self, direction):
        """Method that handles movement for sprite"""
        if direction == "up":
            self.rect.y -= 10
        if direction == "down":
            self.rect.y += 10
        if direction == "right":
            self.rect.x += 10
        if direction == "left":
            self.rect.x -= 10

        self.boundaries()
        

    def update(self):
        self.rect.x += 5