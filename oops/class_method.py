class Person:
    name="anonymous"

    # def changeName(self,name):
    #     Person.name=name
    #     self.__class__.name="akshayanisuman"

    @classmethod
    def changeName(cls, name):
        cls.name=name

p1=Person()
p1.changeName("akshayanisuman")
print(p1.name)
print(Person.name)