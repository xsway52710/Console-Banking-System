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
