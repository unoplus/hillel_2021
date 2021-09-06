# Create by Bender

f = open(r"file.txt")
for line in f:
    print(line.rstrip("\n"), end=" ")
f.close()
