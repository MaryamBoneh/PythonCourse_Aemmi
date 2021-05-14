import pygame
from Apple import Apple
from Snake import Snake

pygame.init()

if __name__ == "__main__":
    width = 700
    height = 600

    dsply = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Super Snake') 
    bg = pygame.image.load("Assignment14/assets/img/background.png")
    clock = pygame.time.Clock()
    
    snake = Snake(dsply)
    apple = Apple(dsply)
    
    # Show Score Text
    font = pygame.font.Font('Assignment14/assets/font/ALGER.ttf', 32)
    text = font.render('Score: 0', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (width // 2, 30)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                    
        print(snake.x, snake.y, '--------', apple.x, apple.y, 'x_move: ',snake.x_move)
        if not snake.x_move:   
            if snake.x < apple.x or snake.x-1 < apple.x or snake.x-2 < apple.x or snake.x-3 < apple.x or snake.x-4 < apple.x :
                snake.grow_dir = 'r'  
                if snake.x == apple.x or snake.x-1 == apple.x or snake.x-2 == apple.x or snake.x-3 == apple.x or snake.x-4 == apple.x:
                    snake.x_move = True
        if not snake.x_move:   
            if snake.x > apple.x or snake.x+1 > apple.x or snake.x+2 > apple.x or snake.x+3 > apple.x or snake.x+4 > apple.x:
                snake.grow_dir = 'l'  
                if snake.x == apple.x or snake.x+1 == apple.x or snake.x+2 == apple.x or snake.x+3 == apple.x or snake.x+4 == apple.x:
                    snake.x_move = True
        if snake.x_move:     
            if snake.y < apple.y:
                snake.grow_dir = 'd'        
            elif snake.y > apple.y:
                snake.grow_dir = 'u'        
                    
        if snake.eat(apple.x, apple.y, apple.r):
            apple = Apple(dsply)
            snake.x_move = False
            print('new apple: ',apple.x, apple.y)
            text = font.render(f'Score: {snake.score}', True, (255, 255, 255))

        dsply.blit(bg, (0, 0))
        dsply.blit(text, textRect)
        snake.move()
        apple.show()
        snake.show()
        pygame.display.update()
        clock.tick(50)

        if snake.score < 0:
            snake.game_over()
    