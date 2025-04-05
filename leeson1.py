#print("program")
"""print("hello "+"Maxim")
name = input("введите свое имя")
print("my name is"+name)"""

import random 
print("Компьютер загадал число от 1 до 10. Попробуйте его угадать.")
number = random.randint(1,10)
attempts = 3
while attempts > 0:
    user_number = input("Введите число")
    user_number = int(user_number)
    if number > user_number:
        attempts = attempts - 1
        print("загаданное число больше")
        print("не угадали,осталось попыток:", attempts)
    if number < user_number:
        attempts = attempts - 1
        print("загаданное число меньше")
        print("не угадали,осталось попыток:", attempts)
    if number == user_number:
        print("вы угадали")
        break
