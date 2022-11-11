import random


first_names = ("Жран", "Дрын", "Жлыг")
last_names = ("Ужасный", "Зловонный", "Борзый")


def make_hero(
        name=None,
        hp=None,
        xp=None,
        attack=None,
        defence=None,
        money=None,
        potions=None,
) -> tuple:
    if not name:
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
    if not hp:
        hp = random.randint(1, 100)
    if not xp:
        xp = random.randint(0, 100)
    if not attack:
        attack = random.randint(1, 100)
    if not defence:
        defence = random.randint(1, 100)
    if not money:
        money = random.randint(1, 100)
    if not potions:
        potions = random.randint(1, 5)

    return (name, hp, xp, attack, defence, money, potions)

if __name__ =="__main__":
    player = make_hero()
    enemy = make_hero()
    enemy_2 = make_hero()
    enemy_3 = make_hero()
    print(player)
    print(enemy)
    print(enemy_2)
    print(enemy_3)

def show_hero(hero:tuple):
    print("имя", hero[0])
    print("жизни", hero[1])
    print("опыт", hero[2])
    print("атака", hero[3])
    print("защита", hero[4])
    print("деньги", hero[5])
    print("зелья", hero[6])



