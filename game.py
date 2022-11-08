import os
import shop


def start_new_game():
    """
    Создать персонажа:
       имя
       здоровье
       деньги
       зелья

    """


    # Создаем персонажа
    # [0] имя, [1] hp, [2] money,[3] зелья
    player = ("Вася Питонов", 100, 50, 0)

    # запускаем главный цикл игры
    is_game = True
    while is_game:
        os.system("cls")
        print("--Персонаж--")
        print("Имя", player[0])
        print("Здоровье", player[1])
        print("Деньги", player[2])
        print("Зелья", player[3])
        print("-- ситуация:")
        print(f"{player[0]} приехал к камню")
        print("-- варианты")
        print("1 - Поехать на битву с разбойниками")
        print("2 - Играть в кости")
        print("3 - Приехать в лавку алхимика")
        print("4 - Выйти в главное меню")

        answer = input("Введите номер ответа и нажмите ENTER ")
        if answer == "1":
            pass
        elif answer == "2":
            pass
        elif answer == "3":
            player = shop.visit_shop(player)
        elif answer == "4":
            is_game = False
            os.system("cls")
