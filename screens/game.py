import random
import pygame
from screens.base_screen import BaseScreen
from components.text_box import TextBox
from components.enemy import Enemy
from components.obstacle import Obstacle
from components.player import Player


class GameScreen(BaseScreen):
    """Class that runs during main gameplay"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the main player
        self.player = Player()

        # Create the enemies
        self.enemy = Enemy()

        # Create the obstacles
        self.obstacle = Obstacle()

        # Put all sprites in group
        self.quit = TextBox(
            (200, 50), "Press Q to Quit", color=(255,255,255), bgcolor=(56, 164, 168)
        )
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        self.sprites.add(self.enemy)
        self.sprites.add(self.obstacle)
        self.sprites.add(self.quit)

    def update(self):
        """Method that updates key presses"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move("up")
            #self.player.down = False

        if keys[pygame.K_DOWN]:
            self.player.move("down")
            #self.player.up = False

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.running = False
                self.next_screen = "welcome"