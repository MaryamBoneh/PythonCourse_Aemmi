import pygame

class Gun:
    def __init__(self, game):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("Assignment12/assets/img/shooter.png")
        self.sound = pygame.mixer.Sound("Assignment12/assets/sound/shotgun.wav")
        self.bullet = 5
        self.game = game

    def show(self):
        self.game.dsply.blit(self.image, (self.x, self.y))

    def fire(self, birds, donkeys):
        self.sound.play()
        self.bullet -= 1
        for bird in birds:
            if pygame.Rect(self.x, self.y, 56, 56).colliderect(pygame.Rect(bird.x, bird.y, 56, 56)):
                birds.remove(bird)
                self.bullet += 2
                return True
            
        for donkey in donkeys:
            if pygame.Rect(self.x, self.y, 80, 130).colliderect(pygame.Rect(donkey.x, donkey.y, 80, 130)):
                donkeys.remove(donkey)
                self.bullet += 10
                return True
            
        return False