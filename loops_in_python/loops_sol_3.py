# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

numbers = int(input("Enter the number: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(numbers, "x", i, "=", numbers*i)