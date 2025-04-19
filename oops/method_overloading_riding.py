class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:  #here we are checking the values are there or not  if not there then it will not go to the next line
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
c1=student(1,1)
print(c1.sum(1,1))  #if we give here less arguments then it shows error



class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        print("in B show")
a1=B()
a1.show()   #overrides here if we don't have in B then it goes to A