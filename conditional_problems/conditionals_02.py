# Problem_2: Movie tickets are priced based on age: $12 for adults(18 and over), 
#$8 for children. 
#Everyone gets a $2 discount on Wednesday.

age = int(input("Enter your age:"))
day = input("Enter the day:")

if age >= 18: 
    price = 12
else:
    price = 8

if day == 'Wednesday':
    price -= 2
    print("Discount of 2$ on Wednesday")

print(f"The ticket price is: ${price}")