
path_to_links = "X:/Prog/Python/requests/"
staff_file = "staff_status.txt"
tested_file = "tested_status.txt"


def read_file(some_path: str) -> list:
    """
    Функция принимает путь с файлом, читает его и сохраняет текст
    :param some_path: Передаёт путь к файлу
    :return: Возвращает текст файла
    """
    try:
        with open(some_path, "r") as some_file:
            some_text = some_file.readlines()
    except Exception as e:
        print(e)

    return some_text


def create_dict(*args: tuple) -> dict:
    """
    Функция принимает кортеж строк и преобразует его в словарь
    :param args: Принимает кортеж из строк
    :return: Возвращает словарь
    """
    some_dict = {}
    value = ""
    for line in args:
        key, *tmp = line.split()
        # Преобразуем полученый список "*tmp" в нормальную строку, для случая,
        # когда ответ от ссылки приходит не цифровым кодом, а каким-то текстом и
        # передаём полученную строку как значение в словарь.
        for i in tmp:
            value += " ".join([i, ""])
        some_dict[key] = value
        value = ""

    return some_dict


def create_diff_dict(staff_dict: dict, tested_dict: dict) -> dict:
    """
    Функция принимает два словоря, вычисляет разность и возвращает новый словарь
    с этой разностью
    :param staff_dict:  Словарь, который служит эталоном
    :param tested_dict: Словарь в котором мы ищем расность с эталоном
    :return: Возврат нового словаря с разностью, либо пустого
    """
    diff_dict = {}
    diff_dict.update({key: staff_dict[key] for key in staff_dict
                      if key not in tested_dict})
    diff_dict.update({key: tested_dict[key] for key in tested_dict
                      if key not in staff_dict})
    diff_dict.update({key: tested_dict[key] for key in tested_dict
                      if key in staff_dict and
                      tested_dict[key] != staff_dict[key]})

    return diff_dict


if __name__ == "__main__":
    staff_status = read_file(path_to_links + staff_file)
    print(staff_status)
    staff_responses = create_dict(*staff_status)

    tested_status = read_file(path_to_links + tested_file)
    tested_responses = create_dict(*tested_status)

    print(create_diff_dict(staff_responses, tested_responses))
