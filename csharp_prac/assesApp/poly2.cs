// /*
// Compile Time Polymorphism also called as Method Overloading. In compile time polymorphism the method names and same but they differ in their,
// 1. Number of Arguments
// 2. Data Type of arguments
// 3. Order of arguments

// Run Time Polymorphism also called as Method Overriding. Run time polymorphism occurs within Inheritance. When a child class defines a method with the same signature name as the Parent class, the Method in the child class Over Rides the Method in the Parent class. When the method is called the method in the child class gets Executed First.
// */

// /* 

// Polymorphism means "One in Many" which is One method in many forms.
// There are two types of Polymorphism. 
// 1. Compile Time Polymorphsim ( Method Overloading ) 
// 2. Run Time Polymorphism  ( Method OverRiding )

// */

// class overloading{
//   public int add( int a, int b ){
//     return a+b;

//   }
//   public double add( double a, double b ){
//     return a+b;
//   }
// }

// class overriding : overloading{
//   public int add( int a, int b, int c ){
//     return a + b + c;
//   }
// }

// class poly2{

//   public static void Main( string[] args ){
//     overloading obj = new overloading();
//     overriding obj1 = new overriding();

//     Console.WriteLine( $"Adding two Integers : {obj.add(8,9)}" );
//     Console.WriteLine( $"Adding two Decimals : {obj.add(2.5,3.75)}" );
//     Console.WriteLine( $"Adding three Integers : {obj1.add(2,3,7)}" );
//   }
  

// }
