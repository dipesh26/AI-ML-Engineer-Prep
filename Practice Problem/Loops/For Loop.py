# 1: Print the first 10 natural numbers using for loop.
# for i in range(10):
    # print(i+1)

# 2: Python program to print all the even numbers within the given range.
# n = int(input("Enter the number: "))
# for i in range(n):
    # if i%2==0:
        # print(i)

# 3: Python program to calculate the sum of all numbers from 1 to a given number.
# n = int(input("Enter the Number: "))
# sum = 0
# for i in range(n+1):
    # sum = sum + i
# print(sum)

# 4: Python program to calculate the sum of all the odd numbers within the given range.
# n = int(input("Enter the Number: "))
# sum = 0
# for i in range(n):
    # if i % 2 != 0:
        # sum = sum + i
# print(sum)

# 5: Python program to print a multiplication table of a given number
# n = int(input("Enter the Number: "))
# for i in range(1,11):
    # mult = n*i
    # print(n,"*",i," = ",mult)

# 6: Python program to display numbers from a list using a for loop.
# n = int(input("Enter the Number: "))
# list = []
# for i in range(n+1):
    # list.append(i)
# print("List: ",list)
# for num in list:
    # print(num)

# 7: Python program to count the total number of digits in a number.
# n = input("Enter the Number: ")
# count = 0
# for i in n:
    # count = count + 1
# print("Total number 

# 8: Python program to check if the given string is a palindrome.
# str = str(input("Enter the String: ")).lower()
# rev_str = ""
# for i in str:
    # rev_str = i + rev_str
# if rev_str == str:
    # print("The given string is a palindrome.")
# else:
    # print("The given string is not palindrome.") 

# 9: Python program that accepts a word from the user and reverses it.
# word = str(input("Enter the word: "))
# rev_word = ""
# for i in word:
    # rev_word = i + rev_word
# print(rev_word)

# 10: Python program to check if a given number is an Armstrong number
            # Armstrong number, 1*1*1 + 5*5*5 + 3*3*3 = 153
# n = input("Enter the number: ")
# sum = 0
# for i in n:
    # sum = sum + (int(i) ** len(n))
# if sum == int(n):
    # print(sum," is a Armstrong number")
# else:
    # print(sum," is not a Armstrong number")

# 11: Python program to count the number of even and odd numbers from a series of numbers.
# num_list = [1,3,5,6,99,134,55]
# even_count = 0
# odd_count = 0
# for i in num_list:
    # if i%2==0:
        # even_count = even_count + 1
        # print(i," is a even number")
    # else:
        # odd_count = odd_count + 1
        # print(i," is a odd number")
# print("\nCount of even numbers: ",even_count)
# print("Count of odd numbers: ",odd_count)

# 12: Python program to display all numbers within a range except the prime numbers.
# start = int(input("Enter start of range: "))
# end = int(input("Enter end of range: "))

# print("\nNon-prime numbers from",start,"to",end,":\n")      

# for num in range(start, end + 1):
#     if num < 2:
#         print(num, end=" ")
#         continue

#     for i in range(2, num):
#         if num % i == 0:
#             print(num, end=" ")
#             break

# 13: Python program to get the Fibonacci series between 0 to 50.
# n = int(input("Enter the number: "))
# a = 0
# b = 1
# sum = 0
# print(a)
# print(b)
# for i in range(n):
#     sum = a + b
#     if sum > n:
#         break
#     a = b
#     b = sum
#     print(sum)

# 14: Python program to find the factorial of a given number.
        #    5! = 5 × 4 × 3 × 2 × 1 = 120
# n = int(input("Enter the number: "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print("The factorial of",n,"is",fact)

# 15: Python program that accepts a string and calculates the number of digits and letters.
# n = input("Enter the string: ")
# digits = 0
# letters = 0
# for i in n:
#     if i.isdigit():
#         digits = digits + 1
#     else:
#         i.isalpha()
#         letters = letters + 1
# print(f"The \"{n}\" string contains \"{digits}\" digits & \"{letters}\" letters")

# 16: Write a Python program that iterates the integers from 1 to 25.
# if no. is multiple of 4 and 5 print fizzbuzz
# if no. is divisible by 4 print fizz and no by 5
# if no. is divisible by 5 print buzz and not by 4
# start = int(input("Enter Start From: "))
# end = int(input("Enter End To: "))
# for num in range(start,end+1):
#     if num%4==0 and num%5==0:
#         print(f"{num} is fizzbuzz")
#         continue
#     elif num%4==0 and num%5!=0:
#         print(f"{num} is fizz")
#         continue
#     elif num%5==0 and num%4!=0:
#         print(f"{num} is buzz")
#     else:
#         print(num)        

# 17: Python program to check the validity of password input by users.
# passw = input("Enter the Password: ")
# length = False
# uppercase = False
# lowercase = False
# number = False
# specialchar = False

# if (len(passw) >= 8) and (len(passw) <= 16):
#     length = True
#     for i in passw:
#         if i.isupper():
#             uppercase = True
#         elif i.islower():
#             lowercase = True
#         elif i.isdigit():
#             number = True
#         if (i=="@" or i=="#" or i=="$" or i=="^" or i=="*" or i=="&"):
#             specialchar = True

#     if(length==True and uppercase==True and lowercase==True and number==True and specialchar==True):
#         print("✅ Valid Password")        
#     else:
#         print("❌ Invalid Password")
#         print("Password must contain \"uppercase\", \"lowercase\", \"digit\", & \"special character (@, #, $, ^, *, &)\"")

# else:
#     print("❌ Password should be at least 8 characters")

# 18: Python program to convert the month name to a number of days.
# month = str(input("Enter the Month: ")).lower()

# if month == "january"or"march"or"may"or"july"or"august"or"october"or"december":
#     print(f"The month of \"{month}\" has 31 days")
# elif month == "february":
#     print(f"The month of \"{month}\" has 28/29 days")
# elif month == "april"or"june"or"september"or"november":
#     print(f"The month of \"{month}\" has 3o days")
# else:
#     print("❌ Enter the valid month")
