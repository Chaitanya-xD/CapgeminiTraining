public class Person{
  public string name {get; set;} 
  public int age {get; set;} 
  public virtual string getDetails(){
    return $"Name: {name}\nAge: {age}" ;
  }
}

public class Student : Person {
  public string StudentId{ get; set;}

  public override string getDetails(){
    return $"Name: {name}\nAge: {age}\nStudent ID: {StudentId}" ;
  }
}
public class Teacher : Person {
  public string EmployeeId{ get; set;}

  public override string getDetails(){
    return $"Name: {name}\nAge: {age}\nEmployee ID: {EmployeeId}" ;
  }
}

class oop6{
  public static void main( string[] args ){
    Person p1 = new Person{ name = "Alice", age = 20 };
    Person s1 = new Student{ name = "Bob", age = 21, StudentId = "21A6624" };
    Person t1 = new Teacher{ name = "Charlie  ", age = 50, EmployeeId = "21AH1" };

    Console.WriteLine(p1.getDetails());
    Console.WriteLine(s1.getDetails());
    Console.WriteLine(t1.getDetails());
  }
}