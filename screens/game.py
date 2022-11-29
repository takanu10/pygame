import random
import pygame
from screens.base_screen import BaseScreen
from components.text_box import TextBox
from components.enemy import Enemy
from components.obstacle import Obstacle
from components.player import Player


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the main player
        self.player = Player()
        #self.paddle = Paddle(200, 30, (0, 255, 0), limits=self.rect)

        # Create the enemies
        self.enemy = Enemy()
        #self.ball = Ball(limits=self.rect)
        #self.ball.speed = 8

        #self.ball.angle = random.randint(0, 31416) / 10000

        # Create the obstacles
        self.obstacle = Obstacle()
        #self.tiles = TileGroup(tile_width=120, tile_height=30)

        # Put all sprites in group
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        self.sprites.add(self.enemy)
        self.sprites.add(self.obstacle)

    def update(self):
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

        #HANDLE COLLISION

        #collided = self.ball.collidetiles(self.tiles)

        #caught_the_ball = self.ball.collidepaddle(self.paddle.rect)

        #FAIL STATE

        #if self.player.rect.top == self.
            # self.running = False
            # self.next_screen = "game_over"

        # if self.ball.rect.bottom > self.paddle.rect.top and not caught_the_ball:
        #     self.running = False
        #     self.next_screen = "game_over"

    def draw(self):
        self.window.fill((37, 92, 94))
        self.sprites.draw(self.window)
        #self.tiles.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.ball.speed = 10
                self.ball.angle = 1.5
