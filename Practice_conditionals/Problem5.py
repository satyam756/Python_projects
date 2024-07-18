'''
5. Wheather Activity Suggestion
Problem: Suggest an activity based on the weather.
(e.g.. Sunny - Go For a walk,
Rainy - Read a book,
Snowy - Build a Snowman)
'''

# Get the weather information 

weather = input("Enter the weather: ")

if weather == "Sunny":
    Activity = "Go for a walk!"
elif weather == "Rainy":
    Activity = "Read a book"
elif weather == "Snowy":
    Activity = "Build a Snowman"
else:
    Activity = "Unknown Wheather"

print(Activity)