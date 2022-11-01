import os
import shop
import player_stats


def start_new_game():
    """
    Создать персонажа:
       имя
       здоровье
       деньги
       зелья

    """


    # Создаем персонажа
    player = ("Вася Питонов", 100, 50, 0)


    # запускаем главный цикл игры
    is_game = True
    while is_game:
        os.system("cls")
        player_stats.show_player_stats(player)
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
