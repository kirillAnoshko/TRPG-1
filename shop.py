import os
def visit_shop(player):

    name = player[0]
    hp = player[1]
    money = player[2]
    potions = player[3]
    os.system("cls")


    while True:
        print("--Персонаж--")
        print("Имя", name)
        print("Здоровье", hp)
        print("Деньги", money)
        print("Зелья", potions)
        print(f"{player[0]} приехал в магазин")
        print("1 - Купить зелье, цена 10 р")
        print("2 - Уйти к камню")
        answer = input("Сделайте выбор и нажмите ENTER ")
        if answer == "1":
            os.system("cls")
            if money >= 10:
                money -= 10
                potions += 1
                print("Купили зелье")
                input("Нажмите ENTER для продолжения")
            else:
                print("У вас нет денег!")
                input("Сделайте выбор и нажмите ENTER ")
        elif answer == "2":
            return (name, hp, money, potions)
