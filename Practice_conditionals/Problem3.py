'''
3. Grade Calculator
Problem: Assign a letter grade based on a student's score:
A (90-100),B (80-89),C (70-79),D (60-69),F (Below 60).
'''

# Get the Score of the Student

Score = int(input("Enter Student Marks: "))

if Score > 100:
    print("Grades should not exceed 100")
    exit()

if Score >= 90:
    print("Your Grade is: A")
elif Score >= 80:
    print("Your Grade is: B")
elif Score >= 70:
    print("Your Grade is: C")
elif Score >= 60 :
    print("Your Grade is: D")
else:
    print("Your Grade is: F")

