appleprice = 20
budget = int(input("Enter your Budget: "))

if(budget - appleprice > 50):
    print("You can Buy the apples")
elif(budget - appleprice >= 100):
    print("it's Okay, You can Buy the apples")
else:
    print("You can not Buy the apples")