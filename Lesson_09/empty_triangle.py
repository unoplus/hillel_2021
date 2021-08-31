# Create by Bender
"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах
полный треугольник
"""


def empty_triangle(high):
    x = 1
    for i in range(high - 1, -1, -1):
        if (high - 1) > i > 0:
            print((' ' * i + '*' * ((high * 2 - 1) - (high * 2 - 2)) + ' ' * x + '*'))
            x += 2
        else:
            print((' ' * i + '*' * ((high * 2 - 1) - (i * 2))))


if __name__ == "__main__":
    user_high = int(input("Ведите высоту фигуры: "))
    empty_triangle(user_high)
