// using System;

// public class Student{

//   private string Name = string.Empty;
//   private int RollNo;

//   public string getName(){
//     return Name;
//   }
//   public int getRollNo(){
//     return RollNo;
//   }
//   public void setName( string name ){
//     Name = name;
//   }
//   public void setRollNo( int rno ){
//     RollNo = rno;
//   }
// }

// public class oop2{
//   public static void main( string[] args ){
//     string name, rno;
//     int Rno;
//     Student s = new Student();

//     while( true ){
//       Console.Write("Enter the Name of the student: ");
//       name = Console.ReadLine();
//       if( name == string.Empty ){
//         Console.WriteLine("Enter Valid Name!");
//       }
//       else{
//         break;
//       }
//     }

//     while( true ){
//       Console.Write("Enter the Roll Number of the student: ");
//       rno = Console.ReadLine();
//       int.TryParse(rno, out Rno);
//       if( Rno <= 0  ){
//         Console.WriteLine("Enter Valid Roll Number!");
//       }
//       else{
//         break;
//       }
//     }
//     s.setName(name);
//     s.setRollNo(Rno);

//     Console.WriteLine($"The Name of the student is {s.getName()}, bearing Roll Number: {s.getRollNo()}");
//   } 
// }
