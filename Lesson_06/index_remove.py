# Create by Bender
"""
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k,
сдвинув влево все элементы, стоящие правее элемента с индексом k.
- Программа получает на вход список (можно сгенерировать при помощи генератора случайных чисел),
затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка
при помощи метода pop() без параметров.
- Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k)
с параметром или оператор del.
"""

from random import randint

k = 4
user_list = [randint(1, 25) for i in range(10)]
for i in range(k+1, len(user_list)-1):
    user_list[i] = user_list[i+1]

user_list.pop()
print(user_list)
