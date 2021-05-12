import pygame
import random
pygame.init()


class Color:
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    dark_green = (0, 102, 0)


class Rocket:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.w = 10
        self.h = 50
        self.color = color
        self.speed = 13
        self.score = 0
        self.area = pygame.draw.rect(Game.dsply, self.color, [self.x, self.y, self.w, self.h])

    def show(self):
        self.area = pygame.draw.rect(Game.dsply, self.color, [self.x, self.y, self.w, self.h])

    def move(self, b):
        if self.y < b.y:
            self.y += self.speed
        elif self.y > b.y:
            self.y -= self.speed

        if self.y < 0:
            self.y = 0
        if self.y > Game.height - self.h:
            self.y = Game.height - self.h

        if b.y_direction == -1:
            self.y -= self.speed
        elif b.y_direction == 1:
            self.y += self.speed


class Ball:
    def __init__(self , xd, yd):
        self.r = 10
        self.x = Game.width / 2
        self.y = Game.height / 2
        self.color = Color.yellow
        self.x_direction = xd
        self.y_direction = yd
        self.speed = 10
        self.area = pygame.draw.circle(Game.dsply, self.color, [self.x, self.y], self.r)

    def show(self):
        self.area = pygame.draw.circle(Game.dsply, self.color, [self.x, self.y], self.r)

    def move(self):
        self.x += self.speed * self.x_direction
        self.y += self.speed * self.y_direction

        if self.y > Game.height or self.y < 0:
            self.y_direction *= -1


class Game:
    width = 700
    height = 400
    dsply = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Ping Pong')
    clock = pygame.time.Clock()
    fps = 30
    font = pygame.font.Font('Assignment13/Ping-Pong/assets/font/atari_full.ttf', 46)

    @staticmethod
    def play():
        me = Rocket(20, Game.height/2, Color.red)
        pc = Rocket(Game.width - 30, Game.height/2, Color.blue)
        ball = Ball(random.choice([1, -1]), random.choice([1, -1]))
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEMOTION:
                    me.y = pygame.mouse.get_pos()[1]
                    if me.y < 5:
                        me.y = 5
                    if me.y > Game.height - me.h - 5:
                        me.y = Game.height - me.h - 5

            ball.move()

            if ball.x < 0:
                pc.score += 1
                ball = Ball(random.choice([1, -1]), random.choice([1, -1]))
            elif ball.x > Game.width:
                me.score += 1
                ball = Ball(random.choice([1, -1]), random.choice([1, -1]))

            if me.area.colliderect(ball.area):
                ball.x += 20
                ball.x_direction *= -1

            if pc.area.colliderect(ball.area):
                ball.x -= 20
                ball.x_direction *= -1

            Game.dsply.fill(Color.dark_green)
            pygame.draw.rect(Game.dsply, Color.white, [0, 0, Game.width, Game.height], 10)
            pygame.draw.aaline(Game.dsply, Color.white, [Game.width/2, 0], [Game.width/2, Game.height])

            if ball.x > Game.width / 2:
                pc.move(ball)
                
            me.show()
            pc.show()
            ball.show()

            bullet_text = Game.font.render(f' {me.score}     {pc.score}', True, (255, 255, 255))
            bullet_textRect = bullet_text.get_rect()
            bullet_textRect.center = (Game.width / 2, 100)
            
            Game.dsply.blit(bullet_text, bullet_textRect)

            pygame.display.update()
            Game.clock.tick(Game.fps)


if __name__ == "__main__":
    game = Game()
    game.play()
