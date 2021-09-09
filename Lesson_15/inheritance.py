# Create by Bender

# Базовый класс
class Class1:
    """Класс с двумя методами"""

    def method1(self):
        print("method1, Class1")

    def method2(self):
        print("method2, Class1")


# Class2 наследует Class1
class Class2(Class1):

    def method3(self):
        print("method3, Class2")


obj = Class2()
obj.method1()
obj.method2()
obj.method3()
