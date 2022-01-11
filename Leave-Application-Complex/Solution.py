# Leave Application 

class Employee:

    def __init__(self,emp_no,emp_name,leaves):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.leaves = leaves

class Company(Employee):
    emps = []

    def leave_available(empno,type_of_leave):
        for i in Company.emps:
            if i.emp_no == empno:
                for ek,ev in i.leaves.items():
                    if ek == type_of_leave:
                        return ev

    def leave_permission(empno,type_of_leave,no_of_leave):
        leave = Company.leave_available(empno,type_of_leave)
        print(leave)
        if leave >= no_of_leave:
            return [leave, True]
        elif leave < no_of_leave:
            return [leave, False]

n = int(input())
obj_list = []
for _ in range(n):
    leaves = {'EL': 0, 'CL': 0, 'SL':0}
    emp_no = int(input())
    emp_name = input()
    for k,_ in leaves.items():
        leaves[k] = int(input())
    obj_list.append(Employee(emp_no,emp_name,leaves))

empno = int(input())
type_of_leave = input()
no_of_leave = int(input())

Company.emps = obj_list
result = Company.leave_permission(empno,type_of_leave,no_of_leave)
remaning_leaves, isGranted = [j for j in result]

if isGranted:
    print("Output:")
    print(remaning_leaves,"Granted",sep="\n")
else:
    print("Output:")
    print(remaning_leaves,"Rejected",sep="\n")
