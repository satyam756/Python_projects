'''
5. Default Parameter Value
Problem: Write a function that greets a user. if no name is provided, it should greet with default name.
'''

def greetUser(name = "User"):
    return "Hello, " + name

name = input("Enter a name: ")
print(greetUser(name))
print(greetUser())