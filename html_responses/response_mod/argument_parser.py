#! /usr/bin/env python3
# creata @cyberscriptor

import sys
import argparse
from response_mod import help_response as hr

__all__ = ["create_params"]

path = "/some_path/"


def create_parser():
    """
    Функция-парсер. Описывает получение параметров вызова скрипта.
    Вызывает функцию-обработчика полученных параметров.
    Возвращает результат работы функции-обработчика.
    """
    pars = argparse.ArgumentParser()
    pars.add_argument("-n", "--name", default="man")
    pars.add_argument("-p", "--path", default=path)
    pars.add_argument("-s", "--sample", action="store_true", default=False)
    pars.add_argument("-m", "--mail", default="")

    return create_params(pars)


def create_params(some_pars) -> list:
    """
    Функция-обработчик переданных параметров пользователем. Принимает на вход
    указанные пользователем параметры, обрабатывает их и, в зависимости от
    результата, вызывает справку и завершает работу, либо возвращает список
    значений параметров.
    :param some_pars: Переданные параметры.
    :return: Возвращает список значений.
    """
    params = some_pars.parse_args()
    if params.name == "man":
        hr.get_help()
        sys.exit(0)
    else:
        params_list = [params.name, params.path, params.sample, params.mail]

        return params_list
