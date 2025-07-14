
month = str(input("Enter the Month: "))
day = int(input("Enter the Day Number: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:      #Default Value
        print("Enter the Valid Number :)")

# Conbine Values:
match day:
    case 1|2|3|4|5:
        print("Today is Weekday")
    case 6|7:
        print("Today is Weekend")
    case _:      #Default Value
        print("Enter the Valid Number :)")

match day:
    case 1|2|3|4|5:
        print("A Weekday in ",month)
    case 6|7:
        print("A WeekEnd in ",month)
    case _:
        print("Enter the Valid Number :)")


# Using if-Satetment

month = int(input("Enter the Month: "))
day = int(input("Enter the Day Number: "))

match day:
    case 1|2|3|4|5:
        if(month == 1):
            print("A Weekday in January")
        elif(month == 2):
            print("A Weekday in Febuary")
        elif(month == 3):
            print("A Weekday in March")
        elif(month == 4):
            print("A Weekday in April")
        elif(month == 5):
            print("A Weekday in May")
        elif(month == 6):
            print("A Weekday in June")
        elif(month == 7):
            print("A Weekday in July'")
        elif(month == 8):
            print("A Weekday in August")
        elif(month == 9):
            print("A Weekday in September")
        elif(month == 10):
            print("A Weekday in October")
        elif(month == 11):
            print("A Weekday in November")
        elif(month == 12):
            print("A Weekday in December")

    case 6|7:
        if(month == 1):
            print("A WeekEnd in January")
        elif(month == 2):
            print("A WeekEnd in Febuary")
        elif(month == 3):
            print("A WeekEnd in March")
        elif(month == 4):
            print("A WeekEnd in April")
        elif(month == 5):
            print("A WeekEnd in May")
        elif(month == 6):
            print("A WeekEnd in June")
        elif(month == 7):
            print("A WeekEnd in July'")
        elif(month == 8):
            print("A WeekEnd in August")
        elif(month == 9):
            print("A WeekEnd in September")
        elif(month == 10):
            print("A WeekEnd in October")
        elif(month == 11):
            print("A WeekEnd in November")
        elif(month == 12):
            print("A WeekEnd in December")
    case _:
        print("Enter the Valid Number :)")