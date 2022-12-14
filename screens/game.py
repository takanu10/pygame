import pygame
from screens.base_screen import BaseScreen
from components.text_box import TextBox
from components.enemy import Enemy
from components.support import Support
from components.player import Player
import json

user_count = 0

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
        #counter for countdown timer
        self.counter, self.text = 10, '10'.rjust(3)
        self.font = pygame.font.SysFont('Consolas', 30)
        
        #overall_time for high score timer in .json 
        self.overall_time = 0
       
        # put all sprites in groups
        self.enemies = pygame.sprite.Group()
        self.supports = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        self.sprites.add(self.quit)
        
        #broadcasts the custom event after specified time 
        self.ADDENEMY = pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.ADDSUPPORT = pygame.time.set_timer(pygame.USEREVENT + 1, 4000)
        #every second, the counter goes down
        self.COUNTDOWN = pygame.time.set_timer(pygame.USEREVENT + 2, 1000)
        #every second, counter goes up; when game over, total sent to json
        self.TIMER = pygame.time.set_timer(pygame.USEREVENT + 3, 1000)
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
        #prints countdown on screen
        self.window.blit(self.font.render(self.text, True, (255,255,255)), (5, 15))

    def update_json(self, filename="./database/database.json"):
        """read + updates json file """
        global user_count
        with open(filename, 'r') as file:
            file_load = json.load(file)
            # file_load["Time"].append(data)
        total = f"{self.overall_time} sec"
        user_count += 1
        file_load.append({"user":user_count,"time":total})
        with open(filename, 'w') as file:
            #converts back to json
            json.dump(file_load, file)

    def manage_event(self, event):
        """Method that tracks key presses """
        #custom event that spawns enemy sprites
        self.user = 0
        if event.type == pygame.USEREVENT:
            self.enemy = Enemy()
            self.enemies.add(self.enemy)
            self.sprites.add(self.enemy)
        #custom event that spawns support sprites
        elif event.type == pygame.USEREVENT + 1:
            self.sup = Support()
            self.supports.add(self.sup)
            self.sprites.add(self.sup)
        #custom event that handles countdown counter
        elif event.type == pygame.USEREVENT + 2:
            self.counter -= 1
            if self.counter > 0:
                self.text = str(self.counter).rjust(3)
            else:
                #if counter hits 0
                # self.user += 1
                self.update_json()
                self.running = False
                self.next_screen = "game_over"
        #timer for how long player lasts overall
        elif event.type == pygame.USEREVENT + 3:
            self.overall_time += 1
        elif pygame.sprite.spritecollideany(self.player, self.enemies):
            # If so, then remove the player and stop the loop
            self.player.kill()
            self.update_json()
            self.running = False
            self.next_screen = "game_over"

        elif pygame.sprite.spritecollideany(self.player, self.supports):
            #if player hits support, time will go down
            self.counter += 5
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.running = False
                self.next_screen = "welcome"
