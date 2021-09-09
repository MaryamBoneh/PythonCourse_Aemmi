import arcade
import random

class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.RED
        self.speed = 4
        self.r = 8
        self.center_x = random.randint(0, w)
        self.center_y = random.randint(0, h)

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)


class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.speed = 4
        self.change_x = 1
        self.change_y = 1
        self.score = 0
        self.body = []
        self.SPRITE_SCALING_PLAYER = 0.5
        self.img = ":resources:images/animated_characters/male_person/malePerson_fall.png"
        self.player = arcade.Sprite(self.img, self.SPRITE_SCALING_PLAYER)
        self.player.center_x = w // 2
        self.player.center_y = h // 2

    def draw(self):
        self.player.draw()

    def move(self):
        self.player.center_x += self.speed * self.change_x
        self.player.center_y += self.speed * self.center_y

    def eat(self):
        self.score += 1


class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 700, 750, 'Super Snake')
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(700, 750)
        self.apple = Apple(700, 750)

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()

    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat()
            self.apple = Apple(700, 750)
            print(self.snake.score)


    def on_key_release(self, key, modifiers):

        if key == 65361:
            self.snake.change_x = -1
            self.snake.change_y = 0
            print('======l======')


        elif key == 65363:
            self.snake.change_x = 1
            self.snake.change_y = 0
            print('======r======')


        elif key == 65362:
            self.snake.change_x = 0
            self.snake.change_y = 1
            print('======t======')


        elif key == 65364:
            self.snake.change_x = 0
            self.snake.change_y = -1
            print('======b======')




game = Game()
arcade.run()