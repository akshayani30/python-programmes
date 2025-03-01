class Car:
    @staticmethod
    def starte():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
class Toyotacar(Car):
    def __init__(self,brand):
        self.brand=brand
class fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type
car1=fortuner("diesel")
car1.stop()