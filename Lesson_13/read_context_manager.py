# Create by Bender
"""
Не нужно вызывать метод close используя менеджер контекста
"""

with open("file_w.txt", mode="r") as fid:
    print(fid.read())
