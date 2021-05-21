import pygame


class Snake():
    def __init__(self, display):
        self.dsply = display
        self.w = 16
        self.h = 16
        self.x = 350
        self.y = 300
        self.color = (250, 228, 0)
        self.color2 = (230, 180, 0)
        self.name = 'joojoo'
        self.score = 0
        self.speed = 5
        self.x_move = False
        self.x_change = 0
        self.y_change = 0
        self.direction = ''
        self.body = []

    def show(self):
        head = [self.x, self.y]
        self.body.append(head)
        pygame.draw.circle(self.dsply, self.color, [self.x, self.y], 10)

        if self.score < len(self.body):
            del self.body[0]

        for i in range(len(self.body)):
            if i % 2 == 0:
                pygame.draw.circle(self.dsply, self.color, [self.body[i][0], self.body[i][1]], 10)
            else:
                pygame.draw.circle(self.dsply, self.color2, [self.body[i][0], self.body[i][1]], 10)

    def move(self):
        if self.direction == 'l':
            self.x -= self.speed

        elif self.direction == 'r':
            self.x += self.speed

        elif self.direction == 'u':
            self.y -= self.speed

        elif self.direction == 'd':
            self.y += self.speed

    def Collision(self):
        print(self.direction)
        for i in range(1, len(self.body)):
            if self.direction == 'd':
                if self.y+10 <= self.body[i][1] and self.x == self.body[i][0]:
                    print('Collision1', self.x, self.y)
                    print('body: ', self.body)
                    self.direction = 'l'

            elif self.direction == 'l':
                if self.x-10 >= self.body[i][0] and self.y == self.body[i][1]:
                    print('Collision2', self.x, self.y)
                    print('body: ', self.body)
                    self.direction = 'u'

            elif self.direction == 'u':
                if self.y-10 >= self.body[i][1] and self.x == self.body[i][0]:
                    print('Collision3', self.x, self.y)
                    print('body: ', self.body)
                    self.direction = 'r'
            else:
                if self.x+10 <= self.body[i][0] and self.y == self.body[i][1]:
                    print('Collision4', self.x, self.y)
                    print('body: ', self.body)
                    self.direction = 'd'
        self.move()

    def eat(self, apple_x, apple_y, r):
        if pygame.Rect(self.x, self.y, 16, 16).colliderect(pygame.Rect(apple_x, apple_y, 16, 16)):
            self.score += 1
            return True
