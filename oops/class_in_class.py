class student:
    def __init__(self,name,roll):
        self.name=name
        self.rollno=roll
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    
    class laptop:
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=student("ak",10)
s2=student("suman",20)
s1.show()

lap1=student.laptop()   
lap1.show()