'''
9. Generate a function with yield
Problem: Write a generator function that yields even numbers up to a specified limit.
'''

def even_generator(limit):
    for i in range(2, limit + 2,2):
        # print(i)
        yield i
# even_generator(10)
for num in even_generator(10):
    print(num)
