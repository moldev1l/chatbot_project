# products = ["хлеб","яблоки","мука","молоко"]
# print(products)
# print(products[0])
# products[2] = "бананы"
# print(products)
# products.append("вода")
# print(products)
# products.remove("яблоки")
# print(products)
# product = products.pop()
# print(products)
# print(product)
# product_num = products.index("молоко")
# print(product_num)
# product = products.pop(product_num)
# print(products)

# games = ["Minecraft","Roblox","Rust","Subnautica","Hades"]
# for game in games:
#     print(game)
# length = len(games)
# for i in range(length):
#     print(f"{i + 1}.{games[i]}")

# if "Dota" in games:
#     print("я играл в доту")
# if "Roblox" in games:
#     print("я играл в роблокс")
# if "Lost" not in games:
#     print("я не играл в лост")

# game = input("какую игру добавить? ")
# if game in games:
#     print("игра уже есть в списке")
# else:
#     games.append(game)
#     print("игра добавлена")
#     print(games)

# import random
#
#
# noun = ["хлеб","стол","ковер","кот","пес","голубь","суслик","кабан","жаба","тапок"]
# adjective = ["вкусный","ароматныЙ","аппетитный","скользкий","довольный","вонючий","бешенный","неудержимый","красивый","гадкий"]
# first_name = random.choice(noun)
# second_name = random.choice(adjective)
# print(f"Гороскоп сказал что ты сегодня {second_name} {first_name}")

#Сделать программу "магического шара": составить список со строками "да", "нет", "не могу сейчас сказать".
# Приветствовать пользователя и вывести ему сообщение - "Задавай волнующий тебя вопрос, на который можно ответить "да" или "нет"".
# На вопросы, вводимые пользователем, надо случайным образом давать ответ.

import random

attempts = 100
while attempts > 0:
    answers = ["да","нет","не могу сейчас сказать"]
    question = input("Задавай волнующий тебя вопрос, на который можно ответить да или нет ")
    answer_random = random.choice(answers)
    print(answer_random)
