'''
5. Find the first non-repeated char
Problem: Given a string find the first non-repeated char
'''

# Get the userinput

inpstr = input("Enter a string: ")

for char in inpstr:
    if inpstr.count(char) == 1:
        print("Char is: ", char)
        break # it will get break after first char