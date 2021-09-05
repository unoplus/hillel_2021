# Create by Bender
"""
Создать текстовый файл, записать в него, построчно,
данные которые вводит пользователь. Окончанием ввода служит пустая строка.
Каждая введённая строка, в файле, должна начинаться с новой строки.
"""


def some_text(user_input="Game Start") -> str:
    """
    Функция записывает пользовательский ввод в файл, начиная с новой строки
    каждый новый ввод строки пользователем.
    Для записи в файл вызывает себя рекурсивно.
    :param user_input: Начальная строка, задана по умолчанию.
    :return:           Возвращает строку
    """

    if user_input == "":
        return "Game Over!"
    else:
        f = open("user_input.txt", "a")
        user_input = input("For close use empty string: ")
        f.write(user_input + "\n")
        f.close()
        return some_text(user_input)


if __name__ == "__main__":
    print(some_text())
