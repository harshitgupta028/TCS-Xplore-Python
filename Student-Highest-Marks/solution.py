class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def calculateResult(self):
        if self.sub1 > 40 and self.sub2 > 40 and self.sub3 > 40:
            avgPer = ((self.sub1 + self.sub1 + self.sub1)/300)*100
            return avgPer
        else:
            return -1

class School(Student):

    def getStudentResult(obj_lis):
        isPass = False
        studentLis = []
        for i in obj_lis:
            result = i.calculateResult()
            if result > 60:
                isPass = True
                studentLis.append([i.name, result])
                print(i.name)
        if not isPass:
            print("No student passed")
        else:
            return studentLis

    def findStudentWithHighestMarks(pass_std):
        temp = pass_std[0][1]
        for i in pass_std:
            if temp < i[1]:
                std_name = i[0]
                temp = i[1]
        return std_name

n = int(input())
obj_lis = []
for i in range(n):
    name = input()
    sub1 = int(input())
    sub2 = int(input())
    sub3 = int(input())
    obj_lis.append(Student(name,sub1,sub2,sub3))

print("List of Passed Students: ") # Additional Lines
res_1 = School.getStudentResult(obj_lis)
print("Student Obtained Maximum Marks: ",end="") # Additional Lines
res_2 = School.findStudentWithHighestMarks(res_1)
print(res_2)
