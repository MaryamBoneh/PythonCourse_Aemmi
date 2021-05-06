import pygame
from Objects import Apple, Pear, Bomb
from Snake import Snake

pygame.init()

if __name__ == "__main__":
    width = 700
    height = 600

    dsply = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Super Snake') 
    bg = pygame.image.load("Assignment11/assets/img/background.png")
    clock = pygame.time.Clock()
    
    snake = Snake(dsply)
    apple = Apple(dsply)
    pear = Pear(dsply)
    bomb = Bomb(dsply)
    
    # Show Score Text
    font = pygame.font.Font('Assignment11/assets/font/ALGER.ttf', 32)
    text = font.render('Score: 0', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (width // 2, 30)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    snake.grow_dir= 'l'
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    snake.grow_dir = 'r'
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    snake.grow_dir = 'u'
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    snake.grow_dir = 'd'

        result = snake.eat(apple.x, apple.y, pear.x, pear.y, bomb.x, bomb.y, apple.r)
        if result == 'apple':
            apple = Apple(dsply)
            text = font.render(f'Score: {snake.score}', True, (255, 255, 255))
        elif result == 'pear':   
            pear = Pear(dsply)
            text = font.render(f'Score: {snake.score}', True, (255, 255, 255))
        elif result == 'bomb':   
            bomb = Bomb(dsply)
            text = font.render(f'Score: {snake.score}', True, (255, 255, 255))
        
        dsply.blit(bg, (0, 0))
        dsply.blit(text, textRect)
        snake.move()
        apple.show()
        snake.show()
        bomb.show()
        pear.show()
        pygame.display.update()
        clock.tick(30)

        if snake.score < 0:
            snake.game_over()
    