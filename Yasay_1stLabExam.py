class BankSys:
    def __init__(self, name, account_num, balance):
        self.name = name
        self.account_num = account_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def withdraw_fee(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.balance -= 25
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_info(self):     
        print("\n--------Welcome to Roms Bank--------")   
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_num}")
        print(f"Balance: {self.balance}")

Name = input("Enter account name: ")
Account_num = input("Enter your account number: ") 
balance = float(input("Enter your balance:"))  
account = BankSys(Name, Account_num, balance)
account.display_info()      

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Withdraw with Fee")
        print("4. Display Account Info")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw (with Fee): "))
            account.withdraw_fee(amount)    
        elif choice == '4':
            account.display_info()
        elif choice == '5':
            print("Thank you for choosing us!")
            break
        else:
            print("Invalid choice. Please try again.")
     


        