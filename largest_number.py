# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Wayne Loan
# Section: 574
# Assignment: 4-6
# Date: 17/09/22
#

#takes in inputs
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))
#checks each input to find the largest number
if a >= b and a >= c:
    print(f"The largest number is {float(a)}")
elif b >= c:
    print(f"The largest number is {float(b)}")
else:
    print(f"The largest number is {float(c)}")