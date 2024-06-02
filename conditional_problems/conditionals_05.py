# Suggest an activity based on the weather
# (eg., Sunny - go for a walk, Rainy - Read a book, Snowy - Build a snowman)

weather = input("How is the Weather ?: ")

if weather == 'Sunny'.lower():
    print("Go for a walk")
elif weather == 'Rainy'.lower():
    print("Read a book")
elif weather == 'Snowy'.lower():
    print("Build a snowman")
else:
    print("Please Enter Valid Weather for eg., Sunny, Rainy or Snowy.")