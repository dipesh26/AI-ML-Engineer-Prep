questions = [
    "1) What is the correct file extension for Python files?",
    "2) Which keyword is used for function creation in Python?",
    "3) What will be the output of print(2 ** 3) in Python?",
    "4) What data type is the object below? x = [1, 2, 3]",
    "5) What is the result of bool('False') in Python?"
]

options = [
    ["A) .pyth", "B) .pt", "C) .py", "D) .pyt"],
    ["A) def", "B) function", "C) fun", "D) define"],
    ["A) 6", "B) 8", "C) 9", "D) 5"],
    ["A) Dictionary", "B) Tuple", "C) List", "D) Set"],
    ["A) False", "B) True", "C) 0", "D) Error"]
    ]

correct_answers = ["C", "A", "B", "C", "B"]

price_amount = [1000, 2000, 4000, 8000, 16000]

# Start of Game
print("\n🎉 Welcome to Kaun Banega Crorepati - Python Edition 🎉\n")

total_amount = 0

for i in range(len(questions)):
    print("\nPrice:",price_amount[i],"              Total Amount:",total_amount,"\n")
    print(questions[i])
    for option in options[i]:
        print("  ",option)
    
    answer = input("\nEnter your Answer (A/B/C/D): ")
    answer = answer.upper()

    if answer == correct_answers[i]:
        print("\n✅ Correct Answer!")
        total_amount = total_amount + price_amount[i]
        print("💰 You have won ₹",price_amount[i])
    else:
        print("\n❌ Wrong Answer!")
        print("The correct answer was:",correct_answers[i])
        break

    input("Please press \"Enter\" for next question: ")

print(f"\n🏁 Game Over! You are taking home: ₹{total_amount}")