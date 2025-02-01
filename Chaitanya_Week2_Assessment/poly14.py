"""
Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
"""

class Notification:
  def send(self):  # Base method for sending notifications
    print("Sending a Notification")

class EmailNotification:
  def send(self):  # Send email notification
    email = input("Enter the Reciepient's email address: ")
    print(f"Sending an email to {email}....")
    print("Email sent sucessfully!")

class SMSNotification:
  def send(self):  # Send SMS notification
    num = input("Enter the Reciepient's mobile number: ")
    print(f"Sending SMS to {num}......")
    print("SMS sent sucessfully!")

def main():  # Main function to send notifications
  em = EmailNotification()
  em.send()

  sms = SMSNotification()
  sms.send()

main()
