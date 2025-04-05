import random
name = input("Введите свое имя: ")
email = input("Введите email: ")
password = str(random.randint(100,999))               
print("Пароль: " + str(password))
confirm_password = input("Подтвердите пароль: ")
if password == confirm_password:
        print("Поздравляю, " + str(name) + " ,вы зарегистрированы!!")
attempts = 1
while attempts > 0:
    if password > confirm_password:
        print("пароль не совпадает")
        confirm_password = input("Подтвердите пароль: ")
        if password == confirm_password:
            print("Поздравляю, " + str(name) + " ,вы зарегистрированы!!")
    if password < confirm_password:
        print("пароль не совпадает")
        confirm_password = input("Подтвердите пароль: ")
        if password == confirm_password:
            print("Поздравляю, " + str(name) + " ,вы зарегистрированы!!")
        break
    
    
