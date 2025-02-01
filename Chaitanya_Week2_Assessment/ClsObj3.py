"""
. You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.

"""
class Book:
  def __init__(self, title, author, isbn):  # Initializing book details
    self.title = title.capitalize()
    self.author = author.capitalize()
    self.isbn = isbn
  
  def display(self):  # Method to display book details
    print(f"\nTitle of the Book: {self.title}")
    print(f"Author of the Book: {self.author}")
    print(f"International Standard Book Number: {self.isbn}\n")

def main():  # Main function to take input and display the book details
  title = input("Enter the Title of the book: ")
  author = input("Who's the Author of the book: ")
  isbn = input("International Standard Book Number: ")

  book = Book(title, author, isbn)

  book.display()

main()
