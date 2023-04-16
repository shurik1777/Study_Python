"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""

import random

coins = int(input("Введите количество монеток: "))
side_coin = 0
nut_count = 0
eagle_count = 0

for i in range(coins):
    side_coin = random.randint(0, 1)
    if side_coin == 0:
        nut_count += 1
        print("Решка")
    else:
        eagle_count += 1
        print("Орёл")

print(
    f"Чтобы все монетки лежали одной стороной, нужно перевернуть минимум "
    f"{nut_count if nut_count < eagle_count else eagle_count} монет(ы)")
