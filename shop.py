def visit_shop(player_name, player_hp, player_money, player_potions):
    os.system("cls")
    player_stats.show_player_stats(player_name, player_hp, player_money, player_potions)
    print(f"{player_name} приехал в магазин")
    print("1 - Купить зелье, цена 10 р")
    print("2 - Уйти к камню")
    input("Сделайте выбор и нажмите ENTER ")

    if answer == "1":
        player_money >= 10
        player_money -= 10
        player_potions += 1






