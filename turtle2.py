import turtle

t = turtle.Turtle()
t.speed(10)
t.shape("turtle")

def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()

def semicircle():
    for i in range(60):
        t.forward(5)
        t.left(6)

def spiral():
    for i in range(160):
        t.forward(i/10)
        t.left(15)

def pentagon():
    for i in range(5):
        t.left(144)
        t.forward(100)

def olympic_circle(x, y, color):
    t.color(color)
    t.width(10)
    move(x, y)
    circle()

def olympic_logo():
    olympic_circle(-120, 60, "blue")
    olympic_circle(0, 60, "black")
    olympic_circle(120, 60, "red")
    olympic_circle(-60, 0, "yellow")
    olympic_circle(60, 0, "green")

def up():
    t.setheading(90)
    t.forward(10)

def down():
    t.setheading(-90)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

def up_down():
    if t.isdown():
        t.up()
    else:
        t.down()

def red():
    t.color("red")

def blue():
    t.color("blue")

def yellow():
    t.color("yellow")

def green():
    t.color("green")

t.screen.onkeypress(green, "g")
t.screen.onkeypress(yellow, "y")
t.screen.onkeypress(blue, "b")
t.screen.onkeypress(red, "r")
t.screen.onkeypress(up_down, "space")
t.screen.onkeypress(down, "Down")
t.screen.onkeypress(left, "Left")
t.screen.onkeypress(right, "Right")
t.screen.onkeypress(up, "Up")
t.screen.listen()
# olympic_logo()

# circle()
# move(100, 100)
# spiral()
# pentagon()


t.screen.mainloop()

# Написать функции смены цвета линии и присвоить их клавишам букв - например,
# клавиша "b" меняет цвет на голубой ("blue"), клавиша "y" - на желтый ("yellow"),
# "g" - на зеленый("green").
# Сделать функцию отрисовки радуги.
# (Подсказка: дуга - это половина круга, т.е. произведение угла поворота на количество повторов должно быть равно 180.
# Чтобы следующая дуга была меньше предыдущей - уменьшаем длину линии)