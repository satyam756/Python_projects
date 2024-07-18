'''
7. Validate input
Problem: Keep asking the user for input until they enter a number between 1 and 10
'''

# Get the user input

while True:
    num = int(input("Enter value between 1 & 10: "))
    print("Your number is", num)
    if 1 <= num <=10:
        break