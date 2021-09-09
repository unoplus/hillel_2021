# Create by Bender

class NewCar:
    """Design of car"""
    # Атрибут экземпляра класса
    model = "no name"

    def start_engine(self):
        """метод - запуск двигателя"""
        print("wrooom!!!")

    def turn(self):
        """метод - выполнения поворота"""
        pass

    def stop(self):
        """метод - торможения"""
        print(f'"{self.model}" stopped')


car_of_future = NewCar()
car_of_future.start_engine()
car_of_future.stop()
