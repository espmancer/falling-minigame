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
        
        # Declare objects
        self.obstacleObject = Obstacle(1, 1)
        self.playerObject = Player(1,1,1,1)
        # Define a light blue background.
        backgroundColor = (144,213,255)
        self.backgroundObject = Background(backgroundColor)
        self.clock = pygame.time.Clock()

        WIDTH = 300
        HEIGHT = 800
        screen = pygame.display.set_mode([WIDTH,HEIGHT])
        self.playerObject.setPosition((150,0))
        self.speedIncrease = 1.0
        running = True

        while running:
            # Make the player fall.
            newX = self.playerObject.getPosition()[0]
            newY = self.playerObject.getPosition()[1] + 1 * self.speedIncrease
            newPosition = (newX, newY)

            self.playerObject.setPosition(newPosition)
            # Poll through all generated events.
            for event in pygame.event.get():
                # Did the player close the window?
                if event.type == pygame.QUIT:
                    running = False
            # Did the player reach the bottom border of the window?
            if self.playerObject.getPosition()[1] >= HEIGHT:
                self.playerObject.setPosition((newX,0))

            # Draw all objects.
            screen.fill(self.backgroundObject.getBackground())
            screen.blit(self.playerObject.image, self.playerObject.rect)
            self.speedIncrease += 1
            # Flip the display.
            pygame.display.flip()
            
            self.clock.tick(60)

        pygame.quit()
      
if __name__ == "__main__":
    pass