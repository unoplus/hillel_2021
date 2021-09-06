# Create by Bender

try:
    raise ValueError("Описание исключения")
except ValueError as msg:
    # Выведет: Описание исключения
    print(msg)
