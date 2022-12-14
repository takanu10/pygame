import pygame
from screens.welcome import WelcomeScreen 
from screens.game import GameScreen 
from screens.game_over import GameOverScreen

class Game:
    """Main class for the application"""

    def __init__(self):
        # Creates the window
        self.window = pygame.display.set_mode((600, 600))
        self.title = pygame.display.set_caption("Brace")

    def run(self):
        """Main method, manages interaction between screens"""
        #Brace is a game in which there's a countdown as the player tries to avoid enemies
        #Support sprites will increase timer by 5 sec when hit
        #json will store player data for highest times 

        #Timer 1: countdown
        #Timer 2: Times how long player stays alive

        # Available screens
        screens = {
            "welcome": WelcomeScreen,
            "game": GameScreen,
            "game_over": GameOverScreen,
        }

        # Start the loop
        run = True
        current_screen = "welcome"
        while run:
            # Obtain the screen class
            pygame.time.delay(100)
            screen_class = screens.get(current_screen)
            if not screen_class:
                raise RuntimeError(f"Screen {current_screen} not found!")

            # Create a new screen object, "connected" to the window
            screen = screen_class(self.window)

            # Run the screen
            screen.run()

            if screen.next_screen is False:
                run = False
            # Switch to the next screen
            current_screen = screen.next_screen


if __name__ == "__main__":
    sprint = Game()
    sprint.run()
