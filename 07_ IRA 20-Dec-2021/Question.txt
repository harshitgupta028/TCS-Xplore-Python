Write the code to define a class to create Employee objects with the
below attributes :
Name
designation
salary
Loan details ( stores the details of different types of loans
employee has taken along with the amount borrowed for a loan type
as key : value pairs - loan type : borrowed amount ).

Define the method in the class which takes as argument values for
all attributes in the above sequence and set the value of attributes
to parameter values while creating an Employee object.

Write the code to define a class to create an Organization object
with the below attributes :

1. A list of Employee objects
2. A list of types of loans Organization offers to employees
3. Designation wise eligible maximum loan amount stored as
key : value pairs - designation : maximum eligible loan amount.

Define a method which takes as argument value of the attribute
and initialize the attribute with the given value while creating
an Organization object .

Define another two methods inside the Organization class as
described below :

A.

A method to check if an employee is eligible to take a loan or not.

Method take as arguments -
1. A string representing the name of an employee.
2. A string representing a loan type.
3. A number representing the amount want to borrow as loan.

If the following conditions are fulfilled , method will return True
and add the value passed as argument for loan type and borrowing
amount ( the 2nd argument and 3rd argument ) as key : value pair to
the loan details of the employee . Conditions to be fulfilled are :

1. An employee with the name passed as the first argument is present in
the employee list of the organization

2. If the employee has not taken the loan of the type given as the
second argument earlier.(not present in the loan details of the employee)

3. If loan of the type given as the second argument is present in the
list of loan types of the Organization

4. If the amount want to borrow as loan (the value passed as 3rd argument)
plus the summation of already borrowed loan amount for different loan
types available in Loan details of the Employee is not greater than
the maximum eligible loan amount for the designation of the Employee
as per the Designation wise eligible maximum loan amount of the
Organization .

If any of these conditions is not fulfilled, method returns False.

B.

A method to find and return the designation wise count of
employees in the Employee list of the Organization still eligible
to borrow loans . An employee with a particular designation is
eligible to borrow a loan only if his / her summation of already
borrowed loans of different type is less than the maximum eligible
loan amount for that designation as per the Designation wise eligible
maximum loan amount of the Organization .

Note :
• All search should be case insensitive .
• Consider no two employees have the same name .

Instructions to write main section of the code :
a . You would require to write the main section completely,
hence please follow the below instructions for the same.

b . You would require to write the main program which is inline
to the " sample input description section " mentioned below and
to read the data in the same sequence .

C. Create the respective objects ( Employee an Organization )
with the given sequence of arguments to fulfill the method
defined in the respective classes referring to the below instructions .

i . Create a list of Employee objects . To creat the list

1. Take as input the count of employee objects you want to create

2. Create a Employee object after reading the data related to Name , designation , salary and Loan Details and add the object to the list of Employee objects which will be provided to

the Organization object . This point repeats for the number of Employee objects considered on the first line of input, point #ci.
 1) to be treated To create the Loan Details dictionary for each employee object, take as input the  count of elements you want to add to the dictionary.
i. Create a (Loan Type: Borrowed amount) key: value pair after reading the data related to it and add the pair to the dictionary for the number of element count read. ii. Create a list of loan types for types of loans offered by the Organization to the Employees by reading the count of loan types you want to add to the list followed by that many loan types one after another iii. Create the dictionary for Designation wise eligible maximum loan amount for the Organization. To create the dictionary, read the count of elements you want to store in the dictionary followed by that read that many pairs of values for "designation : maximum eligible loan amount" one after another and add to the dictionary
iv. Create Organization object by passing the List of Employee objects (created in point #c.i), the
list of loan types (created in point #ci) and dictionary for Designation wise eligible maximum loan amount(created in point #c.) as the arguments d. Take a string as employee name to be passed for the 1st argument to the method defined above to check if an employee is eligible for a loan or not.
e. Take another string as loan type to be passed for the 2nd argument to the method defined above to check if an emplovee is eligible for a method. In the output, the key and values are printed separated by a "." from the dictionary.

for example:
Programmer:3
Analyst:2
You may refer to the sample output for the display format.
You can use/refer the below given sample input and output to verify your solution using 'Test against Custom Input ' option in Hackerrank.
Input Format for Custom Testing
a. The 1st input taken in the main section is the number of Employee objects to be added to the
list of employee.
b. The next set of inputs are the values related to attributes of Employee objects to be added to
the employee List. - the employee name, designation, salary and the count of elements to be added in the Loan details of the Employee followed by the values for loan type and borrowed amount for each element to be added to the Loan details. The above point repeats for the number of
employee objects, read in point#a c. The next lines of input refers the count of loan types followed by the values for loan types.
d. The next lines of inputs are the count of designation wise eligible maximum loan amount pairs to be stored in the organization.


Sample Testcase 1:
Input:

5
Sunita
Faculty
23000
1
Home
200000

Arun
Programmer
30000
1
Personal
4000

Dipak
Tester
25000
2
Travel
10000
Personal
5000

Balen
Analyst
12000
1
Travel
2000

Tarun
Programmer
78000
2
Personal
100000
Travel
2000

3
Travel
Home
Personal

3
Programmer
300000
Faculty
200000
Analyst
100000

Tarun
Home
50000


Testcase Output :
Loan granted .
Personal : 100000
Travel : 2000
Home : 50000
Programmer : 2
Faculty : 0
Analyst : 1
