import tkinter

window = tkinter.Tk()
window.title("калькулятор")
window.geometry("300x300")
window.configure(bg="grey")

def get_num1():
    num1 = text_num1.get()
    num1 = int(num1)
    return num1

def get_num2():
    num2 = text_num2.get()
    num2 = int(num2)
    return num2

def set_answer(result):
    text_answer.delete(0, "end")
    text_answer.insert(0, result)
def add():
    num1 = get_num1()
    num2 = get_num2()
    result = num2 + num1
    set_answer(result)

def sub():
    num1 = get_num1()
    num2 = get_num2()
    result = num1 - num2
    set_answer(result)

def mul():
    num1 = get_num1()
    num2 = get_num2()
    result = num2 * num1
    set_answer(result)

def div():
    num1 = get_num1()
    num2 = get_num2()
    result = num1 / num2
    set_answer(result)


button_add = tkinter.Button(window, text="+", command=add, width=7,height=2,bg="orange")
button_sub = tkinter.Button(window, text="-", command=sub, width=7,height=2,bg="red")
button_mul = tkinter.Button(window, text="*", command=mul, width=7,height=2,bg="green")
button_div = tkinter.Button(window, text="/", command=div, width=7,height=2,bg="white")

button_add.place(x=95,y=110)
button_sub.place(x=160,y=110)
button_mul.place(x=95,y=150)
button_div.place(x=160,y=150)

text_num1 = tkinter.Entry(window,width=20)
text_num2 = tkinter.Entry(window,width=20)
text_answer = tkinter.Entry(window,width=20)

text_num1.place(x=95,y=40)
text_num2.place(x=95,y=80)
text_answer.place(x=95,y=220)

label_num1 = tkinter.Label(window,text="Введите первое число",bg="grey")
label_num2 = tkinter.Label(window,text="Введите второе число",bg="grey")
label_answer = tkinter.Label(window,text="Ответ",bg="grey")

label_num1.place(x=95,y=20)
label_num2.place(x=95,y=60)
label_answer.place(x=95,y=200)




window.mainloop()