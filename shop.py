import os
import player_stats
def visit_shop(player):
    while True:
        os.system("cls")
        player_stats.show_player_stats(player)
        print(f"{player} приехал в магазин")
        print("1 - Купить зелье, цена 10 р")
        print("2 - Уйти к камню")
        answer = input("Сделайте выбор и нажмите ENTER ")           
        if answer == "1":
            os.system("cls")
            if player[2] >= 10:
                player[2] -= 10
                player[3] += 1
                print("Купили зелье")
            else:
                print("У вас нет денег!")    
                input("Сделайте выбор и нажмите ENTER ")
            if answer == "2":
                return player
            





