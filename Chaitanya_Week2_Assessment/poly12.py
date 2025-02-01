"""
Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.

"""

class Payment:
  def process_payment(self):  # Base method for processing payment
    print("Payment Processing..!!")

class CreditCardPayment(Payment):
  def process_payment(self):  # Credit card payment processing
    print("Payment Through Credit Card. Processing....")
    n = int(input("Enter Pin: "))
    print("Payment Successful!")

class PayPalPayment(Payment):
  def process_payment(self):  # PayPal payment processing
    print("Payment Through PayPal. Processing....")
    s = input("Enter recievers Email / Username / Mobile Number: ")
    print(f"Paying Money to {s} through PayPal..")
    print("Payment Successful!")

class BitcoinPayment(Payment):
  def process_payment(self):  # Bitcoin payment processing
    print("Payment Through Bitcoin. Processing....")
    s = input("Enter recievers Bitcoin wallet address: ")
    print(f"Bitcoin Transferred to {s}")  

def main():  # Main function to demonstrate different payment methods
  pmt = Payment()
  pmt.process_payment()

  cc = CreditCardPayment()
  cc.process_payment()
  
  pp = PayPalPayment()
  pp.process_payment()

  btc = BitcoinPayment()
  btc.process_payment()

main()
