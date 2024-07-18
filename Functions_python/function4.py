'''
4. Function Returning Multiple Values
Problem: Create a function that returns both the area and circumference of a circle given it's radius.
'''

import math

def circle_stats(radius):
    area =  math.pi * radius ** 2
    circumfrenece = 2 * math.pi * radius
    return area, circumfrenece

radius = int(input("Enter a number: "))

a,c=circle_stats(radius)
print("Area is: ",a)
print("circumfrence is: ",c)
