'''
6. Transportation Mode Selection
Problem: Choose a mode of transportaion based on the distance.
eg: <3KM: walk, 3-15KM: Bike, > 15KM: car
'''

# Get the user distance

distance = int(input("Enter the Distance: "))

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("Your Tranport mode is:",transport)