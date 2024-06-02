# Problem_8: Check if a password is "Weak", "Medium" or "Strong". 
# Criteria: < 6 char (Weak), 6-10 chars (Medium), > 10 chars (Strong).

psw = input("Enter Password: ")
if len(psw) < 6:
    password = "Weak"
elif len(psw) <= 10:
    password = "Medium"
else:
    password = "Strong"

print("Your Password is ",password)