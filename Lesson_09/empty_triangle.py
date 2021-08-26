# Create by Bender
"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах
полный треугольник
"""

n = int(input("Ведите высоту фигуры: "))
x = 1
for i in range(n - 1, -1, -1):
    if (n - 1) > i > 0:
        print((' ' * i + '*' * ((n * 2 - 1) - (n * 2 - 2)) + ' ' * x + '*'))
        x += 2
    else:
        print((' ' * i + '*' * ((n * 2 - 1) - (i * 2))))
