'''
7. Function with *args
Problem: Write a function that takes variable number of arguments and returns their sum.
'''

def sum_all(*args): # can be given anything with *
    # print(*args)
    # print(args) # returns tupples
    # for i in args:
    #     print(i * 2)
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3))
print(sum_all(1,2,3,4))