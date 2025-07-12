# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
order_size = str(input("Enter the Size of Coffee (Small,Medium,large): ")).lower()
option = str(input("Want \"Extra shot\" of espresso? (y/n): ")).lower()

if option == "y":
    order = order_size + " coffee with Extra shot of espresso."
else:
    order = order_size + " coffee"
print(f"Order: {order}")