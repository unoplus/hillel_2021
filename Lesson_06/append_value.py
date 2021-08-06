# Create by Bender
"""
Дан список целых чисел (можно сгенерировать при помощи генератора случайных чисел),
число k и значение C. Необходимо вставить в список на позицию с индексом k значение C,
сдвинув все элементы, с индексом большим k, вправо. Поскольку при этом количество элементов
в списке увеличивается, в конец списка нужно будет добавить новый элемент (любое значение),
используя метод append().
- Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе
и не создавая дополнительного списка.
- Использовать метод insert() не разрешается.
"""

from random import randint

k = 4
C = 25
user_list = [randint(1, 25) for i in range(10)]
user_list.append(randint(1, 25))

for i in range(len(user_list)-1, k, -1):
    user_list[i] = user_list[i-1]

user_list[k] = C
print(user_list)
