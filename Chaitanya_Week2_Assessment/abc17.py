"""
Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.

"""
from abc import ABC, abstractmethod  # Importing ABC and abstractmethod for creating an abstract class

class IDatabaseOperations(ABC):  # Abstract base class for common database operations
  @abstractmethod
  def insert(self):  
    pass  # Method to insert data into the database

  @abstractmethod
  def update(self):  
    pass  # Method to update data in the database

  @abstractmethod
  def delete(self):  
    pass  # Method to delete data from the database

class SQLDatabase(IDatabaseOperations):  # SQLDatabase class implementing the abstract methods
  def insert(self):  
    print("Inserting into SQL Database")
  
  def update(self):  
    print("Updating the SQL Database")
  
  def delete(self):  
    print("Performing delete on SQL Database")

class NoSQLDatabase(IDatabaseOperations):  # NoSQLDatabase class implementing the abstract methods
  def insert(self):  
    print("Inserting into NoSQL Database")
  
  def update(self):  
    print("Updating the NoSQL Database")
  
  def delete(self):  
    print("Performing delete on NoSQL Database")

def main(): 
  sql = SQLDatabase() 
  nosql = NoSQLDatabase() 

  sql.insert()  
  sql.update()  
  sql.delete()  
  print()  
  nosql.insert()  
  nosql.update()  
  nosql.delete()  

main()  
