# Create by Bender
"""
Реализовать класс цифрового счетчика.
Обеспечьте возможность:
установки максимального и минимального значений
(счетчик считает от меньшего к большему)
увеличения счетчика на 1 ( при переполнении счетчика) при достижении максимума
уваличения не происходит. Метод который инкрементирует счетчик возращает
его значение.
получение значения счетчика.
"""


class FreddyComingForYou:
    """Класс-считалочка ;) с шуткой, а то как-то скучно... 8("""

    def __init__(self, min_val: int, max_val: int) -> None:
        """
        Создание счётчика с граничными элементами. Счётчик равен минимальному.
        Содержит начальные значения переменных счётчика, индекса списка строк
        песенки, строки песенки.
        :param min_val: минимальное значение
        :param max_val: максимальное значение
        """
        self.min_val = min_val
        self.count = self.min_val
        self.str = self.min_val
        self.line = ""
        self.max_val = max_val

    def counting(self) -> int:
        """
        Считаем от минимума к максимуму, увеличивая счётчик на еденицу.
        При каждом чётном выводится строчка песенки 8Р,
        чтобы получалось примерно так: "One, Two... Freddy’s coming for you!..."
        :return: значение счётчика
        """
        song = ["Freddy’s coming for you!", "Better lock your door!",
                "Grab your crucifix!", "Gonna stay up late!",
                "Never sleep again!…"]
        if self.count < self.max_val:
            self.count += 1
            if self.count % 2 and self.count > 2:
                self.line = song[self.str]
                print(self.line)
                self.str += 1
        elif self.count == self.max_val:
            self.line = song[self.str]
            print(self.line)
        return self.count

    def count_status(self) -> int:
        """
        Получение текущего значения счётчика.
        :return: текущее значение счётчика
        """
        return self.count


if __name__ == "__main__":
    run_nightmare = FreddyComingForYou(0, 10)
    print(f"You are here now: {run_nightmare.count_status()}\nLet`s sing!")
    for sing in range(run_nightmare.max_val + 2):
        print(run_nightmare.counting())
    print("Never sleep again!…")
