import random
import pygame
from screens.base_screen import BaseScreen
from components.text_box import TextBox
from components.enemy import Enemy
from components.support import Support
from components.player import Player

class GameScreen(BaseScreen):
    """Class that runs during main gameplay"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the main player
        self.player = Player((100,200), limits=self.rect)
        #Quit text on top right
        self.quit = TextBox(
            (200, 50), "Press Q to Quit", color=(255,255,255), bgcolor=(56, 164, 168)
        )
        #object that tracks time 
        self.clock = pygame.time.Clock()
        self.counter, self.text = 10, '10'.rjust(3)
        self.font = pygame.font.SysFont('Consolas', 30)


        # put all sprites in groups
        self.enemies = pygame.sprite.Group()
        self.supports = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        self.sprites.add(self.quit)

        #broadcasts the custom event after specified time 
        self.ADDENEMY = pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.ADDSUPPORT = pygame.time.set_timer(pygame.USEREVENT + 1, 5000)
        #every second, the counter goes down
        self.TIMER = pygame.time.set_timer(pygame.USEREVENT + 2, 1000)

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

        # while self.run:
        #     for e in pygame.event.get():
        #         if e.type == pygame.USEREVENT: 
        #             counter -= 1
        #             text = str(counter).rjust(3) if counter > 0 else 'boom!'
        #         if e.type == pygame.QUIT: 
        #             run = False

                # screen.fill((255, 255, 255))
                # screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
                # pygame.display.flip()
                # self.clock.tick(60)
        self.sprites.update()

    def draw(self):
        """Method to draw items onto surface"""
        self.quit.rect.x = 395
        self.quit.rect.y = 5
        self.window.fill((37, 92, 94))
        self.sprites.draw(self.window)
        self.window.blit(self.font.render(self.text, True, (0, 0, 0)), (32, 48))


    def manage_event(self, event):
        """Method that tracks key presses """
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            # If so, then remove the player and stop the loop
            self.player.kill()
            self.running = False
            self.next_screen = "game_over"

        if pygame.sprite.spritecollideany(self.player, self.supports):
            #if player hits support, time will go down
            self.counter += 5

        #custom event that adds the enemy sprite
        #enemy
        elif event.type == pygame.USEREVENT:
            self.enemy = Enemy()
            self.enemies.add(self.enemy)
            self.sprites.add(self.enemy)
        #custom event that adds the support sprite
        #support
        elif event.type == pygame.USEREVENT + 1:
            self.sup = Support()
            self.supports.add(self.sup)
            self.sprites.add(self.sup)
        #custom event that handles timer counter
        #timer
        elif event.type == pygame.USEREVENT + 2:
            self.counter -= 1
            self.text = str(self.counter).rjust(3) if self.counter > 0 else 'boom!'

        # elif event.type == : 
        #     counter -= 1
        #     text = str(counter).rjust(3) if counter > 0 else 'boom!'

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.running = False
                self.next_screen = "welcome"
