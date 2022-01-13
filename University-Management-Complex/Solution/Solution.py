# University Management Question

# Test Cases:

# 4
# 1
# Shivakumar
# 3
# Maths
# 10
# Physics
# 10
# Chemistry
# 10
# 2
# Rajesh
# 4
# MATHS
# 5
# PHYSICS
# 5
# CHEMISTRY
# 5
# COMPUTERS
# 5
# 3
# vasudev
# 2
# MATHS
# 4
# PHYSICS
# 4
# 4
# Srinivas
# 3
# Maths
# 8
# Physics
# 8
# Chemistry
# 8
# 3
# maths

class Professor:
     def __init__(self, profId, profName, subjectsDict):
         self.profId = profId
         self.profName = profName
         self.subjectsDict = subjectsDict

class University:
    def getTotalExperience(lis,id):
        exp_lis = []
        isMatched = False
        for k in lis:
            sum = 0
            if k.profId == id:
                isMatched = True
                for _,v in k.subjectsDict.items():
                    sum = sum + v
                exp_lis.append(sum)
        if isMatched:
            return exp_lis
        else:
            return 0

    def selectSeniorProfessorBySubject(lis,subject):
        high_exp = 0
        isAvailable = False
        for l in lis:
            for k,v in l.subjectsDict.items():
                if k.lower() == subject.lower():
                    isAvailable = True
                    if high_exp < v:
                        high_exp = v
                        prof_id = l.profId
                        prof_name = l.profName
                        prof_subject = l.subjectsDict
        if isAvailable:
            return [prof_id,prof_name,prof_subject]
        else:
            return None

n = int(input())
lis = []
for i in range(n):
    profId = int(input())
    profName = input()
    subjectsDict = {}
    for j in range(int(input())):
        subject = input()
        exp = int(input())
        subjectsDict[subject] = exp
    lis.append(Professor(profId,profName,subjectsDict))

id = int(input())
subject = input()

total_exp = University.getTotalExperience(lis,id)[0]
highest_exp = University.selectSeniorProfessorBySubject(lis,subject)

print(total_exp)
print(*highest_exp)
