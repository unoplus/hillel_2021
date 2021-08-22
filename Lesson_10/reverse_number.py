# Create by Bender
"""
Дано число n, десятичная запись которого не содержит нулей. Получите число, записанное теми же цифрами,
но в противоположном порядке.
При решении этой задачи нельзя использовать циклы, строки, списки, массивы,
разрешается только рекурсия и целочисленная арифметика.
Фунция должна возвращать целое число, являющееся результатом работы программы, выводить число по одной цифре нельзя.
"""


def reverse_it(user_num: int, reverse_num=0) -> int:
    """
    Разворот числа
    :param reverse_num: возвращает число задом на перёд
    :param user_num:    целочисленное значение, которое вводит пользователь
    :return:            возвращает результат
    """
    if user_num > 0:
        result = user_num % 10
        reverse_num = reverse_num * 10
        reverse_num = reverse_num + result
        return reverse_it(user_num // 10, reverse_num)
    else:
        return reverse_num


if __name__ == "__main__":
    print(179, end=" => ")
    print(reverse_it(179))
