'''
Задача 24:
В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора
на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
'''

import random

num_of_bushes = int(input("Введите количество кустов: "))
bushes = []

for i in range(num_of_bushes):
    bushes.append(random.randint(1, 10))
print(bushes)

max_sum = bushes[num_of_bushes - 1] + bushes[0] + bushes[1]
max_sum_index = 0
bushes_sum = bushes[num_of_bushes - 2] + bushes[num_of_bushes - 1] + bushes[0]

if bushes_sum > max_sum:
    max_sum = bushes_sum
    max_sum_index = (num_of_bushes - 1)

for i in range(1, num_of_bushes - 1):
    bushes_sum = bushes[i - 1] + bushes[i] + bushes[i + 1]
    if bushes_sum > max_sum:
        max_sum = bushes_sum
        max_sum_index = i
print(f"Максимальное количество ягод будет собрано с "
      f"{max_sum_index + 1 if max_sum_index < num_of_bushes - 1 else num_of_bushes} куста и двух соседних")
