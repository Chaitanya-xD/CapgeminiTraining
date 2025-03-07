public class User{
  public string name {get; set;}
  public string admin {get; set;}

  public virtual void AccessControl(){
    Console.WriteLine($"{name} has Basic Access.");
  }
}

public class Admin: User{
    public Admin(string Name){
      name = Name;
      Console.WriteLine($"{name} is an Admin now.");
    }
    public override void AccessControl(){
        Console.WriteLine($"{name} has access to All Features.");
    }
}

public class Customer: User{
    public Customer(string Name){
      name = Name;
      Console.WriteLine($"{name} is a Customer.");
    }
    public override void AccessControl(){
        Console.WriteLine($"{name} has limited access.");
    }
}

public class oop10{
  public static void main( string[] args ){
    User adm = new Admin("Alice");
    adm.AccessControl();

    User cust = new Customer("Bob");
    cust.AccessControl();

  }
}