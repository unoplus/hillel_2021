# Create by Bender
"""
Создать класс, описывающий группу студентов - `Group`.
Данный класс хранит студентов в виде списка объектов `Student`
также реализованного в виде соответствующего класса.
В классах реализовать необходимый набор атрибутов
Где класс `Student` минимум должен иметь атрибуты `name`, `age`, `grades`
Реализовать необходимый набор методов экземпляра для работы с этими экземплярами
Класс `Group` умеет выводить на печать имена и оценки студентов.
Наследование здесь не понадобится.
"""


class Student:
    def __init__(self, last_name: str, first_name: str, age: int, grades: list):
        """
        Описание модели "студент"...
        :param last_name: Фамилия
        :param first_name: Имя
        :param age: Возраст
        :param grades: Оценки
        """
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.grades = grades

    def average_grade(self) -> float:
        """
        Фуекция для подсчёта среднего балла студента.
        :return: Возвращает средний балл.
        """
        average_grade = 0
        count = 0
        for grade in self.grades:
            average_grade += grade
            count += 1
        average_grade = round(average_grade / count, 2)

        return average_grade


class Group:
    def __init__(self, students: list[Student]):
        """
        Список студентов группы
        :param students: список студентов
        """
        self.students = students

    def add_student(self, student: Student) -> None:
        """
        Добавление студента в группу.
        :param student: Новый студент.
        :return:
        """
        self.students.append(student)

    def remove_student(self, student: Student) -> None:
        """
        даление студента из группы.
        :param student: Исключённый студент
        :return:
        """
        self.students.remove(student)

    def print_students(self):
        for student in self.students:
            if student.average_grade() < 3:
                print("{bold}{red}{:8s}{:10s}{}{endcolor}"
                      .format(student.last_name, student.first_name,
                              student.grades, bold="\033[1m", red="\033[31m",
                              endcolor="\033[0m"))
            else:
                print("{:8s}{:10s}{}"
                      .format(student.last_name, student.first_name,
                              student.grades))


if __name__ == "__main__":
    ivanov_av = Student("Иванов", "Андрей", 17, [4, 3, 4, 3])
    petrova_st = Student("Петрова","Светлана", 18, [4, 3, 4, 5])
    sidorov_vu = Student("Сидоров", "Валентин", 18, [2, 2, 3, 4])
    koval_ni = Student("Коваль", "Настасья", 17, [5, 5, 5, 5])
    group_students = [ivanov_av, petrova_st, sidorov_vu, koval_ni]

    new_group = Group(group_students)
    new_group.print_students()
