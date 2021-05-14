import pygame
import random

class Apple():
    def __init__(self, display):
        self.x = random.randint(65, 630)
        self.y = random.randint(65, 530)
        self.r = 15
        self.dsply = display

    def show(self):
        apple_pic = pygame.image.load("Assignment14/assets/img/apple.png")
        self.dsply.blit(apple_pic, (self.x, self.y))