import time

timestamp = time.strftime('%H: %M: %S')

if(timestamp < "12: 00: 00"):
    print("Good Morning")
elif(timestamp > "12: 00: 00" and timestamp < "17: 00: 00"):
    print("Good Morning")
else:
    print("Good Evening")

print(timestamp)

