# Project Costing

# 4
# 1
# Banking
# 100
# 2
# C
# C++
# 2
# Finance
# 200
# 3
# C
# C++
# Java
# 3
# Pharma
# 500
# 4
# C
# C++
# Java
# Python
# 4
# Transport
# 150
# 1
# Dot Net
# 3
# 200

class Project(object):

    def __init__(self,projectId,projectName,manHours,technologyList):
        self.projectId = projectId
        self.projectName = projectName
        self.manHours = manHours
        self.technologyList = technologyList
        self.avgProjectCost = 0

    def calculateProjCost(self,rate_per_manHours):
        projectCost = self.manHours * rate_per_manHours
        return projectCost

class Orgination(Project):

    def projectAvgCostByTechnology(projectId,rate_per_manHours,projList):
        isMatched = False
        for j in projList:
            if j.projectId == projectId:
                isMatched = True
                projCost = j.calculateProjCost(rate_per_manHours)
                j.avgProjectCost = projCost / len(j.technologyList)

                print(len(j.technologyList))

                return [[j.projectId,j.projectName,j.technologyList], j.manHours, j.avgProjectCost]

        if not isMatched:
            return None

n = int(input())
obj_lis = []

for i in range(n):
    technologyList = []
    projectId = int(input())
    projectName = input()
    manHours = int(input())
    for _ in range(int(input())):
        technologyList.append(input())
    obj_lis.append(Project(projectId,projectName,manHours,technologyList))

id = int(input())
rate_per_manHours = int(input())

result = Orgination.projectAvgCostByTechnology(id, rate_per_manHours,obj_lis)

if result == None:
    print ("No Project Exist!")
else:
    ans_1, ans_2, ans_3 = [ _ for _ in result ]
    print(*ans_1,ans_2,ans_3,sep=" ")
