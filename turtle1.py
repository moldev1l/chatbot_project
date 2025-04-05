import turtle

t = turtle.Turtle()
t.speed(10)
t.shape("turtle")
def square():
    for i in range(4):
        t.left(90)
        t.forward(100)

def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()

def pentagon():
    for i in range(5):
        t.left(72)
        t.forward(100)

def polygon(sides):
    for i in range(sides):
        t.left(360/sides)
        t.forward(50)


square()
move(100, 100)
square()
move(150, -150)
pentagon()
move(150, 150)
polygon(10)
move(-150, -150)

for i in range(60):
    polygon(5)
    t.left(6)








t.screen.mainloop()