import random
class Enemy:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    def do_damage(self, damage):
        self.hp = self.hp - damage




enemy1 = Enemy(hp=330, damage=10)
enemy2 = Enemy(hp=500, damage=8)
enemy3 = Enemy(hp=300, damage=16)

enemies = [enemy1, enemy2, enemy3]
player1 = random.choice(enemies)
enemies.remove(player1)
player2 = random.choice(enemies)


hits = 0
while True:
    if player1.hp <= 0:
        print("Второй победил")
        print("У него осталось здоровья:", player2.hp)
        break

    elif player2.hp <= 0:
        print("Первый победил")
        print("У него осталось здоровья:", player1.hp)
        break

    elif player2.hp <= 0 and player1.hp <= 0:
        print("ничья")
        break

    player1.do_damage(player2.damage)
    player2.do_damage(player1.damage)
    hits += 1
    print(hits, player1.hp, player2.hp)


# Добавить третьего персонажа и сделать рандомный подбор соперников с помощью random.choice()



