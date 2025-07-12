# Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
distance = int(input("Enter the Distance (in km): "))
if distance >= 0:
    if distance < 3:
        transportation = "Walk"
    elif distance <= 15:
        transportation = "Bike"
    elif distance > 15:
        transportation = "Car"
    print(f"Transportation Mode: {transportation}")

else:
    print("❗Invalid Distance! Enter the Valid Distance")