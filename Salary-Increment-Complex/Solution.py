# Salary Increment

class Employee:

    def __init__(self,emp_id,emp_name,emp_role,emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_role = emp_role
        self.emp_salary = emp_salary

    def increment_salary(self,inc_in_per):
        self.emp_salary = (self.emp_salary*(100 + inc_in_per))/100
        return self.emp_salary

class Organization(Employee):
    emp_list = []

    def calculate_salary(role, inc_in_per):
        sal_inc_emp = []
        for i in Organization.emp_list:
            if i.emp_role == role:
                res = i.increment_salary(inc_in_per)
                sal_inc_emp.append([i.emp_name, res])
        return sal_inc_emp

n = int(input())
emp_lis = []

for _ in range(n):
    emp_id = int(input())
    emp_name = input()
    emp_role = input()
    emp_salary = int(input())
    emp_lis.append(Employee(emp_id,emp_name,emp_role,emp_salary))

role = input()
inc_in_per = int(input())

Organization.emp_list = emp_lis

result = Organization.calculate_salary(role,inc_in_per)
for i in result:
    print(i[0])
    print(i[1])
