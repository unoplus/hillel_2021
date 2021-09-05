# Create by Bender
"""
В текстовый файл (файл прилагается), построчно записаны имя и
фамилия учащихся класса и их оценки.
Вывести на экран всех учащихся, чей средний балл меньше 5, также
посчитать и вывести средний балл по классу. Так же, записать в новый
файл всех учащихся в формате "Фамилия И. Ср. балл"
"""


def read_file() -> None:
    """
    Функция читает файл и разбирает по переменным строки.
    Формирует строку ФИО для записи в новый файл.
    Вызывает функцию записи в новый файл.
    :return: Ничего не возвращает
    """

    list_of_fio = ""
    students_file = open("src_14.txt", "r", encoding="utf-8")

    for line in students_file:
        data_list = line.split()
        first_name, last_name, *rating = data_list
        list_of_fio += " ".join([first_name, last_name, "\n"])

    students_file.close()
    new_file(list_of_fio)


def new_file(some_text) -> None:
    """
    Функция принимает строку с ФИО и записывает её в новый файл.
    :param some_text: строка с ФИО студентов
    :return: Ничего не возвращает
    """

    new_students_file = open("src_15.txt", "w", encoding="utf-8")
    new_students_file.write(some_text)
    new_students_file.close()


def max_line() -> None:
    """
    Функция читает файл с ФИО. Ищёт самоую длинную строку.
    Прибавляет к самой длоиной строке четыре пробела.
    Вызывает функцию "students".
    :return: Ничего не возвращает
    """

    new_students_file = open("src_15.txt", "r", encoding="utf-8")
    # Приводим к строке принудительно, иначе
    # "Expected type 'str', got 'Sized' instead"
    size_string = str(max(new_students_file, key=len))
    new_students_file.close()
    size_string += " " * 4
    students(size_string)


def students(some_size: str):
    """
    Функция открывает файл с ФИО и оценками студентов. Высчитывает средний балл
    для каждого студента. Выводит на экран ФИО и средний балл студентов,
    у которых средний балл ниже 5, а также, средний балл всей группы.
    Записывает в новый файл ФИО всех студентов со средним баллом.
    Функция принимает размер строки, по которому будут выравниваться
    все остальные строки. Выравниваться они будут по следующему принципу:
    Считается разница размеров принятой строки с текущей, к текущей строке
    прибавляется эта разница, как пробел.
    :param some_size: шаблонная строка.
    :return: выводит на экран и записывает в файл.
    """

    students_file = open("src_14.txt", "r", encoding="utf-8")
    new_students_file = open("src_15.txt", "w", encoding="utf-8")
    all_average_score = 0
    all_score = 0

    for line in students_file:
        count = 0
        student_score = 0
        outsiders = ""
        data_list = line.split()
        first_name, last_name, *rating = data_list

        for score in rating:
            student_score += int(score)
            count += 1

        average_score = round(student_score / count, 2)
        list_of_fio = " ".join([first_name, last_name])

        if len(list_of_fio) < len(some_size):
            b = len(some_size) - len(list_of_fio)
            list_of_fio += " " * b
            new_students_file.write(f"{list_of_fio}{average_score}\n")

            if average_score < 5:
                outsiders += (list_of_fio + str(average_score))
                print(outsiders)

        all_score = all_score + average_score
        all_average_score = round(all_score / count, 2)

    print(f"\nСредний балл группы: {all_average_score}")
    new_students_file.close()
    students_file.close()


if __name__ == "__main__":
    read_file()
    max_line()
