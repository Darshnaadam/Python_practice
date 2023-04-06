# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check and one number to divide by. 
# If check divides evenly into num, tell that to the user. 
# If not, print a different appropriate message.


num = int(input("Enter the number to check: "))
check = int(input("Enter the number to divide by: "))

if num % 4 == 0:
    print(num," is a multiple of 4")
else:
    print(num," is not a multiple of 4")

if num % 2 == 0:
    print(num," is a even number")
else:
    print(num," is an odd number")

if num % check == 0:
    print(num," divides evenly by ",check)
else:
    print(num," Does not divides evenly by ",check)