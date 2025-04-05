import arcade
import random


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong"
SPEED_X = 5
SPEED_Y = 5

class Bar(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0

class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = -self.change_x

        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y = -self.change_y






class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball("ball.png", 0.1)
        self.bar = Bar("bar.png", 0.1)
        self.setup()
        self.score = 0
        self.attempts = 2
        self.game = True
        self.ball_hit_bar = False




    def setup(self):
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT/2
        direction = random.randint(1, 2)
        if direction == 1:
            self.ball.change_x = SPEED_X
        else:
            self.ball.change_x = -SPEED_X
        self.ball.change_y = SPEED_Y
        self.bar.center_y = SCREEN_HEIGHT/6
        self.bar.center_x = SCREEN_WIDTH/2
        self.bar.change_x = SPEED_X


    def update(self, delta_time):
        self.ball.update()
        self.bar.update()
        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.bottom = self.bar.top
            self.ball.change_y = -self.ball.change_y
            self.score += 1
            self.ball_hit_bar = True
            self.ball.change_x *= 1.1
            self.ball.change_y *= 1.1
        if self.ball.bottom < 0:
            self.attempts -= 1
            self.setup()
        if self.attempts == 0:
            self.game = False
        if not self.game:
            self.ball.stop()
            self.bar.stop()



    def on_draw(self):
        self.clear((8, 3, 97))
        self.ball.draw()
        self.bar.draw()
        arcade.draw_text(f"Score:{self.score}", 10, SCREEN_HEIGHT-30, (0, 0, 0), 20)
        arcade.draw_text(f"Attempts:{self.attempts}", SCREEN_WIDTH-160, SCREEN_HEIGHT-30, (0, 0, 0), 20)
        if self.attempts == 0:
            arcade.draw_text("Ты проиграл", 0, SCREEN_HEIGHT / 2, (255, 33, 33), 50, SCREEN_WIDTH, "center")
        if self.score == 10:
            arcade.draw_text("Ты победил", 0, SCREEN_HEIGHT / 2, (255, 33, 33), 50, SCREEN_WIDTH, "center")
            self.game = False



    def on_key_press(self, key, modifiers):
        if self.game:
            if key == arcade.key.A:
                self.bar.change_x = -SPEED_X

            if key == arcade.key.D:
                self.bar.change_x = SPEED_X

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.bar.change_x = 0

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


arcade.run()


