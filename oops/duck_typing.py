class pycharm:
    def execute(self):
        print("compiling")
        print("running")
class laptop:
    def code(self,ide):
        ide.execute()


ide=pycharm()
lap1=laptop()
lap1.code(ide)


def make_it_quack(animal):
    animal.quack()

class Duck:
    def quack(self):
        print("Quack! Quack!")

class ToyDuck:
    def quack(self):
        print("Squeak! Squeak!")

class Dog:
    def bark(self):
        print("Woof!")

donald = Duck()
daisy = ToyDuck()
fido = Dog()

make_it_quack(donald)  # Output: Quack! Quack!
make_it_quack(daisy)   # Output: Squeak! Squeak!

# make_it_quack(fido)   # This would raise an AttributeError because Dog has no 'quack()' method.