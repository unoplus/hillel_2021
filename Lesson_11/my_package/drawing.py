# Create by Bender
"""
С помощью данного модуля можно вывести на экран некоторые геометрические фигуры.
Фигуры выводятся при помощи символов '*' и ' ', построчно. Вывести можно
следующие фигуры:
заполненый треугольник, пустотелый треугольник, ромб заполненый на половину,
ромб заполненый на половину с вертикальной полосой в центре.
"""

__all__ = ["triangle", "empty_triangle", "rhombus", "rhombus_line"]


def triangle(high: int):
    """
    Функция выводит на экран заполненный треугольник.
    :param high: Параметр высоты фигуры
    :return: Вывод фигуры на экран
    """
    for i in range(high - 1, -1, -1):
        print((' ' * i + '*' * ((high * 2 - 1) - i * 2)))


def empty_triangle(high: int):
    """
    Функция выводит на экран пустотелый треугольник.
    :param high: Параметр высоты фигуры
    :return: Вывод фигуры на экран
    """
    x = 1
    for i in range(high - 1, -1, -1):
        if (high - 1) > i > 0:
            print((' ' * i + '*' * ((high * 2 - 1) - (high * 2 - 2))
                   + ' ' * x + '*'))
            x += 2
        else:
            print((' ' * i + '*' * ((high * 2 - 1) - (i * 2))))


def rhombus(high: int):
    """
    Функция выводит на экран ромб заполненый на половину.
    :param high: Параметр высоты фигуры
    :return: Вывод фигуры на экран
    """
    for i in range(high - 1, -1, -1):
        print((' ' * i + '*' * ((high * 2 - 1) - i * 2)))
    for i in range(0, high):
        if i == high - 1:
            print((' ' * i + '*' * ((high * 2 - 1) - (i * 2))))
        if high - 1 > i > 0:
            print((' ' * i + '*' * ((high * 2 - 1) - (high * 2 - 2))
                   + ' ' * ((high * 2 - 3) - (i * 2)) + '*'))


def rhombus_line(high: int):
    """
    Функция выводит на экран ромб заполненый на половину с вертикальной полосой
    в центре.
    :param high: Параметр высоты фигуры
    :return: Вывод фигуры на экран
    """
    for i in range(high - 1, -1, -1):
        print((' ' * i + '*' * ((high * 2 - 1) - i * 2)))
    for i in range(0, high):
        if i == high - 1:
            print((' ' * i + '*' * ((high * 2 - 1) - (i * 2))))
        if high - 1 > i > 0:
            print((' ' * i + '*' * ((high * 2 - 1) - (high * 2 - 2))
                   + ' ' * (((high * 2 - 3) - (i * 2)) // 2)
                   + "*" + ' ' * (((high * 2 - 3) - (i * 2)) // 2) + '*'))
