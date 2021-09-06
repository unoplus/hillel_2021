# Create by Bender
"""
Получение информации об обрабатываемом исключении, через второй параметр
в инструкции except
"""

try:
    # ошибка деления на 0
    x = 1 / 0
except (NameError, IndexError, ZeroDivisionError) as err:
    # название класса исключения
    print(err.__class__.__name__)
    # текст сообщения об ошибке
    print(err)
