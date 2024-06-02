# Problem_4: Determine if a fruit is ripe, overripe, or unique based on its color. 
# (eg., Banana: Green - unripe, Yellow - Ripe, Brown - Overripe) 

print("We will tell if the Banana is unripe, Ripe or Overripe")
color = input("Enter the color of fruit: ")

if color == 'Green'.lower():
    print("The fruit is unripe")
elif color == 'Yellow'.lower():
    print("The fruit is ripe")
elif color == 'Brown'.lower():
    print("The fruit is overripe")
