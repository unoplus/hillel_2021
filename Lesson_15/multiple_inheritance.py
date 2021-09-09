# Create by Bender

class ClassBase1:
    def name(self):
        print("BASE1")


class ClassBase2:
    def say(self):
        print("Hello")


# ножественное наследование
class ClassChild(ClassBase1, ClassBase2):
    def __init__(self):
        print("This is from ClassChild:")
        self.say()
        self.name()


obj = ClassChild()
