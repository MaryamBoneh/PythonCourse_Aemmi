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
        self.y_move = False
        self.x_change = 0
        self.y_change = 0
        self.grow_dir = ''
        self.body = []


    def show(self):
        head = [self.x, self.y]
        self.body.append(head)
        pygame.draw.circle(self.dsply, self.color, [self.x, self.y], 10)
        
        if self.score < len(self.body):
            del self.body[0]
            
        for i in range(len(self.body)):
            if i % 2 == 0:
                pygame.draw.circle(self.dsply, self.color, [self.body[i][0] , self.body[i][1]], 10)
            else:
                pygame.draw.circle(self.dsply, self.color2, [self.body[i][0] , self.body[i][1]], 10)
            
        
    def move(self):
        if self.grow_dir == 'l':
            self.x -= self.speed
            
        elif self.grow_dir == 'r':
            self.x += self.speed

        elif self.grow_dir == 'u':
            self.y -= self.speed

        elif self.grow_dir == 'd':
            self.y += self.speed


    def eat(self, apple_x, apple_y, r):
        if apple_x - r <= self.x <= apple_x + (1.5 * r) and apple_y - r <= self.y <= apple_y + (1.5 * r):
            self.score += 1
            return True  