"""
Player
This class represents the health and fall, strafe, and rotate speed of the player. 
"""
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, health, fallSpeed, strafeSpeed, rotateSpeed, position=(0.0,0.0)):
        super().__init__()

        self.health = health
        self.fallSpeed = fallSpeed
        self.strafeSpeed = strafeSpeed
        self.rotateSpeed = rotateSpeed
        self.image = pygame.Surface([10,15])

        self.image.fill((0,0,0))

        self.rect = self.image.get_rect()
        (self.rect.x, self.rect.y) = position

    # Get the health of the player.
    def getHealth(self) -> int:
        return self.health
    
    # Get the position of the player.
    def getPosition(self) -> tuple:
        return (self.rect.x, self.rect.y)

    # Set the health of the player.
    def setHealth(self, health):
        self.health = health

    # Set the fall speed of the player.
    def setFallSpeed(self, fallSpeed):
        self.fallSpeed = fallSpeed
    
    # Set the strafe speed of the player.
    def setStrafeSpeed(self, strafeSpeed):
        self.strafeSpeed = strafeSpeed
    
    # Set the rotate speed of the player.
    def setRotateSpeed(self, rotateSpeed):
        self.rotateSpeed = rotateSpeed

    # Set the position of the player.
    def setPosition(self, position):
        (self.rect.x, self.rect.y) = position
    