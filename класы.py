# class Car:
#     def __init__(self, speed, color):
#         self.speed = speed
#         self.color = color
#     speed = 100
#     color = "black"
#     def beep(self):
#         print("beep")
#     def say_speed(self):
#         print(self.speed)
#     def say_color(self):
#         print(self.color)
#
# audi = Car(200, "red")
# audi.beep()
# audi.say_color()
# audi.say_speed()
#
# volkswagen = Car(150, "black")
# volkswagen.beep()
# volkswagen.say_speed()
# volkswagen.say_color()

# class Human:
#     def __init__(self, name, age, nation):
#         self.name = name
#         self.age = age
#         self.nation = nation
#     def say_name(self):
#         print(f"меня зовут {self.name}")
#     def say_age(self):
#         print(f"мне {self.age}")
#     def say_nation(self):
#         print(f"я {self.nation}")
#
# human = Human("Володя", 34, "русский")
# human.say_name()
# human.say_age()
# human.say_nation()
#
# human2 = Human("Гриша", 23, "молдован")
# human2.say_name()
# human2.say_age()
# human2.say_nation()



class Student:
    def __init__(self, school, clas):
        self.school = school
        self.clas = clas

    def say_school(self):
        print(f"Я учусь в школе {self.school}")

    def say_clas(self):
        print(f"Я в {self.clas} классе")

student1 = Student("Номер 3", "9-Б")
student1.say_school()
student1.say_clas()

student2 = Student("Номер 2", "9-А")
student2.say_school()
student2.say_clas()

# Сделать класс Student, унаследованный от класса Human,
# у которого будет свойства "школа" и "класс" и методы для сообщения значений этих свойства