'''

1. Age Group Categorization

Classify a peson's age group: 

Child( < 13),Teenager (13 - 19),Adult (20 - 59),
Senior (60 +).

'''

# Ask user to input his age

Age = int(input("Please Enter Your Age: "))

if Age < 13:
    print("You are a child")
elif Age < 20:
    print("You are an Teenager")
elif Age < 60:
    print("You are a Adult")
else:
    print("You are a Senior ")