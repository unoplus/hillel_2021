#! /usr/bin/env python3
# creata @cyberscriptor

import requests

__all__ = ["get_response", "write_response"]


def get_response(some_path: str, url: list) -> None:
    """
    Функция принимает на вход путь и имя файла для записи и список ссылок.
    Выполняет запросы по ссылкам, получает ответы и передаёт их в
    приватную функцию, для записи в файл.
    :param some_path: принимает путь и имя файла
    :param url: список ссылок
    :return:
    """
    links_with_status = {}
    for link in url:
        try:
            r = requests.get(link, verify=False)
            request = r.status_code
            links_with_status[link] = request
        except Exception as e:
            print(e)
            links_with_status[link] = e

    write_response(some_path, **links_with_status)


def write_response(path: str, **kwargs: dict) -> None:
    """
    Приватная функция, принимает словарь и путь, записывает словарь,
    в форматированном виде, в файл.
    :param path: принимает путь и имя файла для записи
    :param kwargs: словарь со ссылками и ответами
    :return:
    """
    with open(path, "w") as write_file:
        for key, value in kwargs.items():
            write_file.write("{:100s}{:4s}\n".format(key, str(value)))
