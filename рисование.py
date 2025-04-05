import time
import tkinter as tk
import random

colors = ["green", "yellow", "red", "purple", "orange", "blue", "black"]
stop = False

window = tk.Tk()
window.geometry("650x500")
window.title("Фигуры")

canvas = tk.Canvas(window, bg="White", width=500, height=500)
canvas.place(x=0, y=0)

def draw_circle():
    color = random.choice(colors)
    d = random.randint(1, 100)
    x = random.randint(0, 500-d)
    y = random.randint(0, 500-d)
    canvas.create_oval(x, y, x+d, y+d, fill=color)

def draw_oval():
    color = random.choice(colors)
    d = random.randint(1, 100)
    d2 = random.randint(1, 100)
    x = random.randint(0, 500 - d)
    y = random.randint(0, 500 - d)
    canvas.create_oval(x, y, x+d, y+d2, fill=color)

def draw_square():
    color = random.choice(colors)
    border_color = random.choice(colors)
    d = random.randint(1, 100)
    x = random.randint(1, 500)
    y = random.randint(1, 500)
    canvas.create_rectangle(x, y, x+d, y+d, fill=color, outline=border_color)

def infinite_square():
    while True:
        draw_square()
        window.update()
        global  stop
        if stop:
            stop = False
            break

def infinite_circle():
    while True:
        draw_circle()
        window.update()
        global  stop
        if stop:
            stop = False
            break

def animate_circle():
    color = random.choice(colors)
    d = random.randint(1, 100)
    x = random.randint(0, 500 - d)
    y = random.randint(0, 500 - d)
    canvas.create_oval(x, y, x + d, y + d, fill=color)
    circle = canvas.create_oval(x, y, x + d, y + d, fill=color)
    dx = 2
    dy = 2
    while True:
        coords = canvas.coords(circle)
        print(coords)
        left = coords[0]
        top = coords[1]
        right = coords[2]
        bottom = coords[3]
        if left <= 0 or right >=500:
            dx = -dx
        if top <= 0 or bottom >= 500:
            dy = -dy
        canvas.move(circle, dx, dy)
        time.sleep(0.01)
        window.update()



def stop_draw():
    global stop
    stop = True

infinite_button2 = tk.Button(window, width=17, text="Бесконечные кружки", command=infinite_circle)
infinite_button2.place(x=510, y=420)

animate_button = tk.Button(window, width=17, text="Анимированный круг", command=animate_circle)
animate_button.place(x=510, y=350)

stop_button = tk.Button(window, width=17, text="Остановить рисование", command=stop_draw)
stop_button.place(x=510, y=280)


infinite_button1 = tk.Button(window, width=17, text="Бесконечные квадраты", command=infinite_square)
infinite_button1.place(x=510, y=220)


oval_button = tk.Button(window, width=17, text="Нарисовать овал", command=draw_oval)
oval_button.place(x=510, y=90)


circle_button = tk.Button(window, width=17, text="Нарисовать круг", command=draw_circle)
circle_button.place(x=510, y=20)

square_button = tk.Button(window, width=17, text="Нарисовать квадрат", command=draw_square)
square_button.place(x=510, y=150)




window.mainloop()


# cделать функцию бесконечных кругов, тоже с остановкой.