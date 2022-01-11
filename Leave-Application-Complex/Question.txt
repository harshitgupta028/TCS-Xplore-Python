  Create a class Employee which have 3 members
  emp_no,
  emp_name ,
  leaves.
  Leaves is a dictionary with the three keys "EL", "CL", "SL"
  which are the type of leaves.

  Define __init__() to initialize the values.

  Create another class Company which has two fields
  cname and emps.

  cname is the company name and emps is the list of employees.

  Create a function leave_available() to which takes two
  parameters emp_no and type of leave and used to print
  the number of leaves remaining.

  Create another function leave_permission() which takes
  empno , type of leave and num of leave.

  if the available leave of a employee is greater than
  equal to the number of leaves employee want then
  print "Granted" else print "Rejected".

  Take 2 input of empno,empname,leaves(all type)
  take input empid,type of leaves,leaves duration and check if
  granted or not.

Input:
2
1
Rajesh
5
10
15
2
Sudhir
10
10
10
1
SL
20

Output:

10
Rejected
