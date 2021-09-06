# Create by Bender

class MyError(Exception):
    pass


try:
    raise MyError("Сообщение об ошибке")
except MyError as err:
    print(err)
    # Повторно возбуждаем
    raise
