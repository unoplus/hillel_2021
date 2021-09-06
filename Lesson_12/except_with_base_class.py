# Create by Bender

try:
    # ошибка деления на 0
    x = 1 / 0
except ArithmeticError as e:
    print(f"Handle error: {e}")
