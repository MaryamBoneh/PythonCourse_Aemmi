
import pygame
import random

class Bird:
    def __init__(self):
        self.direction = random.choice(["rtl","ltr"])
        self.fps = 30
        self.speed = 3

    def move(self):
        if self.direction == 'ltr':
            self.x += self.speed
        else:
            self.x -= self.speed


class Duck(Bird):
    def __init__(self, game, speed):
        super().__init__()
        self.game = game
        self.speed = speed
        if self.direction == 'ltr':
            self.x = -50
        else:
            self.x = game.width + 50
        self.y = random.randint(505, 530)
        self.image = pygame.image.load("Assignment12/assets/img/duck.png")
    
    
    def show(self):
        if self.direction == 'ltr':
            self.game.dsply.blit(self.image, (self.x, self.y))
        else:
            self.game.dsply.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            
            
class Stork(Bird):
    def __init__(self, game, speed):
        super().__init__()
        self.game = game
        self.speed = speed
        if self.direction == 'ltr':
            self.x = -50
        else:
            self.x = game.width + 50
        self.y = random.randint(40,440)
        self.image = pygame.image.load("Assignment12/assets/img/stork.png")
        
        
    def show(self):
        if self.direction == 'ltr':
            self.game.dsply.blit(self.image, (self.x, self.y))
        else:
            self.game.dsply.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))


class Donkey:
    def __init__(self, game):
        self.game = game
        self.x = -50
        self.y = 100
        self.speed = 13
        self.image = pygame.image.load("Assignment12/assets/img/donkey1.png")
        
    def show(self):
        self.game.dsply.blit(self.image, (self.x, self.y))
        self.x += self.speed