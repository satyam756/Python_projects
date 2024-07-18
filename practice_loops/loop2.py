'''
2. Sum of Even numbers
Problem: Calculate the sum of even numbers up to a given number n.
'''

# get the user input

num = int(input("Enter a number: "))
sum_even = 0
for i in range(1,num+1):
    if i % 2 == 0:
        sum_even += 1

print("sum is", sum_even) 