# Create by Bender

"""
Напишите программу, которая получает натуральнве числа А и В (А < В)
и выводит простые числа в интервале от А до В.
"""

sum_numbers = 0
while True:
    num1, num2 = input("Введите границы диапазона через пробел: ").split(" ")
    if num1.isdigit() and num2.isdigit():
        A = int(num1)
        B = int(num2)
        if A < B:
            break
        else:
            print("Второе число должно быть больше первого!")
    else:
        print("Ведите числа!")

for i in range(A, B+1):
    for k in range(2, i):
        if i % k == 0:
            break
    else:
        print(i)

