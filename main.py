import os
import game
import settings

def show_menu():
    """
    Печатает на экране
    Выборы:
        начать игру
        настройки
        загрузка игры
        выход
    """
    while True:
    # печатаем варианты
        print("1 - Начать игру")
        print("2 - Настройки")
        print("3 - Выход")

        answer = input("Сделайте выбор и нажмите ENTER ")
        os.system("cls")
        if answer == "1":
            game.start_new_game()
        elif answer == "2":
            settings.settings_start()
        elif answer == "3":
            print("Вы вышли из игры")
            break



show_menu() # программа начинается здесь
