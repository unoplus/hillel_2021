#! /usr/bin/env python3
# creata @cyberscriptor

import sys
import re

__all__ = ["read_file", "create_dict", "create_diff_dict"]


def read_file(some_path: str) -> list:
    """
    Функция принимает путь с файлом, читает его и сохраняет текст
    :param some_path: Передаёт путь к файлу
    :return: Возвращает текст файла
    """
    try:
        with open(some_path, "r") as some_file:
            some_text = some_file.read().splitlines()

        return some_text
    except FileNotFoundError as e:
        print(e)
        sys.exit(2)


def __string_filtered(some_string: str) -> str:
    """
    Приватная функция для удаления лишнего из строки, а именно
    идентификатора на объект с ошибкой. Так как идентификаторы на объекты
    всегда уникальны, то невозможно вычислить, в последствии, разницу
    строк, плюс немного косметики - удаление лишних пробелов.
    :param some_string: Принимает строку, для удаления лишнего.
    :return: Возвращает очищенную строку.
    """
    filtered_string = re.sub("<.*>:\s", "", some_string)

    return filtered_string.rstrip()


def create_dict(*args: tuple) -> dict:
    """
    Функция принимает кортеж строк и преобразует его в словарь
    :param args: Принимает кортеж из строк
    :return: Возвращает словарь
    """
    some_dict = {}
    raw_string = ""

    for line in args:
        key, *tmp = line.split()
        # Преобразуем полученый список "*tmp" в нормальную строку, для случая,
        # когда ответ от ссылки приходит не цифровым кодом, а каким-то текстом и
        # передаём полученную строку как значение в словарь.
        for i in tmp:
            raw_string += " ".join([i, ""])
        some_dict[key] = __string_filtered(raw_string)
        raw_string = ""

    return some_dict


def create_diff_dict(sample_dict: dict, tested_dict: dict) -> dict:
    """
    Функция принимает два словоря, вычисляет разность и возвращает новый словарь
    с этой разностью
    :param sample_dict:  Словарь, который служит эталоном
    :param tested_dict: Словарь в котором мы ищем расность с эталоном
    :return: Возврат нового словаря с разностью, либо пустого
    """
    diff_dict = {}
    diff_dict.update({key: sample_dict[key] for key in sample_dict
                      if key not in tested_dict})
    diff_dict.update({key: tested_dict[key] for key in tested_dict
                      if key not in sample_dict})
    diff_dict.update({key: tested_dict[key] for key in tested_dict
                      if key in sample_dict and
                      tested_dict[key] != sample_dict[key]})

    return diff_dict
