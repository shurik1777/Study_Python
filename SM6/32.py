'''
Задача 32:
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
from random import randint

n = int(input('Введите количество элементов: '))
minim = int(input('Минимальный старт чисел: '))
maxim = int(input('Максимальный финиш чисел: '))

my_list1 = []
my_list2 = []

for i in range(n):
    my_list1.append(randint(-10, 10))

print(my_list1)

for i in range(n):
    if minim <= my_list1[i] <= maxim:
        my_list2.append(my_list1[i])

print(my_list2)
