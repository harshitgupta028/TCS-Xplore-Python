#################################### Test case - 1 #############################
# Input:

# 5
# Sunita
# Faculty
# 23000
# 2
# Jan
# 4
# March
# 6
# Arun
# Admin
# 30000
# 3
# Feb
# 4
# March
# 12
# June
# 10
# Dipak
# Admin
# 25000
# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# Balen
# HR
# 12000
# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# Tarun
# HR
# 78000
# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# 18
# 100

# Output:

# Sunita False
# Arun True
# Dipak True
# Balen True
# Tarun True
# 8600

#################################### Test case - 2 ###########################

# Input:

# 5
# Sunita
# Faculty
# 23000
# 4
# Jan
# 4
# March
# 6
# apr
# 6
# June
# 3
# Arun
# Admin
# 30000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# Dipak
# Admin
# 25000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# Balen
# HR
# 12000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# Tarun
# HR
# 78000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# 30
# 100

# Output:

# Sunita False
# Arun False
# Dipak False
# Balen False
# Tarun False
# 0

class Employee:
    def __init__(self,employee_name,designation,salary,overTimeContribution):
        self.employee_name = employee_name
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution
        self.overTimeStatus = False

class Organization(Employee):
    def __init__(self,employee_list):
        self.employee_list = employee_list

    def isEligibleForBonus(self,overTimeThreshold):
        for obj in self.employee_list:
            totalOverTimeHours = 0
            for k,v in obj.overTimeContribution.items():
                totalOverTimeHours = totalOverTimeHours + v
                if totalOverTimeHours >= overTimeThreshold:
                    obj.overTimeStatus = True

    def totalBonusToBePaid(self,ratePerHour):
        total = 0
        for obj in self.employee_list:
            if obj.overTimeStatus:
                for k,v in obj.overTimeContribution.items():
                    total = total + v*ratePerHour
        return total

n = int(input())
obj_list = []
for _ in range(n):
    employee_name = input()
    designation = input()
    salary = int(input())
    overTimeContribution = {}
    for _ in range(int(input())):
        key = input()
        value = int(input())
        overTimeContribution[key] = value
    obj_list.append(Employee(employee_name,designation,salary,overTimeContribution))

org_obj = Organization(obj_list)
overTimeThreshold = int(input())
ratePerHour = int(input())

org_obj.isEligibleForBonus(overTimeThreshold)
totalBonus = org_obj.totalBonusToBePaid(ratePerHour)
for i in obj_list:
    print(i.employee_name,i.overTimeStatus,sep=" ")
print(totalBonus)
