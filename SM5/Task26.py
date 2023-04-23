'''
Задача 26:
Напишите программу, которая на вход принимает
два числа A и B, и возводит число А
в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
'''
number = int(input('Введите число: '))
deg = int(input('Введите в какую целую степень возводить число выше: '))


def get_degree(number_in, deg_in):
    if deg_in == 0:
        return 1
    elif deg_in == 1:
        return number_in
    elif deg_in < 0:
        return 1 / (number_in * get_degree(number_in, abs(deg_in) - 1))
    else:
        return number_in * get_degree(number_in, deg_in - 1)


print(f'Результат возведения -  {get_degree(number, deg)}')
