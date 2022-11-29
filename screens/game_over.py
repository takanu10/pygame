import pygame
from screens.base_screen import BaseScreen
from components.text_box import TextBox


class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.button1 = TextBox(
            (200, 100), "Play Again?", color=(255,255,255), bgcolor=(207, 126, 21)
        )
        self.button2 = TextBox(
            (200, 100), "Quit", color=(255,255,255), bgcolor=(207, 126, 21)
        )
        # self.button1.rect.topleft = (200, 400)
        # self.button2.rect.topleft = (500, 400)
        self.sprites.add(self.button1, self.button2)

    def draw(self):
        self.window.fill((21, 68, 207))
        self.button1.rect.x = 200
        self.button1.rect.y = 150
        self.button2.rect.x = 200
        self.button2.rect.y = 350
        self.sprites.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button1.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "welcome"
            elif self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = False
