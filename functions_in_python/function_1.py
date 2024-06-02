# Write a function to calculate and return the sqaure of a number

def square(number):
    return number ** 2

#result = square(4)
#print(result)

#Taking input
num = int(input('Enter the number and We will calculate the Square of the number:'))
result = square(num)
print('The Square of the number is: ', result)
