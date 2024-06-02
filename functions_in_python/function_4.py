# Create a function that returns both the area circumference of a circle given its radius.
import math

def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

#a, c = circle(3)
#print("Area: ", round(a), "Circumference: ", round(c))

# Taking input from user
r = int(input("Enter the Radius of Circle: "))
a, c = circle(r)
# printing the value until 2 decimal place
print("Area: ", round(a, 2), "Circumference: ", round(c, 2))