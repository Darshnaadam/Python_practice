# Problem_10: Recommend a type of pet food based on the pet species and age. 
# (eg., Dog: < 2 years -puppy food, cat: >5 years - Senior cat food).

species = input("Enter your pet species: ")
age = int(input("Enter your pet age: "))

if (species == 'Dog'.lower() and age <= 2):
    print("Your Dog need junior Puppy food")
elif (species == 'Dog'.lower() and age > 2):
    print("Your Dog need Adult Dog food")
elif (species == 'Cat'.lower() and age < 5):
    print("Your Cat need junior Cat food")
elif (species == 'Cat'.lower() and age > 5):
    print("Your Cat need Senior Cat food")
else:
    print("Enter proper information")