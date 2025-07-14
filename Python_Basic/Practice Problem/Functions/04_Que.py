# Create a function that returns both the area and circumference of a circle given its radius.

def area_and_circumference_calc(r):
    pie = 3.14
    area = pie * (r ** 2)
    circumference = 2 * pie * r
    return area, circumference

r = int(input("Enter the Radius of circle: "))

areaa, circumferenc = area_and_circumference_calc(r)
print(f"Area of a circle: {areaa}")
print(f"circumference of a circle: {circumferenc}")