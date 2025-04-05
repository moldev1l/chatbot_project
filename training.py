# with open("books.txt", encoding="utf-8") as file:
#     print(file.read())
# with open("books.txt", encoding="utf-8") as file:
#     for line in file:
#         print(f"мой школьный предмет: {line}")

# with open("books.txt", "w") as file:
#     file.write("privet")
#
# with open("books.txt", "a") as file:
#     file.write(" \nprivet")

# color = "blue"
# shape = "circle"
# def function():
#     color = "green"
#     shape = "square"
#     print(f"внутри функции цвет - {color}")
#     print(f"внутри функции форма - {shape}")
# print(f"в основной программе - {color}")
# print(f"в основной программе - {shape}")
# function()
#

n = int(input("enter the number: "))
i = 1
result = i ** 3
while i <= n:
    print(str(i) + " ** 3 = " + str(i ** 3))
    i += 1
