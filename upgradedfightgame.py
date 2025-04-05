import random
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def do_damage(self, damage):
        self.hp = self.hp - damage


class User(Enemy):
    def __init__(self, name, hp, damage, armor=10):
        super().__init__(name, hp, damage)
        self.max_hp = hp
        self.armor = armor

    def do_damage(self, damage):
        self.hp = int(self.hp - (damage - self.armor))
        if self.armor >= 0:
            self.armor -= int(damage/2)

            if self.armor <= 0:
                self.armor = 0

    def heal(self):
        if not self.hp >= self.max_hp:
            hp = 20
            self.hp += hp
            print(f"ты восстановил {hp} здоровье,твое текушее здоровье {self.hp}")
        else:
            print(f"у вас уже макимальное колиццхество здоровья")



user = User("Максим", 250, 16)

enemy = Enemy("Рыцарь", 300, 10)
enemy2 = Enemy("Разбойник", 200, 18)
enemy3 = Enemy("Маг", 100, 25)
enemies = [enemy, enemy2, enemy3]

while True:
    print(f"твое здоровье:{user.hp}, твой урон:{user.damage}")
    print(f"здоровье: {enemy.hp}, его урон:{enemy.damage}")
    userinput = input("\n Выберите действие: \n1 - восстановить здоровье \n2 - атаковать \n")
    if userinput == "1":
        user.heal()

    if userinput == "2":
        enemy.do_damage(user.damage)


    user.do_damage(enemy.damage)
    if user.hp <= 0 or enemy.hp <= 0:
        print("игра оконchена")
        break