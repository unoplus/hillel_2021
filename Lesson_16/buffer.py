# Create by Bender
import random


class Buffer:
    """
    Класс принимает числовую последовательность и суммирует каждые
    пять первых членов этой последовательности
    """
    def __init__(self):
        """Инициализируем собственный список и сумму чисел в списке"""
        self.subsequence = []
        self.result = 0

    def add(self, *args) -> None:
        """
        Функция принимает числовые последовательности, суммирует первые пять
        членов этой последовательности и выводит на экран текущую сумму.
        :param args: входящая последовательность
        :return:
        """
        for num in args:
            self.subsequence.append(num)
            if len(self.subsequence) == 5:
                for i in self.subsequence:
                    self.result += i
                self.subsequence.clear()
                print(f"Сумма пяти элементов: {self.result}")
                self.result = 0

    def get_current_part(self) -> list:
        """
        Функция возвращает сохранённые текущие элементы последовательности
        :return: возвращает список элементов
        """
        return self.subsequence


if __name__ == "__main__":
    count = 0
    my_buffer = Buffer()
    # Создаём генератор случайных числовых последовательностей, которые будут
    # передаваться в класс Buffer для дальнейшей обработки
    while count < 10:
        random_subsequence = [random.randint(1, 25)
                              for i in range(random.randint(1, 10))]
        my_buffer.add(*random_subsequence)
        print(f"Текущие элементы: {my_buffer.get_current_part()}")
        count += 1
