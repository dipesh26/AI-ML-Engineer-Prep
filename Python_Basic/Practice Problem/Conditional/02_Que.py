# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
age = int(input("Enter your Age: "))
day = str(input("Enter the day: ")).lower()
adult_price = 12
childer_price = 8
discount = 2

if day == "wednesday":
    if age < 18:
        print(f"Price: ${childer_price}")
        print(f"Wednesday Discount: ${discount}")
        print(f"Price for Movie Ticket is \"${childer_price - discount}\"")
    else:
        print(f"Price: ${adult_price}")
        print(f"Wednesday Discount: ${discount}")
        print(f"Price for Movie Ticket is \"${adult_price - discount}\"")
else:
    if age < 18:
        print(f"Price for Movie Ticket is \"${childer_price}\"")
    else:
        print(f"Price for Movie Ticket is \"${adult_price}\"")