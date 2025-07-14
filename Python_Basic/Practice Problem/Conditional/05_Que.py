# Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
weather = str(input("Enter the Weather (Sunny,Rainy,Snowy): ")).lower()
if weather == "sunny":
    activity = "Go for a walk"
elif weather == "rainy":
    activity = "Read a book"
elif weather == "snowy":
    activity = "Build a snowman"
else:
    print("❗Invalid Weather! Enter the Valid Weather")
print(activity)