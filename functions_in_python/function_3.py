# Write a function multiply that multiplies two numbers, 
# but can also accept and multiply strings

def multiply(p1, p2):
    return p1 * p2

#print(multiply(5, 5))
#print(multiply('a', 5))
#print(multiply(5, 'a'))

#Asking input from users

n1 = int(input("Enter First number: "))
n2 = input("Enter Second number: ")

result = multiply(n1, n2)
print(result)
