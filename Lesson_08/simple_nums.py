# Create by Bender

"""
создать функцию генератор простых чисел в дипазоне заданых 2мя аргументами чисел.
Вывести в консоль результат работы функции-генератора  в диапазоне 1, 100 в одну строчку через пробел.
"""


def simple_num(start, end):
    if start == 0 or start == 1:
        start = 2

    for i in range(start, end):
        if all(i % j != 0 for j in range(start, i)):
            print(i, end=" ")


simple_num(1, 100)
