from abc import ABC, abstractmethod

class Message:
  @abstractmethod
  def send(self):
    pass

class Email(Message):
  def send(self):
    print("Sending an email")

class SMS(Message):
  def send(self):
    print("Sending a SMS")

class WhatsApp(Message):
  def send(self):
    print("Sending a WhatsApp Message")

email = Email() 
sms = SMS() 
whatsapp = WhatsApp() 

email.send()
sms.send()
whatsapp.send()
