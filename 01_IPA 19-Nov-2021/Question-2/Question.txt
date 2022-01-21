Write a code to automate the process of calculation of bonus amount for Employees
in an Organization.

Define a class to create Employee object with the below attributes:
employee_name of type String,
designation of type String,
salary of type Number,
overTimeContribution of type dictionary having name of the month and overtime in
hours (hours contributed as overtime for that month) as key:value pairs (month:overtime),
overTimeStatus of type string representing whether employee is eligible for overtime or not.

Define the required method in the Employee class which takes all the parameters in the
above sequences except the attribute overTimeStatus and sets the value of attribute
to parameter values while creating an object of the class. For the attribute
overTimeStatus a default value is set as False.

Define another class to create an organizantion object with the below attributes:
employee_list of type list having Employee objects.

Define the required method in the organizantion class which takes all the parameters
in the above sequences and sets the value of attribute to parameters values while creating
an object of the class.

Define another method in the organizantion class to check if the employee is
eligible for overtime bonus or not and update the values for the attribute
overTimeStatus.

This method takes the following as argument:
1. a number representing the overTimeThreshold.

This method will update the value for the attribute overTimeStatus to True if
the following condition is fulfilled:

i. the value for the total overtime hours for all months recorded for the Employee
   is not less than the overtime threshold (the value passed as argument).
ii. if above condition is not fulfilled, the value for the attribute overTimeStatus will
    remain as False.

Define another method in the organization class to calculate the total bonus amount
to be paid by the organization.

The bonus amount is calculated only for eligible Employees (having overTimeStatus as True)
based on the total overtime hours for all months recorded for the Employee and the
rate per hour provided.

This method will take as argument a number representing the rate per hour and will
return the total amount the Organization will require to pay as bonus to all
eligible Employees of the Organization.

Note:
All searches should be case insensitive.
Consider no two employees have the same name.

**All remaining things not relevant to question is omitted.**

Input test case-1:

5
Sunita
Faculty
23000
2
Jan
4
March
6
Arun
Admin
30000
3
Feb
4
March
12
June
10
Dipak
Admin
25000
3
Jan
12
July
5
Aug
3
Balen
HR
12000
3
Jan
12
July
5
Aug
3
Tarun
HR
78000
3
Jan
12
July
5
Aug
3
18
100

Output:

Sunita False
Arun True
Dipak True
Balen True
Tarun True
8600

Input test case-2:

5
Sunita
Faculty
23000
4
Jan
4
March
6
apr
6
June
3
Arun
Admin
30000
3
Jan
4
March
6
apr
6
Dipak
Admin
25000
3
Jan
4
March
6
apr
6
Balen
HR
12000
3
Jan
4
March
6
apr
6
Tarun
HR
78000
3
Jan
4
March
6
apr
6
30
100

Output:

Sunita False
Arun False
Dipak False
Balen False
Tarun False
0
