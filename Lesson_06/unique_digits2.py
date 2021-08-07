# Create by Bender
"""
А вот в задаче спрашивается
Посчитайте, сколько уникальных чисел содержится одновременно как в первом списке, так и во втором.
Тоесть число уникально для первого. и для второго списка
Как на счет такого челенджа?
"""
# Если через генераторы списков, то решение совсем-совсем в одну строку не получится
from random import randint
new_list1 = []
new_list2 = []
user_list1 = [randint(1, 25) for i in range(10)]
user_list2 = [randint(1, 25) for i in range(10)]
[(new_list1.append(i)) for i in user_list1 if i not in user_list2]
[(new_list2.append(i)) for i in user_list2 if i not in user_list1]

# Ну как-то так можно решить эту задачу
print(f"{len(set(new_list1))}, {len(set(new_list2))}")

# Так конечно проще и быстрее, но тут получается общий посчёт элементов в обоих списках
print(f"{len(set.symmetric_difference(set(new_list1), set(new_list2)))}")
