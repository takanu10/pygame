import pygame
from screens.base_screen import BaseScreen
from components.text_box import TextBox


class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.button = TextBox(
            (180, 100), "Play", color=(255,255,255), bgcolor=(207, 126, 21)
        )
        self.title = TextBox((180,100), "BRACE", color=(207, 126, 21), bgcolor=(21, 68, 207))
        self.sprites.add(self.button)
        self.sprites.add(self.title)

    def draw(self):
        
        self.window.fill((21, 68, 207))
        self.title.rect.x = 200
        self.title.rect.y = 150
        self.button.rect.x = 200
        self.button.rect.y = 350
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.rect.collidepoint(event.pos):
                self.next_screen = "game"
                self.running = False

        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     self.next_screen = "game"
        #     self.running = False
