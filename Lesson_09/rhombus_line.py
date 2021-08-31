# Create by Bender
"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах
полный ромб полный на половину с чертой
"""


def rhombus_line(high):
    for i in range(high - 1, -1, -1):
        print((' ' * i + '*' * ((high * 2 - 1) - i * 2)))
    for i in range(0, high):
        if i == high - 1:
            print((' ' * i + '*' * ((high * 2 - 1) - (i * 2))))
        if high - 1 > i > 0:
            print((' ' * i + '*' * ((high * 2 - 1) - (high * 2 - 2)) + ' ' * (((high * 2 - 3) - (i * 2)) // 2)
                   + "*" + ' ' * (((high * 2 - 3) - (i * 2)) // 2) + '*'))


if __name__ == "__main__":
    user_high = int(input("Ведите высоту фигуры: "))
    rhombus_line(user_high)
