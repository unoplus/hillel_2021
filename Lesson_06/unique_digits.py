# Create by Bender
"""
Даны два списка чисел (можно сгенерировать при помощи генератора случайных чисел).
Посчитайте, сколько уникальных чисел содержится одновременно как в первом списке, так и во втором.
- Примечание. Эту задачу можно решить в одну строчку. (+ 5 балов если задача решена в одну строчку)
"""
# Если через генераторы списков, то решение совсем-совсем в одну строку не получится
from random import randint

# user_list1 = [randint(1, 25) for i in range(10)]
# user_list2 = [randint(1, 25) for i in range(10)]
user_list1 = [1, 1, 2, 3, 4, 3]
user_list2 = [5, 6, 6, 7, 2]

count = 0
"""for i in user_list1 + user_list2:
    if (user_list1 + user_list2).count(i) == 1:
        count += 1

print(count)"""
print(len([count for i in user_list1 + user_list2 if (user_list1 + user_list2).count(i) == 1]))
"""print(f"{len(set(user_list1))} {len(set(user_list2))}")

# А если задаёт пользователь, то решение в одну строку такое
#print(f"{len(set(input('Введите числа первого набора, через запятую: ').split(',')))} \n"
#      f"{len(set(input('Введите числа второго набора, через запятую: ').split(',')))}")
print(f"{len(set(input('Введите числа первого набора, через запятую: ').split(',')))}\n
{len(set(input('Введите числа второго набора, через запятую: ').split(',')))"}"""
