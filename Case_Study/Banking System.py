import csv
import threading
import time

class Customer:
    def __init__(self, customer_id, name, account_balance, account_type):
        self.customer_id = customer_id
        self.name = name
        self.account_balance = account_balance
        self.account_type = account_type
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            self.transactions.append(f"Deposited {amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            return True
        return False

    def apply_interest(self):
        if self.account_type == 'Savings':
            interest = self.account_balance * 0.05
            self.account_balance += interest
            self.transactions.append(f"Applied interest: {interest}")

class BankingSystem:
    def __init__(self):
        self.customers = []
        self.lock = threading.Lock()
        self.load_customers()

    def load_customers(self):
        try:
            with open(r"C:\Users\SayaliThange\Downloads\CustomerData.csv", 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.customers.append(
                        Customer(
                            int(row['CustomerID']),
                            row['Name'],
                            float(row['AccountBalance']),
                            'Savings' 
                            
                            if int(row['CustomerID']) % 2 == 0 
                            else 'Checking'
                        )
                    )
        except FileNotFoundError:
            print("Error: data.csv file not found.")

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def deposit(self, customer_id, amount):
        customer = self.find_customer(customer_id)
        if customer:
            if amount > 0:
                customer.deposit(amount)
                print(f"Deposited {amount} to {customer.name}'s account.")
            else:
                print("Deposit amount must be greater than 0.")
        else:
            print("Customer not found.")

    def withdraw(self, customer_id, amount):
        customer = self.find_customer(customer_id)
        if customer:
            if customer.withdraw(amount):
                print(f"Withdrew {amount} from {customer.name}'s account.")
            else:
                print("Insufficient balance or invalid amount.")
        else:
            print("Customer not found.")

    def view_transactions(self, customer_id):
        customer = self.find_customer(customer_id)
        if customer:
            print(f"Transaction history for {customer.name}:")
            for transaction in customer.transactions:
                print(transaction)
        else:
            print("Customer not found.")

    def apply_interest_to_all(self):
        with self.lock:
            for customer in self.customers:
                customer.apply_interest()
                print(f"Applied interest to {customer.name}'s account. New balance: {customer.account_balance}")

banking_system = BankingSystem()


def periodic_interest():
    while True:
        try:
            banking_system.apply_interest_to_all()
            time.sleep(10)
        except KeyboardInterrupt:
            print("Stopping periodic interest application.")
            break

interest_thread = threading.Thread(target=periodic_interest, daemon=True)
interest_thread.start()

# User interaction
def user_menu():
    while True:
        print("\nBanking System Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Transactions")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                customer_id = int(input("Enter Customer ID: ").strip())
                amount = float(input("Enter amount to deposit: ").strip())
                banking_system.deposit(customer_id, amount)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == '2':
            try:
                customer_id = int(input("Enter Customer ID: ").strip())
                amount = float(input("Enter amount to withdraw: ").strip())
                banking_system.withdraw(customer_id, amount)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == '3':
            try:
                customer_id = int(input("Enter Customer ID: ").strip())
                banking_system.view_transactions(customer_id)
            except ValueError:
                print("Invalid input. Please enter a numeric Customer ID.")
        elif choice == '4':
            print("Exiting the banking system.")
            break
        else:
            print("Invalid choice. Please try again.")

try:
    user_menu()
except KeyboardInterrupt:
    print("\nExiting banking system.")
