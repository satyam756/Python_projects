'''
3. Cache Return Values
Problem: Implement a decorator that caches the return values of a function,so that when it's called with the same argument,the cached value is returned insted of re-executing the function.
'''
import time

def cache(func):
    cache_values = {}
    def wrapper(*args):
        if args in cache_values:
            return cache_values[args]
        result = func(*args)
        cache_values[args] = result
        return result
    return wrapper

@cache
def log_running_function(a,b):
    time.sleep(4)
    return a+b


print(log_running_function(2,3))
print(log_running_function(2,3))
print(log_running_function(2,5))
