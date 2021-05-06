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
        self.speed = 3
        self.x_change = 0
        self.y_change = 0
        self.grow_dir = ''


    def show(self):
        pygame.draw.rect(self.dsply, self.color, [self.x, self.y, self.w, self.h])
        
        if self.grow_dir == 'l':
            for i in range(self.score + 1):
                if i % 2 == 0:
                    pygame.draw.rect(self.dsply, self.color, [self.x + (i*16), self.y, self.w, self.h])
                else:
                    pygame.draw.rect(self.dsply, self.color2, [self.x + (i*16), self.y , self.w, self.h])
        elif self.grow_dir == 'r':
            for i in range(self.score + 1):
                if i % 2 == 0:
                    pygame.draw.rect(self.dsply, self.color, [self.x - (i*16), self.y, self.w, self.h])
                else:
                    pygame.draw.rect(self.dsply, self.color2, [self.x - (i*16), self.y , self.w, self.h])
        elif self.grow_dir == 'u':
            for i in range(self.score + 1):
                if i % 2 == 0:
                    pygame.draw.rect(self.dsply, self.color, [self.x , self.y + (i*16), self.w, self.h])
                else:
                    pygame.draw.rect(self.dsply, self.color2, [self.x , self.y + (i*16) , self.w, self.h])
        elif self.grow_dir == 'd':
            for i in range(self.score + 1):
                if i % 2 == 0:
                    pygame.draw.rect(self.dsply, self.color, [self.x , self.y - (i*16), self.w, self.h])
                else:
                    pygame.draw.rect(self.dsply, self.color2, [self.x , self.y - (i*16), self.w, self.h])

    def move(self):
        if self.grow_dir == 'l':
            self.x -= self.speed
            
        elif self.grow_dir == 'r':
            self.x += self.speed

        elif self.grow_dir == 'u':
            self.y -= self.speed

        elif self.grow_dir == 'd':
            self.y += self.speed

        # chack if the wall tuched, game over
        if self.x <= 50 or self.x >= 634 or self.y <= 50 or self.y >= 534:
            self.game_over()

        # change speed
        if self.score > 50:
            self.speed = 6
        elif self.score > 25:
            self.speed = 5
        elif self.score > 10:
            self.speed = 4


    def eat(self, apple_x, apple_y, pear_x, pear_y, bomb_x, bomb_y, r):
        if apple_x - r <= self.x <= apple_x + r and apple_y - r <= self.y <= apple_y + r:
            self.score += 1
            return 'apple'        
        if pear_x - r <= self.x <= pear_x + r and pear_y - r <= self.y <= pear_y + r:
            self.score += 2
            return 'pear'
        if bomb_x - r <= self.x <= bomb_x + r and bomb_y - r <= self.y <= bomb_y + r:
            self.score -= 1
            return 'bomb'
        
        
    def game_over(self):
        self.speed = 0
        font_go = pygame.font.Font('Assignment11/assets/font/arial.ttf', 46)
        text_go = font_go.render('Game Over!', True, (255, 255, 255), (0, 0, 0))
        textRect_go = text_go.get_rect()
        textRect_go.center = (300, 300)
        self.dsply.blit(text_go, textRect_go)        
                