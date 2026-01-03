"""
Player
This class represents the health and fall, strafe, and rotate speed of the player. 
"""
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, health, fallSpeed, strafeSpeed, rotateSpeed):
        super().__init__

        self.health = health
        self.fallSpeed = fallSpeed
        self.strafeSpeed = strafeSpeed
        self.rotateSpeed = rotateSpeed

    # Get the health of the player.
    def getHealth(self) -> int:
        return self.health

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
    