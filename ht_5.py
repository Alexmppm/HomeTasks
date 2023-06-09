# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень
# B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
# Решение

print('\n')
print('Задача 26')

def Expon(n, m):
    if m:
        return(n * Expon(n, m-1))
    else:
        return(1)

a = int(input('Введите A --> '))
b = int(input('Введите B --> '))

print(Expon(a, b))

# ----------------------------------------------------------------------------------------------------


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

# Решение

print('\n')
print('Задача 28')

def Summ(n, m):
    if m==0:
        return(n)
    else:
        return(1 + Summ(n, m-1))

a = int(input('Введите a --> '))
b = int(input('Введите b --> '))

print(Summ(a, b))