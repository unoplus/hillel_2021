# Create by Bender

try:
    try:
        x = 1 / 0
    except NameError:
        print("Неопределённый идентификатор")
    except IndexError:
        print("Несуществующий индекс")
    # Обрабатываться не будет
    print("Выражение после вложенного try")
except ZeroDivisionError:
    print("Обработка деления на 0")
    x = 0

print(x)
