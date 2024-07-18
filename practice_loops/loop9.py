'''
9. List Uniqueness Checker
Problem: Check if all elements in a list are unique, if a duplicate is found, exit the loop and print the duplicate

items = ["apple", "banana", "orange", "apple", "mango"]
'''

items = ["apple", "banana", "orange", "apple", "mango"]

# uniqu_item = set(items)
# print(uniqu_item)

uniqu_item = set()

for item in items:
    if item in uniqu_item:
        print("Duplicate: ",item)
        break
    uniqu_item.add(item)
