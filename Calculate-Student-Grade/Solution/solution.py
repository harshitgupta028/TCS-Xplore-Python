# Calculate Student Grade

# Input:
# 123
# Rahul
# 3
# 80
# 70
# 80
#
# Output:
# 76
# B
#
# Input:
# 200
# Asha
# 4
# 90
# 90
# 80
# 60
#
# Output:
# 80
# A

class Student(object):
    def __init__(self,roll,name,marks_list):
        self.roll = roll
        self.name = name
        self.marks_list = marks_list

    def calculate_percentage(self,n):
        return sum(self.marks_list) // n

    def find_grade(self,percentage):
        if percentage >= 80:
            return 'A'
        elif percentage >= 60 and percentage < 80:
            return 'B'
        elif percentage >= 40 and percentage < 60:
            return 'C'
        elif percentage < 40:
            return 'F'

roll = int(input())
name = input()
marks_list = []
n = int(input())
for _ in range(n):
    marks_list.append(int(input()))

obj = Student(roll,name,marks_list)
percentage = obj.calculate_percentage(n)
grade = obj.find_grade(percentage)
print(percentage,grade,sep="\n")
