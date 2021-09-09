# Create by Bender

class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def _print_age(self):
        """Приватный метод, его должны вызывать только методы"""
        print(f"age: {self.age}")

    def get_info(self):
        print(f"name: {self.name}")
        # вызов приватного метода из метода
        self._print_age()

    def __del__(self):
        """Деструктор"""
        print("Bye")


boy = Student("Mike", 17, "M")
girl = Student("Ann", 20, "F")

print(boy.name, girl.name)
# на практике будем старвться не вызывать приватные методы таким способом
girl._print_age()
boy.get_info()
