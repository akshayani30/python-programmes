class student:

    def __init__(self,name,marks):  #peru and marks are attributes it stores the information of student
        self.peru=name    #attributes accessed using self
        self.marks=marks
        print("adding new studet in data base..")
s1=student("akshayani",95)       #initializing name and marks
print(s1.peru,s1.marks)                #s1 and s2 are objects of student class

s2=student("suman",100)
print(s2.peru,s2.marks)
print(s1.peru,s1.marks)