'''
1. Basic Function Syntax
Problem: Write a function to calculate and return the square of a number
'''

def get_square(num):
    out = num ** 2
    print(out)
    return out

num = int(input("Enter a number: "))
result = get_square(num)
print(result)