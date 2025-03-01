class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")
class Toyotacar(Car):
    def __init__(self,type):
        super().__init__(type) #used to access methods of parent class
        super().start()
car1=Toyotacar("petrol")

print(car1.type)
car1.start()