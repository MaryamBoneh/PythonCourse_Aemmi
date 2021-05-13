import pygame
import random
pygame.init()


class Color:
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    orange = (255, 128, 0)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    ligth_blue = (0, 128, 255)
    green = (0, 255, 0)
    purple = (153, 0, 153)
    pink = (255, 0, 117)


class Cell:
    colors = [Color.purple, Color.blue, Color.ligth_blue, Color.green, Color.yellow, Color.orange, Color.red]
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.w = 35
        self.h = 10
        self.c = c
        # self.color = color
        self.area = pygame.draw.rect(Game.dsply, Cell.colors[c], [self.x, self.y, self.w, self.h])

    def show(self):
        self.area = pygame.draw.rect(Game.dsply, Cell.colors[self.c], [self.x, self.y, self.w, self.h])



class Rocket:
    def __init__(self):
        self.x = Game.width / 2 - 40
        self.y = Game.height - 20
        self.w = 80
        self.h = 10
        self.color = Color.pink
        self.speed = 8
        self.score = 0
        self.dir = 0
        self.count = 3
        self.area = pygame.draw.rect(Game.dsply, self.color, [self.x, self.y, self.w, self.h])

    def show(self):
        self.area = pygame.draw.rect(Game.dsply, self.color, [self.x, self.y, self.w, self.h])

    def move(self):
        if self.dir == 'l':
            self.x -= self.speed
            
        elif self.dir == 'r':
            self.x += self.speed
            

class Ball:
    def __init__(self , xd):
        self.r = 10
        self.x = Game.width / 2
        self.y = Game.height - 30
        self.color = Color.white
        self.x_direction = xd
        self.y_direction = -1
        self.speed = 10
        self.area = pygame.draw.circle(Game.dsply, self.color, [self.x, self.y], self.r)

    def show(self):
        self.area = pygame.draw.circle(Game.dsply, self.color, [self.x, self.y], self.r)

    def move(self):
        self.x += self.speed * self.x_direction
        self.y += self.speed * self.y_direction

        if self.y < 0:
            self.y_direction *= -1

        if self.x < 0 or self.x > Game.width:
            self.x_direction *= -1


class Game:
    width = 800
    height = 400
    dsply = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Break Out')
    clock = pygame.time.Clock()
    fps = 30
    font = pygame.font.Font('Assignment13/Break-Out/assets/font/atari_full.ttf', 12)

    @staticmethod
    def play():
        rocket = Rocket()
        ball = Ball(random.choice([1, -1]))
        cells = []
                
        for i in range(20):
            for j in range(7):
                cells.append(Cell(i*40, j*15, j))
                
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEMOTION:
                    rocket.x = pygame.mouse.get_pos()[0]
                    rocket.dir = ''
                    if rocket.x < 0:
                        rocket.x = 0
                    if rocket.x > Game.width - rocket.w:
                        rocket.x = Game.width - rocket.w
                        
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        rocket.dir = 'l'
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        rocket.dir = 'r'

            ball.move()
            rocket.move()
            
            if ball.y > Game.height:
                rocket.count -= 1
                ball = Ball(random.choice([1, -1]))
                rocket.x = Game.width / 2 - 40
                rocket.y = Game.height - 20

            if rocket.area.colliderect(ball.area):
                ball.y -= 30
                ball.y_direction *= -1

            for cell in cells:
                if ball.area.colliderect(cell.area):
                    cells.remove(cell)
                    rocket.score += 1
                    
            #----ui----
            Game.dsply.fill(Color.black)
            rocket.show()
            ball.show()
            for cell in cells:
                cell.show()
            ball.show()
            
            score_text = Game.font.render(f'Score: {rocket.score}', True, Color.white)
            count_text = Game.font.render(f' Ball: 3/{rocket.count}', True, Color.white)
            count_textRect = count_text.get_rect()
            count_textRect.center = (Game.width - 120, Game.height - 80)
            Game.dsply.blit(count_text, count_textRect)
            score_textRect = score_text.get_rect()
            score_textRect.center = (70, Game.height - 80)
            Game.dsply.blit(score_text,  score_textRect)
            
            pygame.display.update()
            Game.clock.tick(Game.fps)

    
if __name__ == "__main__":
    game = Game()
    game.play()
