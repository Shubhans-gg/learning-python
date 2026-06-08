import random

class account:
    def __init__(self,acc_no, balance):
        self.acc_no=acc_no
        self.balance=balance

    def credit(self, amt):
        self.balance=self.balance+amt
        print(amt,"has been deposited")
    
    def debit(self, amt):
        self.balance=self.balance-amt
        print(amt,"has been withdrawn")
    
    def money(self):
        print("Your current account balance is",self.balance)

a=int(input("Enter your acc_no:"))
b=random.randint(0,50000000)
s1=account(a,b)
print("To deposit money press 1")
print("To withdraw money press 2")
print("To check your current account balance press 3")
choice=int(input("Enter your choice:"))
if choice==1:
    amt=int(input("Enter the amount you want to deposit:"))
    s1.credit(amt)
    s1.money()

elif choice==2:
    amt=int(input("Enter the amount you want to withdraw:"))
    if (amt>s1.balance):
        print("Not enough balance")
        s1.money()
    else:
        s1.debit(amt)
        s1.money()

else:
    s1.money()
