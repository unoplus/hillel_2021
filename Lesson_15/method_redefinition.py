# Create by Bender

# Базовый класс
class Class1:

    def __init__(self):
        print("Конструктор базового класса")

    def method1(self):
        print("method1 из Class1")


# Класс Class2 наследует класс Class1
class Class2(Class1):

    def __init__(self):
        print("Конструктор дочернего класса")
        # Вызываем конструктор базового класса
        Class1.__init__(self)

    def method1(self):
        print("method из Class2")
        # Вызываем метод базового класса
        Class1.method1(self)


c = Class2()
c.method1()
