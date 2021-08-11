# Create by Bender

"""
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке,
так и во втором.
- Примечание. Эту задачу на python можно решить в одну строчку.
"""

from random import randint

# С заранее определёнными списками
user_list1 = [1, 1, 2, 3, 4, 2, 5]
user_list2 = [6, 7, 8, 5, 3]

print(len(set.intersection(set(user_list1), set(user_list2))))

# С использованием генераторов
print(len(set.intersection(set([randint(1, 25) for i in range(10)]), set([randint(10, 50) for j in range(15)]))))
