# Problem_3: Assign a letter grade based on a Students Score: A(90-100), B(80-89), c(70-79), D(60-69), F(below 60).

score = int(input("Enter the Score of the Student: "))

if score >= 101:
    print("Please verify your Score again")
    exit()

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

