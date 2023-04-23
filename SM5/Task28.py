'''
Задача 28:
Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются
только +1 и -1.
Также нельзя использовать циклы.

*Пример:*

2 2
    4
'''

number_one = int(input('Введите целое не отрицательно число: '))
number_second = int(input('Введите второе целое не отрицательно число: '))


def sum_numbers(number_one_in, number_second_in):
    if number_second_in == 0:
        return number_one_in
    else:
        return sum_numbers(number_one_in + 1, number_second_in - 1)


print(f'Результат -  {sum_numbers(number_one, number_second)}')
