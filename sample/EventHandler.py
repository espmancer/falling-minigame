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
        self.playerObject = Player(1,5,5,5)
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
            # Adjust the player's current X and Y.
            newX = self.playerObject.getPosition()[0]
            newY = self.playerObject.getPosition()[1] + 1 * self.speedIncrease

            # Poll through all generated events.
            for event in pygame.event.get():
                # Did the player close the window?
                if event.type == pygame.QUIT:
                    running = False

            # Did the player press a key?
            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_a]:
                newX -= self.playerObject.getStrafeSpeed()
            if keys[pygame.K_d]:
                newX += self.playerObject.getStrafeSpeed()
            if keys[pygame.K_w]:
                slowdownAmount = (self.playerObject.getFallSpeed() / self.speedIncrease)
                slowdownAmount -= 1
                newY -= slowdownAmount
            if keys[pygame.K_s]:
                newY += self.playerObject.getFallSpeed() * self.speedIncrease

            # Did the player reach the bottom border of the window?
            if newY >= HEIGHT:
                newY = 0

            # Set the position of the player.
            newPosition = (newX, newY)
            self.playerObject.setPosition(newPosition)
            self.speedIncrease += .01
            
            # Draw all objects.
            screen.fill(self.backgroundObject.getBackground())
            screen.blit(self.playerObject.image, self.playerObject.rect)
            # Flip the display.
            pygame.display.flip()
            
            self.clock.tick(60)
            # print(f"FPS: {self.clock.get_fps(): .2f} Y >= HEIGHT: {newY: .2f} >= {HEIGHT}: {newY >= HEIGHT} ")

        pygame.quit()
      
if __name__ == "__main__":
    pass