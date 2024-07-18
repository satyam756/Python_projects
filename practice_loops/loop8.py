'''
8. Prime Number Checker
Problem: Check if a number is prime.
'''

# Get the user input

number = int(input("Enter a number: "))

is_prime = True

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            is_prime = False
            break
if is_prime:
    print("It's Prime")
else:
    print("Not Prime")