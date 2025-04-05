# def say_hello(name):
#     print(f"hello,{name}!")
# say_hello("Максим")
# say_hello("Федя")

# def area_square(side):
#     area = side * side
#     print(area)
# area_square(5)

# def area_square(side_a,side_b):
#     area = side_a * side_b
#     print(area)
# area_square(5,10)
#
# import random
#
# def lottery():
#     tickets = [6,9,1,8,4]
#     ticket = random.choice(tickets)
#     tickets.remove(ticket)
#     ticket2 = random.choice(tickets)
#     return ticket,ticket2
# winner,winner2 = lottery()
# print(winner,winner2)
#
# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result
# print(factorial(7))

sum = lambda a: a*a
print(sum(53))
sum = lambda a, b: a*b
print(sum(6, 9))
