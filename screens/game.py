import random
import pygame
from screens.base_screen import BaseScreen
from components.text_box import TextBox
from components.enemy import Enemy
from components.support import Support
from components.player import Player

ADDENEMY = pygame.USEREVENT + 1
ADDSUPPORT = pygame.USEREVENT + 1

class GameScreen(BaseScreen):
    """Class that runs during main gameplay"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the main player
        self.player = Player((100,200), limits=self.rect)
        self.quit = TextBox(
            (200, 50), "Press Q to Quit", color=(255,255,255), bgcolor=(56, 164, 168)
        )
        # Put all sprites in group
        self.enemies = pygame.sprite.Group()
        # Create the support items
        self.supports = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        #self.sprites.add(self.supports)
        self.sprites.add(self.quit)

        pygame.time.set_timer(ADDENEMY, 1000)
        pygame.time.set_timer(ADDSUPPORT, 1500)

    def update(self):
        """Method that updates key presses"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move("up")

        if keys[pygame.K_DOWN]:
            self.player.move("down")

        if keys[pygame.K_LEFT]:
            self.player.move("left")

        if keys[pygame.K_RIGHT]:
            self.player.move("right")

        self.sprites.update()

    def draw(self):
        """Method to draw items onto surface"""
        self.quit.rect.x = 395
        self.quit.rect.y = 5
        self.window.fill((37, 92, 94))
        self.sprites.draw(self.window)

    def manage_event(self, event):
        """Method that tracks key presses """
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            # If so, then remove the player and stop the loop
            self.player.kill()
            self.running = False
            self.next_screen = "game_over"

        elif pygame.sprite.spritecollideany(self.player, self.supports):
            #if player hits support, time will go down
            self.player.kill()
            self.running = False
            self.next_screen = "game_over"

        elif event.type == ADDENEMY:
            self.enemy = Enemy()
            self.enemies.add(self.enemy)
            self.sprites.add(self.enemy)

        elif event.type == ADDSUPPORT:
            self.sup = Support()
            self.supports.add(self.sup)
            self.sprites.add(self.sup)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.running = False
                self.next_screen = "welcome"
