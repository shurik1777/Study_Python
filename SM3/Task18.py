import random

number_arr = int(input("Введите количество элементов в массиве натуральным числом: "))
items = [random.randint(1, number_arr * 100) for _ in range(number_arr)]
x_number = int(input("Задайте число к которому нужно найти ближайшее из массива: "))

res = items[0]  # допустим, ближайшее число к искомому первое в списке
for item in items:
    if abs(x_number - item) < abs(x_number - res):
        res = item

print(items)
print(f"Ближайшее число к числу {x_number} является {res}")
