public class Vehicle{
  public virtual void start(){
    Console.WriteLine("Vehicle Starting...");
  }
}

public class Car : Vehicle{
  public override void start(){
    Console.WriteLine("Car Starting...");
  }
}
public class Bike : Vehicle{
  public override void start(){
    Console.WriteLine("Bike Starting...");
  }
}

class oop5{

  public static void main( string[] args ){
    Vehicle v = new Vehicle();
    Car car = new Car();
    Bike bike = new Bike();

    v.start();
    car.start();
    bike.start();
  }
}