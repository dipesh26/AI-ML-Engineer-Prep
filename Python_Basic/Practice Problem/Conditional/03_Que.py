# Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
Student_Score = int(input("Enter your score: "))
if Student_Score <= 100:
    if Student_Score < 60:
        grade = "F"
    elif Student_Score <= 69:
        grade = "D"
    elif Student_Score <= 79:
        grade = "C"
    elif Student_Score <= 89:
        grade = "B"
    else:
        grade = "A"
    print(f"Grade: {grade}")
else:
    print("❗Invalid Score! Enter the Valid Score")