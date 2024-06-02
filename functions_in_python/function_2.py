#write a function that takes two numbers as parameters and return their sum

def add(num1, num2):
    return num1 + num2

#result = add(5,5)
#print(result)

#Taking input from user
n1 = int(input("Enter the First Number: "))
n2 = int(input("Enter the Second Number: "))

result = add(n1,n2)
print("Sum of 2 number is: ", result)