# Create by Bender

try:
    x = 1 / 0
# Обработка сразу нескольких исключений
except (NameError, IndexError, ZeroDivisionError):
    x = 0
print(x)
