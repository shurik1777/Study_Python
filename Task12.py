"""
Задача 12:
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает
два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет
сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""
sum_of_numbers = int(input('Введите сумму задуманных чисел: '))
product_of_numbers = int(input('Введите произведение суммы чисел: '))

number_x = 1
number_y = 1

if product_of_numbers == 0:
    number_x = 0
    number_y = sum_of_numbers
else:
    for number_x in range(1, sum_of_numbers // 2 + 1):
        number_y = sum_of_numbers - number_x
        if number_x * number_y == product_of_numbers:
            print(f"Первое число равно {int(number_x)}, а второе равно: {int(number_y)}")
            break
        else:
            continue
        break
    else:
        print("Данная комбинация не соответствует")

