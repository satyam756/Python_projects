'''
8. Password Strength Checker
Problem: Check if a password is "Weak","Medium" or "Strong"
Criteria: <6 chars (weak),
6-10 chars (Medium),
> 10 chars (Strong)
'''

print("Simple Password Strength checker!")
password = input("Enter your Password: ")

passlen = len(password)

if passlen < 6:
    print("Your Password is Weak")
elif passlen <= 10:
    print("Your Password is Medium")
else:
    print("Your Password is Strong")