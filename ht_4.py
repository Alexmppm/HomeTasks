# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.


# Решение

#
# print('Задача 20')
#
#
# n = int(input('Введите n --> '))
# m = int(input('Введите m --> '))
#
# list1 = [input(f'{i+1} ---> ') for i in range(n)]
# print('\n')
# list2 = [input(f'{i+1} ---> ') for i in range(m)]
#
# set1 = set(list1)
# set2 = set(list2)
#
# newlist = list(set1&set2)
# newlist.sort()
#
# print(*newlist)


# ----------------------------------------------------------------------------------------------------

#
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте
# выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Решение


gbed = [1, 4, 5, 6, 2, 9, 1, 3, 5, 12] # грядка

n = len(gbed)
gbed.append(gbed[0])
gbed.insert(0, gbed[-2])

h = [(gbed[i-1]+gbed[i]+gbed[i+1]) for i in range(1, n+1)]

print(f'Максимальный сбор {max(h)} ягод при сборе с куста {h.index(max(h))+1} и соседних')


