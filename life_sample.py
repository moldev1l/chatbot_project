import random
class Insects:

# 1. задаем атрибуты насекомого (имя, еда, чувство сытости)
    def __init__(self, name):
        self.name = name
        self.food = 100
        self.hunger = 100


# 2. после еды увеличиваем/уменьшаем нужные атрибуты      
    def eat(self):
        if self.food > 0:
            self.hunger += 10
            self.food -= 10
            print(f"{self.name} поел, осталось еды: {self.food}, голод: {self.hunger}")
        else:
            print(f"еды нет, уровень голода: {self.hunger}")

# 3. после поиска еды уменьшаем/увеличиваем нужные атрибуты
    def find_food(self):
        self.food += 30
        self.hunger -= 10
        print(f"{self.name} достал еду, голод: {self.hunger}, еда: {self.food}")

# 4. унаследуем класс пчелы от класса насекомых
class Bee(Insects):
# 5. задаем атрибуты пчелы (количество меда, помимо остальных атрибутов)
    def __init__(self, name):
        super().__init__(name)
        self.honey = 0


# 6. после сбора меда увеличиваем/уменьшаем нужные атрибуты
    def collecting_honey(self):
        self.honey += 10
        self.hunger -= 10
        print(f"{self.name} собрал мед, голод: {self.hunger}, оталось еды:{self.food}")

        
# 7. данный метод готов, нужно будет его запустить в самый последний момент и объяснить, как он работает
    def live(self):
       living = True
       if self.hunger <= 0:
           print(f'{self.name} died :(')
           living = False
           return living
       action = random.randint(1,3)
       if self.hunger < 4:
           if self.food == 0:
               self.find_food()
           else:
               self.eat()
       else:
           if action == 1:
               self.collecting_honey()
           elif action == 2:
               self.eat()
           else:
               self.find_food()


# 8. пчела живет 30 дней (если она погибает, то итерации заканчиваются)
bee = Bee("Пчелка")

for day in range(31):
    print(f"сегодня {day}")
    if bee.live() == False:
        break


