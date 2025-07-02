import sys

class BankAccount:
    def __init__(self, user, balance):
        self.user = user
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDear {self.user}\nYour account has been credited with ₹{amount}.\nAvailable Balance: ₹{self.balance}\n")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"\nDear {self.user},\nYour account has been debited with ₹{amount}.\nAvailable Balance: ₹{self.balance}\n")
        else:
            print("⚠️ Debit Failed - Insufficient Balance.\n")

    def balance_check(self):
        print(f"\nDear {self.user},\nThe available balance in your account.\n💰 ₹{self.balance}\n")

accounts = {
    "mahima" : {"pin" : 2344,"balance" : 8797},
    "sanjay" : {"pin" : 9808,"balance" : 4356},
    }

def register():
    print("\n-- Create a Account --")
    username = input("Enter Username: ").lower()
    if username in accounts:
        print("❌ Username already exists!\n")
        return
    
    pin = int(input("Set 4-digit pin: "))
    conf_pin = int(input("Re-enter 4-digit pin: "))
    if conf_pin != pin:
        print("❌ Pin doesn't match\n")
        return
    
    balance = float(input("💰 Initial Deposit: ₹"))
    if balance <= 0:
        print("❌ To open the account atleat deposit ₹1000")
        return

    accounts[username] = {
        "pin" : pin,
        "balance" : balance
        }
    
    print("\n✅ Account created successfully!\n")
    login()
    return

def login():
    print("-- Login to Account --")
    while True:
        username = input("Enter Username: ").lower()
        if username in accounts:
            while True:
                pin = int(input("Enter 4-digit pin: "))
                if accounts[username]["pin"] == pin:
                    print(f"\n🎉 Welcome {username}!\n")
                    user_obj = BankAccount(username, accounts[username]["balance"])
                    banking(user_obj)
                    return
                else:
                    print("❌ Invalid Pin!\n")
        else:
            print("❌ Invalid username!\n")

def banking(user):
    while True:
        print("[1] Balance Check  [2] Deposit  [3] Withdraw  [4] Exit")
        userinput = int(input("☝️  Choose the Option: "))
        if userinput == 1:
            user.balance_check()
        elif userinput == 2:
            deposit_amt = int(input("Enter the Amount: ₹"))
            user.deposit(deposit_amt)
        elif userinput == 3:
            withdraw_amt = int(input("Enter the Amount: ₹"))
            user.withdraw(withdraw_amt)
        elif userinput == 4:
            print("👋 Thank you for banking with us. Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid Input!\n")
        break

print(f"----- 🏦 Welcome to Python Bank -----")
print("[1] Login  [2] Register  [3] Exit")
choice = int(input("☝️  Choose the Option: "))

while True:
    if choice == 1:
        login()
    elif choice == 2:
        register()
    elif choice == 3:
        print("👋 Thank you for visiting. Goodbye!")
        break
    else:
        print("❌ Invalid Option!\n")

