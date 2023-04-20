'''
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах. Пользователь вводит 2 числа.
n — кол-во элементов первого множества.
m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
'''

import random

len_a = int(input("Введите длину первого списка: "))
len_b = int(input("Введите длину второго массива: "))

list_a = []
list_b = []

for i in range(len_a):
    list_a.append(random.randint(0, 9))
print(list_a)

for i in range(len_b):
    list_b.append(random.randint(0, 9))
print(list_b)

set_a = set(list_a)
set_b = set(list_b)

resulting_set = set_a.intersection(set_b)
resulting_list = list(resulting_set)

print("Результат по возрастающей: ")
print(sorted(resulting_list))
