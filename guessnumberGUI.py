import tkinter as tk
import random


window = tk.Tk()
window.geometry("200x150")
window.title("Угадай число")
attempts = 10


def guess(event):
    global attempts
    number = entry.get()
    if number == "":
        label["text"] = "Введи число от 1 до 100"
    else:
        if attempts > 0:
            attempts -= 1
            attempts_label["text"] = f"Количество попыток:{attempts}"
            number = int(number)
            if number == random_number:
                label["text"] = "Ты угадал!"
                attempts = 0
                check_button.configure(state=tk.DISABLED)
                reset_button.configure(state=tk.NORMAL)
            if number < random_number:
                label["text"] = "Загаданное число больше"
            if number > random_number:
                label["text"] = "Загаданное число меньше"
            entry.delete(0, "end")
        else:
            label["text"] = "Можешь играть снова"
            check_button.configure(state=tk.DISABLED)
            reset_button.configure(state=tk.NORMAL)

def reset():
    global random_number, attempts
    random_number = random.randint(1, 100)
    attempts = 10
    attempts_label["text"] = f"Количество попыток:{attempts}"
    label["text"] = "Введи число от 1 до 100"
    entry.delete(0, "end")
    check_button.configure(state=tk.NORMAL)
    reset_button.configure(state=tk.DISABLED)



label = tk.Label(window, text="Угадай число от 1 до 100")
label.place(x=30, y=0)
attempts_label = tk.Label(window, text=f"Количество попыток:{attempts}")
attempts_label.place(x=40, y=30)

entry = tk.Entry(window)
entry.place(x=40, y=50)
entry.focus_set()


check_button = tk.Button(window, text="Проверка", width=17, command=lambda e="<Return>":guess(e))
check_button.place(x=40, y=80)

reset_button = tk.Button(window, text="Играть снова", width=17, command=reset, state=tk.DISABLED)
reset_button.place(x=40, y=110)

random_number = random.randint(1, 100)












window.bind("<Return>", guess)
window.mainloop()

# В функции guess: после блока условия if attempts > 0 добавить блок else,
# в котором делаем надпись label - "Можешь сыграть снова.",
# и меняем состояния кнопок - check_button делаем неактивной, reset_button - активной.