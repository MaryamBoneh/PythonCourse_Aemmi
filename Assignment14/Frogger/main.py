import pygame
import random

pygame.init()


class Color:
    yellow = (255, 255, 0)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)


class Object:
    def __init__(self):
        self.direction = random.choice(["rtl", "ltr"])
        self.speed = 5

    def show(self):
        if self.direction == 'ltr':
            Game.dsply.blit(self.image, (self.x, self.y))
        else:
            Game.dsply.blit(pygame.transform.flip(
                self.image, True, False), (self.x, self.y))

    def move(self):
        if self.direction == 'ltr':
            self.x += self.speed
        else:
            self.x -= self.speed


class Wood(Object):
    def __init__(self):
        super().__init__()
        if self.direction == 'ltr':
            self.x = - 50
            self.y = random.choice([80, 180, 280])
        else:
            self.x = Game.width + 50
            self.y = random.choice([130, 230])
        self.image = pygame.image.load('Assignment14/Frogger/assets/img/wood.png')


class Car(Object):
    cars_pic = ['car1.png', 'car2.png', 'car3.png', 'car4.png']

    def __init__(self):
        super().__init__()
        if self.direction == 'ltr':
            self.x = - 50
            self.y = random.choice([400, 500, 600])
        else:
            self.x = Game.width + 50
            self.y = random.choice([450, 550])
        self.selected_car = 'Assignment14/Frogger/assets/img/' + random.choice(Car.cars_pic)
        self.image = pygame.image.load(self.selected_car)


class Frog:
    def __init__(self):
        self.x = Game.width / 2 - 50
        self.y = Game.height - 60
        self.image = pygame.image.load("Assignment14/Frogger/assets/img/frog.png")
        self.speed = 50
        self.area = Game.dsply.blit(self.image, (self.x, self.y))
        self.moving = ''

    def show(self):
        self.area = Game.dsply.blit(self.image, (self.x, self.y))

    def move(self):
        if self.moving == 'ltr':
            self.x += 5
        elif self.moving == 'rtl':
            self.x -= 5


class Game:
    width = 600
    height = 712
    dsply = pygame.display.set_mode((width, height))
    fps = 30
    score = 0
    frog_count = 5
    bg = pygame.image.load('Assignment14/Frogger/assets/img/background.png')
    clock = pygame.time.Clock()
    font = pygame.font.Font('Assignment14/Frogger/assets/font/atari_full.ttf', 32)
    font2 = pygame.font.Font('Assignment14/Frogger/assets/font/atari_full.ttf', 18)
    is_gameOver = False
    destenations = [[20, 50], [140, 170], [260, 290], [380, 410], [500, 530]]

    @staticmethod
    def play():
        Game.is_gameOver = False
        frogs = [Frog()]
        cars = []
        woods = []

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        frogs[-1].x -= 50
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        frogs[-1].x += 50
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        frogs[-1].y -= 50
                        if frogs[-1].y == 302:
                            frogs[-1].y -= 20
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        frogs[-1].y += 50
                        if frogs[-1].y == 332:
                            frogs[-1].y += 20
                    frogs[-1].moving = ''

            if random.random() < 0.02:
                cars.append(Car())
            if random.random() < 0.025:
                woods.append(Wood())

            for car in cars:
                car.move()

            for wood in woods:
                wood.move()
                
            Game.dsply.blit(Game.bg, (0, 0))

            for car in cars:
                car.show()

            for wood in woods:
                wood.show()

            for frog in frogs:
                frog.show()

            if frogs[-1].moving == 'rtl' or 'ltr':
                frogs[-1].move()

            if frogs[-1].y > 400:
                for car in cars:
                    if frogs[-1].area.colliderect(pygame.Rect(car.x, car.y, 100, 51)):
                        Game.is_gameOver = True

            elif frogs[-1].y < 300 and frogs[-1].y > 80:
                if len(woods) >= 1:
                    for wood in woods:
                        if frogs[-1].area.colliderect(pygame.Rect(wood.x, wood.y, 201, 51)):
                            frogs[-1].moving = wood.direction

                    if not any(frogs[-1].area.colliderect(pygame.Rect(wood.x, wood.y, 201, 51)) for wood in woods):
                        Game.is_gameOver = True

                else:
                    if frogs[-1].y >= 282:
                        Game.is_gameOver = True
                        
            elif frogs[-1].y < 80:
                # if any(frogs[-1].x > des[0] or frogs[-1].x < des[1] for des in Game.destenations):
                for des in Game.destenations:
                    if frogs[-1].x >= des[0] and frogs[-1].x < des[1]:
                        print( Game.destenations,'*************',frogs[-1].x,des[0] , des[1])
                        Game.destenations.remove(des)
                        frogs.append(Frog())
                        Game.frog_count -= 1
                        break
                else:
                    Game.is_gameOver = True
                    
            if Game.is_gameOver or Game.frog_count == 0:
                if Game.is_gameOver:
                    text1 = Game.font.render('Game Over!', True, Color.red, Color.black)
                    text2 = Game.font2.render('press any key  to continue', True, Color.red, Color.black)

                if Game.frog_count == 0:
                    text1 = Game.font.render('You Win!', True, Color.green, Color.yellow)
                    text2 = Game.font2.render('press any key  to continue', True, Color.green, Color.yellow)
                    
                textRect1 = text1.get_rect()
                textRect1.center = (Game.width / 2, Game.height / 2)
                textRect2 = text2.get_rect()
                textRect2.center = (Game.width / 2, Game.height / 2 + 50)
                Game.frog_count = 5
                    
                while True:
                    Game.dsply.blit(text1, textRect1)
                    Game.dsply.blit(text2, textRect2)
                    frogs[-1].show()
                    pygame.display.update()
                    Game.clock.tick(Game.fps)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                        elif event.type == pygame.KEYDOWN:
                            Game.play()
                
            pygame.display.update()
            Game.clock.tick(30)


if __name__ == "__main__":
    pygame.display.set_caption('Frogger')
    Game.play()
