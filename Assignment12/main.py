import pygame
import random
import time
from Gun import Gun
from Cloud import Cloud
from Animal import Stork, Duck, Donkey, Bird

pygame.init()

class Game:
    def __init__(self):
        self.width = 1073
        self.height = 665
        self.dsply = pygame.display.set_mode((self.width, self.height))
        self.fps = 30
        self.score = 0
        self.bg = pygame.image.load("Assignment12/assets/img/background.jpg")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Assignment12/assets/font/ALGER.ttf', 26)
        self.start_now = time.time()
        self.new_speed = Bird().speed


    def play(self):
        pygame.mouse.set_visible(False)
        my_gun = Gun(game)
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
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if my_gun.fire(birds, donkeys):
                        self.score += 1
                    if my_gun.bullet == 0:
                        self.game_over()

            random_number = random.random()
            if random_number < 0.02:
                birds.append(Duck(game, self.new_speed))
            elif random_number < 0.04:
                birds.append(Stork(game, self.new_speed))
            if random_number < 0.004:
                clouds.append(Cloud(game))
            if random_number < 0.002:
                donkeys.append(Donkey(game))

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
                    
                    
            score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            textRect = score_text.get_rect()
            textRect.center = (self.width // 2, self.height - 40)
            
            bullet_text = self.font.render(f'Bullets: {my_gun.bullet}', True, (255, 255, 255))
            bullet_textRect = bullet_text.get_rect()
            bullet_textRect.center = (100, self.height - 40)
            
            self.dsply.blit(bullet_text, bullet_textRect)
            self.dsply.blit(score_text, textRect)

            pygame.display.update()
            self.clock.tick(30)
            
                
    def game_over(self):
        print('game over')
        text = self.font.render('Game Over!', True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.width // 3, self.height // 2)
        self.dsply.blit(text, textRect)        
                


if __name__ == "__main__":
    pygame.display.set_caption('Birds Shot')
    game = Game()
    game.play()
