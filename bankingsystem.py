from bankaccount import BankAccount
class BankingSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        account_number = int(input("enter account number:"))
        holder_name = input("enter holder name:")
        balance = float(input("enter balance:"))
        account = BankAccount(account_number, holder_name, balance)
        self.accounts.append(account)
        print("account created sucessfully.")

    def display_account(self):
        if len(self.accounts) == 0:
            print("no account available.")
        else:
            for account in self.accounts:
                print("account found.")
                account.display()
    
    def search_account(self):
        account_number = int(input("enter account number:"))
        for account in self.accounts:
            if account.account_number == account_number:
                print("account found.")
                account.display()
                return account
        print("account not found.")
        return None

    def deposit_money(self):
        account = self.search_account()
        if account:
            amount = float(input("enter amount to deposit money:₹"))
            account.deposit(amount)

    def withdraw_money(self):
        account = self.search_account()
        if account:
            amount = float(input("enter amount to withdraw money:₹"))
            account.withdraw(amount)

    def delete_account(self):
        account_number = int(input("enter account number to delete account:"))
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print("account deleted sucessfully.")
                return
        print("account not found.")
            


