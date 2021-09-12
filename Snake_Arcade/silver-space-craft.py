import arcade
import random
import time


class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/animated_characters/zombie/zombie_fall.png")
        self.speed = 4
        self.center_x = w
        self.center_y = random.randint(0, h)
        self.angle = 0
        self.width = 48
        self.height = 48


    def move(self):
        self.center_x -= self.speed


class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.speed = 5
        self.center_x = host.center_x
        self.center_y = host.center_y

    def move(self):
        self.center_x += self.speed


class SpaceCraft(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.width = 48
        self.height = 48
        self.speed = 5
        self.center_x = 10
        self.center_y = h // 2
        self.change_x = 0
        self.change_y = 0
        self.bullet_list = []

    def move(self):
        self.center_y += self.speed * self.change_y


    def fire(self):
        self.bullet_list.append(Bullet(self))

    

class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 400
        super().__init__(width=self.w, height=self.h, title="Space Craft")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture("/Users/maryamboneh/Documents/hale tamrin/first_game/bg2.png")
        self.me = SpaceCraft(self.w, self.h)
        self.enemy_list = []
        self.start_time = time.time()


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image)
        self.me.draw()
        
        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].draw()

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()


    def on_update(self, delta_time):
        self.end_time = time.time()
        if self.end_time - self.start_time > 5:
            self.enemy_list.append(Enemy(self.w, self.h))
            self.start_time = time.time()
        
        self.me.move()

        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].move()
        
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()


    def on_key_release(self, key, modifiers):
            self.me.change_y = 0


    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:
            self.me.fire()

        if key == arcade.key.UP:
            self.me.change_y = 1

        elif key == arcade.key.DOWN:
            self.me.change_y = -1
            

game = Game()
arcade.run()
