# age = 15
# if age < 14:
#     print("ты младше 14")
# if age > 14:
#     print("ты старше 14")
# if age == 14:
#     print("тебе 14")
# if age != 14:
#     print("тебе не 14")
# if 6 <= age <= 18:
#     print("ты школьник")
# if "хлеб" == "хлеб":
#     print("это хлеб")
# if 5 == "5":#так делать нельзя
#     pass
# things = "на столе стоит ноутбук и стакан"
# if "ноутбук" in things:
#     print("я нашел ноутбук")
# if "телефон" not in things:
#     print("а телефон не нашел")

# number = int(input("введите число"))
# if number % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")

# temp = int(input("какая сейчас температура воздуха?"))
# if temp <= 0:
#     print("очень холодно")
# elif 0 < temp <= 12:
#     print(" холодно")
# elif 12 < temp <= 18:
#     print("прохладно")
# elif 18 < temp <= 25:
#     print("тепло")
# elif 25 < temp <= 35:
#     print("жарко")

# money = False
# seats = True
# if money == True and seats == True:
#     print("ты можешь купить билет")
# age = 15
# parents = True
# if age >= 18 or parents == True:
#     print("ты можешь купить билет")

# print("Давай сыграем в игру. Введи любое число. Если оно делится на 3, я скажу 'Fizz', если оно делится на 5, я скажу 'Buzz', а если оно делится и на 3 и на 5, я скажу 'FizzBuzz'!")
# number = int(input("введите число"))
# if number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Bazz")
# elif number % 3 == 0 and number % 5 == 0:
#     print("FizzBazz")

# Сделать программу, которая спрашивает номер месяца (от 1 до 12) и выводит в консоль ответ, к какому сезону относится введенный месяц ("зимний месяц", "весенний месяц", "летний месяц" или "осенний месяц"). Если номер введен не от 1 до 12, выводить "Вы ввели неверный номер".

# number = int(input("введите число от 1 до 12 "))
# if 0 < number <= 2:
#     print("сейчас зима")
# elif 2 < number <= 5:
#     print("сейчас весна")
# elif 5 < number <= 8:
#     print("сейчас лето")
# elif 8 < number <= 11:
#     print("сейчас осень")
# elif 11 < number == 12:
#     print("сейчас зима")
# if number > 12:
#     print("вы ввели неверный номер")
# if number < 1:
#     print("вы ввели неверный номер")

# bank = int(input("сколько денег на счету? "))
# if bank > 75000:
#     bank -= 75000
#     print("курс успешно приобретен")
#     if bank < 5000:
#         bank += 1000
#         print("сделана скидка")
# else:
#     print("вам не хватает денег")
# print("остаток в банке: ", bank)
# print("хорошего дня")

# son = int(input("какое число я загадал? "))
# father = 5
# if father == son:
#     print("угадал, можешь идти гулять!")
# elif father > son or father > son:
#     print("ты не угадал,ты не идешь гулять! ")
# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print("Число чётное")
# else:
#     print("число нечетное")
# orange = int(input("сколько доходов от апельсин? "))
# apple = int(input("сколько доходов от яблок? "))
# expenses = int(input("расходы: "))
# if orange + apple > expenses:
#     print("доходы превышают расходы")
# else:
#     print("расходы превышают доходы")
# print("Добро пожаловать в игру «Угадай число»!")

# print("Настя загадывает число. Дима, не подглядывай!")
# nastya_number = int(input("Введите число: "))
# dima_number = int(input("Введите число: "))
#
# if nastya_number == dima_number:
#     print("Ура! Угадал!")
# else:
#     print("Нет, это не то, что я загадала.")

# password = int(input("введите пароль"))
# a = 0
# if password == 123890:
#     print("верный пароль")
#     а = 15
# print(а)

# a = input("введите первое число ")
# b = input("введите второе число ")
# c = input("введите третье число ")
# if a > b:
#     max_number = a
# else:
#     max_number = b
# if c > max_number:
#     max_number = c
#
# print("максимальное число: ", max_number)

# product = int(input("введите сумму чека "))
# delivery = int(input("введите сумму доставки "))
# discount = 0
# if product > 10000:
#     print("хороший чек! доставка снижена вдвое ")
#     delivery /= 2
#     if product % 2 ==0:
#         print("покупателю положен подарок ")
#         discount = 500
#
# price = product + delivery - discount
# print("полная стоимость товара: ", price)

# x = int(input("введите х "))
# y = int(input("введите y "))
# if x == y:
#     print("Х равен У")
# else:
#     if x > y:
#         print("Х больше У")
#     else:
#         print("Х меньше У")

# score_points = int(input("сколько баллов у игрока: "))
# if score_points >= 55000:
#     score_points -= 55000
#     if score_points < 5000:
#         score_points += 1000
#         print("получен бонус")
#     print("артефакт успешни приобретен")
# else:
#     print("вам не хватает баллов")
# print("остаток баллов у игрока:", score_points)
# print("удачной игры!")

