# counter = 10
# while counter > 0:
#     print(counter)
#     counter -= 2
# while True:
#     print("это бесконечный цикл")
#     stop = input("остановить цикл")
#     if stop == "да":
#         break
# counter = 0
# while counter < 10:
#     counter += 1
#     if counter % 2 == 0:
#         continue
#     print(counter)

# word = "book"
# for char in word:
#     print(5)

# for i in range(1,5 + 1):
#     print(i)
# import random
#
#
# points = 100
#
# while points > 0:
#     number = int(input("назовите число от 2 до 12 "))
#     bet = int(input("назовите ставку "))
#     random_number = random.randint(1, 6)
#     random_number2 = random.randint(1, 6)
#     final_number = random_number2 + random_number
#     print(f"рандомные числа:{random_number2} и {random_number}")
#     print(f"сумма рандомных чисел: {final_number}")
#     if (final_number < 7 and number < 7) or (final_number > 7 and number > 7):
#         points += bet
#         print(f"вы угадали, теперь у вас {points} очков")
#     elif number == final_number:
#         points = bet * 4
#         print(f"ваше число совпало с рандомным числом, теперь у вас {points} очков ")
#     else:
#         points -= bet
#         print(f"вы не угадали, теперь у вас {points} очков")
#     question = input("хотите ли вы продолжить да/нет ")
#     if question == "нет":
#         print(f"игра закончена,обший выйгрыш {bet}")
#         break

# password = int(input("введите пароль: "))
# while password != 235:
#     print("неверный пароль")
#     password = int(input("Попробуйте еще раз: "))
# print("Пароль верный,Добро пожаловать! ")

# balance = int (input("сколько денег пришло: "))
# while balance > 5000:
#     product_cost = int(input("сколько стоит продукт? "))
#     balance -= product_cost
# print("внимание, на карте осталось мало денег.Остановитесь.")
# print("баланс счета:", balance)

# number = int(input('Введите число: '))
# total = 0
# while number > 0:
#     # if number == 0:
#     #     break
#     total += number
#     number = int(input('Введите число: '))
# print(total)

# number = int(input("введите число: "))
# while number <= 200:
#     print(number)
#     number += number

# weather = int(input("сколько градусов на улице? "))
# meters = 0
# while weather > 15:
#     meters += 20
#     weather -= 2
#     if weather <= 15:
#         break
#     meters += 10
# print("Пройдено метров:", meters)

# number = int(input("введите число: "))
# summ = 0
# while number != 0:
#     last_num = number % 10
#     print(last_num)
#     if last_num == 5:
#         print("обнаружен разрыв.")
#         break
#     summ += last_num
#     number //= 10
# print("сумма:", summ)

# goal = 5
# found = 0
# total_books = int(input("Сколько книг выдал библиотекарь? "))
#
# while found < goal and total_books > 0:
#     checked = int(input("Сколько книг просмотрено? "))
#     if checked > total_books:
#         checked = total_books
#         total_books -= checked
#     found += int(input("Сколько из них требует реставрации? "))
# if found >= goal:
#     print("Ура! Практика завершена!")
# else:
#     print("Библиотекарь: На сегодня всё. Благодарю за помощь!")
# 
# money = int(input("введите начальную сумму денег: "))
# while money <= 10000:
#     number = int(input("сколько выпало на кубике? "))
#     if number == 3:
#         print("Вы проиграли всё!")
#         money -= money
#         break
#     else:
#         print("Быиграли 500 рублей")
#         money += 500
# print("итого осталось:", money)

# rate_check = False
# while True:
#     active = int(input("Продолжить активность? 1/0 "))
#     if active == 0:
#         print("приложение закрывается...")
#         break
#     rate = int(input("Поставите оценю приложению? 1/0 "))
#     if rate == 1:
#         rate_check = True
# print("работа завершена.")
# if rate_check:
#     print("пользователь поставит оценку.")
# else:
#     print("пользователь не поставит оценку")

# count = 10
# while count >= 0:
#     if count == 0:
#         print('Время вышло!')
#     else:
#         print(count)
#     count -= 1
# password = 4589
# while True:
#     print("Компьютер заблокирован. Вернёшь скейт - скажу код разблокировки!")
#     code_check = int(input("введите код: "))
#     if code_check == password:
#         break
# print("Код верный, завершаю работу...")
#
# bags = int(input("Сколько мешков нужно перетащить? "))
# total_weight = 0
# bags_count = 0
# while bags_count < bags:
#     weight = int(input("сколько весит мешок? "))
#     total_weight += weight
#     bags_count += 1
#     print("перенесли мешков: ", bags_count, "из ", bags)
#
# print("Общий вес мешков: ", total_weight)
#
# count = int(input("сколько раз? "))
# while count > 0:
#     print("Я — программист!")
#     count -= 1


# count = int(input("сколько раз напомнить? "))
# while count > 0:
#     print("Вы хотели не забыть о чём-то")
#     count -= 1
# print("Программа для отслеживания температуры")
# count_failures = 0
# stop_program = False
# last_temperature = -999
#
# while not stop_program:
#     sensor = int(input("Какая температура на датчике? "))
#     if sensor == last_temperature:
#         count_failures += 1
#         print("Внимание: дублирующее значение температуры", sensor, "обнаружено!")
#         print("Зафиксировано сбоев датчика:", count_failures)
#
#         continue_collecting_data = int(input("Хотите продолжить сбор данных? 1-да, 0-нет: "))
#         if continue_collecting_data == 0:
#             print("Сбор данных остановлен")
#             stop_program = True
#         else:
#             last_temperature = -999
#     last_temperature = sensor

number = int(input("введите число: "))
while number >= 0:
    if number == 3:
        number -= 1
        continue
    print(number)
    number -= 1
