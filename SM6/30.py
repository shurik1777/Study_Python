'''
Задача 30:
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов
нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''


def get_number_from_console(message):
    while True:
        try:
            return int(input(message))
            break
        except:
            print("Введите натуральное число")


start = get_number_from_console("Введите начальный элемент: ")
dif = get_number_from_console("Введите разность: ")
num_of_elements = get_number_from_console("Введите количество элементов: ")

result = [start + (i - 1) * dif for i in range(1, num_of_elements + 1)]
print(result)
