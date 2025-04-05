"""fruits = ["banan","apple","orange"]
print(fruits)
fruits.append("peach")
print(fruits)
question = "banan" in fruits
print(question)
question = "banan" not in fruits
print(question)"""

import random
print("Компютер загадал слово. Попробуйте отгадать это слово.")
words = ["книга","окно","яблоко","школа","дом","ноутбук","погода","число","тетрадь"]
word = random.choice(words)
letters = []
attempts = 10
while attempts > 0:
    victory = True
    letter = input("введите букву ")
    letters.append(letter)
    print(letters)
    for char in word:
        if char in letters:
            print(char,end = "")
        else:
            print("*",end = "")
            victory = False
    print()
    if letter not in word:
        attempts -= 1
        print("такой буквы нет, у вас осталось попыток " + str(attempts))
    if attempts == 0:
        print("вы проиграли")
    if victory == True:
        print("вы победили")
        break
    #Добавить случайный выбор загадываемого слова из списка
        

