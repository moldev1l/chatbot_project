import arcade
import random



SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Racing"

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("bg.png")
        self.car = Car("blue_car.png", 0.8)
        self.enemy = Enemy("yellow_car.png", 0.8)
    def setup(self):
        self.car.center_x = SCREEN_WIDTH/2
        self.car.center_y = 100

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.car.draw()


    def update(self, delta_time):
        self.car.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.car.change_x = -5
            self.car.angle = 20

        if key == arcade.key.D:
            self.car.change_x = 5
            self.car.angle = -20

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.car.change_x = 0
            self.car.angle = 0




class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x


class Enemy(arcade.Sprite):
    pass


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
