# Create by Bender
"""
Демонстрация работы с импортированными пакетами и модулями.
Скрипт сортирует сгенерированный список, сортированный список будет
сконвертирован в число, с той же последовательностью элементов,
которое затем будет развёрнуто задом на перёд и выведено на экран.
"""

import random
from my_package import algorithms as al
import my_sorter_module as sort

help(al)
help(sort)


def list_to_num(some_list: list) -> int:
    """
    Функция служит для конвертирования списка в число
    с той же последовательностью элементов и вызова
    функции для разворота полученного числа
    :param some_list: Принимает сортированный список
    :return:          Возвращае число задом на перёд
    """
    some_string = ""
    for i in some_list:
        some_string += str(i)
    some_num = int(some_string)
    return al.reverse_it(some_num)


list_gen = [random.randint(1, 25) for i in range(10)]
print(f"This is unsorted list: {list_gen}")

bubble_list = sort.bubble_sort(list_gen)
print(f"This is bubble_sort list: {bubble_list}")

quick_list = sort.quick_sort(list_gen)
print(f"This is quick_sort list: {quick_list}")

print(list_to_num(quick_list))
