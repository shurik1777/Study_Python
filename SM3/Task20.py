'''
Задача 20:
В настольной игре Скрабл (Scrabble)
 каждая буква имеет определенную ценность.
 В случае с английским алфавитом очки распределяются так:
 A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
 B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков;
 J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так:
 А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
 Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
 Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.

 Напишите программу, которая вычисляет стоимость введенного
 пользователем слова. Будем считать, что на вход подается
 только одно слово, которое содержит либо только английские,
 либо только русские буквы.

*Пример:*
ноутбук
    12
'''
points = {1:'AEIOULNSTRАВЕИНОРСТ',
      2:'DGДКЛМПУ',
      3:'BCMPБГЁЬЯ',
      4:'FHVWYЙЫ',
      5:'KЖЗХЦЧ',
      8:'JZШЭЮ',
      10:'QZФЩЪ'}
text = input("Введите слово на русском или английском: ").upper()

cost = 0
for char in text:
    for key, val in points.items():
        if char in val:
            cost += key
print(f"Через перебор = {cost}")

scrabble = {}

scrabble.update(dict.fromkeys('AEIOULNSTRАВЕИНОРСТ', 1))
scrabble.update(dict.fromkeys('DGДКЛМПУ', 2))
scrabble.update(dict.fromkeys('BCMPБГЁЬЯ', 3))
scrabble.update(dict.fromkeys('FHVWYЙЫ', 4))
scrabble.update(dict.fromkeys('KЖЗХЦЧ', 5))
scrabble.update(dict.fromkeys('JZШЭЮ', 8))
scrabble.update(dict.fromkeys('QZФЩЪ', 10))

print(f"Через словарь {sum(scrabble[char] for char in text)}")
