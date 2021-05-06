import pygame
import random

class Object():
    def __init__(self, display):
        self.x = random.randint(65, 630)
        self.y = random.randint(65, 530)
        self.r = 15
        self.dsply = display
        
        
class Apple(Object):
    def __init__(self, display):
        super().__init__(display)

    def show(self):
        apple_pic = pygame.image.load("Assignment11/assets/img/apple.png")
        self.dsply.blit(apple_pic, (self.x, self.y))
    
        
class Pear(Object):
    def __init__(self, display):
        super().__init__(display)

    def show(self):
        pear_pic = pygame.image.load("Assignment11/assets/img/pear.png")
        self.dsply.blit(pear_pic, (self.x, self.y))
        
        
class Bomb(Object):
    def __init__(self, display):
        super().__init__(display)

    def show(self):
        bomb_pic = pygame.image.load("Assignment11/assets/img/bomb.png")
        self.dsply.blit(bomb_pic, (self.x, self.y))
     