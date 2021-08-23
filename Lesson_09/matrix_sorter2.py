# Create by Bender
"""
Написать функцию сортировки двухмерного списка МхМ (матрицы).
Значение М - задаётся пользователем, с клавиатуры. Может быть любым целым, положительным числом, больше 5.
"""
import random


def matrix_sorter(some_size):
    random_list = [[random.randint(1, 50) for j in range(some_size)] for i in range(some_size)]
    temp_list = []
    size_list = 0

    for i in range(some_size):
        for j in range(some_size):
            size_list += random_list[j][i]
        temp_list.append(size_list)
        size_list = 0
    random_list.append(temp_list)
    print_sorter(random_list)

    while size_list != size_matrix:
        for i in range(len(random_list)):
            if i == len(random_list) - 1:
                for j in range(0, i - 1):
                    if random_list[i][j + 1] < random_list[i][j]:
                        random_list[i][j], random_list[i][j + 1] = random_list[i][j + 1], random_list[i][j]
                        for bubble in range(len(random_list) - 1):
                            random_list[bubble][j], random_list[bubble][j + 1] \
                                = random_list[bubble][j + 1], random_list[bubble][j]
        size_list += 1

    for i in range(some_size - 1):
        for j in range(some_size):
            for bubble in range(some_size - i - 1):
                if j % 2 != 0:
                    if random_list[bubble + 1][j] < random_list[bubble][j]:
                        random_list[bubble][j], random_list[bubble + 1][j] \
                            = random_list[bubble + 1][j], random_list[bubble][j]
                else:
                    if random_list[bubble + 1][j] > random_list[bubble][j]:
                        random_list[bubble][j], random_list[bubble + 1][j] \
                            = random_list[bubble + 1][j], random_list[bubble][j]

    print_sorter(random_list)


def print_sorter(random_list):
    print()
    for i in range(len(random_list)):
        for j in range(len(random_list) - 1):
            print(f"{random_list[i][j] : > 4}", end="")
        print()


while True:
    size_matrix = int(input("Введите размер матрицы. Число должно быть больше 5: "))
    if size_matrix <= 5:
        print("Ваше число должно быть больше 5!")
    else:
        break

matrix_sorter(size_matrix)
