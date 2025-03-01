class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.math+self.chem)/3)+"%"   #how many times we change subject marks it wont change percenge

    @property
    def calpercentage(self):
        return str((self.phy+self.math+self.chem)/3)+"%"

stu1=Student(99,98,95)
print(stu1.percentage)

stu1.phy=85
print(stu1.percentage)  # after updating the phy marks here it does not change percentge
print(stu1.calpercentage)  #here it chamges percentage value