"""
Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.

"""

class BankAccount:
  def __init__(self, name):  # Initializing account holder's name and balance
    self.name = name
    self.balance = 0

  def deposit(self, n):  # Method to deposit money
    self.balance += n
    print(f"\nSuccessfully Deposited {n}$")
    print(f"Account Balance: {self.balance}$\n")

  def withdraw(self, w):  # Method to withdraw money
    if w > self.balance:
      print(f"\nInsufficient Balance, cannot withdraw {w}$")
      print(f"Available Balance: {self.balance}$\n")
    else:
      self.balance -= w
      print(f"\nWithdrawal Successful")
      print(f"Available Balance: {self.balance}$\n")

def main():  # Main function to handle user input and operations
  name = input("Enter the name of the Account Holder: ")
  bnk = BankAccount(name)

  while True:
    n = input("Enter the operation you want to perform\n1. Deposit\n2. Withdrawal\n3. Quit\nOption: ")

    if n not in ['1', '2', '3']:
      print("Choose a correct option: 1 or 2 or 3\n")
    else:
      if n == '3':
        break
      elif n == '2':
        n = int(input("Enter the amount you want to withdraw: "))
        bnk.withdraw(n)
      else:
        n = int(input("Enter the amount you want to deposit: "))
        bnk.deposit(n)

main()
