'''
6. Lambda Function
Problem: Create a Lambda function to compute the cube of a number.
'''

cube = int(input("Enter a number: "))

output = lambda x: x ** 3

print(output(cube))