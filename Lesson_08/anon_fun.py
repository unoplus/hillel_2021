# Create by Bender

"""
Написать анонимную функцию которая приниммает 2 значения x,y,
где y по умолчанию == числу. Результат работы функции - число x  в степени y.
Используя функцию map получить список чисел которые утворились в результате применения
лямбда функции к каждому элементы.
Для проверки привести тестовый пример в консоль.
"""

import random

# С заранее определённым списком и числом
user_list = [1, 1, 2, 3, 4, 2, 5]
a = 3
print(list(map((lambda x, y=2: x**y), user_list, len(user_list) * [a])))

# С использованием генератора range
print(list(map((lambda x, y=2: x**y), range(10), 10 * [random.randint(1, 10)])))

# С использованием генератора списков
print(list(map((lambda x, y=2: x**y),
               [random.randint(1, 25) for i in range(10)],
               len([random.randint(1, 25) for i in range(10)]) * [random.randint(1, 10)])))
