public class Book{
  public Book(){
    Console.WriteLine("This is a Book");
  }
  public Book(string Title, string Author){
    Console.WriteLine($"This is a Book.\nTitle of the Book: {Title}\nAuthor of the Book: {Author}");
  }
  public Book(string Title, string Author, string ISBN){
    Console.WriteLine($"This is a Book.\nTitle of the Book: {Title}\nAuthor of the Book: {Author}");
    Console.WriteLine($"ISBN Number: {ISBN}");
  }
}

public class oop3{
  public static void main( string[] args ){
    Book book = new Book();
    Console.WriteLine();
    Book book1 = new Book( "Pride and Prejudice", "Jane Austen");
    Console.WriteLine();
    Book book2 = new Book( "Kimi no Na wa", "Makoto Shinkai", "978-4-0410-2622-9");

  }
}