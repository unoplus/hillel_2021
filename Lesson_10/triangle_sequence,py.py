# Create by Bender
"""
Решение последовательности через рекурсию.
"""


def count_first(nums, n, i=1, j=1):
    if n == 0:
        return None

    if n == 1:
        return 1

    if i == (n + 1):
        return nums

    if i == j * (j + 1) // 2:
        nums += str(j) + ", "
        j += 1
        i += 1
    else:
        nums += str(j) + ", "
        i += 1

    return count_first(nums, n, i, j)


if __name__ == "__main__":
    print(count_first("", 5))
