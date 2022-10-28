import os

def show_player_stats(player_name, player_hp, player_money, player_potions):
    os.system("cls")
    print(f"имя:{player_name}")
    print(f"здоровье:{player_hp}")
    print(f"деньги:{player_money}")
    print(f"зелья:{player_potions}")

