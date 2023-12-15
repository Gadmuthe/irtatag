Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class ATM:
...     def __init__(self):
...         self.balance = 1000
...     def check_balance(self):
...         print(f"Your current balance is:  ${self.balance}")
...     def deposit(self, amount):
...         if amount > 0 :
...             self.balance += amount
...             print(f"Deposited ${amount} successfully.")
...         else:
...             print("Invalid amount for deposit.")
...     def withdraw(self, amount):
...         if amount <= self.balance and amount > 0:
...             self.balance -= amount
...             print(f"Withdrawn ${amount} successfully.")
...         elif amount <= 0:
...             print("Invalid amount for withdrawal.")
...         else:
...             print("Insufficient funds.")
... 
...             
>>> atm = ATM()
>>> atm.check_balance()
Your current balance is:  $1000
>>> atm.deposit(500)
Deposited $500 successfully.
>>> atm.check_balance()
Your current balance is:  $1500
>>> atm.withdraw(300)
Withdrawn $300 successfully.
>>> atm.check_balance()
Your current balance is:  $1200
>>> atm.withdraw(1500)
Insufficient funds.
