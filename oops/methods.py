class student:
    college_name="mallareddy"

    def __init__(self,name,marks):
        self.name=name
        self.mark=marks
    def welcome(self):
        print("welcome",self.name)
    def get_marks(self):
        return self.mark
s1=student("suman",100)
print(s1.name,s1.mark)
s2=student("akshayani",95)
print(s2.name,s2.mark)
s1.welcome()
print("marks:",s1.get_marks())
s2.welcome()
print("marks:",s2.get_marks())


