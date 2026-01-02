"""
Obstacle
This class represents the damage and rise speed of any obstacle.
"""
import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, damage, riseSpeed):
        super().__init__
        
        self.damage = damage
        self.riseSpeed = riseSpeed