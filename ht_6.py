# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
#


# Решение

a1 = int(input('Введите a1 --> '))
d = int(input('Введите d --> '))
n = int(input('Введите n --> '))

s = [a1 + (i - 1) * d for i in range(1, n+1)]
print(s)

# ------------------------------------------------------------------------------------------------------------

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Решение

import random

s = [random.randint(1, 100) for i in range(10)]
n = []

a_min = int(input('Введите min --> '))
a_max = int(input('Введите max --> '))

for i in range(len(s)):
    if (s[i]>=a_min) and (s[i]<=a_max):
        n.append(i)

print(n)
