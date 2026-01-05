"""
EventHandler
This class will handle all game events by calling each appropriate class method.
"""
import pygame
from Obstacle import Obstacle
from Player import Player
from Background import Background

class EventHandler():
    def __init__(self):
        pygame.init()
        
        self.obstacleObject = Obstacle(1, 1)
        self.playerObject = Player(1,1,1,1)
        # Define a light blue background.
        backgroundColor = (144,213,255)
        self.backgroundObject = Background(backgroundColor)

        screen = pygame.display.set_mode([300,800])
        self.playerObject.setPosition((150,0))
        running = True

        while running:
            # Make the player fall.
            newX = self.playerObject.getPosition()[0]
            newY = self.playerObject.getPosition()[1] + 0.1
            newPosition = (newX, newY)

            self.playerObject.setPosition(newPosition)
            # Poll through all events.
            for event in pygame.event.get():
                # Did the player close the window?
                if event.type == pygame.QUIT:
                    running = False

            # Draw all objects.
            screen.fill(self.backgroundObject.getBackground())
            screen.blit(self.playerObject.image, self.playerObject.rect)
            # Flip the display.
            pygame.display.flip()

        pygame.quit()
      
if __name__ == "__main__":
    pass