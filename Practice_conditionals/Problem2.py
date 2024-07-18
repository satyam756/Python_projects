'''
2. Movie Ticket Pricing
Problem: Movie tickets are priced based on age:
$12 for adults(18 and over),
$8 for children,
Everyone gets a $2 discount on Wednesday.
'''

# Get the user age
Age = int(input("Please enter your age: "))

# Get the day if Wednesday
Day = input("What's the day today?: ")

# make price $12 if age is greater than or eq 18 else 8
price = 12 if Age >=18 else 8

if Day == "Wednesday":
    price -= 2

print("Your Movie ticket price is:$",price)