# Create by Bender

"""
Ввести натуральное число и найти сумму его цуфр.
Пример:
Введите натуральное число:
12345
Сумма цифр 15.
"""
sum_numbers = 0
while True:
    cmd = input("Введите натуральное число: ")
    if cmd.isdigit():
        number = int(cmd)
        break

list_of_numbers = list(str(number))
for i in list_of_numbers:
    sum_numbers += int(i)

print(sum_numbers)
