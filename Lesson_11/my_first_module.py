# Create by Bender
"""
Пишем и подключаем свой модуль.
"""


def get_integer_from_input() -> int:
    """
    function to demo modules
    :return: integer - number which user should input
    """
    n: int = 0

    while True:
        str_n = input("your positive number: ")
        if str_n.isnumeric():
            n = int(str_n)
            break
        else:
            print("Input is not correct please try again")

    return n


if __name__ == "__main__":
    print(get_integer_from_input())
    