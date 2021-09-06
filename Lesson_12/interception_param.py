# Create by Bender

a = 12

try:
    x = a / 0
except ZeroDivisionError as e:
    print(f"Обработали исключение: {e}")
    x = 0

print(x)
