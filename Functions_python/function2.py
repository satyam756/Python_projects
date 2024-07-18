'''
2. Function with Multiple Parameters
Problem: Create a function that takes 2 numbers as parameters and returns their sum.
'''

def SumOfTwo(num1,num2):
    return num1 + num2

num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))

print(f"sum of {num1} and {num2} is: ", SumOfTwo(num1,num2))