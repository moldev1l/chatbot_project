import tkinter as tk
import tkinter.messagebox as tmb
import random

window = tk.Tk()
window.geometry("400x250")
window.title("Цвет слово")

instructions = tk.Label(window, text="Напиши цвет слова, а не само слово! Жми Enter,чтобы играть", font=("Arial", 10))
instructions.place(x=10, y=10)

color_label = tk.Label(window, text="color", font=("Arial", 50))
color_label.place(x=120, y=80)

entry = tk.Entry(window, font=("Arial", 10))
entry.place(x=120, y=180)
entry.focus_set()

timer = 30
correct_answer = 0
incorrect_answer = 0
score_label = tk.Label(window, text=f"Правильно: {correct_answer}", font=("Arial", 10))
fails_label = tk.Label(window, text=f"Неправильно: {incorrect_answer}", font=("Arial", 10))
time_label = tk.Label(window, text=f"Осталось времени: {timer}")

score_label.place(x=10, y=40)
fails_label.place(x=10, y=60)
time_label.place(x=10, y=210)

colors = ["red", "blue", "yellow", "black", "green", "pink", "orange"]

def time():
    global timer
    if timer > 0:
        timer -= 1
        time_label["text"] = f"Осталось {timer} секунд"
        time_label.after(1000, time)
    else:
        tmb.showinfo("Конец игры", "Время вышло")


def color_word():
    color_label["fg"] = random.choice(colors)
    color_label["text"] = random.choice(colors)

def check(event):
    global correct_answer, incorrect_answer, timer
    if timer > 0:
        user_color = entry.get()
        word_color = color_label["fg"]
        if user_color == word_color:
            print("ДА")
            correct_answer += 1
            score_label["text"] = f"Правильно: {correct_answer}"
        else:
            print("нет")
            incorrect_answer += 1
            fails_label["text"] = f"Неправильно: {incorrect_answer}"
        color_word()
        entry.delete(0, "end")
    else:
        if correct_answer > incorrect_answer:
            tmb.showinfo("Хороший результат", "Ты молодец")
        else:
            tmb.showinfo("Неважный результат", "В следующий раз получится лучше")


window.bind("<Return>", check)
color_word()
time_label.after(1000, time)

# В функции timer: после блока условия if time_left > 0 добавить блок else,
# в котором выводить всплывающее окно из библиотеки tkinter.messagebox - "Конец игры", "Время вышло".
# В функции check: после блока условия if time_left > 0 добавить блок else,
# в котором делаем проверку - если правильных ответов больше неправильных - сделать всплывающее окно - "Хороший результат", "Ты молодец".
# Иначе - "Неважный результат", "В следующий раз получится лучше".












window.mainloop()



