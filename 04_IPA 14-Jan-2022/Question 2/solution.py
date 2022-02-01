# 4
# 101
# jhon M
# specialist
# 6
# 102
# Mitul Barua
# Faculty
# 4
# 103
# Rosy Borah
# Faculty
# 3
# 104
# Reza
# Generalist
# 2
# faculty
# 4
# Specialist
# 5
# Generalist
# 3

class Employee:
    def __init__(self, empId, empName, role, age_in_role):
        self.empId = empId
        self.empName = empName
        self.role = role
        self.age_in_role = age_in_role
        self.promotion = None

class Organization:
    def __init__(self, empList, promoDic):
        self.empList = empList
        self.promoDic = promoDic

    def calculateEligibilityStatus(self):
        details = {}
        for obj in self.empList:
            for key,value in self.promoDic.items():
                if obj.role.lower() == key.lower():
                    if obj.age_in_role == self.promoDic[key]:
                        details[obj.empId] = "eligible"
                        obj.promotion = True
                    elif obj.age_in_role > self.promoDic[key]:
                        details[obj.empId] = "overdue"
                        obj.promotion = True
                    elif obj.age_in_role < self.promoDic[key]:
                        details[obj.empId] = str(self.promoDic[key] - obj.age_in_role) + " years left"
        return details

empObjLis = []
for _ in range(int(input())):
    empId = int(input())
    empName = input()
    role = input()
    age_in_role = int(input())
    empObjLis.append(Employee(empId,empName,role,age_in_role))

promoDic = {}
for i in range(3):
    key = input()
    value = int(input())
    promoDic[key] = value

obj = Organization(empObjLis, promoDic)
details = obj.calculateEligibilityStatus()
for k,v in details.items():
    print(k, v)
