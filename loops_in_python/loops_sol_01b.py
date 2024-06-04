# Problem: Given a list of numbers, count how many are positive.
# Asking for user input

numbers = input("Please enter a list of numbers: ")
numbers_list = [float(num) for num in numbers.split()]
positive_count = 0

for num in numbers_list:
    if num > 0:
        positive_count += 1

print("Number of positive count in a given list are: ",positive_count)
