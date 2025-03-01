class Account:
    def __init__(self,bal,accno):
        self.balance=bal
        self.acc_no=accno
    
    def debit(self,amount):
        self.balance -=amount
        print("Rs.",amount,"debited")
        print("total balance=",self.balance)

    def credit(self,amount):
        self.balance +=amount
        print("Rs.",amount,"credited")
        print("total balance=",self.get_balance())
    def get_balance(self):
        return self.balance
acc1=Account(1000,143)
acc1.debit(500)
acc1.credit(500)