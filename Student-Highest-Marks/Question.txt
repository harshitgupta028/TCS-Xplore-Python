Create a class Student with the below attributes
name of type String
sub1 of type float
sub2 of type float
sub3 of type float

Create the __init__ method which takes all parameters in the above sequence

Create a method calculateResult() in the Student class
It checks if the student has scored greater than 40 in all the individual
3 subjects. If so, it further calculates the average and returns average.

Create another class School with the below attributes
name of type String
studentDict of type dictionary

Where key is a Student object and value refers to the result pass or fail
Create the __init__ method which takes all parameters in the above sequence

Define the two methods getStudentResult and findStudentWithHighestMarks
in this School class

getStudentResult : This method internaly calls calculateResult method
of Student class to get average. This method checks if the student average
greater than 60 then it updates the student dictionary value as pass. Displays
the names of students who passed. If o student passed print 'No student passed'

findStudentWithHighestMarks This method accept the list of passed.
Display the name of the highest scored student

Input:

4
Harshit Gupta
91
88
78
Ayush Joshi
94
83
90
Mahi Meena
95
87
90
Yogesh Singh
41
42
41


Output:

List of Passed Students:
Harshit Gupta
Ayush Joshi
Mahi Meena
Student Obtained Maximum Marks: Mahi Meena
