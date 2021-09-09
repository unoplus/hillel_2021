# Create by Bender

class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        """Деструктор"""
        print("Bye")


boy = Student("Mike", 17, "M")
girl = Student("Ann", 17, "F")
print(boy.name, girl.name)
