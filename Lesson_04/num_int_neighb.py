# Create by Bender

"""
Ввести натуральное число и определить, верно ли, что в его записи есть две одинаковые цифры
стощие рядом.
Рассмотрим два случая, когда пользователь вводит число, которое передаётся как строка
и когда пользователь вводит число, которое передаётся как число.
Данный файл "num_int_neighb.py" описывает реализацию числа как число.
"""

# Число как число
count = 0
while True:
    cmd = input("Введите натуральное число: ")
    if cmd.isdigit():
        number = int(cmd)
        break

find_number = list(str(number))
for i in range(len(find_number)-1):
    if find_number[i] == find_number[i + 1]:
        count += 1

if count > 0:
    print(f"{number}\nДа.")
else:
    print(f"{number}\nНет.")
