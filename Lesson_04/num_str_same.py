# Create by Bender

"""
Ввести натуральное число и определить, верно ли, что в его записи есть две одинаковые цифры
(необязательно стоящие рядом).
Рассмотрим два случая, когда пользователь вводит число, которое передаётся как строка
и когда пользователь вводит число, которое передаётся как число.
Данный файл "num_str_same.py" описывает реализацию числа как строки.
"""

# Число как строка (можно решить несколькими способами, на свой вкус представлю два;))
# Способ 1, сортировка.
count = 0
while True:
    number = input("Введите натуральное число: ")
    if number.isdigit():
        break

same_number = sorted(number)
for i in range(len(same_number)-1):
    if same_number[i] == same_number[i + 1]:
        count += 1

if count > 0:
    print(f"{number}\nДа.")
else:
    print(f"{number}\nНет.")

# Способ 2, разница "весов" (понимаем, что цикл "wile" выполняется и для участка кода ниже).
same_number2 = set(number)
if len(same_number2) != len(number):
    print(f"{number}\nДа.")
else:
    print(f"{number}\nНет.")
