import os
import random


def visit_casino(player):
    name = player[0]
    hp = player[1]
    money = player[2]
    potions = player[3]
    os.system("cls")
    casino_money = 100
    while money and casino_money:
