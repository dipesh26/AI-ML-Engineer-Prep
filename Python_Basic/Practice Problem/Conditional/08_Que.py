# Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
passw = input("Enter the Password: ")

if (len(passw) < 6):
    print("Weak")
elif (len(passw) <= 10):
        print("Medium")
else:
    print("Strong")