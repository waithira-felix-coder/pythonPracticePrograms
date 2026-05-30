class BankAccount:

   def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        # Public attribute
        self.__balance = balance # Private attribute
# Public method to access the private balance
   def get_balance(self):
       return self.__balance
# Public method to safely update balance
   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount
           print(f"Deposited {amount}. New balance: {self.__balance}")
           elif:
             print("Deposit must be positive.")
# Public method to safely withdraw money
   def withdraw(self, amount):
       if 0 < amount <= self.__balance:
           self.__balance -= amount
           print(f"Withdrew {amount}. New balance: {self.__balance}")
           elif:
               print("Insufficient funds or invalid amount.")
# ---------- Main program to test the class ----------
# Create a new account
account = BankAccount("Alice", 1000)

# Display initial balance
print(f"\nAccount Holder: {account.account_holder}")
print(f"Initial Balance: {account.get_balance()}")
# Deposit money
account.deposit(500)
# Withdraw money
account.withdraw(300)
# Try to withdraw more than balance
account.withdraw(2000)
# Try to directly access the private balance (should fail)
try:
print(account.__balance)
except AttributeError:
print("Cannot access private attribute '__balance' directly.")
# Accessing the balance correctly
print(f"Final Balance: {account.get_balance()}")
