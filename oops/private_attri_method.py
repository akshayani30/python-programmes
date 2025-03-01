class Account:
    __college="mallareddy"
    def __init__(self,acc_num,name):
        self.acc_num=acc_num
        self.__name=name    #it does not print outside the class
        print(self.__name)
    def reset_name(self):
        print(self.__name)
acc1=Account("1234","ak")
print(acc1.acc_num)
acc1.reset_name()
#print(acc1.__name)   #it gives error
#print(acc1.__college)  #it wont print
print(acc1._Account__name)