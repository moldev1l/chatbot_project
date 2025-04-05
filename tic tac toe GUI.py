import tkinter
import tkinter as tk
import tkinter.messagebox as tkm

window = tk.Tk()


window.title("Крестики нолики")
window.geometry("300x300")
window.resizable(False, False)
area = []
turn = 0
def push(button):
    global turn
    if turn % 2 == 0:
        turn_char = "X"
        tkm.showinfo(title="Информация", message=f"\nТекущий номер хода: {turn}"
                                                 f"\nСейчас шёл: X"
                                                 f"\nСледующий идёт: 0")
        button["background"] = "blue"
    else:
        turn_char = "0"
        tkm.showinfo(title="Информация", message=f"\nТекущий номер хода: {turn}"
                                                 f"\nСейчас шёл: 0"
                                                 f"\nСледующий идёт: X")
        button["background"] = "green"
    if button["text"] == "":
        button["text"] = turn_char
        turn += 1
    if winner() == "X":
        print("Вы победили!")
        tkm.showinfo(title="Победитель", message="Победили X")
        new_game()
    if winner() == "0":
        print("Вы победили!")
        tkm.showinfo(title="Победитель", message="Победили 0")
        new_game()
    if winner() == "" and turn == 10:
        print("ничья")
        tkm.showinfo(title="Конец игры", message="Ничья")
        new_game()
    print(turn)

def new_game():
    global area, turn
    turn = 1
    for x in range(3):
        for y in range(3):
            area[x][y]["text"] = ""


for x in range(3):
    area.append([])
    for y in range(3):
        button = tk.Button(window, text="", width=13, height=6)
        area[x].append(button)
        area[x][y].place(x=x*100, y=y*100)
        area[x][y]["command"] = lambda selected_button = button: push(selected_button)

def winner():
    if area[0][0]["text"] == "X" and area[0][1]["text"] == "X" and area[0][2]["text"] == "X":
        return "X"
    if area[1][0]["text"] == "X" and area[1][1]["text"] == "X" and area[1][2]["text"] == "X":
        return "X"
    if area[2][0]["text"] == "X" and area[2][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "X" and area[1][0]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    if area[0][1]["text"] == "X" and area[1][1]["text"] == "X" and area[2][1]["text"] == "X":
        return "X"
    if area[0][2]["text"] == "X" and area[1][2]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "X" and area[1][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][2]["text"] == "X" and area[1][1]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "0" and area[0][1]["text"] == "0" and area[0][2]["text"] == "0":
        return "0"
    if area[1][0]["text"] == "0" and area[1][1]["text"] == "0" and area[1][2]["text"] == "0":
        return "0"
    if area[2][0]["text"] == "0" and area[2][1]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][0]["text"] == "0" and area[1][0]["text"] == "0" and area[2][0]["text"] == "0":
        return "0"
    if area[0][1]["text"] == "0" and area[1][1]["text"] == "0" and area[2][1]["text"] == "0":
        return "0"
    if area[0][2]["text"] == "0" and area[1][2]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][0]["text"] == "0" and area[1][1]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][2]["text"] == "0" and area[1][1]["text"] == "0" and area[2][0]["text"] == "0":
        return "0"
    return ""



window.mainloop()

# Сделать в функции push вывод всплывающего окна с информацией о номере текущего хода,
# кто сейчас ходит и кто идет следующим.
# Добавить в функцию push изменение цвета кнопки c помощью параметра background (или bg).
# Для крестиков - цвет кнопки сделать, например, красным, для ноликов - синим.