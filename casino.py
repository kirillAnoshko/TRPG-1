import os
import random
import hero_engine


def visit_casino(player):
    money = player[5]
    casino_money = 100
    os.system("cls")
    print(f"{player[0]} приехал играть в казино")
    print("1-Начать игру")
    print("2-уехать к камню")
    answer = input("Сделайте выбор и нажмите ENTER ")

    if answer == "1":
        user_turn = random.randint(1, 6)
        casino_turn = random.randint(1, 6)
        print("игрок выбросил", user_turn)
        print("казино выбросило", casino_turn)
    if user_turn > casino_turn:
        print("игрок победил")
        user_money += 1
        casino_money -= 1
    elif casino_turn > user_turn:
        print("казино победило")
        casino_money += 1
        user_money -= 1
    else:
        print("ничья")

    elif answer == "2":
        return(name, hp, money, potions)

