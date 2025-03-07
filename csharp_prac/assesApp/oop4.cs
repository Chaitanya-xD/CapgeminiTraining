public abstract class Shape{
  public abstract float CalculateArea();
}

public class Circle : Shape {

    public float radius { get; set; }

    public Circle(float r){
      radius = r; 
    }
    public override float CalculateArea()
    {
        return (float)3.14 * radius * radius;
    }
}
public class Rectangle : Shape {

    public float length { get; set; }
    public float breadth { get; set; }

    public Rectangle(float l, float b){
      length = l;
      breadth = b;
    }
    public override float CalculateArea()
    {
        return  length * breadth ;
    }
}

public class oop4{
  public static void main(string[] args){
    Circle circle = new Circle(5); 
    Rectangle rectangle = new Rectangle(8, 5);

    Console.WriteLine($"The Area of the Circle is {circle.CalculateArea()}");
    Console.WriteLine($"The Area of the Rectangle is {rectangle.CalculateArea()}");

  }
}

