class Account:
    def __init__(self,acc_no,name,balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposite_money(obj,dep_amnt):
        obj.balance = obj.balance + dep_amnt
        return obj.balance

    def withdraw_money(obj,with_amnt):
        obj.balance = obj.balance - with_amnt
        if obj.balance > 1000:
            return obj.balance
        else:
            return 0

acc_no = int(input())
name = input()
balance = int(input())
obj = Account(acc_no,name,balance)
d_or_w = input()
d_or_w_amnt = int(input())
if d_or_w == "d":
    result = Account.deposite_money(obj,d_or_w_amnt)
    print("Balance: ",result)
else:
    result = Account.withdraw_money(obj,d_or_w_amnt)
    print("Amount is less then 1000:",result)
