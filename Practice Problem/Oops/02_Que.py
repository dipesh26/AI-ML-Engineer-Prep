# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, account_no, balance):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Dear Customer,\nYour account {self.account_no} has been debited with ₹{amount}\nAvailable Balance: {self.balance}\n")
        else:
            print("⚠️ Debit Failed - Insufficient Balance\n")

    def credit(self, amount):
        self.balance += amount
        print(f"Dear Customer,\nYour account {self.account_no} has been credited with ₹{amount}\nAvailable Balance: {self.balance}\n")

    def check_balance(self):
        print(f"Dear Customer,\nThe available balance in your account {self.account_no}\n💰 ₹{self.balance}\n")

# acc_no = int(input("Enter your Account No.: "))
user1 = Account(9876543210, 45000)
user1.check_balance()
user1.credit(3000)
user1.debit(5600)