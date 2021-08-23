# Create by Bender
"""
Дана монотонная последовательность, в которой каждое натуральное число k встречается ровно k раз:
1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ...
По данному натуральному n выведите первые n членов этой последовательности. Попробуйте обойтись только одним циклом for.
"""


def count_first(nums, n):
    j = 1
    if n == 0:
        return None

    if n == 1:
        return 1

    for i in range(1, n):
        print(j, end=" ")
        if i == j * (j + 1) // 2:
            j += 1

    return j


if __name__ == "__main__":
    print(count_first(None, 5))
