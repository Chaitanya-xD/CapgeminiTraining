"""
Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.

"""
from abc import ABC, abstractmethod  # Importing ABC and abstractmethod

class UserAuthentication:  # Abstract base class for user authentication
  @abstractmethod
  def login(self):  # Abstract method for login
    pass

  @abstractmethod
  def logout(self):  # Abstract method for logout
    pass

class GoogleAuth(UserAuthentication):  # Google authentication implementation
  def login(self):  
    print("Logging in using google...")
    self.email = input("Enter your email address: ")
    self.password = input("Enter your password: ")
    print(f"Logged in as {self.email}")  
  
  def logout(self):  
    print(f"Logged out.")

class FacebookAuth(UserAuthentication):  # Facebook authentication implementation
  def login(self):  
    print("Logging in using Facebook...")
    self.uname = input("Enter your Facebook username: ")
    self.password = input("Enter your password: ")
    print(f"Logged in as {self.uname}")  
  
  def logout(self):  
    print(f"Logged out.")

def main():  # Main function
  ga = GoogleAuth()  
  fb = FacebookAuth()  

  ga.login()  
  ga.logout()

  fb.login()  
  fb.logout()

main()  
