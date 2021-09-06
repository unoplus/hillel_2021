# Create by Bender

import sys

tmp_out = sys.stdout
fid = open(r"file.txt", mode="a")
sys.stdout = fid
print("Эта строка должна оказаться записаной в файле")
sys.stdout = tmp_out
print("A теперь: пишем строку в стандартный вывод")
# Закрываем файл
fid.close()

# Но print() поддерживает перенарправление печати в файл
with open(r"file.txt", mode="a") as fid:
    print("Ещё и эта строка должна оказаться записаной в файле", file=fid)
