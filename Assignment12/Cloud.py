import pygame
import random

class Cloud:
    def __init__(self, game):
        self.game = game
        self.x = random.randint(0, game.width)
        self.y = -50
        self.speed = 1
        self.image = pygame.image.load("Assignment12/assets/img/cloud.png")
        
    def show(self):
        self.game.dsply.blit(self.image, (self.x, self.y))
        self.y += self.speed
            