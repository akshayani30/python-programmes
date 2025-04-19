class A:
    def __init__ (self):
        print("in A init")
    def feature1(self):
        print("feature 1")
    def feature2(self):
        print("feature 2")
class D:
    def __init__ (self):
        super().__init__()
        print("in D init")

class B(D,A): # here we are inheriting the class A and D     MRO  method resolution order
    def __init__(self):
        super().__init__()

        print("n B init")
    def feature3(self):
        print("feature 3")
    def feature4(self):
        print("feature 4")
a1=B()
a1.feature1()  # if there is no init in class B then it goes to class A bcoz we are in heritin the class A

