class Vehicle:
    def move(self):
        raise NotImplementedError


class MotorVehicle(Vehicle):
    def start_engine(self):
        print("Engine started")


class Car(MotorVehicle):
    pass


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling forward")
