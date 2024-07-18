'''
3. Multiplication table printer
Problem: Print the multiplication table for given number upto 10,but skip the 5th iteration.
'''

# Get the user input

table = int(input("Enter a number: "))

for i in range(1,11):
    if i == 5:
        continue
    print(table, 'X', i, '=', table*i)