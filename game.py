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
    player_name = input("Введите имя игрока и нажмите ENTER ")
    if not player_name:
        player_name = "Безымянный"
    player_hp = 100
    player_money = 50
    player_potions = 0

    # запускаем главный цикл игры
    is_game = True
    while is_game:
        os.system("cls")
        player_stats.show_player_stats(player_name, player_hp, player_money, player_potions)
        print("-- ситуация:")
        print(f"{player_name} приехал к камню")
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
            shop.visit_shop(player_name, player_hp, player_money, player_potions)
        elif answer == "4":
            is_game = False
            os.system("cls")
