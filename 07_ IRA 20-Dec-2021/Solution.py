
# 5
# Sunita
# Faculty
# 23000
# 1
# Home
# 200000
# Arun
# Programmer
# 30000
# 1
# Personal
# 4000
# Dipak
# Tester
# 25000
# 2
# Travel
# 10000
# Personal
# 5000
# Balen
# Analyst
# 12000
# 1
# Travel
# 2000
# Tarun
# Programmer
# 78000
# 2
# Personal
# 100000
# Travel
# 2000
# 3
# Travel
# Home
# Personal
# 3
# Programmer
# 300000
# Faculty
# 200000
# Analyst
# 100000
# Tarun
# Home
# 50000

class Employee:
    def __init__(self,empName,empDesignation, empSalary, loan):
        self.empName = empName
        self.empDesignation = empDesignation
        self.empSalary = empSalary
        self.loan = loan

class Organization:
    def __init__(self,empObj,loanType,maxDesiganationAmount):
        self.empList = empObj
        self.loanType = loanType
        self.maxDesiganationAmount = maxDesiganationAmount

    def eligibleForLoan(self,name,type,amount):
        isFound = False
        for obj in self.empList:
            if obj.empName.lower() == name.lower() and type.lower() not in obj.loan and type.lower() in self.loanType:
                su = amount

                for _,v in obj.loan.items():
                    su = su + v

                for k,v in self.maxDesiganationAmount.items():
                    if k == obj.empDesignation.lower():
                        if su < v:
                            obj.loan[type] = amount
                            return obj
                        else:
                            return False
        if not isFound:
            return False

    def stillEligibleForLoan(self):
        eligible = {}
        for obj in self.empList:
            su = 0
            des = obj.empDesignation
            for k,v in obj.loan.items():
                su = su + v
            if des.lower() in self.maxDesiganationAmount:
                if su < self.maxDesiganationAmount[des.lower()]:
                    if des not in eligible:
                        eligible[des] = 1
                    else:
                        eligible[des] = eligible[des] + 1
                else:
                    eligible[des] = 0
        dic1 = dict(sorted(eligible.items(), key=lambda item:item[0], reverse=True))
        return dic1

empObj = []
for _ in range(int(input())):
    empName = input()
    empDesignation = input()
    empSalary = int(input())
    loan = {}
    for i in range(int(input())):
        key = input().lower()
        value = int(input())
        loan[key] = value
    empObj.append(Employee(empName,empDesignation,empSalary,loan))

loanType = []
for _ in range(int(input())):
    inp = input().lower()
    loanType.append(inp)

maxDesiganationAmount = {}
for _ in range(int(input())):
    key = input().lower()
    value = int(input())
    maxDesiganationAmount[key] = value

name = input()
type = input()
amount = int(input())

obj = Organization(empObj,loanType,maxDesiganationAmount)
res = obj.eligibleForLoan(name,type,amount)
if res:
    print("Loan Granted.")
    for k,v in res.loan.items():
        print(k,": ",v)
else:
    print("Not Found")

eligible = obj.stillEligibleForLoan()
for k,v in eligible.items():
    print(k,": ",v)
