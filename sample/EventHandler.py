"""
EventHandler
This class will handle all game events by calling each appropriate class method.
"""
import pygame
from Obstacle import Obstacle
from Player import Player

class EventHandler():
    def __init__(self):
        self.obstacleObject = Obstacle()
        self.playerObject = Player()