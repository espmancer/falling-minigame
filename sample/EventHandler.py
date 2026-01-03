"""
EventHandler
This class will handle all game events by calling each appropriate class method.
"""
import pygame
from Obstacle import Obstacle
from Player import Player

class EventHandler():
    def __init__(self):
        pygame.init()
        
        self.obstacleObject = Obstacle(1, 1)
        self.playerObject = Player(1,1,1,1)

        screen = pygame.display.set_mode([300,800])
        running = True

        while running:
            # Poll through all events.
            for event in pygame.event.get():
                # Did the player close the window?
                if event.type == pygame.QUIT:
                    running = False

            # Define a light blue background.
            backgroundColor = (144,213,255)

            # Color in the background. 
            screen.fill(backgroundColor)

            # Define a black circle to represent the player.
            playerColor = (0,0,0)
            playerRadius = 25
            playerX = 250
            playerY = 250
            playerCenter = (playerX, playerY)

            # Draw the player.
            pygame.draw.circle(screen, playerColor, playerCenter, playerRadius)

            # Flip the display.
            pygame.display.flip()

        pygame.quit()
      
if __name__ == "__main__":
    pass