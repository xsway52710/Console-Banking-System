import hashlib

class Account:
    def __init__(self, username: str, password: str, account_id: int, balance: float = 0.0):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.id = account_id
        self.balance = balance        
        
    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password: str) -> bool:
        return self.password_hash == self._hash_password(password)
    
    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    
import json
from typing import Optional

class Bank:
    def __init__(self, storage_file = "accounts.json"):
        self.storage_file = storage_file
        self.accounts = self._load_accounts()

    def _load_accounts(self):
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                return {acc["id"]: Account(acc["username"], acc["password"], acc["id"], acc["balance"]) for acc in data}
        except FileNotFoundError:
            return {}

    def _save_accounts(self):
        with open(self.storage_file, "w") as f:
            json.dump([{"username": acc.username, "id": acc.id, "balance": acc.balance, "password": acc.password_hash} for acc in self.accounts.values()], f, indent=4)

    def create_account(self, username: str, password: str, initial_balance: float = 0.0) -> Account:
        account_id = len(self.accounts) + 1
        account = Account(username, password, account_id, initial_balance)
        self.accounts[account_id] = account
        self._save_accounts()
        return account

    def authenticate(self, username: str, password: str) -> Optional[Account]:
        for acc in self.accounts.values():
            if acc.username == username and acc.check_password(password):
                return acc
        return None
    
class BankCLI:
    def __init__(self, bank: Bank):
        self.bank = bank

    def run(self):
        while True:
            print("\n--- Banking System ---")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

    def create_account(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        acc = self.bank.create_account(username, password)
        print(f"Account created! Your ID is {acc.id}")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        account = self.bank.authenticate(username, password)
        if not account:
            print("Invalid credentials.")
            return
        self.account_menu(account)

    def account_menu(self, account: Account):
        while True:
            print(f"\n--- Welcome {account.username} ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. Logout")

            choice = input("Choose an option: ")

            try:
                if choice == "1":
                    amount = float(input("Amount: "))
                    account.deposit(amount)
                    print("Deposit successful.")
                elif choice == "2":
                    amount = float(input("Amount: "))
                    account.withdraw(amount)
                    print("Withdrawal successful.")
                elif choice == "3":
                    print(f"Balance: {account.balance}")
                elif choice == "4":
                    self.bank._save_accounts()
                    print("Logged out.")
                    break
                else:
                    print("Invalid choice.")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    bank = Bank()
    app = BankCLI(bank)
    app.run()
