# Create by Bender
"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах
полный треугольник
"""


def triangle(high):
    for i in range(high - 1, -1, -1):
        print((' ' * i + '*' * ((high * 2 - 1) - i * 2)))


if __name__ == "__main__":
    user_high = int(input("Ведите высоту фигуры: "))
    triangle(user_high)
