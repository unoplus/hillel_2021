# Create by Bender
"""
Даны числа a и b. Определите, сколько существует последовательностей из a нулей и b единиц,
в которых никакие два нуля не стоят рядом.
"""


def without_00(a, b):
    if a > b + 1:
        return 0
    if a == 0 or b == 0:
        return 1

    return without_00(a, b - 1) + without_00(a - 1, b - 1)


if __name__ == "__main__":
    print(without_00(2, 2))
