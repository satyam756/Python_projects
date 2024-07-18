'''
7. Coffee Customization
Problem: Customize a coffee order:
Small,Medium or large with an option for "extra shot" of expresso.
'''

# get order_size
# extra_shot = "y"
order_size = input("Enter your order S,M,L: ")
extra_shot = input("Do you need extra shot?: ")

if extra_shot == "y":
    coffe = order_size + " Coffe with an extra shot"
else:
    coffe = order_size + " Coffee"

print(coffe)