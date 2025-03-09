class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def add(self,num2):     #def __add__  dunder function
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return complex(newReal,newImg)


num1=complex(1,2)
num1.showNumber()

num2=complex(2,4)
num2.showNumber()
num3=num1.add(num2)   #num3=num1+num2
num3.showNumber()


