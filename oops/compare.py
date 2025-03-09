class Computer:
    def __init__(self):
        self.name="ak"
        self.age=20
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=Computer()
c1.age=20
c1.name="aks"
c2=Computer()
if c1.compare(c2):
    print("they are same")
else:
    print("they are different")
print(c1.name)
print(c2.name)