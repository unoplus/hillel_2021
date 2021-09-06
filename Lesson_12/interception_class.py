# Create by Bender

a = 12

try:
    x = a / 0
except ZeroDivisionError:
    print("Обработали деление на 0")
    x = 0

print(x)
