# Problem: Reverse a string using a loop.

string = input("Enter the string: ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print(reversed_string)