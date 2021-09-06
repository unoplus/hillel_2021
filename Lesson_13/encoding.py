# Create by Bender

fid = open(r"file.txt", "w", encoding="utf-8")
# Записываем строку в файл
fid.write("Строка")

with open(r"file.txt", "r", encoding="utf-16") as f:
    for line in f:
        print(line)
