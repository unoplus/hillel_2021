# Create by Bender

def get_factorial(n: int) -> int:
    """
    Факториал числа!
    :param n: целочисленное факториал которого необходимо вычислить
    :return: возвращает целое число результат вычисления факториала от n
    """

    if n == 1 or n == 0:
        return 1
    else:
        return n * get_factorial(n - 1)


print(get_factorial(5))
