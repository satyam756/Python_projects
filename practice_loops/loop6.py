'''
6. Factorial Calculator
Problem: Compute the factorial of a number using a while loop
'''

# Get the user input for factorial 

number = int(input("Enter a number: "))

factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("the factorial is: ",factorial)