Banking System (Python)

A simple command-line banking system built in Python.
It supports creating accounts, secure authentication with hashed passwords, deposits, withdrawals, and persistent account storage in a JSON file.

⸻

Features
	•	Account creation with unique IDs
	•	Password hashing (SHA-256, via hashlib)
	•	Secure authentication
	•	Deposit & withdrawal with error handling
	•	Persistent storage using accounts.json
	•	Interactive CLI menu system

⸻

Project Structure

banking_system.py   # Main script containing Account, Bank, and BankCLI classes
accounts.json       # Stores accounts data (auto-created on first run)

How to Run
	1.	Clone or download the project.
	2.	Run the script: python banking_system.py

Use the CLI menu:
	•	Create Account → Register with username & password
	•	Login → Authenticate and access your account
	•	Deposit/Withdraw → Manage your balance
	•	Balance → Check your funds
	•	Logout/Exit → Save accounts and quit

Security
	•	Passwords are never stored in plain text.
	•	They are hashed using SHA-256 before saving in accounts.json.

Example entry in accounts.json:
[
    {
        "username": "alice",
        "id": 1,
        "balance": 100.0,
        "password": "5e884898da28047151d0e56f8dc629..."
    }
]

Example Usage:
--- Banking System ---
1. Create Account
2. Login
3. Exit
Choose an option: 1
Enter username: alice
Enter password: secret
Account created! Your ID is 1

--- Banking System ---
1. Create Account
2. Login
3. Exit
Choose an option: 2
Username: alice
Password: secret

--- Welcome alice ---
1. Deposit
2. Withdraw
3. Balance
4. Logout
Choose an option: 1
Amount: 50
Deposit successful.

Author = Sami Nejati
