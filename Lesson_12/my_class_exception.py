# Create by Bender
"""
Можно создать свой класс для использования собственного исключения
"""


class MyError(Exception):
    def __init__(self, value):
        self.msg = value

    def __str__(self):
        return self.msg


# Обработка пользовательского исключения
try:
    raise MyError("Описание исключения")
except MyError as err:
    # Вызывается метод __str__()
    print(err)
    # Обращение к атрибуту класса
    print(err.msg)

# Повторно возбуждаем исключение raise MyError ("Описание исключения")
raise MyError("Описание исключения")
