# Problem_6: Choose a mode of transportation based on the distance 
# (eg., <2 km: walk, 3-15 km: bike, >15: car).

distance = int(input("Enter the distance to be traveled: "))
if distance < 2:
    transportation = 'Walk'
elif distance < 15:
    transportation = 'take a Bike'
else:
    transportation = 'take a Car'

print("I think you should", transportation)
