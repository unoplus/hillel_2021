# Create by Bender

import sys

# Сохраняем ссылку на sys.stdin
tmp_in = sys.stdin
# ткрываем  файл на чтение
fid = open(r"file.txt")
sys.stdin = fid

while True:
    try:
        # Считываем строку из файла
        line = input()
        # Выводим строку
        print(line)
    except EOFError:
        # Если достигнут конец файла
        break

# возвращаем объект потока в переменную sys.stdin
sys.stdin = tmp_in
fid.close()

