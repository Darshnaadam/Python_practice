# Take a list and write a program that prints out all the elements of the list that are less than 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
""" for i in a:
    if i < 5:
        print(i) """
b = []
for i in a:
    if i < 10:
        b.append(i) # it will store the value of i in list b
        b.sort()
print(b)