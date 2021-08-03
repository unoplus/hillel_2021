# Create by Bender

"""
Ввести натуральное число и определить, верно ли, что в его записи есть две одинаковые цифры
(необязательно стоящие рядом).
Рассмотрим два случая, когда пользователь вводит число, которое передаётся как строка
и когда пользователь вводит число, которое передаётся как число.
Данный файл "num_int_same.py" описывает реализацию числа как число.
"""

# Число как число
result = []
count = 0
while True:
    cmd = input("Введите натуральное число: ")
    if cmd.isdigit():
        number = int(cmd)
        break

find_number = list(str(number))
for i in find_number:
    if i not in result:
        result.append(i)
    else:
        count += 1

if count > 0:
    print(f"{number}\nДа.")
else:
    print(f"{number}\nНет.")
