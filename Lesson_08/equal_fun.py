# Create by Bender

"""
Написать функцию которая принимает на вход параметры : список чисел любой дины и число .
Функция должна проверить есть ли в списке 2 числа сума которых еквивалентна числу переданому 2м параметром.
Функция должна вернуть булевое значение - результат поиска фукции.
Для проверки вызвать 2 раза функцию с разными тестовыми примерами.
"""
import random


# С заранее определённым списком и числом
user_list = [1, 1, 3, 5, 13, 8]
user_list2 = [2, 1, 4, 5, 13]
num = 14
num2 = 11


def comparison_func(lst, val):
    result = 0
    for i in lst:
        for j in lst:
            result = i + j
            yield result == val
        else:
            yield result == val


answer = 0
comparison = comparison_func(user_list, num)
for answer in comparison:
    if answer:
        print(answer)
        break
else:
    print(answer)

comparison = comparison_func(user_list2, num2)
for answer in comparison:
    if answer:
        print(answer)
        break
else:
    print(answer)


# С использованием генераторов
def comparison_func2(random_list, random_num):
    result2 = 0
    print(random_list, random_num)
    for x in random_list:
        for y in random_list:
            result2 = x + y
            yield result2 == random_num
        else:
            yield result2 == random_num


answer2 = 0
comparison2 = comparison_func2([random.randint(1, 25) for i in range(10)], random.randint(1, 25))
for answer2 in comparison2:
    if answer2:
        print(answer2)
        break
else:
    print(answer2)

comparison2 = comparison_func2([random.randint(33, 55) for i in range(10)], random.randint(66, 99))
for answer2 in comparison2:
    if answer2:
        print(answer2)
        break
else:
    print(answer2)
