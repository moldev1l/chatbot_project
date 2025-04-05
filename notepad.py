import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm

window = tk.Tk()
window.title("Блокнот")
window.geometry("400x400")

file_name = ""


def open_file():
    content_text.delete(1.0, "end")
    global file_name
    file_name = tfd.askopenfilename()
    with open("books.txt") as file:
        content_text.insert(1.0, file.read())


def save_as_file():
    global file_name
    file_name = tfd.asksaveasfilename()
    content = content_text.get(1.0, "end")
    with open(file_name, "w") as file:
        file.write(content)


def save_file():
    global file_name
    if file_name == "":
        save_as_file()
    else:
        content = content_text.get(1.0, "end")
        with open(file_name, "w") as file:
            file.write(content)
    if tkm.showinfo("Сохранение файла", f"Сохаранение записаны в файл {file_name}"):
        file_name = ""
        content_text.delete(1.0, "end")



def new_file():
    global file_name
    if tkm.askokcancel("Создание нового файла", "Вы уверены? Несохраненный текст будет удален"):
        file_name = ""
        content_text.delete(1.0, "end")


def help_file():
    global file_name
    if tkm.showinfo("помошь", "\nНовый файл - создать новый файл "
                              "\nОткрыть - открыть сушествуеший файл "
                              "\nСохранить - сохранить файл "
                              "\nСохранить как - сохранить файл с новым именем "):
        file_name = ""


def about_the_program():
    global file_name
    if tkm.showinfo("Блокнот: сведения", "\nВерсия: 1.0"
                                         "\nРазработано: Maxim Juravcshi"):
        file_name = ""


content_text = tk.Text(window, wrap="word")
content_text.place(x=0, y=0, relwidth=1, relheight=1)

main_menu = tk.Menu(window)
window.configure(menu=main_menu)

file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Файл", menu=file_menu)

help_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Справка", menu=help_menu)

help_menu.add_command(label="Помошь", compound="left", command=help_file)
help_menu.add_command(label="О программе", compound="left", command=about_the_program)

new_file_icon = tk.PhotoImage(file="new_file.gif")
open_file_icon = tk.PhotoImage(file="open_file.gif")
save_file_icon = tk.PhotoImage(file="save_file.gif")

file_menu.add_command(label="Новый файл", image=new_file_icon, compound="left", command=new_file)
file_menu.add_command(label="Открыть", image=open_file_icon, compound="left", command=open_file)
file_menu.add_command(label="Сохранить", image=save_file_icon, compound="left", command=save_file)
file_menu.add_command(label="Сохранить как", image=save_file_icon, compound="left", command=save_as_file)

window.mainloop()
