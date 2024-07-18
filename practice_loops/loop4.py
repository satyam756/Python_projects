'''
4. Reverse a String
Problem: Reverse a String using a loop
'''

# Get input string

userinp = input("Enter a String: ")

reverse_str = ""

for char in userinp:
    reverse_str = char + reverse_str 

print(reverse_str)