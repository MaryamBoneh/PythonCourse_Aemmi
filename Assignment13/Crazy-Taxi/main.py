import pygame
import random
pygame.init()


class Color:
    black = (0, 0, 0)
    red = (255, 0, 0)


class Taxi:
    def __init__(self):
        self.x = Game.width / 2 - 25
        self.y = Game.height - 105
        self.speed = 5
        self.dir = ''
        self.image = pygame.image.load('Assignment13/Crazy-Taxi/assets/img/taxi.png')
        self.area = Game.dsply.blit(self.image, (self.x, self.y))
        
    def show(self):
        self.area = Game.dsply.blit(self.image, (self.x, self.y))
        
    def move(self):
        if self.dir == 'l':
            self.x -= self.speed
            
        elif self.dir == 'r':
            self.x += self.speed
            
        elif self.dir == 't':
            self.x = self.x
          
            
class Car:
    cars_pic=['car1.png', 'car2.png', 'car3.png', 'car4.png', 'car5.png', 'car6.png']
    speed = 5
    def __init__(self):
        self.x = random.randint(0, Game.width - 50)
        self.y = -50
        self.selected_car = 'Assignment13/Crazy-Taxi/assets/img/'+ random.choice(Car.cars_pic)
        self.image = pygame.image.load(self.selected_car)
        self.area = Game.dsply.blit(self.image, (self.x, self.y))
        
    def show(self):
        self.area = Game.dsply.blit(self.image, (self.x, self.y))
        self.y += Car.speed

        
class Game:
    width = 400
    height = 661
    fps = 30
    clock = pygame.time.Clock()
    dsply = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Crazy Taxi')
    bg = pygame.image.load("Assignment13/Crazy-Taxi/assets/img/asphalt-road.jpg")
    bgY1 = 0
    bgY2 = width
    movingUpSpeed = 10
    font_go = pygame.font.Font('Assignment13/Crazy-Taxi/assets/font/atari_full.ttf', 32)
    font_pak = pygame.font.Font('Assignment13/Crazy-Taxi/assets/font/atari_full.ttf', 12)

    def update(self):
        Game.bgY1 -= Game.movingUpSpeed
        Game.bgY2 -= Game.movingUpSpeed
        if Game.bgY1 <= -Game.width:
            Game.bgY1 = Game.width
        if Game.bgY2 <= -Game.width:
            Game.bgY2 = Game.width
            
    def render(self):
        Game.dsply.blit(Game.bg, (0, Game.bgY1))
        Game.dsply.blit(Game.bg, (0, Game.bgY2))
        
    @staticmethod
    def play():
        cars = []
        taxi = Taxi()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        taxi.dir = 'l'

                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        taxi.dir = 'r'

                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        taxi.dir = 't'

            Game.dsply.blit(Game.bg, (0, 0))
            Game.update(Game)
            Game.render(Game)

            if random.random() < 0.01:
                cars.append(Car())
                
            for car in cars:
                car.show()
                
            for car in cars:
                if taxi.area.colliderect(car.area):
                    text_go = Game.font_go.render('Game Over!', True, Color.red, Color.black)
                    textRect_go = text_go.get_rect()
                    textRect_go.center = (Game.width / 2, Game.height / 2)
                    text_pak = Game.font_pak.render('press any key  to continue', True, Color.red, Color.black)
                    textRect_pak = text_pak.get_rect()
                    textRect_pak.center = (Game.width / 2, Game.height / 2 + 50)
                    while True:
                        Game.dsply.blit(text_go, textRect_go) 
                        Game.dsply.blit(text_pak, textRect_pak) 
                        taxi.show()
                        pygame.display.update()
                        Game.clock.tick(Game.fps)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                            elif event.type == pygame.KEYDOWN:
                                Game.play()
            Car.speed += 0.005   
            taxi.show()
            taxi.move()
            pygame.display.update()
            Game.clock.tick(Game.fps)

if __name__ == "__main__":
    Game.play()