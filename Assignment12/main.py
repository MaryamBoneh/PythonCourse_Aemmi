import pygame
import random
import time 

pygame.init()


class Bird:
    def __init__(self):
        self.direction = random.choice(["rtl","ltr"])
        self.fps = 30
        # self.sound = pygame.mixer.Sound("Assignment12/assets/sound/صدا برای پرنده")
        self.speed = 5
        pygame.display.set_caption('Birds Shot')

    

    def move(self):
        if self.direction == 'ltr':
            self.x += self.speed
        else:
            self.x -= self.speed

class Duck(Bird):
    def __init__(self):
        super().__init__()
        if self.direction == 'ltr':
            self.x = -50
        else:
            self.x = game.width + 50
        self.y = random.randint(505, 530)
        self.image = pygame.image.load("Assignment12/assets/img/duck.png")
    
    
    def show(self):
        if self.direction == 'ltr':
            game.dsply.blit(self.image, (self.x, self.y))
        else:
            game.dsply.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            
            
class Stork(Bird):
    def __init__(self):
        super().__init__()
        if self.direction == 'ltr':
            self.x = -50
        else:
            self.x = game.width + 50
        self.y = random.randint(40,440)
        self.image = pygame.image.load("Assignment12/assets/img/stork.png")
        
        
    def show(self):
        if self.direction == 'ltr':
            game.dsply.blit(self.image, (self.x, self.y))
        else:
            game.dsply.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            
            
class Cloud:
    def __init__(self):
        self.x = random.randint(0, game.width)
        self.y = -50
        self.speed = 1
        self.image = pygame.image.load("Assignment12/assets/img/cloud.png")
        print('cloud=============')
        
    def show(self):
        game.dsply.blit(self.image, (self.x, self.y))
        self.y += self.speed
            
        
class Donkey:
    def __init__(self):
        self.x = -50
        self.y = 100
        self.speed = 10
        self.image = pygame.image.load("Assignment12/assets/img/donkey1.png")
        print('*****donkey******')
        
    def show(self):
        game.dsply.blit(self.image, (self.x, self.y))
        self.x += self.speed
            
        
        
            
class Gun:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("Assignment12/assets/img/shooter.png")
        self.sound = pygame.mixer.Sound("Assignment12/assets/sound/shotgun.wav")
        self.score = 0
        self.bullet = 20

    def show(self):
        game.dsply.blit(self.image, (self.x, self.y))

    def fire(self):
        self.sound.play()


class Game:
    def __init__(self):
        self.width = 1073
        self.height = 665
        self.dsply = pygame.display.set_mode((self.width, self.height))
        self.fps = 30
        self.bg = pygame.image.load("Assignment12/assets/img/background.jpg")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Assignment12/assets/font/ALGER.ttf', 26)
   

    def play(self):
        pygame.mouse.set_visible(False)
        my_gun = Gun()
        birds = []
        clouds = []
        donkeys = []

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    my_gun.x = pygame.mouse.get_pos()[0]
                    my_gun.y = pygame.mouse.get_pos()[1]

            random_number = random.random()
            if random_number < 0.02:
                birds.append(Duck())
            elif random_number < 0.04:
                birds.append(Stork())
            if random_number < 0.004:
                clouds.append(Cloud())
            if random_number < 0.002:
                donkeys.append(Donkey())
                
            for bird in birds:
                bird.move()

            self.dsply.blit(self.bg, (0, 0))
            my_gun.show()

            for bird in birds:
                bird.show()
                
            for donkey in donkeys:
                donkey.show()
                
            for cloud in clouds:
                cloud.show()
                if cloud.y == 250:
                    clouds.remove(cloud)
            score_text = self.font.render(f'Score: {my_gun.score}', True, (255, 255, 255))
            textRect = score_text.get_rect()
            textRect.center = (self.width // 2, self.height - 40)
            bullet_text = self.font.render(f'Bullets: {my_gun.bullet}', True, (255, 255, 255))
            bullet_textRect = bullet_text.get_rect()
            bullet_textRect.center = (100 , self.height - 40)
            self.dsply.blit(bullet_text, bullet_textRect)
            self.dsply.blit(score_text, textRect)

            pygame.display.update()
            self.clock.tick(30)


if __name__ == "__main__":
    pygame.display.set_caption('Birds Shot')
    game = Game()
    game.play()