# money = int(input("введите число денег: "))
# cheese = 60
# icecream = 20
# if money >= cheese:
#     print("на сыр хватило ")
#     money -= 60
#     if money >= icecream:
#         print("и на мороженое тоже!")
#     else:
#         print("денег маловато")
# else:
#     print("денег не хватило даже на сыр")

# profit = int(input("введите вашу прибыль: "))
# if profit < 10000:
#     tax = profit * 13 / 100
#     print("размер налога 13% равен: ", tax)
# elif profit < 50000:
#     tax = profit * 20 / 100
#     print("размер налога 20% равен: ", tax)
# else:
#     tax = profit * 30 / 100
#     print("размер налога 30% равен: ", tax)
#
# weight1 = int(input("введите вес первого  груза: "))
# weight2 = int(input("введите вес второго груза: "))
# if weight1 > weight2:
#     print("первый груз тяжелее")
# elif weight1 < weight2:
#     print("второй груз тяжелее")
# else:
#     print("оба груза весят одинаково")
#
# cent1 = int(input("введите вес первой монетки"))
# cent2 = int(input("введите вес второй монетки"))
# cent3 = int(input("введите вес третьей монетки"))
# if cent1 == cent2:
#     print("третья легче")
# elif cent2 == cent3:
#     print("первая легче")
# else:
#     print("вторая легче")
# year = int(input("введите год выпуска "))
# speed_count = int(input("введите количество скоростей "))
# if year >= 2018 and speed_count >= 12:
#     print("велосипед подходит ")
# else:
#     print("не ссответсвует критериям ")
#
# year = int(input("введите год выпуска "))
# speed_count = int(input("введите количество скоростей "))
# if year < 2018 or speed_count < 12:
#     print("не ссответсвует критериям ")
# else:
#     print("велосипед подходит ")

# x = int(input("введите точку икс: "))
# left_border = int(input("введите левую границу: "))
# right_border = int(input("введите правую границу: "))
# if x <= left_border or x >= right_border:
#     print("точка не соответствует интервалу.(0-100) ")
# else:
#     print("тоцка соответствует интервалу. ")

# age = int(input("введите возраст участника: "))
# speed = int(input("введите время которое пробежал 100м: "))
# if age >= 18 and speed <= 15:
#     print("участник допускается.")
# else:
#     print("участник не допускается.")

# result_exam = int(input("введите результат екзаменов: "))
# medal = int(input("есть ли у вас золотая медаль(0-нет,1-да)"))
# if result_exam < 280 or medal == 0:
#     print("К сожалению, ты не прошёл в наш университет")
# else:
#     print("Поздравляем! Ты поступил!")

# temperature = int(input("введите температуру: "))
# if temperature > 100 or temperature < 0:
#     print("Температура в пределах нормы")
# else:
#     print("всё нормально.")
# year = int(input("введите год: "))
# if (year % 4 == 0) and not (year % 100 == 0) or (year % 400):
#     print("год високосный ")
# else:
#     print("год не високосный")
# experience = int(input("опыт"))
#
# # Какое значение переменной level должно быть задано изначально?
# level = 1
#
# # Проверки каких условий должна выполнить программа? Напишите их ниже.
# if experience >= 5000:
#     level = 4
# elif experience >= 2500:
#     level = 3
# elif experience >= 1000:
#     level = 2
# print('Уровень персонажа:', level)

# time = int(input("Введите время (0-23): "))
# if (time >= 8) and (time < 10) or (time >= 12 and time < 14) or (time >= 20 and time < 22):
#     print("поссылку можно получить ")
# else:
#     print("поссылку нельзя получить ")

# n = int(input("Введите положительное число: "))
#
# if n < 0:
#     print("Ошибка: введите положительное число")
# else:
#     count = 0
#     while n > 0:
#         n //= 10
#         count += 1
#     print("Количество цифр:", count)

# tasks_completed = 0
# answered_phone = False
# hour = 1
#
# while hour <= 8:
#     tasks_in_hour = int(input(str(hour) + "-й час.Сколько задач решит Максим? "))
#
#     tasks_completed += tasks_in_hour
#
#     if answered_phone == False:
#         phone_call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
#         if phone_call == 1:
#             answered_phone = True
#     hour += 1
# print("Рабочий день закончился. Всего выполнено задач: " + str(tasks_completed))
# if answered_phone:
#     print("Нужно зайти в магазин.")


# x = int(input("Введите начальную сумму вклада: "))
# p = int(input("Введите процент увеличения в год: "))
# y = int(input("Введите целевую сумму: "))
# years = 0
# while x < y:
#     years += 1
#     new_x = x + x * p // 100
#     print(str(years) + " год. " + str(x) + " + " + str(p) + "%" + " = " + str(new_x))
#     x = new_x
# print("Кол-во лет для достижения порога:", years)

secret_number = int(input("Загадали число от 1 до 10? Введите его: "))
attempts = 0
print("Попробуйте угадать загаданное число!")
while True:
    user_input = int(input("Введите число: "))
    attempts += 1
    if user_input < secret_number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif user_input > secret_number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    else:
        print("Вы угадали! Число попыток:", attempts)
        break
