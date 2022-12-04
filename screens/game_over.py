import pygame
from screens.base_screen import BaseScreen
from components.text_box import TextBox
import webbrowser
from subprocess import Popen

class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.title = TextBox((180,100), "Game Over!", color=(207, 126, 21), bgcolor=(21, 68, 207))
        self.button1 = TextBox(
            (200, 100), "Play Again", color=(255,255,255), bgcolor=(207, 126, 21)
        )
        self.button2 = TextBox(
            (200, 100), "Quit", color=(255,255,255), bgcolor=(207, 126, 21)
        )
        self.button3 = TextBox(
            (200, 100), "High Scores", color=(255,255,255), bgcolor=(207, 126, 21)
        )
        self.sprites.add(self.title, self.button1, self.button2, self.button3)

    def draw(self):
        self.window.fill((21, 68, 207))
        self.title.rect.x = 210
        self.title.rect.y = 150
        self.button1.rect.x = 70
        self.button1.rect.y = 300
        self.button2.rect.x = 330
        self.button2.rect.y = 300
        self.button3.rect.x = 200
        self.button3.rect.y = 440
        self.sprites.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            #restarts game
            if self.button1.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "game"
            #quits game
            elif self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = False
            #goes to flask high scores 
            elif self.button3.rect.collidepoint(event.pos):
                Popen("python app.py")
                webbrowser.open('http://127.0.0.1:5000/')

