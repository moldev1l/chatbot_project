import turtle

t = turtle.Turtle()
t.speed(10)
t.shape("turtle")



def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()
# def up():
#     t.setheading(90)
#     t.forward(10)
#
# up()

def semicircle(color, lenght, position):
    t.setheading(90)
    t.color(color)
    move(position, 0)
    for i in range(30):
        t.forward(lenght)
        t.left(6)


# def rainbow_semicircle(x, y, color):
#     t.color(color)
#     t.width(10)
#     move(x, y)


def rainbow():
    t.width(10)
    semicircle("red", 10, 120)
    semicircle("orange", 9.5, 110)
    semicircle("yellow", 9, 100)
    semicircle("green", 8.5, 90)
    semicircle("blue", 8, 80)
    semicircle("lightblue", 7.5, 70)
    semicircle("violet", 7, 60)

rainbow()






t.screen.mainloop()