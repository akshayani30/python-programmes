class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def get_avg(self):
        sum=0
        for value in self.marks:
            sum += value
            print("hii",self.name,"your avg score is:",sum//3)

s1=student("akshayani", [100, 99, 98])
s1.get_avg()

s1.name="suman"   #we can also change the name
s1.get_avg()