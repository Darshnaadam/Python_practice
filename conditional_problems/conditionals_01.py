# Problem_1: Classify a persons age group: child (< 13), Teenager (13-19), Adult (19-59), senior (60+)

age = int(input("Enter Your Age: "))

if age < 13:
    print("You are a child")

elif age <  20:
    print("You are a teenager")

elif age < 60:
    print("You are an adult")

else:
    print("You are a senior")