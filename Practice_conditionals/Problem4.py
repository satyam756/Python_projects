'''
4. Fruit Ripness Checker
Problem: Determine if a fruit is ripe,overripe or unrip 
based on it's color. (e.g, Banana: Green - Unrip,
Yellow - Ripe,Brown - Overripe)
'''

# Take user input

fruit = input("Enter Fruit")
color = input("Enter color")

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
else:
    print("Unknown Fruit")