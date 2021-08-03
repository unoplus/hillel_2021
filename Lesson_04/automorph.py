# Create by Bender

"""
Натуральное число называется автоморфным, если оно равно последним цифрам своего квадрата.
Например, 25**2 = 625. Напишите программу, которая получает натуральное число и выводит
на экран все автоморфные числа, не превосходящие N.
"""

result, count, divider = 0, 1, 10

while True:
    cmd = input("Введите натуральное число: ")
    if cmd.isdigit():
        number = int(cmd)
        break

while result < number:
    result = count**2
    if count == divider:
        divider *= 10
    if (result * result) % divider == count:
        print(f"{count}**{count}={result}")
    count += 1
