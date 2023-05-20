"""Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов,
то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Стихотворение Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
    **Вывод:** Парам пам-пам"""
str_str = input('Нужно ввести -> пара-ра-рам рам-пам-папам па-ра-па-да '
                '\n или -> пара ра рам рам пам папам па ра па да:\n').split()
chant = [sum(1 for ch in word if ch in 'аяуюоеёэиы') for word in str_str]
if len(set(chant)) == 1:
    print("Парам пам-пам -> с ритмом все в порядке")
else:
    print("Пам парам -> нет ритма")

