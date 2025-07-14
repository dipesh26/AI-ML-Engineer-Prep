
# Table Generater using for loop.
print("---Table Generator---")
num = int(input("Enter the No.: "))
print("Table of",num, ":)")
i = 1

for i in range(1,11):
    print(num, "*", i, "=", num*i)