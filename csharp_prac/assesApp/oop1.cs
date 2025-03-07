using System;

public class BankAccount
{
  private decimal balance = 0;


  public void Deposit(decimal amount)
  {
    if (amount > 0)
    {
      balance += amount;
      Console.WriteLine($"Deposited: {amount:C}. New Balance: {balance:C}");
    }
    else
    {
      Console.WriteLine("Deposit amount must be positive.");
    }
  }

  public void Withdraw(decimal amount)
  {
    if (amount > 0)
    {
      if (balance >= amount)
      {
        balance -= amount;
        Console.WriteLine($"Withdrew: {amount:C}. New Balance: {balance:C}");
      }
      else
      {
        Console.WriteLine("Insufficient balance for withdrawal.");
      }
    }
    else
    {
      Console.WriteLine("Withdrawal amount must be positive.");
    }
  }

  public decimal GetBalance()
  {
    return balance;
  }
}

class oop1
{
  public static void main(string[] args)
  {
    BankAccount account = new BankAccount();

    while ( true ){
      Console.Write("Choose the operation you want to perform\n1. Check Balance\n2. Deposit\n3. Withdrawl\n4. Quit\nEnter Option: ");
      string input = Console.ReadLine();
      int n;
      int.TryParse(input, out n);

      if( n == 1 ){
        Console.WriteLine( $"Account Balance: {account.GetBalance()}" );
      }
      else if( n == 2 ){
        Console.Write("Enter the amount you want to deposit: ");
        string t = Console.ReadLine();
        int money;
        int.TryParse(t, out money);
        account.Deposit(money);
      }
      else if( n == 3 ){
        Console.Write("Enter the amount you want to withdraw: ");
        string t = Console.ReadLine();
        int money;
        int.TryParse(t, out money);
        account.Withdraw(money);
      }
      else{
        break;
      }
    }
  }
}
