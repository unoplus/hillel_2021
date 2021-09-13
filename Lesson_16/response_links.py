import requests


path_to_links = "X:/Prog/Python/requests/"
file_with_links = "some_links.txt"
file_with_response = "links_with_response.txt"


def read_links(some_path: str) -> list:
    """
    Функция принимает путь с файлом в котором хранятся ссылки на различные
    ресурсы и сохраняет их в список.
    :some_path: Передаём путь к файлу
    :return: Возвращает список со ссылками
    """
    try:
        with open(some_path, "r") as file_links:
            list_of_links = [line.strip() for line in file_links]

        get_response(list_of_links)
        return list_of_links
    except Exception as e:
        print(e)


def get_response(url: list) -> dict:
    """
    Функция принимает на вход список ссылок и возвращает ответы на запросы,
    от этих ссылок
    :param url: список ссылок
    :return: словарь в котором будет ссылка и ответ, который вернулся
    """
    links_with_status = {}
    for link in url:
        try:
            r = requests.get(link)
            request = r.status_code
            links_with_status[link] = request
        except Exception as e:
            print(e)
            links_with_status[link] = e

    write_response(**links_with_status)
    return links_with_status


def write_response(**kwargs: dict) -> None:
    """
    Функция принимает словарь и записывает его, в форматированном виде,
    в файл
    :param kwargs: словарь со ссылками и ответами
    :return:
    """
    with open(path_to_links + file_with_response, "w") as write_file:
        for item in kwargs.items():
            key, value = item
            write_file.write("{:100s}{:4s} \n".format(key, str(value)))


read_links(path_to_links + file_with_links)
