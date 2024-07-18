'''
10. Recursive Function
Problem: Create a recursive function to calculate the factorial of a number
'''

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


num = int(input("Enter a number: "))

output = fact(num)

print(f"Factorial of {num} is {output}")

