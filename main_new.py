from random import randint, choice

first_names = ("Жран", "Дрын", "Жлыг")
last_names = ("Ужасный", "Зловонный", "Борзый")


def make_hero(
        name=None,
        hp_now=100,
        hp_max=100,
        level=None,
        xp_now=0,
        xp_next=100,
        attack=1,
        defence=100,
        luck=1,
        money=None ,
        inventory=None

) -> list:

    """
    Персонаж-это список
    [0] name - имя
    [1] hp_now - здоровье текущее
    [2] hp_max - здоровье максимальное
    [3] level - уровень
    [4] xp_now - опыт текущий
    [5] xp_next - опыт до следующего уровня
    [6] attack - сила атаки,применяется в бою
    [7] defence - защита,применяется в бою
    [8] luck - удача
    [9] money - деньги
    [10] inventory - список предметов

    """
    if not name:
        name = choice(first_names) + " " + choice(last_names)
    if not hp_now:
        hp_now = randint(1, 100)
        hp_max = hp_now
    if not money:
        money = randint(0, 100)
    if not level:
        level = randint(1, 210)
    if not inventory:
        inventory = []

    return [name,
            hp_now,
            hp_max,
            level,
            xp_now,
            xp_next,
            attack,
            defence,
            luck,
            money,
            inventory
    ]
p1 = make_hero()
p2 = make_hero()
p3 = make_hero()
print(p1)
print(p2)
print(p3)

def show_hero(hero):
    print("имя", hero[0])
    print("здоровье", hero[1], "из", hero[2])
    print("") #TODO: Показать предметы и их количество


