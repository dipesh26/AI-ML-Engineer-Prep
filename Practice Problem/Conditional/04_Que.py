# Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
fruit = "banana"
color = str(input("Enter the color of Fruit (Green,Yellow,Brown): ")).lower()

if fruit == "banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overripe")
    else:
        print("❗Invalid Color! Enter the Valid Color")
else:
    print("❗Invalid Fruit! Enter the Valid Fruit")