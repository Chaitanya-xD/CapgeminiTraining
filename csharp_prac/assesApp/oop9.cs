interface IPrintable{
  void print();
}
interface ISerializable{
  void save();
}

public class Report: IPrintable, ISerializable{

   public void print(){
        Console.WriteLine("Printing report details.");
    }

    public void save(){
        Console.WriteLine("Simulating saving report.");
    }

}

public class oop9{
  public static void main(string[] args){
    Report report = new Report();
    report.print();
    report.save();
  }
}