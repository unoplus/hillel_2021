# Create by Bender
"""
Реализовать приложение которое принимает на вход значение чисел от 3 до 9;
Выполняет проверку на правильность введеного числа в указаном диапазоне.
Если не в диапазоне - сообщает о проблеме и заканчивает работу.Иначе - печатает пирамиду из чисел.
"""

user_number = int(input("Введите число от 3 до 9: "))
if 3 <= user_number <= 9:
    for i in range(1, user_number + 1):
        result = " "
        for j in range(1, i):
            result += str(j)
        for j in range(i, 0, -1):
            result += str(j)
        print(result)
else:
    print("Вы ввели неверное значение!")
