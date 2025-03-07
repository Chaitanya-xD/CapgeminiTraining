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
//   public double add( int a, double b ){
//     return a+b;
//   }
// }

// class poly1{

//   public static void Main( string[] args ){
//     overloading obj = new overloading();
//     overriding obj1 = new overriding();

//     Console.WriteLine( $"Adding two Integers : {obj.add(2,3)}" );
//     Console.WriteLine( $"Adding two Decimals : {obj.add(2.5,3.75)}" );
//     Console.WriteLine( $"Adding an Integer and a Decimal : {obj1.add(2,3.75)}" );
//   }
  

// }
