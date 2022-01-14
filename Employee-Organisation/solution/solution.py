
# Employee Organisation

# 2
# A
# 1
# 30
# M
# B
# 2
# 40
# F
# 10
# 50

class Employee:
    def __init__(self,name,id,age,gender):
        self.name = name
        self.id = id
        self.age = age
        self.gender = gender

class Organisation(Employee):

    def getEmployeeCount(obj_lis):
        return len(obj_lis)

    def findEmployeeAge(obj_lis,id):
        for i in obj_lis:
            if i.id == id:
                return i.age
        return -1

    def countEmployee(obj_lis,age):
        count = 0
        for i in obj_lis:
            if i.age == age:
                count = count + 1
        return count


obj_lis = []
n = int(input())
for _ in range(n):
    name = input()
    id = int(input())
    age = int(input())
    gender = input()
    obj_lis.append(Employee(name,id,age,gender))

id = int(input())
age = int(input())

print(Organisation.getEmployeeCount(obj_lis))
print(Organisation.findEmployeeAge(obj_lis,id))
print(Organisation.countEmployee(obj_lis,age))
