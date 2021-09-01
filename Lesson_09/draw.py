# Create by Bender
"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах
полый треугольник, полный треугольник, ромб полный на половину, ромб полный на половину с чертой
"""

# full triangle
# n = 5
# x = "*"
# for i in range(n - 1, 0, -1):
#     print((' ' * i + '*' * ((n*2-1) - i * 2)))

# empty triangle
n = 5
x = 1
for i in range(n - 1, -1, -1):
    if (n - 1) > i > 0:
        print((' ' * i + '*' * ((n * 2 - 1) - (n * 2 - 2)) + ' ' * x + '*'))
        x += 2
    else:
        print((' ' * i + '*' * ((n * 2 - 1) - (i * 2))))

# rhombus
n = 10
for i in range(n - 1, -1, -1):
    print((' ' * i + '*' * ((n * 2 - 1) - i * 2)))
for i in range(0, n):
    if i == n - 1:
        print((' ' * i + '*' * ((n * 2 - 1) - (i * 2))))
    if n - 1 > i > 0:
        print((' ' * i + '*' * ((n * 2 - 1) - (n * 2 - 2)) + ' ' * (((n * 2 - 3) - (i * 2)) // 2)
               + "*" + ' ' * (((n * 2 - 3) - (i * 2)) // 2) + '*'))

# for i in range(0, n - 1):
#     print((' ' * i + '*' * ((n*2-1) - i * 2)))

# n = 4
# s = "*"
# for i in range(0, n, 1):
#     if i == 0 or i == n - 1:
#         print(s * n)
#     else:
#         print(s + (" " * (n - 2)) + s)
#
# n = 4
# table = ("*  *" if i not in [0, n-1] else '****' for i in range(n))
# for row in table:
#     print(row)

# n = 7
# for i in range(n*2-1, 0, -1):
#     print(' ' * -i + '*' * ((n*2-1) - i * 2) + ' ' * -i)
