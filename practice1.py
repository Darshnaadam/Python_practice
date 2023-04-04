# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime # importing module datetime for current year
name = input("What is your name? : ")
age = int(input("What is your age? : "))

current_year = datetime.datetime.today().year
turning_100 = current_year + (100-age)

print("Hi "+name+" you will turn 100 in year: ",turning_100)