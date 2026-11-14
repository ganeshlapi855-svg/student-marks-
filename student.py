#develop a python application to accept a student's name and marks in three subjects
#and calculate the total marks. push the code to a Github repository. Modify the program to calculate the average
#marks and display pass/fail status. commit and push the madified code to the same repository

name = input("enter student name")

print("enter student marks of three subjects")

sub1 = input("enter marks of sub 1 :")
sub2 = input("enter marks of sub 2 :")
sub3 = input("enter marks of sub 3 :")

total_marks = int(sub1) + int(sub2) + int(sub3)

print ("Student Name:", name)
print ("Total Marks:", total_marks)     
  