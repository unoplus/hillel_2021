# Create by Bender
"""
Написать функцию сортировки двухмерного списка МхМ (матрицы).
Значение М - задаётся пользователем, с клавиатуры. Может быть любым целым, положительным числом, больше 5.
"""
import random


def matrix_sorter(size_matrix):
    random_list = [[random.randint(1, 50) for j in range(size_matrix)] for i in range(size_matrix)]
    for i in range(len(random_list)):
        size_list = 0
        temp_list = []

        for j in range(len(random_list)):
            temp_list.append(random_list[i][j])
            size_list += random_list[i][j]
        temp_list.append(size_list)
        random_list[i] = temp_list
        size_list = 0
    print_sorter(random_list)

    while size_list != size_matrix:
        for i in range(len(random_list) - 1):
            for j in range(size_matrix, size_matrix + 1):
                if random_list[i + 1][j] < random_list[i][j]:
                    random_list[i], random_list[i + 1] = random_list[i + 1], random_list[i]
        size_list += 1

    for num in range(size_matrix):
        temp_list = random_list[num]
        print(temp_list)
        size_list = len(temp_list)
        if num % 2 != 0:
            for i in range(size_list - 1):
                for j in range(size_list - 3, i - 1, -1):
                    if temp_list[j + 1] < temp_list[j]:
                        temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
        else:
            for i in range(size_list - 1):
                for j in range(size_list - 3, i - 1, -1):
                    if temp_list[j + 1] > temp_list[j]:
                        temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]

    print_sorter(random_list)


def print_sorter(random_list):
    print()
    for i in range(len(random_list) + 1):
        for j in range(len(random_list)):
            print(f"{random_list[j][i] : > 4}", end="")
        print()


while True:
    size_matrix = int(input("Введите размер матрицы. Число должно быть больше 5: "))
    if size_matrix <= 5:
        print("Ваше число должно быть больше 5!")
    else:
        break

matrix_sorter(size_matrix)