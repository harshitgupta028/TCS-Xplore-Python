
# 2
# 12345
# 12
# 30.0
# 10.0
# salary
# 45678
# 98
# 400.0
# 200.0
# salary
# 45678
# 98
# 100
# salary

from collections import OrderedDict

class Account:
    def __init__(self,cardNumber,pin,balance,withdrawalAmount,accountType):
        self.cardNumber = cardNumber
        self.pin = pin
        self.balance = balance
        self.withdrawalAmount = withdrawalAmount
        self.accountType = accountType

    def calculateBalance(self,withdAmount):
        if self.balance >= withdAmount:
            self.balance = self.balance - withdAmount
            self.withdrawalAmount = withdAmount

class ATM(Account):
    def __init__(self,obj_lis):
        self.obj_lis = obj_lis

    def updatedBalance(self,cardNo,cardPin,withdAmount):
        for obj in self.obj_lis:
            if obj.cardNumber == cardNo and obj.pin == cardPin:
                obj.calculateBalance(withdAmount)
                return obj
        else:
            return None

    def printBalance(self,acntType):
        acntDic = {}
        for obj in self.obj_lis:
            if obj.accountType == acntType:
                acntDic[obj.cardNumber] = obj.balance
        return acntDic

n = int(input())
obj_lis = []
for _ in range(n):
    cardNumber = int(input())
    pin = int(input())
    balance = float(input())
    withdrawalAmount = float(input())
    accountType = input()
    obj_lis.append(Account(cardNumber,pin,balance,withdrawalAmount,accountType))

cardNo = int(input())
cardPin = int(input())
withdAmount = float(input())
acntType = input()

ATM_obj = ATM(obj_lis)
obj1 = ATM_obj.updatedBalance(cardNo,cardPin,withdAmount)
dic = ATM_obj.printBalance(acntType)
dic1 = dict(sorted(dic.items(), key=lambda items: items[1]))
print(obj1.cardNumber,obj1.balance,obj1.withdrawalAmount)
for k,v in dic1.items():
    print(k, v)
