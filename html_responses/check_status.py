#! /usr/bin/env python3
# creata @cyberscriptor

from response_mod import dict_diff_mod as ddm
from response_mod import write_response_mod as wrm
from response_mod import argument_parser as parser
from response_mod import send_mail as email

sample_file = "status_sample.txt"
tested_file = "status_tested.txt"
diff_responses_file = "status_diff.txt"


def create_sample_file(some_path: str, some_file: str, links: str) -> tuple:
    """
    Функция для создания файла-шаблона. Принимает путь к файлу со ссылками.
    Обрабатывает ссылки и сохраняет ссылку с ответом в файл-шаблон.
    Возвращает путь к созданному файлу-шаблону.
    :param some_path: Строка с путём к файлам.
    :param some_file: Строка с именем файла-шаблона.
    :param links: Строка с именем файла со ссылками.
    :return: Кортеж из пути и имени созданного файла-шаблона.
    """
    list_with_links = ddm.read_file(some_path + links)
    wrm.get_response(some_path + some_file, list_with_links)

    return some_path, some_file


def create_tested_file(some_path: str, some_file: str, links: str) -> dict:
    """
    Функция для вычисления разницы файлов-ответов. Принимает путь к файлу со
    ссылками. Обрабатывает ссылки и сохраняет ссылку с ответом в файл-тест.
    Сравнивает файл-шаблон с файлом-тестом, вычисляет разницу и возвращает
    возвращает в виде словоря. Если разницы нет, то возвращает пустой словарь.
    :param some_path: Строка с путём к файлам.
    :param some_file: Строка с именем файла-теста.
    :param links: Строка с именем файла со ссылками.
    :return: Словарь с разницей.
    """
    list_with_links = ddm.read_file(some_path + links)
    wrm.get_response(some_path + some_file, list_with_links)
    sample_status = ddm.read_file(some_path + sample_file)
    sample_responses = ddm.create_dict(*sample_status)
    tested_status = ddm.read_file(some_path + tested_file)
    tested_responses = ddm.create_dict(*tested_status)

    return ddm.create_diff_dict(sample_responses, tested_responses)


if __name__ == '__main__':
    file_with_links, path_to_files, sample, mail = parser.create_parser()
    if sample:
        path_to_sample, file_sample = create_sample_file(path_to_files,
                                                         sample_file,
                                                         file_with_links)
        if not mail:
            print(f'Создан файл-шаблон: "{path_to_files + file_sample}"')
        else:
            print(f'Создан файл-шаблон: "{path_to_files + file_sample}"')
            subject = "Файл-шаблон"
            body = (f'Создан файл-шаблон: "{path_to_files + file_sample}",'
                    f'присутствует во вложении.')
            email.send_mail_with_attachment(subject, mail, body,
                                            path_to_files + file_sample)
    else:
        diff_responses = create_tested_file(path_to_files, tested_file,
                                            file_with_links)

        if not diff_responses:
            if not mail:
                print(f"Сверка прошла успешно, разницы не выявлено.")
            else:
                print(f"Сверка прошла успешно, разницы не выявлено.")
                subject = "Результат сверки"
                body = f'Сверка прошла успешно, разницы не выявлено.'
                email.send_mail_without_attachment(subject, mail, body)
        else:
            if not mail:
                print(f"Ошибочные ответы:\n")

                for key, value in diff_responses.items():
                    print("{:100s}{:4s}\n".format(key, str(value)))

                wrm.write_response(path_to_files + diff_responses_file,
                                   **diff_responses)
                print(f'Проверка прошла с ошибками, подробности в файле: '
                      f'"{path_to_files + diff_responses_file}"')

            else:
                wrm.write_response(path_to_files + diff_responses_file,
                                   **diff_responses)
                print(f'Проверка прошла с ошибками, подробности в файле: '
                      f'"{path_to_files + diff_responses_file}"')

                subject = "Сверка прошла с ошибками!"
                body = (f'Создан файл-разницы:'
                        f'"{path_to_files + diff_responses_file}",'
                        f'присутствует во вложении.')
                email.send_mail_with_attachment(subject, mail, body,
                                                path_to_files +
                                                diff_responses_file)
