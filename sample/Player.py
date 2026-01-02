"""
Player
This class represents the health and fall, strafe, and rotate speed of the player. 
"""
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, health, fallSpeed, strafeSpeed, rotateSpeed):
        super().__init__

        this.health = health
        this.fallSpeed = fallSpeed
        this.strafeSpeed = strafeSpeed
        this.rotateSpeed = rotateSpeed
    