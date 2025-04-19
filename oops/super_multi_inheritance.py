class Car:                                  #parent 1
    colour="balck"
    def __init__(self,varient):
        self.varient=varient
        print("car init")
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car):                       # parent 2
    manufacturer="toyota cars ltd"
    def __init__ (self,brand,varient):

        super().__init__(varient)
        print("toyota init")
        self.brand=brand

class Fortuner(Toyotacar):                  #child class
    def __init__(self,type,brand,varient):
        super().__init__(brand,varient)
        print("fortuner init")
        #super().__init__(brand)
        self.type=type  

car1=Fortuner("diesel","toyota","suv")
print(car1.type)
print(car1.brand) # we cant acces other vs object attributes
car1.start()
print(car1.colour)
print(car1.manufacturer)
print(car1.varient)