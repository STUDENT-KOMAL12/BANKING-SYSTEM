class BankAccount:
    def __init__(self, account_number, holder_name, balance = 0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited sucessfully.") 

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn sucessfully.")
        else:
            print("insufficient balance.")

    def display(self):
        print("\nAccount Details.")
        print("account_number :", self.account_number)
        print("holder_name    :", self.holder_name)
        print("balance        :₹", self.balance)
        print("-" * 40)




